"""
Day 70 CODE Task A — general-n piece registry generator.

Builds a base piece + variants (P_n routings, L_1 routings, R-double
families at every level) for arbitrary n. Lifts the n=5 scaffold pattern
(code/2026-06-13-n5-axis-count/n5_pieces.py) directly.

Base piece (the "obvious" routing):
  p_i -> B_i           (for i=1..n-1)
  p_n -> free direction (default in BT_2 balanced)
  L_1 -> free direction (default B_1)
  L_i -> M_i           (for i=2..n-1)
  L_n -> S             (Main_n partner)
  s_i -> (B_i, T_i)    (balanced) (for i=1..n-1)
  s_n (odd n) -> singleton routing (default: not routed)
  linkLHS (even n) -> (B_{n-1}, T_{n-1}) balanced (analog of n=4)

Variants:
  - P_n routed at every level: BT_i, BT_i doubled, S, M_i, splits.
  - L_1 routed at M_2..M_{n-1}, BT_2..BT_{n-1}, S, L_1 doubled at M_2.
  - R-double family at each level a=1..n-1 with alpha in {0,1,2}.
"""

from __future__ import annotations
from general_axis import aii_struct


def _aii_names(n):
    s = aii_struct(n)
    aii_v = s["vars"]
    P = [aii_v[i] for i in s["prefix_idx"]]   # length n
    L = [aii_v[i] for i in s["long_idx"]]     # length n
    SH = [aii_v[i] for i in s["short_idx"]]   # length n-1 (even) or n (odd)
    LAMBDA = aii_v[s["linkLHS_idx"]] if n % 2 == 0 else None
    return P, L, SH, LAMBDA


def base_piece(n):
    """The base piece at level n."""
    P, L, SH, LAMBDA = _aii_names(n)
    spec = {}
    # M_i routings: M_i <- L_i (for i=2..n-1)
    for i in range(2, n):
        spec[f"M_{i}"] = [(1, L[i - 1])]
    # B_i, T_i for i=1..n-1
    for i in range(1, n):
        b_terms = [(1, P[i - 1]), (1, SH[i - 1])]
        t_terms = [(1, SH[i - 1])]
        if i == 1:
            b_terms.append((1, L[0]))
        if i == 2:
            b_terms.append((1, P[n - 1]))
            t_terms.append((1, P[n - 1]))
        # Add linkLHS routing for even n in BT_{n-1} balanced.
        if n % 2 == 0 and LAMBDA is not None and i == n - 1:
            b_terms.append((1, LAMBDA))
            t_terms.append((1, LAMBDA))
        spec[f"B_{i}"] = b_terms
        spec[f"T_{i}"] = t_terms
    # S <- L_n
    spec["S"] = [(1, L[n - 1])]
    return spec


def _ensure_index(spec, key, terms):
    if key not in spec:
        spec[key] = []
    spec[key].extend(terms)


def _clone(spec):
    return {k: list(v) for k, v in spec.items()}


def _remove_term(spec, key, aii_var_to_remove):
    if key in spec:
        spec[key] = [t for t in spec[key] if t[1] != aii_var_to_remove]


def make_p_n_variants(n):
    """P_n routing variants (free prefix var).
    Builds variants where P_n is routed in different ways from default
    (default = BT_2 balanced)."""
    P, L, SH, LAMBDA = _aii_names(n)
    variants = {}
    base = base_piece(n)

    # Remove default P_n routing (in BT_2)
    def with_pn_routing(routing):
        spec = _clone(base)
        # strip P_n from default location (B_2 and T_2)
        _remove_term(spec, "B_2", P[n - 1])
        _remove_term(spec, "T_2", P[n - 1])
        for (key, coef) in routing:
            _ensure_index(spec, key, [(coef, P[n - 1])])
        return spec

    # P_n in BT_i balanced for i=1..n-1
    for i in range(1, n):
        if i == 2:
            continue
        variants[f"Pn_in_BT{i}"] = with_pn_routing([(f"B_{i}", 1), (f"T_{i}", 1)])
    # P_n doubled in BT_2
    variants["Pn_dbl_BT2"] = with_pn_routing([(f"B_2", 2), (f"T_2", 2)])
    # P_n in S
    variants["Pn_in_S"] = with_pn_routing([("S", 1)])
    # P_n split between BT_2 and BT_3 (already each contributes 1; this
    # gives the "shared" routing).
    if n >= 4:
        variants["Pn_split_BT2_BT3"] = with_pn_routing(
            [("B_2", 1), ("T_2", 1), ("B_3", 1), ("T_3", 1)])
    # P_n in M_i: need P_{i-1} >= M_i, P_i >= M_i. Routed as M_i + B_i
    # to keep things feasible.
    for i in range(2, n):
        spec = _clone(base)
        _remove_term(spec, "B_2", P[n - 1])
        _remove_term(spec, "T_2", P[n - 1])
        _ensure_index(spec, f"M_{i}", [(1, P[n - 1])])
        # ensure source of P_i >= M_i: route P_n into B_i too (and B_{i-1}
        # if i > 1)
        _ensure_index(spec, f"B_{i}", [(1, P[n - 1])])
        if i >= 2:
            _ensure_index(spec, f"B_{i - 1}", [(1, P[n - 1])])
        # We need T_{i-1} <= B_{i-1}: not modifying T_{i-1}, so OK.
        # The other tricky constraint is T_i <= B_i: untouched.
        # If the piece fails, we'll see in feasibility check.
        variants[f"Pn_in_M{i}"] = spec

    return variants


def make_l1_variants(n):
    """L_1 routing variants (free long var)."""
    P, L, SH, LAMBDA = _aii_names(n)
    variants = {}
    base = base_piece(n)

    def with_l1_routing(routing):
        spec = _clone(base)
        _remove_term(spec, "B_1", L[0])
        for (key, coef) in routing:
            _ensure_index(spec, key, [(coef, L[0])])
        return spec

    # L_1 in B_i for i=2..n-1
    for i in range(2, n):
        variants[f"L1_in_B{i}"] = with_l1_routing([(f"B_{i}", 1)])
    # L_1 in S
    variants["L1_in_S"] = with_l1_routing([("S", 1)])
    # L_1 in M_i for i=2..n-1 (need B_1 to still cover P_1 >= M_2 etc)
    for i in range(2, n):
        spec = _clone(base)  # keeps L_1 in B_1
        _ensure_index(spec, f"M_{i}", [(1, L[0])])
        # For i > 2 we may need L_1 in intermediate B's; mimic the n=5
        # M3, M4 variants:
        for j in range(2, i):
            _ensure_index(spec, f"B_{j}", [(1, L[0])])
        # If i == 2 then B_1 already covers P_1 >= M_2.
        variants[f"L1_in_M{i}"] = spec
    # L_1 doubled at M_2 (need high B_1)
    spec = _clone(base)
    _ensure_index(spec, "M_2", [(2, L[0])])
    # B_1 base had (1, L_1); pump to 3
    _remove_term(spec, "B_1", L[0])
    _ensure_index(spec, "B_1", [(3, L[0])])
    _ensure_index(spec, "T_1", [(1, L[0])])
    variants["L1_M2dbl"] = spec
    # L_1 in BT_2 balanced (free direction)
    variants["L1_BT2"] = with_l1_routing(
        [("B_2", 1), ("T_2", 1)])

    return variants


def make_singleton_variant(n):
    """At odd n, s_n is a "singleton" var (no Main_i mentions it).
    Build a variant routing it through S with coef 2 (analog of n=3,5)."""
    if n % 2 == 0:
        return {}
    P, L, SH, LAMBDA = _aii_names(n)
    spec = base_piece(n)
    _ensure_index(spec, f"B_{n-1}", [(1, SH[n - 1])])
    _ensure_index(spec, "S", [(2, SH[n - 1])])
    return {f"sn_2S": spec}


def make_r_double_family(n, level, alpha):
    """R-double family at level a (1..n-1) with parameter alpha.

    Doubles s_a in B_a, sends 2*s_a to S, sends alpha*P_1 to S.
    Lift of the n=4/n=5 R-double pattern.

    For level a=1, also adds L_1 to T_1 (the n=5 pattern).
    """
    P, L, SH, LAMBDA = _aii_names(n)
    spec = base_piece(n)
    # Modify B_a: add (1, SH[a-1]) (one more S_a to make 2*S_a total)
    _ensure_index(spec, f"B_{level}", [(1, SH[level - 1])])
    # S: add (2, SH[a-1]) + (alpha, P[0])
    _ensure_index(spec, "S", [(2, SH[level - 1]), (alpha, P[0])])
    # For level 1, also add L_1 to T_1 (already in base in B_1, but pattern
    # at n=5: T_1: S_1 + L_1).
    if level == 1:
        _ensure_index(spec, "T_1", [(1, L[0])])
    return spec


def build_registry(n):
    """Build full piece registry at level n."""
    registry = {}
    registry[f"P{n}_base"] = base_piece(n)
    pn_vars = make_p_n_variants(n)
    for name, spec in pn_vars.items():
        registry[f"P{n}_{name}"] = spec
    l1_vars = make_l1_variants(n)
    for name, spec in l1_vars.items():
        registry[f"P{n}_{name}"] = spec
    sn = make_singleton_variant(n)
    for name, spec in sn.items():
        registry[f"P{n}_{name}"] = spec
    # R-double family at each level
    for lv in range(1, n):
        for alpha in (0, 1, 2):
            registry[f"Rdouble_lv{lv}_alpha{alpha}"] = make_r_double_family(
                n, lv, alpha)
    return registry
