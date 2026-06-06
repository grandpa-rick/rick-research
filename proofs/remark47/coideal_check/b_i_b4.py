"""
Computational verification of on-slice coideal commutativity at B_4.

Ports b_i_b3.py from B_3 to B_4.

B_4 setup (1-indexed simple roots):
  alpha_1 = e_1 - e_2  (long)
  alpha_2 = e_2 - e_3  (long)
  alpha_3 = e_3 - e_4  (long)
  alpha_4 = e_4        (short)

Positive roots (16 total):
  Long minus: e_a - e_b for 1 <= a < b <= 4 (6 of them)
  Long plus:  e_a + e_b for 1 <= a < b <= 4 (6 of them)
  Short:      e_a for a=1..4 (4 of them)

Unit factors:
  k(1) = k(2) = k(3) = 1   (long simples)
  k(4) = 2                  (short simple at the B_n end)

THEOREM (on-slice commutativity, ported).
For each simple i of B_4, on the depth-k slice
    S_i := { pi in Kp(infty) : eps_i(pi) >= k(i) },
the commutator [e_i^{k(i)}, B_i] = 0,  where B_i = e_i + f_i.

OFF-SLICE OBSTRUCTION (ported).
At eps_i(pi) = k(i) - 1:  [e_i^{k(i)}, B_i] pi = e_i^{k(i)-1} pi.

Convex order (Bourbaki, B_4):
  block 1 (e_1 involved): EM12, EM13, EM14, E1, EP14, EP13, EP12
  block 2 (e_2 involved, not e_1): EM23, EM24, E2, EP24, EP23
  block 3 (e_3 involved, not e_1,e_2): EM34, E3, EP34
  block 4: E4
"""

from collections import defaultdict
from typing import Dict, Tuple, Optional, List

# B_4 positive roots
# Long minus
EM12 = 'e1-e2'
EM13 = 'e1-e3'
EM14 = 'e1-e4'
EM23 = 'e2-e3'
EM24 = 'e2-e4'
EM34 = 'e3-e4'
# Long plus
EP12 = 'e1+e2'
EP13 = 'e1+e3'
EP14 = 'e1+e4'
EP23 = 'e2+e3'
EP24 = 'e2+e4'
EP34 = 'e3+e4'
# Short
E1 = 'e1'
E2 = 'e2'
E3 = 'e3'
E4 = 'e4'

# Convex order (Bourbaki w_0 reduced word).
ROOTS_CONVEX = [
    EM12, EM13, EM14, E1, EP14, EP13, EP12,        # block 1 (e_1 involved)
    EM23, EM24, E2, EP24, EP23,                     # block 2 (e_2 involved)
    EM34, E3, EP34,                                  # block 3 (e_3 involved)
    E4,                                              # block 4
]
ROOTS = ROOTS_CONVEX  # alias for enumeration

# Coefficients in standard basis (e_1, e_2, e_3, e_4)
ROOT_VEC = {
    EM12: (1,-1, 0, 0), EM13: (1, 0,-1, 0), EM14: (1, 0, 0,-1),
    EM23: (0, 1,-1, 0), EM24: (0, 1, 0,-1), EM34: (0, 0, 1,-1),
    EP12: (1, 1, 0, 0), EP13: (1, 0, 1, 0), EP14: (1, 0, 0, 1),
    EP23: (0, 1, 1, 0), EP24: (0, 1, 0, 1), EP34: (0, 0, 1, 1),
    E1:   (1, 0, 0, 0), E2:   (0, 1, 0, 0), E3:   (0, 0, 1, 0), E4: (0, 0, 0, 1),
}

KP = Dict[str, int]


# ====================================================================
# Kostant-partition helpers
# ====================================================================

def kp_clean(pi: KP) -> KP:
    return {r: c for r, c in pi.items() if c}


def kp_add(pi: KP, root: str, delta: int) -> KP:
    out = dict(pi)
    out[root] = out.get(root, 0) + delta
    if out[root] == 0:
        del out[root]
    return out


def kp_repr(pi: KP) -> str:
    pi = kp_clean(pi)
    if not pi:
        return '<vacuum>'
    return ' + '.join(f'{c}*{r}' for r, c in sorted(pi.items()))


def kp_key(pi: KP) -> Tuple:
    return tuple(sorted(kp_clean(pi).items()))


def kp_total(pi: KP) -> int:
    return sum(c for c in pi.values())


# ====================================================================
# Root arithmetic: beta +/- alpha_i in B_4
# Long simples (1, 2, 3): exchange the e_i and e_{i+1} components.
# Short simple (4): e_4 changes sign.
# Result is a positive root or None.
# ====================================================================

SIMPLE_ROOT_NAME = {1: EM12, 2: EM23, 3: EM34, 4: E4}


def simple_root(i: int) -> str:
    return SIMPLE_ROOT_NAME[i]


def _vec_to_root(v: Tuple[int, int, int, int]) -> Optional[str]:
    """Look up positive root from coordinate vector, or None if not in Phi^+."""
    for r, w in ROOT_VEC.items():
        if w == v:
            return r
    return None


def root_minus_alpha(beta: str, i: int) -> Optional[str]:
    """beta - alpha_i. Returns positive-root name, or None if not in Phi^+ (incl. 0)."""
    v = list(ROOT_VEC[beta])
    if i in (1, 2, 3):
        # alpha_i = e_i - e_{i+1}, so beta - alpha_i: v[i-1] -= 1, v[i] += 1.
        v[i-1] -= 1
        v[i] += 1
    elif i == 4:
        # alpha_4 = e_4
        v[3] -= 1
    else:
        raise ValueError(i)
    return _vec_to_root(tuple(v))


def root_plus_alpha(beta: str, i: int) -> Optional[str]:
    v = list(ROOT_VEC[beta])
    if i in (1, 2, 3):
        v[i-1] += 1
        v[i] -= 1
    elif i == 4:
        v[3] += 1
    else:
        raise ValueError(i)
    return _vec_to_root(tuple(v))


# ====================================================================
# Alpha_i-string structure on Phi^+(B_4).
# Each alpha_i partitions Phi^+ into strings (chains) plus singletons.
# Chains: roots {beta, beta+alpha_i, ...} (length 2 for long simples, up to 3 for short).
# Singletons: roots not touching alpha_i.
#
# Per CST Def 2.14 bracketing structure:
#
# Long simple (i = 1, 2, 3): alpha_i-strings are length-2 chains.
#   For each chain in convex order (of the top):
#     contribute ')'^{c_top} '('^{c_bot}.
#   The simple root alpha_i itself: contributes ')'^{c_simple} at the end.
#   Non-touching singletons contribute nothing.
#
# Short simple (i = 4): alpha_4-strings are length-3 chains.
#   For each chain (bot, mid, top) in convex order:
#     ')'^c_mid  '('^{2 c_bot}  ')'^{2 c_top}  '('^c_mid
#   Singleton simple alpha_4 = E4: ')'^c_E4 at end.
#   Non-touching singletons: nothing.
# ====================================================================

def _chains_for_long(i: int) -> List[Tuple[str, str, str]]:
    """For long simple i in {1,2,3}: list of (bot, top, label) chains in CONVEX
    order of the TOP. Convention: top = beta+alpha_i, bot = beta.

    The chains for alpha_i (long) are: all positive roots beta whose alpha_i-string
    has length 2, i.e. (beta, beta+alpha_i) both in Phi^+.
    """
    # Find all (bot, top) pairs in Phi^+ with top = bot + alpha_i.
    chains = []
    simple_i_name = simple_root(i)
    for bot in ROOTS_CONVEX:
        if bot == simple_i_name:
            continue  # alpha_i itself: handled as singleton ')' at end
        top = root_plus_alpha(bot, i)
        if top is None:
            continue
        chains.append((bot, top))
    # Sort by convex position of top.
    conv_pos = {r: idx for idx, r in enumerate(ROOTS_CONVEX)}
    chains.sort(key=lambda bt: conv_pos[bt[1]])
    return chains


def _chains_for_short() -> List[Tuple[str, str, str]]:
    """For alpha_4 (short): list of (bot, mid, top) chains in convex order of the MID.
    Chains: bot = e_a - e_4, mid = e_a, top = e_a + e_4 for a = 1, 2, 3.
    """
    triples = []
    for a in [1, 2, 3]:
        bot = {1: EM14, 2: EM24, 3: EM34}[a]
        mid = {1: E1,   2: E2,   3: E3}[a]
        top = {1: EP14, 2: EP24, 3: EP34}[a]
        triples.append((bot, mid, top))
    # Sort by convex position of mid.
    conv_pos = {r: idx for idx, r in enumerate(ROOTS_CONVEX)}
    triples.sort(key=lambda bmt: conv_pos[bmt[1]])
    return triples


# Cached:
_LONG_CHAINS = {i: _chains_for_long(i) for i in (1, 2, 3)}
_SHORT_CHAINS = _chains_for_short()


def S_i(pi: KP, i: int) -> List[Tuple[str, str]]:
    """Bracketing sequence for alpha_i in B_4 (CST Def 2.14)."""
    s = []
    if i in (1, 2, 3):
        # Long simple: each length-2 chain contributes ')'^c_top '('^c_bot
        # in convex order of the top. Then ')'^c_simple.
        for (bot, top) in _LONG_CHAINS[i]:
            for _ in range(pi.get(top, 0)):
                s.append((')', top))
            for _ in range(pi.get(bot, 0)):
                s.append(('(', bot))
        simp = simple_root(i)
        for _ in range(pi.get(simp, 0)):
            s.append((')', simp))
        return s
    if i == 4:
        # Short simple: each length-3 chain (bot, mid, top) contributes
        #   ')'^c_mid '('^{2 c_bot} ')'^{2 c_top} '('^c_mid
        # in convex order of the mid. Then ')'^c_E4.
        for (bot, mid, top) in _SHORT_CHAINS:
            for _ in range(pi.get(mid, 0)):
                s.append((')', mid))
            for _ in range(2 * pi.get(bot, 0)):
                s.append(('(', bot))
            for _ in range(2 * pi.get(top, 0)):
                s.append((')', top))
            for _ in range(pi.get(mid, 0)):
                s.append(('(', mid))
        for _ in range(pi.get(E4, 0)):
            s.append((')', E4))
        return s
    raise ValueError(f"i must be 1..4, got {i}")


def cancel(s: list) -> list:
    """Repeatedly cancel adjacent '(', ')' pairs."""
    s = list(s)
    while True:
        for k in range(len(s) - 1):
            if s[k][0] == '(' and s[k + 1][0] == ')':
                del s[k:k + 2]
                break
        else:
            return s


# ====================================================================
# Crystal operators e_i, f_i (CST Def 2.14)
# ====================================================================

def e_i(pi: KP, i: int) -> Optional[KP]:
    """e_i pi: rightmost ')' in S_i^c, beta -> beta - alpha_i (or removed if 0)."""
    pi = kp_clean(pi)
    sc = cancel(S_i(pi, i))
    rightmost_close = None
    for k in range(len(sc) - 1, -1, -1):
        if sc[k][0] == ')':
            rightmost_close = sc[k]
            break
    if rightmost_close is None:
        return None
    beta = rightmost_close[1]
    new_root = root_minus_alpha(beta, i)
    out = kp_add(pi, beta, -1)
    if new_root is not None:
        out = kp_add(out, new_root, +1)
    return kp_clean(out)


def f_i(pi: KP, i: int) -> KP:
    """f_i pi: leftmost '(' in S_i^c, gamma -> gamma + alpha_i.
    If no '(' in S_i^c, f_i pi = pi + alpha_i (simple root added)."""
    pi = kp_clean(pi)
    sc = cancel(S_i(pi, i))
    leftmost_open = None
    for tok in sc:
        if tok[0] == '(':
            leftmost_open = tok
            break
    if leftmost_open is None:
        return kp_clean(kp_add(pi, simple_root(i), +1))
    gamma = leftmost_open[1]
    new_root = root_plus_alpha(gamma, i)
    out = kp_add(pi, gamma, -1)
    if new_root is not None:
        out = kp_add(out, new_root, +1)
    return kp_clean(out)


def e_i_k(pi: KP, i: int, k: int) -> Optional[KP]:
    cur = pi
    for _ in range(k):
        cur = e_i(cur, i)
        if cur is None:
            return None
    return cur


def f_i_k(pi: KP, i: int, k: int) -> KP:
    cur = pi
    for _ in range(k):
        cur = f_i(cur, i)
    return cur


def eps_i(pi: KP, i: int) -> int:
    sc = cancel(S_i(pi, i))
    return sum(1 for c, _ in sc if c == ')')


def phi_i(pi: KP, i: int) -> int:
    sc = cancel(S_i(pi, i))
    return sum(1 for c, _ in sc if c == '(')


# ====================================================================
# Linear combinations of Kostant partitions
# ====================================================================

class LinComb:
    __slots__ = ('terms',)

    def __init__(self, terms=None):
        self.terms = dict(terms) if terms else {}

    @classmethod
    def zero(cls):
        return cls({})

    @classmethod
    def from_kp(cls, pi, coeff=1):
        if pi is None or coeff == 0:
            return cls.zero()
        p = kp_clean(pi)
        return cls({kp_key(p): (p, coeff)})

    def __add__(self, other):
        out = dict(self.terms)
        for k, (pi, c) in other.terms.items():
            if k in out:
                old_pi, old_c = out[k]
                new_c = old_c + c
                if new_c == 0:
                    del out[k]
                else:
                    out[k] = (old_pi, new_c)
            else:
                out[k] = (pi, c)
        return LinComb(out)

    def __sub__(self, other):
        return self + (-1) * other

    def __rmul__(self, scalar):
        if scalar == 0:
            return LinComb.zero()
        return LinComb({k: (pi, scalar * c) for k, (pi, c) in self.terms.items()})

    def __eq__(self, other):
        return dict(self.terms) == dict(other.terms)

    def is_zero(self):
        return not self.terms

    def num_terms(self):
        return len(self.terms)

    def __repr__(self):
        if not self.terms:
            return '0'
        parts = []
        for k in sorted(self.terms.keys()):
            pi, c = self.terms[k]
            if c == 1:
                parts.append(f'({kp_repr(pi)})')
            elif c == -1:
                parts.append(f'-({kp_repr(pi)})')
            else:
                parts.append(f'{c}*({kp_repr(pi)})')
        return ' + '.join(parts).replace('+ -', '- ')


def apply_e(lc, i):
    out = LinComb.zero()
    for k, (pi, coeff) in lc.terms.items():
        out = out + LinComb.from_kp(e_i(pi, i), coeff)
    return out


def apply_f(lc, i):
    out = LinComb.zero()
    for k, (pi, coeff) in lc.terms.items():
        out = out + LinComb.from_kp(f_i(pi, i), coeff)
    return out


def apply_e_k(lc, i, k):
    cur = lc
    for _ in range(k):
        cur = apply_e(cur, i)
    return cur


def apply_B(lc, i):
    """B_i = e_i + f_i."""
    return apply_e(lc, i) + apply_f(lc, i)


def k_i(i):
    return 1 if i in (1, 2, 3) else 2


# ====================================================================
# Enumeration
# ====================================================================

def enumerate_partitions(max_total):
    """Enumerate Kostant partitions pi with sum c <= max_total."""
    out = []
    n = len(ROOTS)
    def recurse(idx, remaining, partial):
        if idx == n:
            out.append(dict(partial))
            return
        for c in range(remaining + 1):
            partial2 = dict(partial)
            if c > 0:
                partial2[ROOTS[idx]] = c
            recurse(idx + 1, remaining - c, partial2)
    recurse(0, max_total, {})
    return out


# ====================================================================
# TEST 0: Crystal axiom verification
# ====================================================================

def test_crystal_axioms(max_total=3):
    print("\n=== TEST 0: Crystal axiom sanity check ===")
    print("  Required: e_i f_i = id always; f_i e_i = id when e_i pi != None.\n")
    all_pass = True
    for i in [1, 2, 3, 4]:
        n_total = 0
        n_ef = 0
        n_fe_slice = 0
        n_fe_slice_ok = 0
        bad_ef = []
        bad_fe = []
        for pi in enumerate_partitions(max_total):
            n_total += 1
            f_pi = f_i(pi, i)
            e_f_pi = e_i(f_pi, i)
            if e_f_pi == kp_clean(pi):
                n_ef += 1
            else:
                bad_ef.append((pi, f_pi, e_f_pi))
            e_pi = e_i(pi, i)
            if e_pi is not None:
                n_fe_slice += 1
                f_e_pi = f_i(e_pi, i)
                if f_e_pi == kp_clean(pi):
                    n_fe_slice_ok += 1
                else:
                    bad_fe.append((pi, e_pi, f_e_pi))
        print(f"  i = {i}:")
        print(f"    e_i f_i = id:           {n_ef}/{n_total}")
        print(f"    f_i e_i = id on slice:  {n_fe_slice_ok}/{n_fe_slice}")
        if bad_ef:
            all_pass = False
            print(f"    *** e_i f_i FAILURES (showing first 5):")
            for pi, f_pi, e_f_pi in bad_ef[:5]:
                print(f"      pi = {kp_repr(pi)} -> f_i pi = {kp_repr(f_pi)} -> e_i f_i pi = {kp_repr(e_f_pi)}")
        if bad_fe:
            all_pass = False
            print(f"    *** f_i e_i FAILURES on slice (showing first 5):")
            for pi, e_pi, f_e_pi in bad_fe[:5]:
                print(f"      pi = {kp_repr(pi)} -> e_i pi = {kp_repr(e_pi)} -> f_i e_i pi = {kp_repr(f_e_pi)}")
    # Test phi_i / f_i^{phi_i+1} = ?
    # Actually: standard crystal axiom is f_i^{phi_i+1} pi = None? No -- on B(infty) f never returns None.
    # But ε_i and φ_i should satisfy: number of '(' in S_i^c equals phi_i. (already by definition)
    # And: e_i applied to pi when eps_i = 0 returns None.
    print("\n  Sanity: e_i returns None iff eps_i = 0.")
    for i in [1, 2, 3, 4]:
        nfail = 0
        for pi in enumerate_partitions(max_total):
            eps = eps_i(pi, i)
            e_pi = e_i(pi, i)
            if (eps == 0) != (e_pi is None):
                nfail += 1
        print(f"    i={i}: failures = {nfail}")
        if nfail > 0:
            all_pass = False
    return all_pass


# ====================================================================
# TEST A: On-slice commutativity  [e_i^{k(i)}, B_i] = 0 on S_i.
# ====================================================================

def test_commutativity_e_k_onslice(max_total=4):
    print("\n=== TEST A: [e_i^{k(i)}, B_i] on the depth-k slice S_i ===\n")
    summary = {}
    for i in [1, 2, 3, 4]:
        k = k_i(i)
        print(f"  i = {i}, k = {k}")
        total = 0
        good = 0
        bad = 0
        bad_examples = []
        for pi in enumerate_partitions(max_total):
            if eps_i(pi, i) < k:
                continue
            total += 1
            pi_lc = LinComb.from_kp(pi)
            ek = apply_e_k(pi_lc, i, k)
            B_ek = apply_B(ek, i)
            B = apply_B(pi_lc, i)
            ek_B = apply_e_k(B, i, k)
            comm = ek_B - B_ek
            if comm.is_zero():
                good += 1
            else:
                bad += 1
                if len(bad_examples) < 5:
                    bad_examples.append((pi, comm))
        print(f"    on-slice partitions tested: {total}")
        print(f"    commutator zero:           {good}")
        print(f"    commutator nonzero:        {bad}")
        if bad_examples:
            print(f"    Sample falsifiers:")
            for pi, comm in bad_examples:
                print(f"      pi = {kp_repr(pi)}: [e^k, B] = {comm}")
        summary[i] = (total, good, bad)
        print()
    return summary


# ====================================================================
# TEST B: Off-slice obstruction
# ====================================================================

def test_offslice(max_total=4):
    print("\n=== TEST B: Off-slice obstruction ===\n")
    summary = {}
    for i in [1, 2, 3, 4]:
        k = k_i(i)
        print(f"  i = {i}, k = {k}")
        for target_eps in range(k):
            print(f"\n    Off-slice locus: eps_{i} = {target_eps}")
            total = 0
            match = 0
            mismatch = 0
            mismatch_examples = []
            for pi in enumerate_partitions(max_total):
                if eps_i(pi, i) != target_eps:
                    continue
                total += 1
                pi_lc = LinComb.from_kp(pi)
                ek = apply_e_k(pi_lc, i, k)
                B_ek = apply_B(ek, i)
                B = apply_B(pi_lc, i)
                ek_B = apply_e_k(B, i, k)
                comm = ek_B - B_ek
                if target_eps == k - 1:
                    expected_pi = e_i_k(pi, i, k - 1) if k - 1 > 0 else kp_clean(pi)
                    expected_lc = LinComb.from_kp(expected_pi) if expected_pi is not None else LinComb.zero()
                else:
                    expected_lc = LinComb.zero()
                if comm == expected_lc:
                    match += 1
                else:
                    mismatch += 1
                    if len(mismatch_examples) < 3:
                        mismatch_examples.append((pi, comm, expected_lc))
            print(f"      tested {total}: match {match}, mismatch {mismatch}")
            if mismatch_examples:
                print(f"      Sample mismatches:")
                for pi, comm, exp in mismatch_examples:
                    print(f"        pi = {kp_repr(pi)}: comm = {comm}, expected = {exp}")
            summary[(i, target_eps)] = (total, match, mismatch)
        print()
    return summary


# ====================================================================
# MAIN
# ====================================================================

if __name__ == '__main__':
    import sys, time
    print("=" * 75)
    print("B_4 type-AII coideal commutativity verification")
    print("  B_i := e_i + f_i (q=0 image of split type-AII coideal generator)")
    print("  k(1) = k(2) = k(3) = 1 (long simples); k(4) = 2 (short simple)")
    print("=" * 75)

    AXIOM_MAX = 3
    SLICE_MAX = 5

    t0 = time.time()
    axioms_ok = test_crystal_axioms(max_total=AXIOM_MAX)
    print(f"\n  Crystal axiom check elapsed: {time.time()-t0:.1f}s")
    if not axioms_ok:
        print("\n!!! CRYSTAL AXIOMS FAILED. STOPPING.")
        sys.exit(1)

    t0 = time.time()
    test_commutativity_e_k_onslice(max_total=SLICE_MAX)
    print(f"  Commutativity test elapsed: {time.time()-t0:.1f}s")

    t0 = time.time()
    test_offslice(max_total=SLICE_MAX)
    print(f"  Off-slice test elapsed: {time.time()-t0:.1f}s")
