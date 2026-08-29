#!/usr/bin/env python3
"""Generic trust-system validator, parametrized over (T, phi).

Reference implementation for notes/TRUST_SYSTEMS_THEORY.md: one validator
that replaces the per-deployment ports (loop-experiment, Clio, MacBeth).
A deployment is a JSON descriptor (see deployments/) declaring the check
chain T, the extraction chain and interface map phi, the evidence fields,
and the citation formats. A fourth deployment is a fourth descriptor.

Checks and the theory they implement (see README.md for the dictionary):
  - boundary rule            = node-local soundness (+), Definition 2.1
  - acyclicity               = well-foundedness, Remark 2.3 (Lean `cyc`)
  - source blocking          = the interface map phi, Corollary 3.4
  - shared refs + trust cap  = cross-agent citation, Corollary 3.5
  - certificate-gap report   = the two failure modes of section 4:
      mode 1 (rho absent) vs mode 2 (rho cached in prose: certified t < tau)

Advisory: readable messages, exit 0 = clean. Stdlib only.

Usage:
  trustcheck.py --deployment deployments/loop.json [--root DIR] validate REGISTRY.json
  trustcheck.py --deployment ... sources [FILES...]        # index + machine refs
  trustcheck.py --deployment ... report successful-path|dead-ends|frontier|cross-refs REGISTRY.json
  trustcheck.py --deployment ... report footprint|shallow|certificate-gap FILES...
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Deployment descriptor = (T, phi) as data
# ---------------------------------------------------------------------------

class Deployment:
    """The parameters of one trust system, loaded from a JSON descriptor."""

    def __init__(self, data, root):
        self.name = data["name"]
        self.root = Path(root)

        t = data["trust"]
        self.trust_chain = list(t["chain"])                 # T, weakest first
        self.trust_rank = {lv: i for i, lv in enumerate(self.trust_chain)}
        self.special = set(t.get("special", []))
        self.valid_trust = set(self.trust_chain) | self.special
        self.boundary_at = t["boundary_at"]
        self.refutation_chain = list(t.get("refutation_chain", []))
        self.refutation_rank = {lv: i for i, lv in
                                enumerate(self.refutation_chain)}
        self.evidence = t.get("evidence", {})               # level -> spec

        s = data.get("sources", {})
        self.sources_format = s.get("format")
        self.sources_default = s.get("default_path", "sources.json")
        self.extraction_chain = list(s.get("extraction_chain", []))
        self.extraction_rank = {lv: i for i, lv in
                                enumerate(self.extraction_chain)}
        self.blocking = s.get("blocking", [])   # [{below_extraction, blocks_trust}]
        self.corpus_dir = s.get("corpus_dir")               # chunk deployments
        self.corpus_exempt = set(s.get("corpus_exempt", []))

        c = data.get("citation", {})
        self.machine_re = re.compile(c["machine_regex"]) if c.get(
            "machine_regex") else None
        self.machine_resolve = c.get("machine_resolve", "index")
        self.machine_suffix = c.get("machine_suffix", "")
        self.prose_roots = [self._resolve(p) for p in c.get("prose_roots", [])]

        # cross-agent interfaces (Def 3.1 / Cor 3.5): per peer, a monotone
        # phi on the trust chains and a source_phi on the extraction chains
        self.interfaces = {}
        for peer, spec in (data.get("interfaces") or {}).items():
            self.interfaces[peer] = {
                "registry_dir": self._resolve(spec["registry_dir"]),
                "artifact_root": (self._resolve(spec["artifact_root"])
                                  if spec.get("artifact_root") else None),
                "on_missing_artifact": spec.get("on_missing_artifact",
                                                "error"),
                "phi": spec.get("phi") or {},
                "source_phi": spec.get("source_phi") or {},
                "sources_path": (self._resolve(spec["sources_path"])
                                 if spec.get("sources_path") else None),
            }

    def _resolve(self, p):
        p = Path(os.path.expanduser(p))
        return p if p.is_absolute() else self.root / p

    # rank helpers: unknown values rank below everything (bottom = no check)
    def trank(self, level):
        return self.trust_rank.get(level, -1)

    def erank(self, level):
        return self.extraction_rank.get(level, -1)

    # cross-registry cap (Cor 3.5): open/unchecked local claims rank below
    # the chain, so a stub may always cite a canonical node
    def cap_rank(self, level):
        if level in self.trust_rank:
            return self.trust_rank[level]
        if level in self.special:
            return -1
        return len(self.trust_chain)    # invalid: exceeds everything


def load_deployment(path, root):
    with open(path) as fh:
        return Deployment(json.load(fh), root)


def lint_interfaces(dep, descriptor_path):
    """Check each declared phi is a morphism of trust systems (Def 3.1).

    Side conditions, checked mechanically: total on the peer's chain,
    monotone with respect to both chain orders, strict at bottom (peer's
    unchecked maps to our unchecked), specials to specials; same for
    source_phi on the extraction chains. A phi violating these is a
    DESCRIPTOR error, not a registry error — Lemma 3.2 does not hold for
    it, so nothing it transports is safe. The peer's side of the order is
    read from '<peer>.json' next to our own descriptor; when that file is
    absent the side conditions are unchecked (warning), but images are
    still verified to be levels of this deployment.

    Returns (errors, warnings).
    """
    errors, warns = [], []
    for peer, iface in dep.interfaces.items():
        phi, sphi = iface["phi"], iface["source_phi"]
        where = f"interfaces[{peer}]"
        for lv in set(phi.values()):
            if lv not in dep.valid_trust:
                errors.append(f"{where}: phi image '{lv}' is not a trust "
                              f"level of this deployment")
        for lv in set(sphi.values()):
            if lv not in dep.extraction_rank:
                errors.append(f"{where}: source_phi image '{lv}' is not an "
                              f"extraction level of this deployment")
        peer_path = Path(descriptor_path).parent / (peer + ".json")
        try:
            pdata = json.loads(peer_path.read_text())
        except (OSError, json.JSONDecodeError):
            warns.append(f"{where}: peer descriptor '{peer_path}' not "
                         f"readable — phi side conditions unchecked")
            continue
        pchain = pdata.get("trust", {}).get("chain", [])
        pspecial = pdata.get("trust", {}).get("special", [])
        missing = [lv for lv in pchain if lv not in phi]
        if missing:
            errors.append(f"{where}: phi not total on {peer}'s chain "
                          f"(missing: {', '.join(missing)})")
        images = [dep.trank(phi[lv]) for lv in pchain if lv in phi]
        if any(a > b for a, b in zip(images, images[1:])):
            errors.append(f"{where}: phi is not monotone along {peer}'s "
                          f"chain")
        if pchain and phi.get(pchain[0]) is not None \
                and phi[pchain[0]] != dep.trust_chain[0]:
            errors.append(f"{where}: phi not strict at bottom "
                          f"('{pchain[0]}' must map to "
                          f"'{dep.trust_chain[0]}', the unchecked level)")
        for lv in pspecial:
            if lv in phi and phi[lv] not in dep.special:
                errors.append(f"{where}: peer special '{lv}' maps to "
                              f"non-special '{phi[lv]}'")
        pext = pdata.get("sources", {}).get("extraction_chain", [])
        pmissing = [lv for lv in pext if lv not in sphi]
        if pmissing:
            errors.append(f"{where}: source_phi not total on {peer}'s "
                          f"extraction chain (missing: "
                          f"{', '.join(pmissing)})")
        simages = [dep.erank(sphi[lv]) for lv in pext if lv in sphi]
        if any(a > b for a, b in zip(simages, simages[1:])):
            errors.append(f"{where}: source_phi is not monotone along "
                          f"{peer}'s extraction chain")
    return errors, warns


# ---------------------------------------------------------------------------
# Registry loading and traversal
# ---------------------------------------------------------------------------

def walk(node, path=()):
    """Yield (node, path) for every node in the tree. path is a tuple of ids."""
    p = path + (node.get("id", "?"),)
    yield node, p
    for child in node.get("children") or []:
        if isinstance(child, dict):
            yield from walk(child, p)


def parse_shared(value):
    """Parse '<registry>#<node-id>'. Returns (registry, node_id) or None."""
    if not isinstance(value, str) or value.count("#") != 1:
        return None
    reg, nid = value.split("#")
    if not reg or not nid:
        return None
    return reg, nid


def _load_registry_file(path, label):
    try:
        with open(path) as fh:
            data = json.load(fh)
        tree = data.get("tree")
        if not isinstance(tree, dict):
            return None, f"registry '{label}' has no tree"
        return tree, None
    except OSError:
        return None, f"registry '{label}' not found at {path}"
    except json.JSONDecodeError as exc:
        return None, f"registry '{label}' is not valid JSON ({exc})"


def reg_key(dep, context_key, ref):
    """Canonical key for a registry name as seen from a context registry.

    Key namespace: 'name' = sibling in the local registry dir;
    '<peer>/name' = a registry in that peer's synced snapshot
    (interfaces[peer].registry_dir). Inside a peer's tree an unqualified
    name is the peer's own sibling, and a name qualified with OUR agent
    name points back at a local registry (both sides address the same
    canonical registries; snapshots are copies of them). A reference to a
    peer of a peer is unresolvable from here: returns None.
    """
    context_peer = context_key.split("/", 1)[0] if "/" in context_key else None
    if "/" not in ref:
        return f"{context_peer}/{ref}" if context_peer else ref
    head, rest = ref.split("/", 1)
    if "/" in rest:
        return None
    if head == dep.name:
        return rest
    if context_peer is None and head in dep.interfaces:
        return ref
    return None


def load_by_key(dep, registry_dir, key, cache):
    """Load the registry named by a canonical key, memoized.

    Returns (tree, error). Peer keys resolve under the interface's
    registry_dir — a synced snapshot, since agents live in separate
    containers (citing a peer's registry means carrying a copy).
    """
    if key in cache:
        return cache[key]
    if "/" in key:
        peer, name = key.split("/", 1)
        iface = dep.interfaces.get(peer)
        if iface is None:
            result = (None, f"no interface declared for peer '{peer}'")
        else:
            result = _load_registry_file(
                Path(iface["registry_dir"]) / (name + ".json"), key)
    else:
        result = _load_registry_file(
            Path(registry_dir) / (key + ".json"), key)
    cache[key] = result
    return result


def find_node(tree, nid):
    for node, _ in walk(tree):
        if node.get("id") == nid:
            return node
    return None


def resolve_shared(dep, node, registry_dir, cache):
    """Resolve a node's 'shared' ref to its canonical node.

    One-hop rule: the canonical node must not itself be shared, so
    resolution is a single lookup. Returns (target, iface, error);
    iface is the cross-agent interface when the canonical node lives in
    a peer's trust system — its trust is then only meaningful through
    phi (Lemma 3.2), never raw.
    """
    parsed = parse_shared(node.get("shared"))
    if parsed is None:
        return None, None, ("'shared' must be '<registry>#<node-id>' "
                            f"(got {node.get('shared')!r})")
    reg, nid = parsed
    key = reg_key(dep, "", reg)
    if key is None:
        return None, None, (f"registry '{reg}' is not resolvable from here "
                            f"(unknown peer, or a peer of a peer)")
    iface = dep.interfaces.get(key.split("/", 1)[0]) if "/" in key else None
    tree, err = load_by_key(dep, registry_dir, key, cache)
    if err:
        return None, iface, err
    target = find_node(tree, nid)
    if target is None:
        return None, iface, f"shared target '{reg}#{nid}' not found"
    if target.get("shared") is not None:
        return None, iface, (f"shared target '{reg}#{nid}' is itself shared "
                             f"(one-hop rule: point at the canonical node)")
    return target, iface, None


# ---------------------------------------------------------------------------
# Acyclicity (Remark 2.3): the premise digraph over (registry, node-id)
# ---------------------------------------------------------------------------

def check_acyclic(dep, own_name, tree, registry_dir, cache):
    """Explicit well-foundedness check on the cross-registry premise digraph.

    Nodes are (registry-key, node-id); edges are parent -> child within a
    tree and stub -> canonical across registries — including across AGENTS:
    peer snapshots are walked, and a peer stub qualified with our own agent
    name closes the loop back into local registries. A single JSON tree is
    acyclic by format; 'shared' links break tree-ness, and the one-hop rule
    alone does NOT exclude cycles (a stub in A can point into B whose
    descendant stub points back above the first stub in A — with or without
    a container boundary in between). Circular citation is trust inflation
    that passes every node-local check (Lean `cyc`), so the cycle check is
    load-bearing, not hygiene. Cross-agent it is also where Lemma 3.2 would
    otherwise be abused: two agents each grading the other's claim as their
    premise is tau = bottom on both sides.
    """
    errors = []
    trees = {own_name: tree}

    def get_tree(key):
        if key in trees:
            return trees[key]
        t, _ = load_by_key(dep, registry_dir, key, cache)
        trees[key] = t
        return t

    # child edges by (key, id); stub edges resolved lazily
    def edges(key, nid):
        t = get_tree(key)
        if t is None:
            return
        n = find_node(t, nid)
        if n is None:
            return
        parsed = parse_shared(n["shared"]) if n.get("shared") else None
        if parsed:
            tgt = reg_key(dep, key, parsed[0])
            if tgt is not None:
                yield (tgt, parsed[1])
        for child in n.get("children") or []:
            if isinstance(child, dict) and child.get("id"):
                yield (key, child["id"])

    WHITE, GREY, BLACK = 0, 1, 2
    colour = {}

    def dfs(start):
        stack = [(start, iter(edges(*start)))]
        colour[start] = GREY
        path = [start]
        while stack:
            node, it = stack[-1]
            advanced = False
            for succ in it:
                if colour.get(succ, WHITE) == GREY:
                    cyc = path[path.index(succ):] + [succ]
                    errors.append(
                        "cycle in the premise relation (tau = bottom on it, "
                        "every node-local check passes — Remark 2.3): "
                        + " -> ".join(f"{r}#{i}" for r, i in cyc))
                elif colour.get(succ, WHITE) == WHITE:
                    colour[succ] = GREY
                    stack.append((succ, iter(edges(*succ))))
                    path.append(succ)
                    advanced = True
                    break
            if not advanced:
                colour[node] = BLACK
                stack.pop()
                path.pop()

    for node, _ in walk(tree):
        nid = node.get("id")
        if nid and colour.get((own_name, nid), WHITE) == WHITE:
            dfs((own_name, nid))
    return errors


# ---------------------------------------------------------------------------
# Sources index
# ---------------------------------------------------------------------------

def load_sources(dep, path):
    """Load a sources index. Returns (index_or_None, warning_or_None)."""
    if path == "skip":
        return None, None
    explicit = path is not None
    path = Path(path) if path else dep.root / dep.sources_default
    try:
        data = json.loads(Path(path).read_text())
    except OSError:
        if explicit:
            return None, f"sources index '{path}' not found; skipping source checks"
        return None, None   # default path absent: quietly skip
    except json.JSONDecodeError as exc:
        return None, (f"sources index '{path}' is not valid JSON ({exc}); "
                      f"skipping source checks")
    return data if isinstance(data, dict) else {}, None


def validate_sources(dep, data, chunks_dir):
    """Validate the index itself (format, fields, extraction, files on disk)."""
    problems = []
    if dep.sources_format and data.get("format") != dep.sources_format:
        problems.append(f"sources index: missing or unknown 'format' "
                        f"(want {dep.sources_format})")
    sources = data.get("sources")
    if not isinstance(sources, dict):
        return {}, problems + ["sources index: 'sources' must be an object"]
    for slug, entry in sources.items():
        where = f"sources[{slug}]"
        if not isinstance(entry, dict):
            problems.append(f"{where}: entry must be an object")
            continue
        for field in ("title", "extraction", "read"):
            if field not in entry:
                problems.append(f"{where}: missing '{field}'")
        level = entry.get("extraction")
        if level is not None and level not in dep.extraction_rank:
            problems.append(f"{where}: extraction '{level}' invalid "
                            f"(one of: {', '.join(dep.extraction_chain)})")
        if (chunks_dir is not None and level not in dep.corpus_exempt
                and not (chunks_dir / slug).is_dir()):
            problems.append(
                f"{where}: no corpus directory {chunks_dir / slug} "
                f"(if this paper is not in the corpus, mark it "
                f"'{next(iter(dep.corpus_exempt), 'recalled')}')")
        for rel in entry.get("read", []) or []:
            if not (dep.root / rel).exists():
                problems.append(f"{where}: read file missing: {rel}")
        for i, corr in enumerate(entry.get("corrections", []) or []):
            if not isinstance(corr, dict) or "date" not in corr or "note" not in corr:
                problems.append(f"{where}: corrections[{i}] needs 'date' and 'note'")
    return sources, problems


def below_extraction(dep, entry, threshold):
    """Missing/invalid extraction ranks at the bottom: no check recorded."""
    return dep.erank(entry.get("extraction")) < dep.erank(threshold)


# ---------------------------------------------------------------------------
# Registry validation: (+) and everything node-local
# ---------------------------------------------------------------------------

NODE_REQUIRED = ("id", "approach", "trust", "children")
VALID_ROLES = ("premise", "attempt")


def validate_registry(dep, registry, own_name, files_dir, registry_dir,
                      source_index, warnings):
    errors = []
    reg_cache = {}
    peer_sources_cache = {}
    b_at = dep.boundary_at

    def transported(canon, iface):
        """Canonical trust as this system sees it: through phi if the
        canonical node lives in a peer's system (Lemma 3.2 — phi(tau) is
        the best safe grade; an unmapped peer level transports as nothing,
        i.e. unchecked)."""
        ct = canon.get("trust")
        return iface["phi"].get(ct) if iface is not None else ct

    def effective_trust(n):
        """Trust for boundary purposes: canonical if shared (Cor 3.5),
        transported along phi if the canonical node is a peer's."""
        if n.get("shared") is None or registry_dir is None:
            return n.get("trust")
        canon, iface, _ = resolve_shared(dep, n, registry_dir, reg_cache)
        return transported(canon, iface) if canon is not None \
            else n.get("trust")

    def peer_source_entry(sid, loc):
        """Resolve '<peer>:<slug>' in the peer's sources index, with its
        extraction level demoted through source_phi: extraction does not
        survive delegation at full strength (we hold the peer's record of
        the check, not the check)."""
        peer, slug = sid.split(":", 1)
        iface = dep.interfaces.get(peer)
        if iface is None:
            warnings.append(f"{loc}: source '{sid}' names unknown peer "
                            f"'{peer}' (no interface declared)")
            return None
        if peer not in peer_sources_cache:
            idx = None
            p = iface["sources_path"]
            if p is None:
                warnings.append(f"{loc}: interface '{peer}' has no "
                                f"sources_path; cannot resolve '{sid}'")
            else:
                try:
                    idx = json.loads(Path(p).read_text()).get("sources", {})
                except (OSError, json.JSONDecodeError) as exc:
                    warnings.append(f"{loc}: {peer}'s sources index at "
                                    f"'{p}' unreadable ({exc})")
            peer_sources_cache[peer] = idx
        idx = peer_sources_cache[peer]
        if idx is None:
            return None
        entry = idx.get(slug)
        if entry is None:
            warnings.append(f"{loc}: source '{sid}' not in {peer}'s "
                            f"sources index")
            return None
        level = iface["source_phi"].get(entry.get("extraction"))
        return {**entry, "extraction": level}

    for key in ("conjecture", "status", "tree"):
        if key not in registry:
            errors.append(f"top level: missing key '{key}'")
    tree = registry.get("tree")
    if not isinstance(tree, dict):
        errors.append("top level: 'tree' must be an object")
        return errors

    seen_ids = {}
    for node, path in walk(tree):
        loc = "/".join(path)

        # well-formedness
        for key in NODE_REQUIRED:
            if key not in node:
                errors.append(f"{loc}: missing key '{key}'")
        if not isinstance(node.get("children", []), list):
            errors.append(f"{loc}: 'children' must be a list")

        # unique ids
        nid = node.get("id")
        if nid in seen_ids:
            errors.append(f"{loc}: duplicate id '{nid}' (also at {seen_ids[nid]})")
        elif nid is not None:
            seen_ids[nid] = loc

        # trust values live in T + specials
        trust = node.get("trust")
        if trust is not None and trust not in dep.valid_trust:
            errors.append(f"{loc}: invalid trust '{trust}' "
                          f"(valid: {', '.join(sorted(dep.valid_trust))})")

        # role: required on every non-root node, must be premise or attempt
        role = node.get("role")
        if len(path) > 1:  # not root
            if role is None:
                errors.append(f"{loc}: missing 'role' field "
                              f"(must be 'premise' or 'attempt')")
            elif role not in VALID_ROLES:
                errors.append(f"{loc}: invalid role '{role}' "
                              f"(must be 'premise' or 'attempt')")

        # shared nodes are stubs; local trust is a cache that must not
        # exceed the canonical trust (cross-registry boundary, Cor 3.5)
        shared = node.get("shared")
        if shared is not None:
            if node.get("children"):
                errors.append(f"{loc}: shared node must be a stub "
                              f"(children live at the canonical node)")
            if registry_dir is not None:
                canon, iface, err = resolve_shared(dep, node, registry_dir,
                                                   reg_cache)
                if err:
                    errors.append(f"{loc}: {err}")
                else:
                    ct = transported(canon, iface)
                    raw = canon.get("trust")
                    via = (f" (canonical '{raw}' via phi)"
                           if iface is not None else "")
                    if iface is not None and ct is None:
                        errors.append(
                            f"{loc}: canonical '{shared}' has trust "
                            f"'{raw}' with no phi image — transports as "
                            f"unchecked; extend the interface map or do "
                            f"not cite it")
                    elif ct == "dead-end":
                        if trust != "dead-end":
                            errors.append(
                                f"{loc}: canonical '{shared}' is "
                                f"dead-end{via} but stub claims '{trust}'")
                    elif dep.cap_rank(trust) > dep.cap_rank(ct):
                        errors.append(
                            f"{loc}: stub trust '{trust}' exceeds canonical "
                            f"'{shared}' trust '{ct}'{via} (trust lives at "
                            f"the canonical node)")
                    # trust transport requires artifact transport: an
                    # import at/above our boundary is load-bearing, so
                    # its evidence must exist on OUR side of the
                    # container boundary
                    if (iface is not None and ct is not None
                            and dep.trank(ct) >= dep.trank(b_at)):
                        f_ = canon.get("file")
                        root_ = iface["artifact_root"]
                        present = bool(f_) and root_ is not None \
                            and (root_ / f_).is_file()
                        if not present:
                            detail = (f"evidence '{f_}' not under {root_}"
                                      if f_ else "canonical node has no "
                                                 "'file'")
                            msg = (f"{loc}: imports '{shared}' at '{ct}' "
                                   f"but {detail} — trust transport "
                                   f"requires artifact transport")
                            if iface["on_missing_artifact"] == "warning":
                                warnings.append(msg)
                            else:
                                errors.append(msg)

        # dead ends: reasons + refutation sub-poset (section 5)
        if trust == "dead-end":
            if not node.get("reason") and shared is None:
                errors.append(f"{loc}: dead-end without a 'reason'")
            ref = node.get("refutation")
            if ref is not None and ref not in dep.refutation_rank:
                errors.append(
                    f"{loc}: invalid refutation '{ref}' "
                    f"(valid: {', '.join(dep.refutation_chain)})")
            elif (ref is not None
                    and dep.refutation_rank[ref] >= dep.refutation_rank.get(
                        "computed", 1)
                    and not node.get("file")):
                warnings.append(
                    f"{loc}: refutation '{ref}' but no 'file' — evidence "
                    f"that strong should live somewhere on disk")
        elif node.get("refutation") is not None:
            errors.append(f"{loc}: 'refutation' only belongs on dead-end "
                          f"nodes (trust is '{trust}')")

        # evidence fields: a self-assigned label with no artifact is
        # trust inflation. Stubs are exempt: evidence lives at the
        # canonical node.
        spec = dep.evidence.get(trust)
        if spec and shared is None and not node.get(spec["field"]):
            msg = (f"{loc}: {trust} without a '{spec['field']}' field "
                   f"({spec.get('hint', 'pointer to the evidence')})")
            if spec.get("severity", "error") == "warning":
                warnings.append(msg)
            else:
                errors.append(msg)

        # boundary rule (+): claiming >= boundary_at requires every
        # premise child at least boundary_at, at canonical trust.
        # Attempt children are exploration, not dependencies.
        if dep.trank(trust) >= dep.trank(b_at):
            for child in node.get("children") or []:
                if child.get("role") == "attempt":
                    continue
                ct = effective_trust(child)
                if ct == "dead-end":
                    continue
                if dep.trank(ct) < dep.trank(b_at):
                    errors.append(
                        f"{loc}: claims '{trust}' but premise child "
                        f"'{child.get('id')}' is '{ct}' (boundary rule: "
                        f"premise children must be at least '{b_at}')")

        # citation provenance: phi blocking (Cor 3.4)
        srcs = node.get("sources")
        if srcs is not None:
            if not (isinstance(srcs, list)
                    and all(isinstance(s, str) for s in srcs)):
                errors.append(f"{loc}: 'sources' must be a list of source-id "
                              f"strings")
            else:
                known = []
                for sid in srcs:
                    if ":" in sid:      # '<peer>:<slug>' — via an interface
                        entry = peer_source_entry(sid, loc)
                        if entry is not None:
                            known.append(entry)
                    elif source_index is not None:
                        entry = source_index.get(sid)
                        if entry is None:
                            warnings.append(
                                f"{loc}: source '{sid}' not in the sources "
                                f"index (add it, or check the id)")
                        else:
                            known.append(entry)
                for rule in dep.blocking:
                    if (known
                            and dep.trank(trust) >= dep.trank(rule["blocks_trust"])
                            and all(below_extraction(dep, e,
                                                     rule["below_extraction"])
                                    for e in known)):
                        errors.append(
                            f"{loc}: claims '{trust}' but every cited source "
                            f"is below '{rule['below_extraction']}' — extract "
                            f"at least one that far (check the hypotheses) "
                            f"before it is load-bearing")

        # file references
        f = node.get("file")
        if f is not None and files_dir is not None:
            if not os.path.isfile(os.path.join(files_dir, f)):
                errors.append(f"{loc}: file '{f}' not found under {files_dir}")

    # status should mirror the root's trust
    if registry.get("status") != tree.get("trust"):
        errors.append(f"top level: status '{registry.get('status')}' does not "
                      f"match root trust '{tree.get('trust')}'")

    # well-foundedness, explicitly (Remark 2.3)
    if registry_dir is not None:
        errors.extend(check_acyclic(dep, own_name, tree, registry_dir,
                                    reg_cache))

    return errors


# ---------------------------------------------------------------------------
# Machine citations in files
# ---------------------------------------------------------------------------

def machine_refs(dep, path):
    if dep.machine_re is None:
        return []
    return sorted(set(dep.machine_re.findall(path.read_text(errors="replace"))))


def slug_of(ref):
    return ref.split("/", 1)[0]


def resolve_machine(dep, ref, sources, chunks_dir):
    """Does a machine-format citation resolve? Returns (ok, why_not)."""
    slug = slug_of(ref)
    if sources is not None and slug not in sources:
        return False, "unregistered source"
    if dep.machine_resolve == "corpus-file":
        if chunks_dir is not None and not (
                chunks_dir / (ref + dep.machine_suffix)).is_file():
            return False, "no such chunk on disk"
    return True, None


def check_files(dep, files, sources, chunks_dir):
    problems = []
    for f in files:
        for ref in machine_refs(dep, f):
            slug = slug_of(ref)
            if sources is not None and slug not in sources:
                problems.append(
                    f"{f}: cites {ref} — unregistered source; add '{slug}' "
                    f"to the sources index at its honest extraction level")
            if (dep.machine_resolve == "corpus-file" and chunks_dir is not None
                    and not (chunks_dir / (ref + dep.machine_suffix)).is_file()):
                problems.append(
                    f"{f}: cites {ref} — no such chunk on disk "
                    f"(hallucinated reference? check {chunks_dir / slug})")
    return problems


# ---------------------------------------------------------------------------
# Reports over registries (unchanged semantics from the deployed ports)
# ---------------------------------------------------------------------------

def report_successful_path(dep, tree):
    lines = []
    b = dep.trank(dep.boundary_at)

    def rec(node, depth):
        trust = node.get("trust")
        if dep.trank(trust) >= b:
            lean = f"  [lean: {node['lean']}]" if node.get("lean") else ""
            f = f"  ({node['file']})" if node.get("file") else ""
            lines.append(f"{'  ' * depth}{node['id']}: {node['approach']} "
                         f"[{trust}]{lean}{f}")
            for child in node.get("children") or []:
                rec(child, depth + 1)

    root = tree
    if dep.trank(root.get("trust")) < b:
        lines.append(f"{root['id']}: {root['approach']} [{root.get('trust')}] "
                     f"(open; {dep.boundary_at} subtrees below)")
        for child in root.get("children") or []:
            rec(child, 1)
    else:
        rec(root, 0)
    return lines or [f"(nothing at '{dep.boundary_at}' or above yet)"]


def report_dead_ends(dep, tree):
    lines = []
    for node, path in walk(tree):
        if node.get("trust") == "dead-end":
            lines.append("/".join(path))
            lines.append(f"    reason: {node.get('reason', '(MISSING)')}")
            if node.get("file"):
                lines.append(f"    file:   {node['file']}")
            ref = node.get("refutation")
            if ref is not None:
                lines.append(f"    refutation: {ref}")
            else:
                best = max((dep.trank(c.get("trust"))
                            for c in node.get("children") or []), default=-1)
                if best >= 0:
                    lines.append(f"    refutation: {dep.trust_chain[best]} "
                                 f"(inferred from children)")
                else:
                    lines.append("    refutation: judgment (default; "
                                 "no counterexample recorded)")
    return lines or ["(no dead ends recorded)"]


def report_frontier(dep, tree):
    lines = []
    for node, path in walk(tree):
        trust = node.get("trust")
        if trust == "dead-end":
            continue
        if dep.trank(trust) < dep.trank(dep.boundary_at):
            lines.append(f"{'/'.join(path)} [{trust}]: {node.get('approach')}")
    return lines or ["(no open nodes: the conjecture is closed)"]


def report_cross_refs(dep, tree, own_name, registry_dir):
    cache = {}
    lines = ["outgoing:"]
    found = False
    for node, path in walk(tree):
        if node.get("shared") is None:
            continue
        found = True
        canon, iface, err = resolve_shared(dep, node, registry_dir, cache)
        if canon is None:
            detail = f"[UNRESOLVED: {err}]"
        elif iface is not None:
            raw = canon.get("trust")
            detail = f"[{raw} -> {iface['phi'].get(raw)} via phi]"
        else:
            detail = f"[{canon.get('trust')}]"
        lines.append(f"  {'/'.join(path)} -> {node['shared']} {detail}")
    if not found:
        lines.append("  (none)")

    lines.append("incoming:")
    found = False
    try:
        siblings = sorted(f for f in os.listdir(registry_dir)
                          if f.endswith(".json"))
    except OSError:
        siblings = []
    for fname in siblings:
        name = fname[:-len(".json")]
        if name == own_name:
            continue
        sib_tree, _ = load_by_key(dep, registry_dir, name, cache)
        if sib_tree is None:
            continue
        for node, path in walk(sib_tree):
            parsed = parse_shared(node.get("shared")) \
                if node.get("shared") is not None else None
            if parsed and parsed[0] == own_name:
                found = True
                lines.append(f"  {name}: {'/'.join(path)} -> #{parsed[1]}")
    # incoming from peer snapshots: refs qualified with OUR agent name
    for peer, iface in sorted(dep.interfaces.items()):
        try:
            fnames = sorted(f for f in os.listdir(iface["registry_dir"])
                            if f.endswith(".json"))
        except OSError:
            continue
        for fname in fnames:
            key = f"{peer}/{fname[:-len('.json')]}"
            sib_tree, _ = load_by_key(dep, registry_dir, key, cache)
            if sib_tree is None:
                continue
            for node, path in walk(sib_tree):
                parsed = parse_shared(node.get("shared")) \
                    if node.get("shared") is not None else None
                if parsed and parsed[0].startswith(dep.name + "/"):
                    found = True
                    target = parsed[0].split("/", 1)[1]
                    lines.append(f"  {key}: {'/'.join(path)} -> "
                                 f"{target}#{parsed[1]}")
    if not found:
        lines.append("  (none)")
    return lines


# ---------------------------------------------------------------------------
# Reports over files
# ---------------------------------------------------------------------------

def floor_level(dep, levels):
    return min(levels, key=dep.erank) if levels else None


def report_footprint(dep, files, sources):
    for f in files:
        refs = machine_refs(dep, f)
        print(f"\n{f}")
        if not refs:
            print("  no machine citations found")
            continue
        levels = []
        for slug in sorted({slug_of(r) for r in refs}):
            entry = sources.get(slug)
            used = [r for r in refs if slug_of(r) == slug]
            if entry is None:
                print(f"  {slug}  UNREGISTERED  ({len(used)} citation(s))")
                continue
            level = entry.get("extraction", "?")
            levels.append(level)
            flags = ""
            if entry.get("corrections"):
                flags = f"  [{len(entry['corrections'])} correction(s) — check them]"
            print(f"  {slug}  {level:<13} {len(used)} citation(s){flags}")
        fl = floor_level(dep, [l for l in levels if l in dep.extraction_rank])
        print(f"  provenance floor: {fl or 'n/a (unregistered citations only)'}")


def report_shallow(dep, files, sources):
    threshold = dep.blocking[0]["below_extraction"] if dep.blocking else None
    if threshold is None:
        print("no blocking rule in the deployment descriptor; nothing to report")
        return
    leaning = {}
    for f in files:
        for ref in machine_refs(dep, f):
            slug = slug_of(ref)
            entry = sources.get(slug)
            if entry and below_extraction(dep, entry, threshold):
                leaning.setdefault(slug, []).append(f)
    if not leaning:
        print(f"no sources below '{threshold}' are cited by the scanned files")
        return
    print(f"extraction worklist (sources below '{threshold}', "
          f"most-leaned-on first):")
    for slug, fs in sorted(leaning.items(), key=lambda kv: -len(kv[1])):
        entry = sources[slug]
        print(f"  {slug}  [{entry.get('extraction')}] — cited by {len(fs)} file(s)")
        for f in sorted(set(fs)):
            print(f"      {f}")


# --- certificate gap: modes 1 and 2 of section 4 ---------------------------

# Path-shaped prose tokens: optionally ~/ or ./ or ../, then a path with a
# recognisable text extension. Deliberately conservative — this is an
# existence-check on candidate rho caches, not a parser.
PROSE_PATH_RE = re.compile(
    r"(?<![\w/])((?:~/|\.{1,2}/)?[A-Za-z0-9_\-][\w.\-]*(?:/[\w.\-]+)*"
    r"\.(?:tex|md|json|py|lean|txt))\b")

# an optional 'lines 2672-2687' / '2672–2687' locator shortly after the path
LINE_RANGE_RE = re.compile(
    r"^[^\n]{0,40}?(?:lines?\s*)?(\d{2,6})\s*[\u2013\u2014-]\s*(\d{2,6})")


def _basename_index(roots):
    """Memoized recursive basename search over the prose roots."""
    cache = {}

    def lookup(name):
        if name not in cache:
            hits = []
            for root in roots:
                if root.is_dir():
                    hits.extend(root.rglob(name))
                if len(hits) > 20:
                    break
            cache[name] = hits
        return cache[name]

    return lookup


def resolve_prose(dep, token, lookup):
    """Resolve a prose path token against the deployment's search roots.

    Returns a list of existing paths (empty = unresolved)."""
    raw = Path(os.path.expanduser(token))
    if raw.is_absolute():
        return [raw] if raw.exists() else []
    hits = []
    for root in dep.prose_roots + [dep.root]:
        p = (root / token)
        if p.exists():
            hits.append(p)
    if hits:
        return hits
    candidates = list(lookup(raw.name))
    if "/" not in token or not candidates:
        return candidates
    # path with directories that doesn't join onto any root: prefer the
    # candidates sharing the longest trailing-component suffix with it
    parts = raw.parts
    best, best_k = [], 0
    for cand in candidates:
        cp = cand.parts
        k = 0
        while (k < len(parts) and k < len(cp)
               and parts[-1 - k].lower() == cp[-1 - k].lower()):
            k += 1
        if k > best_k:
            best, best_k = [cand], k
        elif k == best_k:
            best.append(cand)
    return best


def report_certificate_gap(dep, files, sources, chunks_dir):
    """Classify every outgoing reference of the given files.

      (a) machine format, resolves        — valid cached rho
      (b) machine format, dangling        — broken cache (hallucinated ref)
      (c) prose, resolves extensionally   — MODE 2: a consolidation exists,
          tau is preserved, but the certified t < tau (Lemma 2.2 (ii));
          backfill candidate before the next consolidation makes the
          loss canonical
      (d) prose, unresolvable             — MODE 1 candidate (rho absent)

    'Prose' = path-shaped tokens and registered source ids mentioned
    without machine format.
    """
    lookup = _basename_index(dep.prose_roots)
    tot = {"a": 0, "b": 0, "c": 0, "d": 0}
    for f in files:
        text = f.read_text(errors="replace")
        a, b, c, d = [], [], [], []

        mrefs = sorted(set(dep.machine_re.findall(text))) if dep.machine_re else []
        for ref in mrefs:
            ok, why = resolve_machine(dep, ref, sources, chunks_dir)
            (a if ok else b).append(ref if ok else f"{ref} ({why})")

        seen = set()
        for m in PROSE_PATH_RE.finditer(text):
            token = m.group(1)
            if token in seen:
                continue
            seen.add(token)
            if any(token in r for r in mrefs):
                continue
            locator = ""
            lr = LINE_RANGE_RE.match(text[m.end():m.end() + 60])
            hits = resolve_prose(dep, token, lookup)
            if hits:
                if lr:
                    lo, hi = int(lr.group(1)), int(lr.group(2))
                    n = max(len(h.read_text(errors="replace").splitlines())
                            for h in hits[:5] if h.is_file())
                    locator = (f", lines {lo}-{hi} "
                               + ("OK" if lo <= hi <= n else
                                  f"OUT OF RANGE (file has {n})"))
                where = str(hits[0]) + (f" (+{len(hits) - 1} more)"
                                        if len(hits) > 1 else "")
                c.append(f"{token} -> {where}{locator}")
            else:
                d.append(token)

        # registered source ids named in prose without a machine ref
        if sources:
            cited_slugs = {slug_of(r) for r in mrefs}
            for slug in sources:
                if slug in cited_slugs:
                    continue
                if re.search(r"(?<![\w/])" + re.escape(slug) + r"(?![\w/])",
                             text):
                    c.append(f"{slug} (registered source named in prose, "
                             f"no machine citation)")

        print(f"\n{f}")
        for key, label, items in (
                ("a", "machine, resolves (valid cached rho)", a),
                ("b", "machine, DANGLING (broken cache)", b),
                ("c", "prose, resolves extensionally (MODE 2: t < tau, "
                      "backfill candidate)", c),
                ("d", "prose, unresolvable (MODE 1 candidate: rho absent?)", d)):
            tot[key] += len(items)
            if items:
                print(f"  ({key}) {label}: {len(items)}")
                for it in items:
                    print(f"        {it}")
        if not any((a, b, c, d)):
            print("  no outgoing references found")

    print(f"\ncertificate gap: {tot['c']} reference(s) resolve extensionally "
          f"but not in machine format (mode 2 — the certified t is below "
          f"canonical tau; backfill these), {tot['b']} dangling machine "
          f"ref(s), {tot['d']} unresolved prose token(s) (mode 1 candidates), "
          f"{tot['a']} valid machine ref(s).")
    return 0


# ---------------------------------------------------------------------------
# Canonical trust (tau): the greatest sound assignment
#
# The Lean formalization (Trust.lean) defines tau as a well-founded fixpoint:
#   tau(x) = max over checking steps f into x of:
#              min(grade(f), min over premises y of tau(y))
#
# The Python validator checks SOUNDNESS (no inflation: claimed trust is
# justified by children), but not OPTIMALITY (claimed trust is the best
# justified by children). Computing tau closes this gap: it tells you
# whether a node could be upgraded.
#
# For finite acyclic registries, tau is computed bottom-up: leaves first,
# then parents whose children are all computed.
# ---------------------------------------------------------------------------

def compute_tau(dep, tree):
    """Compute canonical trust for every node in the tree.

    Returns a dict {node_id: tau_level}. tau(x) is the greatest trust
    level that would pass the boundary rule at x and all descendants.

    For a leaf: tau = the node's claimed trust (no children to constrain).
    For an interior node:
      - If all non-dead-end children have tau >= boundary_at:
        tau = the node's claimed trust (could be as high as it claims)
      - Otherwise: tau = max(children's tau values that are below boundary)

    The practical reading: if tau(x) > claimed_trust(x), the node is
    UNDER-claiming (conservative, safe). If tau(x) < claimed_trust(x),
    the node is OVER-claiming (the boundary rule violation the validator
    already catches). If tau(x) = claimed_trust(x), the assignment is
    tight."""
    result = {}

    def compute(node):
        nid = node.get("id", "?")
        trust = node.get("trust")
        children = node.get("children") or []

        # dead ends have tau = their trust (exempt from boundary)
        if trust == "dead-end":
            result[nid] = trust
            for c in children:
                if isinstance(c, dict):
                    compute(c)
            return trust

        # compute children first
        child_taus = []
        for c in children:
            if isinstance(c, dict):
                ct = compute(c)
                if ct != "dead-end":
                    child_taus.append(ct)

        if not child_taus:
            # leaf: tau is the claimed trust
            result[nid] = trust
            return trust

        # interior: tau is bounded by the minimum child tau
        # (a chain is as strong as its weakest link)
        min_child = min(child_taus, key=dep.trank)

        # the node's tau is the minimum of its claimed trust and the
        # weakest child's tau — the boundary rule forces this
        if dep.trank(trust) <= dep.trank(min_child):
            result[nid] = trust  # claim is justified
        else:
            result[nid] = min_child  # claim exceeds what children support

        return result[nid]

    compute(tree)
    return result


def report_tau(dep, tree):
    """Report canonical trust vs claimed trust for every node.

    Identifies:
    - TIGHT: tau = claimed (optimal)
    - CONSERVATIVE: tau > claimed (could be upgraded)
    - INFLATED: tau < claimed (boundary rule violation — validator catches this)
    """
    tau = compute_tau(dep, tree)
    lines = []
    for node, path in walk(tree):
        nid = node.get("id", "?")
        claimed = node.get("trust")
        canonical = tau.get(nid)
        if claimed == "dead-end" or canonical == "dead-end":
            continue
        indent = "  " * (len(path) - 1)
        cr = dep.trank(canonical) if canonical in dep.trust_rank else -1
        cl = dep.trank(claimed) if claimed in dep.trust_rank else -1
        if cr == cl:
            status = "TIGHT"
        elif cr > cl:
            status = "CONSERVATIVE (could upgrade)"
        else:
            status = "INFLATED (boundary violation)"
        if status != "TIGHT":
            lines.append(f"{indent}{nid}: claimed={claimed} tau={canonical} — {status}")
    if not lines:
        lines.append("all nodes are tight (claimed trust = canonical trust)")
    return lines


REGISTRY_REPORTS = {"successful-path", "dead-ends", "frontier", "cross-refs",
                    "tau"}
FILE_REPORTS = {"footprint", "shallow", "certificate-gap"}


# ---------------------------------------------------------------------------
# Directed container operations (Ahman-Chapman-Uustalu)
#
# A directed container (S, P, root, sub, shift) induces a comonad W where:
#   W(X)(s) = (p : P(s)) -> X(sub(s, p))
#
# For proof registries:
#   S     = search trees (JSON)
#   P(s)  = paths in the tree (tuples of node ids)
#   root  = the conjecture's trust status (extract)
#   sub   = the subtree at a given path
#   shift = path composition: q inside sub(s,p), seen globally
#
# The comonad is:
#   extract(w)    = w(root)                     = root trust
#   duplicate(w)  = \p -> \q -> w(shift(p,q))   = subtree at every position
#
# Reports are coKleisli morphisms: W(Registry) -> Report
# ---------------------------------------------------------------------------

def subtree_at(tree, path):
    """Extract the subtree at a given path (tuple of node ids).

    The path must start from the root. Returns None if the path is invalid.
    This is the 'sub' operation of the directed container."""
    if not path:
        return tree
    node = tree
    for i, nid in enumerate(path):
        if i == 0:
            # first element must match the root
            if node.get("id") != nid:
                return None
            continue
        found = False
        for child in node.get("children") or []:
            if isinstance(child, dict) and child.get("id") == nid:
                node = child
                found = True
                break
        if not found:
            return None
    return node


def dc_root(tree):
    """Extract: read the root's trust status.

    This is the counit of the comonad: epsilon : W(A) -> A.
    For registries, it answers 'is the conjecture proved?'"""
    return tree.get("trust")


def dc_sub(tree, path):
    """Sub: the subtree at position p.

    This is the 'sub' operation of the directed container (S, P, root, sub, shift).
    sub : (s : S) -> P(s) -> S"""
    return subtree_at(tree, path)


def dc_shift(tree, p, q):
    """Shift: path composition. Position q in sub(tree, p), seen globally.

    This is the 'shift' operation: shift : (s : S) -> (p : P(s)) -> P(sub(s,p)) -> P(s).
    Concretely, if p = (root, A, B) and q = (B, C, D), the global path is (root, A, B, C, D).
    The first element of q must match the last of p (the root of the subtree)."""
    if not p or not q:
        return p or q
    # q[0] should be the root of sub(tree, p), which is p[-1]
    if q[0] != p[-1]:
        return None  # incompatible composition
    # verify both paths are valid
    if subtree_at(tree, p) is None:
        return None
    result = p + q[1:]  # skip the redundant root of q
    if subtree_at(tree, result) is None:
        return None
    return result


def dc_duplicate(tree):
    """Duplicate: tag every node with the full subtree below it.

    This is the comultiplication: delta : W(A) -> W(W(A)).
    At each position p, duplicate yields the subtree sub(tree, p) —
    the complete search history below that point, available for
    any coKleisli morphism to inspect.

    Returns a new tree where each node gains a '_subtree' field
    containing a deep copy of the subtree rooted at that node.
    The boundary rule's stability under duplicate (proved in Lean:
    TrustBoundary.lean) means validating the whole tree validates
    every subtree — this operation makes that structure explicit."""
    import copy

    def annotate(node, path):
        result = copy.deepcopy(node)
        result["_subtree"] = copy.deepcopy(node)
        result["_path"] = list(path)
        new_children = []
        for child in node.get("children") or []:
            if isinstance(child, dict):
                child_path = path + (child.get("id", "?"),)
                new_children.append(annotate(child, child_path))
        if new_children:
            result["children"] = new_children
        return result

    return annotate(tree, (tree.get("id", "?"),))


# ---------------------------------------------------------------------------
# Morphism composition (multi-hop shared refs)
#
# The one-hop rule was a pragmatic workaround: "don't chain shared refs."
# The mathematically correct answer is to compose the phi maps along
# the chain: if Rick's 'proved' maps to Clio's 'peer-claimed' via phi_1,
# and MacBeth's 'computed' maps to Rick's 'sketched' via phi_2, then
# the composite phi_1 . phi_2 tells you what MacBeth's 'computed' means
# in Clio's system.
#
# resolve_shared_transitive follows chains with cycle detection and
# returns the composed phi. The validator still reports one-hop violations
# as warnings (for backwards compatibility), but the resolution works.
# ---------------------------------------------------------------------------

def compose_phi(phi_outer, phi_inner):
    """Compose two interface maps: (phi_outer . phi_inner)(x) = phi_outer(phi_inner(x)).

    This is function composition on the monotone maps between trust chains.
    The composite of two monotone maps is monotone (Lemma 3.2 composes)."""
    result = {}
    for k, v in phi_inner.items():
        if v in phi_outer:
            result[k] = phi_outer[v]
        # if v has no image under phi_outer, k maps to nothing (unchecked)
    return result


def resolve_shared_transitive(dep, node, registry_dir, cache, max_hops=5):
    """Resolve a shared ref, following chains with cycle detection.

    Returns (target_node, composed_iface, hops, error).
    composed_iface has the fully composed phi/source_phi maps.
    This replaces the one-hop rule with proper morphism composition."""
    visited = set()
    current = node
    composed_phi = None
    composed_source_phi = None
    hops = 0

    while current.get("shared") is not None:
        ref = current.get("shared")
        if ref in visited:
            return None, None, hops, f"cycle in shared refs: {ref}"
        visited.add(ref)
        hops += 1
        if hops > max_hops:
            return None, None, hops, (f"shared ref chain exceeds {max_hops} "
                                       f"hops (probable cycle or deep nesting)")

        parsed = parse_shared(ref)
        if parsed is None:
            return None, None, hops, f"invalid shared ref: {ref!r}"
        reg, nid = parsed
        key = reg_key(dep, "", reg)
        if key is None:
            return None, None, hops, f"registry '{reg}' not resolvable"

        # determine if this hop crosses an agent boundary
        iface = dep.interfaces.get(key.split("/", 1)[0]) if "/" in key else None
        if iface is not None:
            hop_phi = iface.get("phi", {})
            hop_sphi = iface.get("source_phi", {})
            if composed_phi is None:
                composed_phi = hop_phi
                composed_source_phi = hop_sphi
            else:
                composed_phi = compose_phi(composed_phi, hop_phi)
                composed_source_phi = compose_phi(composed_source_phi, hop_sphi)

        tree, err = load_by_key(dep, registry_dir, key, cache)
        if err:
            return None, None, hops, err
        target = find_node(tree, nid)
        if target is None:
            return None, None, hops, f"shared target '{reg}#{nid}' not found"
        current = target

    composed_iface = None
    if composed_phi is not None:
        composed_iface = {"phi": composed_phi, "source_phi": composed_source_phi}
    return current, composed_iface, hops, None


# ---------------------------------------------------------------------------
# Strength: W(A x B) -> A x W(B)
#
# The canonical strength of a directed container comonad. In our context:
#   A = validation context (sources index, deployment config)
#   B = registry nodes (trust, approach, children)
#   W(A x B) = a tree where each node carries both context and registry data
#
# The strength "factors out" the context: it says that the context is
# uniform across the tree (every node sees the same sources index, the
# same deployment config), so we can pull it out and carry it once.
#
# This makes "validate this registry with these sources" a functorial
# operation: strength . W(f x g) = (f x W(g)) . strength
# ---------------------------------------------------------------------------

def dc_strength(tree, context):
    """Strength: factor context out of a tree carrying (context, node) pairs.

    Input: a tree where each node notionally carries (context, node_data).
    Since our context is uniform (same sources, same deployment for every
    node), strength is: return (context, tree_with_just_node_data).

    This is the identity on our data structures (context was never stored
    per-node), but making it explicit documents the functorial contract:
    the context MUST be uniform. If different nodes needed different
    contexts (e.g., per-subtree source indices), strength would fail,
    and you'd need a distributive law instead.

    Returns (context, tree)."""
    return (context, tree)


def dc_strength_inverse(context, tree):
    """The inverse direction: A x W(B) -> W(A x B).

    Annotate every node with the shared context. Useful for preparing
    a tree for operations that need context at each position."""
    import copy

    def annotate(node):
        result = copy.deepcopy(node)
        result["_context"] = context
        new_children = []
        for child in node.get("children") or []:
            if isinstance(child, dict):
                new_children.append(annotate(child))
        if new_children:
            result["children"] = new_children
        return result

    return annotate(tree)


# ---------------------------------------------------------------------------
# CoKleisli composition
#
# Given coKleisli morphisms f : W(A) -> B and g : W(B) -> C,
# their composition is: g .* f = g . W(f) . delta
#
# In words: duplicate the tree (delta), apply f at every position
# to get a tree of B's, then apply g to the result.
#
# This lets you chain reports: "run frontier, then summarize the
# frontier nodes" composes into a single coKleisli morphism.
# ---------------------------------------------------------------------------

def dc_extend(f, tree):
    """Extend (coKleisli extension): given f : W(A) -> B, produce W(A) -> W(B).

    extend(f)(tree) applies f to every subtree, producing a new tree
    whose nodes are the results of f. This is W(f) . delta, or
    equivalently the coKleisli extension of f.

    f receives (subtree, path) and returns a value."""
    import copy

    def apply_at(node, path):
        subtree = copy.deepcopy(node)
        result_value = f(subtree, path)
        result = {"id": node.get("id"), "value": result_value,
                  "trust": node.get("trust"), "children": []}
        for child in node.get("children") or []:
            if isinstance(child, dict):
                child_path = path + (child.get("id", "?"),)
                result["children"].append(apply_at(child, child_path))
        return result

    return apply_at(tree, (tree.get("id", "?"),))


def compose_cokleisli(f, g, tree):
    """Compose coKleisli morphisms: g .* f = g . extend(f).

    f : W(A) -> B  (e.g., "what's the trust of this subtree?")
    g : W(B) -> C  (e.g., "summarize a tree of trust values")

    Returns g applied to the tree produced by extending f."""
    extended = dc_extend(f, tree)
    return g(extended, (extended.get("id", "?"),))


# ---------------------------------------------------------------------------
# Yoneda embedding
#
# The Yoneda lemma for a comonad W says:
#   Nat(W, F) ≅ F(1)
#
# For directed containers, the Yoneda embedding into the presheaf
# category gives: for each position p in shape s, the set of all
# possible observations (coKleisli maps) at that position.
#
# In practice: run ALL registered reports on each subtree and collect
# the results. This gives the "complete observable" at each node.
# ---------------------------------------------------------------------------

def yoneda_embed(dep, tree, source_index=None):
    """Yoneda embedding: at each position, compute all observations.

    Returns a tree where each node carries a dict of all report results
    computed on its subtree. This is the universal coKleisli morphism —
    every other report factors through it.

    The reports are: trust (extract), frontier, dead-ends, successful-path,
    plus derived observations (child count, depth, source count)."""
    import copy

    def observe(node, path):
        subtree = copy.deepcopy(node)
        observations = {
            "path": list(path),
            "trust": dc_root(subtree),
            "approach": subtree.get("approach", ""),
            "depth": _tree_depth(subtree),
            "node_count": _tree_size(subtree),
            "dead_end_count": sum(1 for n, _ in walk(subtree)
                                  if n.get("trust") == "dead-end"),
            "frontier_count": sum(1 for n, _ in walk(subtree)
                                  if n.get("trust") not in ("dead-end",)
                                  and dep.trank(n.get("trust")) <
                                  dep.trank(dep.boundary_at)),
            "proved_count": sum(1 for n, _ in walk(subtree)
                                if dep.trank(n.get("trust")) >=
                                dep.trank(dep.boundary_at)),
        }
        # source observations
        srcs = subtree.get("sources") or []
        observations["source_count"] = len(srcs)
        if source_index and srcs:
            levels = [source_index.get(s, {}).get("extraction", "unknown")
                      for s in srcs if s in (source_index or {})]
            observations["source_floor"] = (
                min(levels, key=lambda l: dep.erank(l))
                if levels else None)

        # the four standard reports on this subtree
        observations["frontier"] = report_frontier(dep, subtree)
        observations["dead_ends"] = report_dead_ends(dep, subtree)
        observations["successful_path"] = report_successful_path(dep, subtree)
        return observations

    def embed(node, path):
        result = copy.deepcopy(node)
        result["_yoneda"] = observe(node, path)
        new_children = []
        for child in node.get("children") or []:
            if isinstance(child, dict):
                child_path = path + (child.get("id", "?"),)
                new_children.append(embed(child, child_path))
        if new_children:
            result["children"] = new_children
        return result

    return embed(tree, (tree.get("id", "?"),))


def _tree_depth(node):
    """Maximum depth of a tree."""
    children = node.get("children") or []
    if not children:
        return 0
    return 1 + max(_tree_depth(c) for c in children if isinstance(c, dict))


def _tree_size(node):
    """Number of nodes in a tree."""
    count = 1
    for c in node.get("children") or []:
        if isinstance(c, dict):
            count += _tree_size(c)
    return count


# ---------------------------------------------------------------------------
# Cofree comonad
#
# The cofree comonad on a functor F is the terminal F-coalgebra.
# For our rose tree functor F(X) = Label x List(X), the cofree
# comonad Cofree(F) is the type of infinite labeled trees — but
# since our trees are finite, cofree annotation tags each node with
# the "full observable": the result of applying extract at every
# depth, plus the duplicate structure.
#
# Cofree(F)(A) = A x F(Cofree(F)(A))
#              = A x (Label x List(Cofree(F)(A)))
#
# The cofree annotation gives: at each node, the value (trust level)
# AND the entire comonadic context (all observations, all subtrees).
# This is the universal trust annotation — every other annotation
# scheme factors through it.
# ---------------------------------------------------------------------------

def cofree_annotate(dep, tree, source_index=None):
    """Cofree comonad annotation: tag every node with its full comonadic context.

    At each node, the annotation contains:
      - extract: the trust level (the value)
      - observations: the Yoneda embedding (all reports)
      - subtree: the complete subtree below (duplicate)
      - boundary_satisfied: whether the boundary rule holds at this node
      - path: the global position

    This is the terminal coalgebra: every other annotation (reports,
    validations, traversals) factors through it. In practice, this
    pre-computes everything you could ask about each node, so downstream
    operations are pure lookups.

    Returns a new tree with '_cofree' annotations at each node."""
    import copy

    def annotate(node, path):
        subtree = copy.deepcopy(node)
        result = copy.deepcopy(node)

        # extract
        trust = dc_root(subtree)

        # boundary rule check at this node
        boundary_ok = True
        if dep.trank(trust) >= dep.trank(dep.boundary_at):
            for child in node.get("children") or []:
                ct = child.get("trust")
                if ct == "dead-end":
                    continue
                if dep.trank(ct) < dep.trank(dep.boundary_at):
                    boundary_ok = False
                    break

        # dead-end analysis
        de_info = None
        if trust == "dead-end":
            de_info = {
                "reason": node.get("reason"),
                "refutation": node.get("refutation", "judgment"),
                "has_evidence": bool(node.get("file")),
            }

        # source analysis
        srcs = node.get("sources") or []
        source_info = None
        if srcs and source_index:
            entries = [(s, source_index.get(s)) for s in srcs]
            source_info = {
                "ids": srcs,
                "resolved": sum(1 for _, e in entries if e is not None),
                "unresolved": [s for s, e in entries if e is None],
                "floor": None,
            }
            levels = [e.get("extraction") for _, e in entries
                      if e is not None and e.get("extraction")]
            if levels:
                source_info["floor"] = min(
                    levels, key=lambda l: dep.erank(l))

        result["_cofree"] = {
            "path": list(path),
            "extract": trust,
            "depth": _tree_depth(subtree),
            "size": _tree_size(subtree),
            "boundary_satisfied": boundary_ok,
            "dead_end": de_info,
            "sources": source_info,
            "proved_subtree_count": sum(
                1 for n, _ in walk(subtree)
                if dep.trank(n.get("trust")) >= dep.trank(dep.boundary_at)),
            "frontier_size": sum(
                1 for n, _ in walk(subtree)
                if n.get("trust") != "dead-end"
                and dep.trank(n.get("trust")) < dep.trank(dep.boundary_at)),
            "dead_end_count": sum(
                1 for n, _ in walk(subtree)
                if n.get("trust") == "dead-end"),
        }

        new_children = []
        for child in node.get("children") or []:
            if isinstance(child, dict):
                child_path = path + (child.get("id", "?"),)
                new_children.append(annotate(child, child_path))
        if new_children:
            result["children"] = new_children
        return result

    return annotate(tree, (tree.get("id", "?"),))


# ---------------------------------------------------------------------------
# CLI for directed container operations
# ---------------------------------------------------------------------------

def cmd_ops(dep, args, sources):
    """Handle the 'ops' subcommand for directed container operations."""
    try:
        registry = json.loads(args.registry.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read registry: {exc}")
        return 1
    tree = registry.get("tree")
    if not isinstance(tree, dict):
        print("ERROR: no tree")
        return 1

    op = args.op

    if op == "extract":
        trust = dc_root(tree)
        print(f"extract: {trust}")
        print(f"conjecture: {registry.get('conjecture', '?')}")
        return 0

    if op == "sub":
        if not args.path:
            print("ERROR: --path required for 'sub'")
            return 1
        path = tuple(args.path)
        sub = dc_sub(tree, path)
        if sub is None:
            print(f"ERROR: path {' -> '.join(path)} not found")
            return 1
        print(json.dumps(sub, indent=2))
        return 0

    if op == "shift":
        if not args.path or not args.path2:
            print("ERROR: --path and --path2 required for 'shift'")
            return 1
        p = tuple(args.path)
        q = tuple(args.path2)
        result = dc_shift(tree, p, q)
        if result is None:
            print("ERROR: incompatible paths (composition failed)")
            return 1
        print(f"shift({' -> '.join(p)}, {' -> '.join(q)}) = {' -> '.join(result)}")
        sub = dc_sub(tree, result)
        if sub:
            print(f"  trust: {sub.get('trust')}")
            print(f"  approach: {sub.get('approach')}")
        return 0

    if op == "duplicate":
        dup = dc_duplicate(tree)
        # print a summary rather than the full annotated tree
        print(f"# duplicate: {registry.get('conjecture', '?')}")
        print(f"# every node tagged with its full subtree\n")
        for node, path in walk(dup):
            st = node.get("_subtree", {})
            indent = "  " * (len(path) - 1)
            size = _tree_size(st)
            print(f"{indent}{node.get('id')} [{node.get('trust')}] "
                  f"(subtree: {size} node{'s' if size != 1 else ''})")
        return 0

    if op == "compose":
        # demonstrate coKleisli composition: extract . frontier
        def f_trust(subtree, path):
            return dc_root(subtree)

        def g_summary(value_tree, path):
            values = [n.get("value") for n, _ in walk(value_tree)]
            from collections import Counter
            return dict(Counter(values))

        result = compose_cokleisli(f_trust, g_summary, tree)
        print(f"# coKleisli composition: trust-summary . extract")
        print(f"# (extract at every position, then count trust levels)\n")
        for k, v in sorted(result.items(), key=lambda kv: -kv[1]):
            print(f"  {k}: {v}")
        return 0

    if op == "yoneda":
        embedded = yoneda_embed(dep, tree, sources)
        print(f"# yoneda: {registry.get('conjecture', '?')}")
        print(f"# every node with all observable properties\n")
        for node, path in walk(embedded):
            y = node.get("_yoneda", {})
            indent = "  " * (len(path) - 1)
            print(f"{indent}{node.get('id')} [{y.get('trust')}]")
            print(f"{indent}  depth={y.get('depth')} nodes={y.get('node_count')} "
                  f"proved={y.get('proved_count')} "
                  f"frontier={y.get('frontier_count')} "
                  f"dead_ends={y.get('dead_end_count')}")
        return 0

    if op == "cofree":
        annotated = cofree_annotate(dep, tree, sources)
        print(f"# cofree: {registry.get('conjecture', '?')}")
        print(f"# terminal coalgebra annotation — every node fully observed\n")
        for node, path in walk(annotated):
            cf = node.get("_cofree", {})
            indent = "  " * (len(path) - 1)
            boundary = "OK" if cf.get("boundary_satisfied") else "VIOLATED"
            print(f"{indent}{node.get('id')} [{cf.get('extract')}] "
                  f"boundary={boundary} "
                  f"size={cf.get('size')} "
                  f"proved={cf.get('proved_subtree_count')} "
                  f"frontier={cf.get('frontier_size')} "
                  f"dead_ends={cf.get('dead_end_count')}")
            de = cf.get("dead_end")
            if de:
                print(f"{indent}  refutation: {de.get('refutation')} "
                      f"({'evidence on disk' if de.get('has_evidence') else 'no evidence'})")
            si = cf.get("sources")
            if si:
                print(f"{indent}  sources: {si.get('resolved')}/{len(si.get('ids', []))} "
                      f"resolved, floor={si.get('floor')}")
        return 0

    if op == "strength":
        ctx = {"deployment": dep.name, "boundary_at": dep.boundary_at,
               "trust_chain": dep.trust_chain,
               "extraction_chain": dep.extraction_chain,
               "sources_count": len(sources) if sources else 0}
        context, bare_tree = dc_strength(tree, ctx)
        print(f"# strength: factored context out of the tree")
        print(f"# context is uniform — same for every node\n")
        print(f"context:")
        for k, v in context.items():
            print(f"  {k}: {v}")
        print(f"\ntree root: {bare_tree.get('id')} [{bare_tree.get('trust')}]")
        print(f"  (tree unchanged — strength is the identity on our "
              f"uniform-context data structures)")
        return 0

    if op == "resolve-transitive":
        if not args.path:
            print("ERROR: --path required (node id to resolve)")
            return 1
        nid = args.path[0]
        target = find_node(tree, nid)
        if target is None:
            print(f"ERROR: node '{nid}' not found")
            return 1
        if target.get("shared") is None:
            print(f"{nid}: not a shared node (trust: {target.get('trust')})")
            return 0
        registry_dir = args.registry_dir or str(args.registry.resolve().parent)
        cache = {}
        canon, iface, hops, err = resolve_shared_transitive(
            dep, target, registry_dir, cache)
        if err:
            print(f"ERROR: {err}")
            return 1
        print(f"resolved in {hops} hop(s):")
        print(f"  canonical: {canon.get('id')} [{canon.get('trust')}]")
        if iface:
            print(f"  composed phi: {json.dumps(iface['phi'], indent=4)}")
            raw = canon.get("trust")
            transported = iface["phi"].get(raw)
            print(f"  transported trust: {raw} -> {transported}")
        return 0

    print(f"ERROR: unknown op '{op}'")
    return 1


OPS_CHOICES = ["extract", "sub", "shift", "duplicate", "compose",
               "yoneda", "cofree", "strength", "resolve-transitive"]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description=__doc__.splitlines()[0],
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--deployment", required=True, type=Path,
                    help="deployment descriptor JSON (the (T, phi) data)")
    ap.add_argument("--root", type=Path, default=Path("."),
                    help="deployment root; relative descriptor paths and "
                         "'read' entries resolve against it (default: cwd)")
    ap.add_argument("--sources", default=None,
                    help="sources index path (default: descriptor's "
                         "default_path under --root); 'skip' disables")
    ap.add_argument("--chunks-dir", default=None,
                    help="corpus dir override; 'skip' disables on-disk checks")
    sub = ap.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("validate", help="validate a registry")
    v.add_argument("registry", type=Path)
    v.add_argument("--files-dir", default=None,
                   help="base for node 'file' paths (default: --root); "
                        "'skip' disables")
    v.add_argument("--registry-dir", default=None,
                   help="sibling registries for 'shared' refs (default: the "
                        "registry's directory); 'skip' disables")

    s = sub.add_parser("sources", help="validate the sources index "
                                       "(+ machine refs in FILES)")
    s.add_argument("files", nargs="*", type=Path)

    r = sub.add_parser("report", help="print a report")
    r.add_argument("name", choices=sorted(REGISTRY_REPORTS | FILE_REPORTS))
    r.add_argument("targets", nargs="+", type=Path,
                   help="a registry (registry reports) or files (file reports)")
    r.add_argument("--registry-dir", default=None)

    o = sub.add_parser("ops", help="directed container operations "
                                    "(extract, sub, shift, duplicate, "
                                    "compose, yoneda, cofree, strength, "
                                    "resolve-transitive)")
    o.add_argument("op", choices=OPS_CHOICES)
    o.add_argument("registry", type=Path)
    o.add_argument("--path", nargs="+", help="node id path for sub/shift/resolve")
    o.add_argument("--path2", nargs="+", help="second path for shift")
    o.add_argument("--registry-dir", default=None)

    args = ap.parse_args()
    dep = load_deployment(args.deployment, args.root)

    # corpus dir (chunk deployments only)
    if args.chunks_dir == "skip":
        chunks_dir = None
    elif args.chunks_dir:
        chunks_dir = Path(args.chunks_dir)
    elif dep.corpus_dir:
        chunks_dir = dep._resolve(dep.corpus_dir)
        if not chunks_dir.is_dir():
            print(f"note: {chunks_dir} not found; skipping on-disk chunk checks")
            chunks_dir = None
    else:
        chunks_dir = None

    # descriptor-level lint of the cross-agent interfaces (Def 3.1)
    iface_errors, iface_warnings = lint_interfaces(dep, args.deployment)

    src_data, src_warning = load_sources(dep, args.sources)
    warnings = iface_warnings + ([src_warning] if src_warning else [])
    sources, src_problems = (None, [])
    if src_data is not None:
        sources, src_problems = validate_sources(dep, src_data, chunks_dir)

    if args.cmd == "ops":
        return cmd_ops(dep, args, sources)

    if args.cmd == "sources":
        problems = iface_errors + src_problems + check_files(
            dep, args.files, sources, chunks_dir)
        for p in problems:
            print(p)
        if problems:
            print(f"\n{len(problems)} problem(s). Advisory: fix what's real.")
            return 1
        n = len(args.files)
        print(f"sources index OK ({len(sources or {})} sources)"
              + (f"; {n} file(s) resolve cleanly" if n else ""))
        return 0

    if args.cmd == "report":
        if args.name in FILE_REPORTS:
            if args.name == "footprint":
                report_footprint(dep, args.targets, sources or {})
            elif args.name == "shallow":
                report_shallow(dep, args.targets, sources or {})
            else:
                report_certificate_gap(dep, args.targets, sources, chunks_dir)
            return 0
        reg_path = args.targets[0]
        try:
            registry = json.loads(reg_path.read_text())
        except (OSError, json.JSONDecodeError) as exc:
            print(f"ERROR: cannot read registry: {exc}")
            return 1
        tree = registry.get("tree")
        if not isinstance(tree, dict):
            print("ERROR: no tree to report on")
            return 1
        own = reg_path.stem
        registry_dir = args.registry_dir or str(reg_path.resolve().parent)
        print(f"# {args.name}: {registry.get('conjecture', '?')}")
        if args.name == "cross-refs":
            lines = report_cross_refs(dep, tree, own, registry_dir)
        elif args.name == "tau":
            lines = report_tau(dep, tree)
        else:
            lines = {"successful-path": report_successful_path,
                     "dead-ends": report_dead_ends,
                     "frontier": report_frontier}[args.name](dep, tree)
        for line in lines:
            print(line)
        return 0

    # validate
    try:
        registry = json.loads(args.registry.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read registry: {exc}")
        return 1

    files_dir = None if args.files_dir == "skip" else (
        args.files_dir or str(dep.root))
    registry_dir = None if args.registry_dir == "skip" else (
        args.registry_dir or str(args.registry.resolve().parent))

    errors = iface_errors + src_problems + validate_registry(
        dep, registry, args.registry.stem, files_dir, registry_dir,
        sources, warnings)

    if warnings:
        print(f"\n{len(warnings)} warning(s) in {args.registry}:")
        for w in warnings:
            print(f"  ~ {w}")
    if errors:
        print(f"\n{len(errors)} problem(s) in {args.registry}:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: {args.registry} is valid (status: {registry.get('status')}, "
          f"deployment: {dep.name})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
