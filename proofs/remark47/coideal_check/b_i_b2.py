"""
Computational verification of on-slice coideal commutativity at B_2.

CLEAN STATEMENT.

Let B_i := e_i + f_i be the q=0 image of the type-AII split coideal generator
F_i + zeta E_i K_i^{-1} on B(infty) of type B_2 (with zeta = 1 and K_i^{-1} -> 1
at the crystal limit on the slice).

Let k(i) := units of the s_i orbit swap on Phi^+(B_2):
   k(1) = 1  (s_1-orbit {alpha_1+alpha_2, alpha_2} is a 1-unit short-short swap)
   k(2) = 2  (s_2-orbit {alpha_1, alpha_1+2alpha_2} is a 2-unit long-long swap)

THEOREM (on-slice commutativity).
For each simple i of B_2, on the depth-k slice
    S_i := { pi in Kp(infty) : eps_i(pi) >= k(i) },
the commutator
    [e_i^{k(i)}, B_i] = 0.

OFF-SLICE OBSTRUCTION.
At the boundary eps_i(pi) = k(i) - 1, [e_i^{k(i)}, B_i] pi = -e_i^{k(i)-1} pi
is non-zero.

CST BRIDGE (Criswell-Salisbury-Tingley Thm 3.1, arXiv:1708.04311).
On a tighter sub-slice S_i' ⊂ S_i (characterized below), the operator Aug~_i
of Rick (= reduced orbit-swap at simple i in the s_i-orbit) literally equals
e_i^{k(i)} on Kp(infty), as a deterministic map.  On S_i', therefore,
[Aug~_i, B_i] = 0 follows directly.

Off S_i' (still on S_i = {eps >= k}), Aug~_i and e_i^{k(i)} disagree (Aug~_i acts
via a "long-range" orbit-swap on the alpha_i-chain, while e_i^{k(i)} accumulates
intermediate states).  We characterize S_i' for each i in B_2.

This file verifies both statements computationally.
"""

from collections import defaultdict
from typing import Dict, Tuple, Optional, List

# B_2 positive roots
B11 = 'beta_11'   # alpha_1 = e_1 - e_2 (long)
B12 = 'beta_12'   # alpha_1 + alpha_2 = e_1 (short, s_2-fixed)
G12 = 'gamma_12'  # alpha_1 + 2 alpha_2 = e_1 + e_2 (long)
B22 = 'beta_22'   # alpha_2 = e_2 (short)

ROOTS = [B11, B12, G12, B22]
# Coefficients (a, b) of alpha_1, alpha_2 for each root
ROOT_AB = {B11: (1, 0), B12: (1, 1), G12: (1, 2), B22: (0, 1)}

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


# ====================================================================
# Bracketing sequences S_i(pi) for B_2, per CST Def 2.14
# ====================================================================

def S_i(pi: KP, i: int) -> List[Tuple[str, str]]:
    """Build i-th bracketing sequence as list of (char, root) pairs in convex order."""
    s = []
    if i == 1:
        # alpha_1-chain on Phi^+: (beta_{2,2}, beta_{1,2}) — 1 f_1 step.
        #   beta_{1,1} singleton: e_1 drops it (contributes ')').
        #   gamma_{1,2} singleton: no contribution.
        # CST-style ordering analogous to S_2:
        #   ')' from chain-top (beta_{1,2}), then '(' from chain-bottom (beta_{2,2}),
        #   then ')' singletons at end (beta_{1,1}).
        # Verified to satisfy crystal axioms e_1 f_1 = id (see test_crystal_axioms).
        for _ in range(pi.get(B12, 0)):
            s.append((')', B12))
        for _ in range(pi.get(B22, 0)):
            s.append(('(', B22))
        for _ in range(pi.get(B11, 0)):
            s.append((')', B11))
    elif i == 2:
        # Matches main_check.py / CST Def 2.14:
        # S_2(alpha) = ')'^{c_B12} '('^{2*c_B11} ')'^{2*c_G12} '('^{c_B12} ')'^{c_B22}.
        # (alpha_2-chain: beta_{1,1} -> beta_{1,2} -> gamma_{1,2}, 2 f_2 steps.)
        for _ in range(pi.get(B12, 0)):
            s.append((')', B12))
        for _ in range(2 * pi.get(B11, 0)):
            s.append(('(', B11))
        for _ in range(2 * pi.get(G12, 0)):
            s.append((')', G12))
        for _ in range(pi.get(B12, 0)):
            s.append(('(', B12))
        for _ in range(pi.get(B22, 0)):
            s.append((')', B22))
    else:
        raise ValueError(f"i must be 1 or 2, got {i}")
    return s


def cancel(s: list) -> list:
    """Repeatedly cancel adjacent '(',')' pairs."""
    s = list(s)
    while True:
        for k in range(len(s) - 1):
            if s[k][0] == '(' and s[k + 1][0] == ')':
                del s[k:k + 2]
                break
        else:
            return s


# ====================================================================
# Root arithmetic
# ====================================================================

def simple_root(i):
    return B11 if i == 1 else B22


def root_minus_alpha(beta, i):
    """beta - alpha_i.  Returns root name or None if not in Phi^+ (incl. 0)."""
    if i == 1:
        return {B11: None, B12: B22, G12: None, B22: None}[beta]
    return {B11: None, B12: B11, G12: B12, B22: None}[beta]


def root_plus_alpha(beta, i):
    """beta + alpha_i.  Returns root name or None if not in Phi^+."""
    if i == 1:
        return {B11: None, B12: None, G12: None, B22: B12}[beta]
    return {B11: B12, B12: G12, G12: None, B22: None}[beta]


# ====================================================================
# Crystal operators e_i, f_i (CST Def 2.14)
# ====================================================================

def e_i(pi: KP, i: int) -> Optional[KP]:
    """e_i pi: pick rightmost ')' in S_i^c, replace its root beta by beta-alpha_i."""
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
    """f_i pi: pick leftmost '(' in S_i^c, replace its root gamma by gamma+alpha_i.
    If no '(' in S_i^c, f_i pi = pi + alpha_i."""
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
    """epsilon_i(pi) = number of ')' in S_i^c(pi)."""
    sc = cancel(S_i(pi, i))
    return sum(1 for c, _ in sc if c == ')')


def phi_i(pi: KP, i: int) -> int:
    """phi_i(pi) = number of '(' in S_i^c(pi)."""
    sc = cancel(S_i(pi, i))
    return sum(1 for c, _ in sc if c == '(')


# ====================================================================
# Linear combinations of Kostant partitions
# ====================================================================

class LinComb:
    """Z-linear combination of Kostant partitions."""

    __slots__ = ('terms',)

    def __init__(self, terms=None):
        # terms: dict kp_key -> (pi_dict, coeff)
        self.terms = dict(terms) if terms else {}

    @classmethod
    def zero(cls):
        return cls({})

    @classmethod
    def from_kp(cls, pi: KP, coeff=1):
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


def apply_e(lc: LinComb, i: int) -> LinComb:
    out = LinComb.zero()
    for k, (pi, coeff) in lc.terms.items():
        out = out + LinComb.from_kp(e_i(pi, i), coeff)
    return out


def apply_f(lc: LinComb, i: int) -> LinComb:
    out = LinComb.zero()
    for k, (pi, coeff) in lc.terms.items():
        out = out + LinComb.from_kp(f_i(pi, i), coeff)
    return out


def apply_e_k(lc: LinComb, i: int, k: int) -> LinComb:
    cur = lc
    for _ in range(k):
        cur = apply_e(cur, i)
    return cur


def apply_B(lc: LinComb, i: int) -> LinComb:
    """B_i = e_i + f_i."""
    return apply_e(lc, i) + apply_f(lc, i)


# ====================================================================
# Aug~ orbit-swap (deterministic, e-direction = raise wt by k*alpha_i)
# ====================================================================

def aug_e(pi: KP, i: int) -> Optional[KP]:
    """Aug~_i e-direction: orbit-swap c_donor -= 1, c_receiver += 1.

    i=1: orbit {B12, B22}, donor B12, receiver B22. Wt change +alpha_1.
    i=2: orbit {B11, G12}, donor G12, receiver B11. Wt change +2 alpha_2.
    """
    if i == 1:
        if pi.get(B12, 0) < 1:
            return None
        out = kp_add(pi, B12, -1)
        out = kp_add(out, B22, +1)
        return kp_clean(out)
    if i == 2:
        if pi.get(G12, 0) < 1:
            return None
        out = kp_add(pi, G12, -1)
        out = kp_add(out, B11, +1)
        return kp_clean(out)
    raise ValueError(i)


def aug_f(pi: KP, i: int) -> Optional[KP]:
    """Aug~_i f-direction: orbit-swap c_donor -= 1, c_receiver += 1, wt change -k*alpha_i."""
    if i == 1:
        if pi.get(B22, 0) < 1:
            return None
        out = kp_add(pi, B22, -1)
        out = kp_add(out, B12, +1)
        return kp_clean(out)
    if i == 2:
        if pi.get(B11, 0) < 1:
            return None
        out = kp_add(pi, B11, -1)
        out = kp_add(out, G12, +1)
        return kp_clean(out)
    raise ValueError(i)


def k_i(i):
    return 1 if i == 1 else 2


# ====================================================================
# Enumeration
# ====================================================================

def enumerate_partitions(max_total):
    out = []
    for c11 in range(max_total + 1):
        for c12 in range(max_total + 1 - c11):
            for cG12 in range(max_total + 1 - c11 - c12):
                for c22 in range(max_total + 1 - c11 - c12 - cG12):
                    pi = {}
                    if c11: pi[B11] = c11
                    if c12: pi[B12] = c12
                    if cG12: pi[G12] = cG12
                    if c22: pi[B22] = c22
                    out.append(pi)
    return out


# ====================================================================
# TEST A: [e_i^{k(i)}, B_i] = 0 on the depth-k slice {eps_i >= k}.
# ====================================================================

def test_commutativity_e_k(max_total=5):
    print("\n=== TEST A: [e_i^{k(i)}, B_i] on the depth-k slice S_i = {eps_i >= k} ===\n")
    for i in [1, 2]:
        k = k_i(i)
        print(f"  i = {i}, k = {k}")
        total = 0
        good = 0
        bad = 0
        bad_examples = []
        for pi in enumerate_partitions(max_total):
            eps = eps_i(pi, i)
            if eps < k:
                continue
            total += 1
            # Compute [e_i^k, B_i] pi as a LinComb.
            pi_lc = LinComb.from_kp(pi)
            # B_i (e_i^k pi)
            ek = apply_e_k(pi_lc, i, k)
            B_ek = apply_B(ek, i)
            # e_i^k (B_i pi)
            B = apply_B(pi_lc, i)
            ek_B = apply_e_k(B, i, k)
            comm = ek_B - B_ek
            if comm.is_zero():
                good += 1
            else:
                bad += 1
                if len(bad_examples) < 5:
                    bad_examples.append((pi, eps, comm))
        print(f"    on-slice partitions tested: {total}")
        print(f"    commutator zero: {good}")
        print(f"    commutator nonzero: {bad}")
        if bad_examples:
            print(f"    NONZERO EXAMPLES:")
            for pi, eps, comm in bad_examples:
                print(f"      pi = {kp_repr(pi)}, eps_{i} = {eps}, [e^k, B] = {comm}")
        print()


# ====================================================================
# TEST B: [e_i^{k(i)}, B_i] OFF the slice (eps_i < k).
# ====================================================================

def test_commutativity_offslice(max_total=5):
    print("\n=== TEST B: [e_i^{k(i)}, B_i] OFF the slice ===\n")
    for i in [1, 2]:
        k = k_i(i)
        print(f"  i = {i}, k = {k}")
        for target_eps in range(k):
            print(f"\n    Off-slice locus: eps_{i} = {target_eps}")
            total = 0
            zero = 0
            nonzero = 0
            examples = []
            for pi in enumerate_partitions(max_total):
                eps = eps_i(pi, i)
                if eps != target_eps:
                    continue
                total += 1
                pi_lc = LinComb.from_kp(pi)
                ek = apply_e_k(pi_lc, i, k)  # = 0 since eps < k
                B_ek = apply_B(ek, i)
                B = apply_B(pi_lc, i)
                ek_B = apply_e_k(B, i, k)
                comm = ek_B - B_ek
                if comm.is_zero():
                    zero += 1
                else:
                    nonzero += 1
                    if len(examples) < 3:
                        examples.append((pi, comm))
            print(f"      tested {total} partitions.  Commutator zero: {zero}.  Non-zero: {nonzero}.")
            if examples:
                for pi, comm in examples:
                    print(f"        pi = {kp_repr(pi)}, [e^k, B] = {comm}")


# ====================================================================
# TEST C: When does Aug~_i (e-direction) literally equal e_i^{k(i)} on Kp?
# ====================================================================

def test_aug_identification(max_total=5):
    print("\n=== TEST C: When Aug~_i = e_i^{k(i)} literally on Kp(infty) ===\n")
    for i in [1, 2]:
        k = k_i(i)
        print(f"  i = {i}, k = {k}")
        print(f"  Aug~_i: c_{'B12' if i==1 else 'G12'} -= 1, c_{'B22' if i==1 else 'B11'} += 1.")
        match = []
        mismatch = []
        for pi in enumerate_partitions(max_total):
            eps = eps_i(pi, i)
            aug = aug_e(pi, i)
            ek = e_i_k(pi, i, k)
            # Normalize None to vacuum-empty for comparison? Or just compare None == None.
            if aug == ek:
                match.append((pi, eps))
            else:
                mismatch.append((pi, eps, aug, ek))
        n_match = len(match)
        n_mismatch = len(mismatch)
        print(f"    {n_match} pi where aug_e == e_i^k.")
        print(f"    {n_mismatch} pi where they differ.")
        print(f"    Mismatch examples:")
        for pi, eps, aug, ek in mismatch[:8]:
            print(f"      pi = {kp_repr(pi)}: aug = {kp_repr(aug) if aug else '0'}, e^k = {kp_repr(ek) if ek else '0'}  (eps_{i} = {eps})")
        # Characterize the match set
        print(f"\n    Characterizing the match set...")
        match_partitions_only = [(pi, eps) for pi, eps in match if aug_e(pi, i) is not None]
        # The "interesting" matches: where aug is nonzero (= donor cap >= 1).
        print(f"    Match set with aug != 0:")
        for pi, eps in match_partitions_only[:10]:
            c_B11 = pi.get(B11, 0); c_B12 = pi.get(B12, 0); c_G12 = pi.get(G12, 0); c_B22 = pi.get(B22, 0)
            print(f"      pi = {kp_repr(pi)}: c_B11={c_B11}, c_B12={c_B12}, c_G12={c_G12}, c_B22={c_B22}, eps={eps}")
        print()


# ====================================================================
# TEST D: [Aug~_i (orbit-swap), B_i] = 0 directly.
# Test on the sub-slice S_i' where Aug~_i = e_i^k holds.
# ====================================================================

def test_commutativity_aug_orbit_swap(max_total=5):
    print("\n=== TEST D: [Aug~_i orbit-swap, B_i] directly (sub-slice where aug = e^k) ===\n")
    for i in [1, 2]:
        k = k_i(i)
        print(f"  i = {i}, k = {k}")
        good = 0
        bad = 0
        examples = []
        n_subslice = 0
        for pi in enumerate_partitions(max_total):
            aug = aug_e(pi, i)
            ek = e_i_k(pi, i, k)
            if aug is None and ek is None:
                continue  # both zero
            if aug != ek:
                continue  # not in subslice S_i'
            if aug is None:
                continue  # both zero but trivially equal
            n_subslice += 1
            # On subslice: Aug~_i pi = e_i^k pi (literally).
            # Test commutativity by computing both sides via aug_e and B_i.
            pi_lc = LinComb.from_kp(pi)
            # B_i (Aug~_i pi) = (e+f)(aug_e pi)
            aug_pi_lc = LinComb.from_kp(aug)
            B_aug = apply_B(aug_pi_lc, i)
            # Aug~_i (B_i pi) = aug_e applied to (e+f) pi, term-by-term
            B = apply_B(pi_lc, i)
            aug_B = LinComb.zero()
            for kk, (term_pi, coeff) in B.terms.items():
                aug_term = aug_e(term_pi, i)
                aug_B = aug_B + LinComb.from_kp(aug_term, coeff)
            comm = aug_B - B_aug
            if comm.is_zero():
                good += 1
            else:
                bad += 1
                if len(examples) < 5:
                    examples.append((pi, comm))
        print(f"    Sub-slice partitions (aug = e^k, both nonzero): {n_subslice}")
        print(f"    [Aug~, B] zero: {good}, nonzero: {bad}")
        if examples:
            print(f"    Nonzero examples:")
            for pi, comm in examples:
                print(f"      pi = {kp_repr(pi)}: [Aug~, B] = {comm}")
        print()


# ====================================================================
# MAIN
# ====================================================================

def test_crystal_axioms(max_total=5):
    """Verify e_i f_i = id on all Kp(infty) at B_2 (basic crystal axiom)."""
    print("\n=== CRYSTAL AXIOM SANITY: e_i f_i = id and f_i e_i = id on slice ===\n")
    for i in [1, 2]:
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
            # f_i e_i = id when e_i pi != 0
            e_pi = e_i(pi, i)
            if e_pi is not None:
                n_fe_slice += 1
                f_e_pi = f_i(e_pi, i)
                if f_e_pi == kp_clean(pi):
                    n_fe_slice_ok += 1
                else:
                    bad_fe.append((pi, e_pi, f_e_pi))
        print(f"  i = {i}:")
        print(f"    e_i f_i = id: {n_ef}/{n_total}")
        print(f"    f_i e_i = id on slice: {n_fe_slice_ok}/{n_fe_slice}")
        if bad_ef:
            print(f"    e_i f_i FAILURES:")
            for pi, f_pi, e_f_pi in bad_ef[:5]:
                print(f"      pi = {kp_repr(pi)}, f_i pi = {kp_repr(f_pi)}, e_i f_i pi = {kp_repr(e_f_pi)}")
        if bad_fe:
            print(f"    f_i e_i FAILURES on slice:")
            for pi, e_pi, f_e_pi in bad_fe[:5]:
                print(f"      pi = {kp_repr(pi)}, e_i pi = {kp_repr(e_pi)}, f_i e_i pi = {kp_repr(f_e_pi)}")


if __name__ == '__main__':
    print("=" * 75)
    print("B_2 type-AII coideal commutativity verification")
    print("  B_i := e_i + f_i  (the q=0 image of the type-AII coideal generator)")
    print("  k(1) = 1, k(2) = 2")
    print("=" * 75)

    test_crystal_axioms(max_total=4)
    test_commutativity_e_k(max_total=5)
    test_commutativity_offslice(max_total=5)
    test_aug_identification(max_total=4)
    test_commutativity_aug_orbit_swap(max_total=5)
