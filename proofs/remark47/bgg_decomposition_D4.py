"""
BGG-Verma bigraded decomposition for D_4 = so(8).

Mirrors bgg_decomposition_B3.py.  D_4 is simply-laced (one root length),
so there is no canonical (q,t)-bigrading coming from root-length.  We still
define a useful bigrading by splitting the 12 positive roots into two natural
W(A_3)-orbits:

    'L'  =  e_i + e_j   (i < j)    [bidegree (1,0)]   — "plus-roots", 6 of them
    'S'  =  e_i - e_j   (i < j)    [bidegree (0,1)]   — "minus-roots", 6 of them

The full Weyl group W(D_4) does NOT preserve this split (sign-change reflections
mix the two), so this bigrading is W(A_3)-equivariant but NOT W(D_4)-equivariant.
That is fine for the *bookkeeping* — we still compute χ_{q,t} = supp_even - supp_odd
and the "acyclic" check is intrinsic.

We also report the simpler single-graded χ_q (each root contributes q^1) as a
sanity check.

Conventions:
* Root system D_4 in R^4. Positive roots: {e_i ± e_j : 1 ≤ i < j ≤ 4}, 12 in total.
* Simple roots: α_1 = e_1-e_2, α_2 = e_2-e_3, α_3 = e_3-e_4, α_4 = e_3+e_4.
* ρ = sum of fundamental weights = (3, 2, 1, 0).  (Equivalently ρ = ½·sum_{α>0}α.)
* Weyl group W(D_4): signed permutations with EVEN number of sign-flips, |W|=192.
* Dot action: w·λ = w(λ+ρ) - ρ.
* (q,t)-Kostant K_{q,t}(β) = Σ_{decomp of β into pos roots} q^(#L-roots) t^(#S-roots).
* BGG identity: KL_{λ,μ}(q,t) = Σ_w (-1)^{ℓ(w)} K_{q,t}(w·λ - μ).

D_4 has TWO spin lattices (the two half-spin representations):
  Spin1:  ρ + integer combos of fundamental weights with ω_3 odd  — equivalently
          λ ∈ (½, ½, ½, ½) + Z^4 with λ_4 having the SAME sign-parity as ω_3-content.
  Spin2:  half-integer weights but in the OTHER ω_4 coset.

For dominant half-spin weights in D_4 with all λ_i ≥ 0 of form (a+½, b+½, c+½, d+½):
  the parity bit is (a+b+c+d) mod 2 (this distinguishes the two spin lattices).
  We will tag each spin pair by (parity_of_λ, parity_of_μ) and report separately.
"""

from fractions import Fraction
from collections import defaultdict, Counter
from itertools import permutations, product


# ============================================================
# Root system D_4
# ============================================================

N = 4

def positive_roots_D4():
    """Return list of positive roots, tagged 'L' (e_i+e_j) or 'S' (e_i-e_j)."""
    roots = []
    # "S" = e_i - e_j, i<j
    for i in range(N):
        for j in range(i + 1, N):
            v = [0] * N
            v[i] = 1
            v[j] = -1
            roots.append((tuple(v), 'S'))
    # "L" = e_i + e_j, i<j
    for i in range(N):
        for j in range(i + 1, N):
            v = [0] * N
            v[i] = 1
            v[j] = 1
            roots.append((tuple(v), 'L'))
    return roots


POS_ROOTS = positive_roots_D4()
POS_ROOTS_SET = set(r for r, _ in POS_ROOTS)
NEG_ROOTS_SET = set(tuple(-x for x in r) for r in POS_ROOTS_SET)

# ρ for D_4 = (n-1, n-2, ..., 1, 0) = (3, 2, 1, 0).
RHO = tuple(Fraction(N - 1 - i) for i in range(N))

# Sanity check: |POS_ROOTS| = 2 * C(4,2) = 12.
assert len(POS_ROOTS) == 12

# Verify ρ = ½ sum of positive roots:
_rho_check = [Fraction(0)] * N
for r, _ in POS_ROOTS:
    for i in range(N):
        _rho_check[i] += Fraction(r[i], 2)
assert tuple(_rho_check) == RHO, (tuple(_rho_check), RHO)


# ============================================================
# Weyl group W(D_4): signed permutations with EVEN number of sign-flips.
# |W(D_4)| = 4! * 2^3 = 192.
# ============================================================

def weyl_D4():
    """Yield list of (w_func, length, label) for w in W(D_4)."""
    out = []
    for perm in permutations(range(N)):
        for signs in product([1, -1], repeat=N):
            # Even number of negative signs
            if sum(1 for s in signs if s == -1) % 2 != 0:
                continue
            sg = signs
            pm = perm
            def w(v, sg=sg, pm=pm):
                return tuple(sg[i] * v[pm[i]] for i in range(N))
            length = length_via_inversions(w)
            out.append((w, length, (pm, sg)))
    return out


def length_via_inversions(w_func):
    """ℓ(w) = #(positive roots whose image is negative)."""
    cnt = 0
    for r in POS_ROOTS_SET:
        wr = w_func(r)
        if wr in NEG_ROOTS_SET:
            cnt += 1
    return cnt


# ============================================================
# Bigraded Kostant partition function for D_4.
# ============================================================
#
# Order roots to maximize pruning: group by leading-nonzero coord.
# - Group A (lead = coord 0): all roots with first coord = 1.
#       e_1-e_2, e_1-e_3, e_1-e_4, e_1+e_2, e_1+e_3, e_1+e_4    [6 roots]
# - Group B (lead = coord 1): roots with first coord = 0, second = 1.
#       e_2-e_3, e_2-e_4, e_2+e_3, e_2+e_4   [4 roots]
# - Group C (lead = coord 2): roots with first two = 0, third = 1.
#       e_3-e_4, e_3+e_4   [2 roots]
# - Group D: would be roots with first three = 0, fourth = 1 — but there are none
#   (no single e_4 positive root in D_4).
#
# Note: in D_4 there is no positive root supported on the last coordinate alone;
# the constraint coord 3 = 0 must be enforced by combinations within Groups A-C.
# In particular, the "minus" roots e_i - e_4 contribute -1 in coord 3, and the
# "plus" roots e_i + e_4 contribute +1 in coord 3. So coord-3 balancing happens
# across groups.

POS_ROOTS_ORDERED = []
# Group A: first coord = 1
for j in range(1, N):
    v = [0] * N; v[0] = 1; v[j] = -1
    POS_ROOTS_ORDERED.append((tuple(v), 'S'))
for j in range(1, N):
    v = [0] * N; v[0] = 1; v[j] = 1
    POS_ROOTS_ORDERED.append((tuple(v), 'L'))
# Group B: first coord = 0, second coord = 1
for j in range(2, N):
    v = [0] * N; v[1] = 1; v[j] = -1
    POS_ROOTS_ORDERED.append((tuple(v), 'S'))
for j in range(2, N):
    v = [0] * N; v[1] = 1; v[j] = 1
    POS_ROOTS_ORDERED.append((tuple(v), 'L'))
# Group C: first two coords = 0, third coord = 1
POS_ROOTS_ORDERED.append(((0, 0, 1, -1), 'S'))
POS_ROOTS_ORDERED.append(((0, 0, 1, 1), 'L'))

assert len(POS_ROOTS_ORDERED) == 12
assert set(r for r, _ in POS_ROOTS_ORDERED) == POS_ROOTS_SET

# Index boundaries where pruning by coord index kicks in.
GROUP_A_END = 6   # after 6 roots processed, only Group B+C remain; remaining[0] must be 0
GROUP_B_END = 10  # after 10 roots processed, only Group C remains; remaining[1] must be 0
# After all 12 roots, remaining must be (0,0,0,0).


def kostant_qt_D4(beta):
    """Return dict (q,t) -> nonneg int = #decompositions of β as pos-root combo,
    weighted by (#L, #S).  β must be integer-valued.
    """
    # Validate integrality
    bvals = []
    for x in beta:
        try:
            xi = int(x)
        except (TypeError, ValueError):
            return {}
        if x != xi:
            return {}
        bvals.append(xi)
    target = tuple(bvals)

    # Quick rejects:
    # All positive roots have first coord in {0,1}, so remaining[0] must be ≥ 0
    # throughout.  Similarly for cumulative leading sums.
    if target[0] < 0:
        return {}
    # Sum of all coords of any pos root is in {0, 2} for L and {0} for S.
    # So sum(target) must be ≥ 0 and even.
    s = sum(target)
    if s < 0 or s % 2 != 0:
        return {}

    memo = {}

    def recurse(idx, remaining):
        # Pruning by group boundaries
        if idx >= GROUP_A_END and remaining[0] != 0:
            return {}
        if idx >= GROUP_B_END and remaining[1] != 0:
            return {}
        if idx == len(POS_ROOTS_ORDERED):
            if remaining == (0, 0, 0, 0):
                return {(0, 0): 1}
            return {}
        if remaining[0] < 0:
            return {}

        key = (idx, remaining)
        if key in memo:
            return memo[key]

        root, kind = POS_ROOTS_ORDERED[idx]
        # Compute max copies of this root.
        # In Group A (first coord = 1): n ≤ remaining[0].
        # In Group B (second coord = 1, first = 0): n ≤ remaining[1].
        # In Group C (third coord = 1, first/second = 0): n ≤ remaining[2].
        if idx < GROUP_A_END:
            max_n = max(0, remaining[0])
        elif idx < GROUP_B_END:
            max_n = max(0, remaining[1])
        else:
            max_n = max(0, remaining[2])
        # Conservative outer bound
        max_n = min(max_n, sum(abs(r) for r in remaining) + 1)

        result = defaultdict(int)
        for n in range(max_n + 1):
            new_rem = tuple(remaining[i] - n * root[i] for i in range(N))
            if new_rem[0] < 0:
                break
            # Within group A, later group-A roots also have first coord 1,
            # so if new_rem[0] < 0 we must break.  (Already checked.)
            sub = recurse(idx + 1, new_rem)
            for (q, t), c in sub.items():
                if kind == 'L':
                    result[(q + n, t)] += c
                else:
                    result[(q, t + n)] += c

        result = dict(result)
        memo[key] = result
        return result

    out = recurse(0, target)
    return {k: v for k, v in out.items() if v != 0}


def kostant_qt(beta):
    return kostant_qt_D4(beta)


# ============================================================
# BGG-Verma analysis
# ============================================================

def analyze(lam, mu, weyl=None):
    """Return dict with chi (bigraded), chi_q (single-graded), mult_even, mult_odd,
    positive_qt, acyclic_qt, positive_q (single-graded positivity), agree.

    NOTE: In D_n (simply-laced), the (q,t)-bigrading we use (L=e_i+e_j, S=e_i-e_j)
    is NOT W(D_n)-invariant — sign-flip Weyl elements exchange L and S roots.
    So bigraded acyclicity is NOT expected.  The single-graded χ_q (where every
    root contributes q^1) IS canonical and is the actual D_n KL polynomial.
    """
    if weyl is None:
        weyl = weyl_D4()
    lr = tuple(Fraction(lam[i]) + RHO[i] for i in range(N))
    mr = tuple(Fraction(mu[i]) + RHO[i] for i in range(N))

    chi = defaultdict(int)
    mult_even = defaultdict(int)
    mult_odd = defaultdict(int)
    for w_func, length, label in weyl:
        wlr = w_func(lr)
        diff = tuple(wlr[i] - mr[i] for i in range(N))
        kqt = kostant_qt(diff)
        sign = (-1) ** length
        for k, v in kqt.items():
            chi[k] += sign * v
            if length % 2 == 0:
                mult_even[k] += v
            else:
                mult_odd[k] += v

    chi = {k: v for k, v in chi.items() if v != 0}
    # Single-graded chi_q: collapse bidegree (a, b) to a+b.
    chi_q = defaultdict(int)
    for (qd, td), c in chi.items():
        chi_q[qd + td] += c
    chi_q = {k: v for k, v in chi_q.items() if v != 0}

    positive_qt = all(v >= 0 for v in chi.values())
    positive_q = all(v >= 0 for v in chi_q.values())
    acyclic_qt = True
    all_keys = set(mult_even.keys()) | set(mult_odd.keys())
    for k in all_keys:
        if mult_odd.get(k, 0) > mult_even.get(k, 0):
            acyclic_qt = False
            break
    agree = (positive_qt == acyclic_qt)

    return {
        'lam': lam, 'mu': mu,
        'chi': chi,
        'chi_q': chi_q,
        'mult_even': dict(mult_even),
        'mult_odd': dict(mult_odd),
        'positive_qt': positive_qt,
        'positive_q': positive_q,
        'acyclic_qt': acyclic_qt,
        # Keep old names for backward compat
        'positive': positive_qt,
        'acyclic': acyclic_qt,
        'agree': agree,
    }


def fmt_q(d):
    """Format a dict deg -> coef as a polynomial in q."""
    if not d:
        return "0"
    parts = []
    for deg, c in sorted(d.items()):
        if deg == 0:
            mon = "1"
        elif deg == 1:
            mon = "q"
        else:
            mon = f"q^{deg}"
        if c == 1:
            parts.append(mon)
        elif c == -1:
            parts.append("-" + mon)
        else:
            parts.append(f"{c}*{mon}")
    return " + ".join(parts).replace("+ -", "- ")


def fmt_qt(d):
    if not d:
        return "0"
    parts = []
    for (qd, td), c in sorted(d.items()):
        if qd == 0 and td == 0:
            mon = "1"
        elif qd == 0:
            mon = "t" if td == 1 else f"t^{td}"
        elif td == 0:
            mon = "q" if qd == 1 else f"q^{qd}"
        else:
            qmon = "q" if qd == 1 else f"q^{qd}"
            tmon = "t" if td == 1 else f"t^{td}"
            mon = qmon + tmon
        if c == 1:
            parts.append(mon)
        elif c == -1:
            parts.append("-" + mon)
        else:
            parts.append(f"{c}*{mon}")
    return " + ".join(parts).replace("+ -", "- ")


# ============================================================
# Enumerate dominant pairs.
# Dominance for D_n: λ_1 ≥ λ_2 ≥ ... ≥ λ_{n-1} ≥ |λ_n|.
# ============================================================

def enumerate_dominant_integer_pairs(max_lam1=3):
    pairs = []
    for l1 in range(max_lam1 + 1):
        for l2 in range(l1 + 1):
            for l3 in range(l2 + 1):
                # λ_4 in [-l3, l3]
                for l4 in range(-l3, l3 + 1):
                    lam = (l1, l2, l3, l4)
                    # μ dominant integer with μ_1 ≤ l1 etc — we want μ s.t. λ ≥ μ in suitable sense.
                    # Simplest: enumerate μ in {0,...,l1} block with same dominance.
                    for m1 in range(l1 + 1):
                        for m2 in range(m1 + 1):
                            for m3 in range(m2 + 1):
                                for m4 in range(-m3, m3 + 1):
                                    mu = (m1, m2, m3, m4)
                                    pairs.append((lam, mu))
    return pairs


def enumerate_spin_pairs(max_lam1_doubled=7):
    """Spin pairs: weights (λ_1, λ_2, λ_3, λ_4) with all λ_i half-integers,
    dominant: λ_1 ≥ λ_2 ≥ λ_3 ≥ |λ_4|, and 2*λ_1 ≤ max_lam1_doubled.

    Each spin weight has a "spin parity":
        spin1 if λ_4 > 0 (i.e., λ_4 = positive half-integer in dominant orbit),
        spin2 if λ_4 < 0.
    (Equivalently, the parity of the integer part of 2λ_4 + something — but for
    *dominant* spin weights with λ_4 ≠ 0, sign of λ_4 distinguishes the lattices.
    For λ_4 = 0 the weight is fixed by the diagram automorphism and lies on the
    wall between the two spin reps.)

    NOTE: In D_4, λ_4 takes values in {±1/2, ±3/2, ...} for spin weights.
    The dominant chamber for D_n requires λ_3 ≥ |λ_4|, so both signs of λ_4 are allowed
    so long as |λ_4| ≤ λ_3.  λ_4 ≠ 0 since λ_4 is a half-integer.
    """
    F = Fraction
    half = F(1, 2)
    pairs = []
    for l1d in range(1, max_lam1_doubled + 1, 2):  # 1, 3, 5, 7 -> λ_1 = 1/2, 3/2, 5/2, 7/2
        for l2d in range(1, l1d + 1, 2):
            for l3d in range(1, l2d + 1, 2):
                for l4d_abs in range(1, l3d + 1, 2):
                    for l4_sign in (1, -1):
                        l4d = l4_sign * l4d_abs
                        lam = (F(l1d, 2), F(l2d, 2), F(l3d, 2), F(l4d, 2))
                        # Spin parity: sign(λ_4).  We label as 'spin1' if positive, 'spin2' if negative.
                        spin_type = 'spin1' if l4d > 0 else 'spin2'
                        for m1d in range(1, l1d + 1, 2):
                            for m2d in range(1, m1d + 1, 2):
                                for m3d in range(1, m2d + 1, 2):
                                    for m4d_abs in range(1, m3d + 1, 2):
                                        for m4_sign in (1, -1):
                                            m4d = m4_sign * m4d_abs
                                            mu = (F(m1d, 2), F(m2d, 2), F(m3d, 2), F(m4d, 2))
                                            mu_spin = 'spin1' if m4d > 0 else 'spin2'
                                            pairs.append((lam, mu, spin_type, mu_spin))
    return pairs


# ============================================================
# Sanity tests
# ============================================================

def kostant_qt_bruteforce(beta, max_n_each=4, max_total=8):
    """Brute-force Kostant calculation for verification."""
    from itertools import product as iproduct
    target = tuple(int(x) for x in beta)
    roots = POS_ROOTS_ORDERED
    count = defaultdict(int)
    for ns in iproduct(range(max_n_each + 1), repeat=len(roots)):
        if sum(ns) > max_total:
            continue
        s = [0] * N
        for n, (r, _) in zip(ns, roots):
            for i in range(N):
                s[i] += n * r[i]
        if tuple(s) == target:
            q = sum(n for n, (_, k) in zip(ns, roots) if k == 'L')
            t = sum(n for n, (_, k) in zip(ns, roots) if k == 'S')
            count[(q, t)] += 1
    return dict(count)


def sanity_tests():
    print("=" * 70)
    print("Sanity tests — Kostant function")
    print("=" * 70)
    # K((0,0,0,0)) = 1
    print(f"K_qt((0,0,0,0)) = {fmt_qt(kostant_qt((0,0,0,0)))}  (expected: 1)")
    # Verify K((1,1,0,0)) matches brute force.  Note: D_4 has many chain-cancellation
    # decompositions (e.g., (e_1-e_2)+(e_2-e_3)+(e_3-e_4)+(e_1+e_4) = (2,0,0,0)),
    # so K_qt is NOT obvious by hand.
    bf = kostant_qt_bruteforce((1, 1, 0, 0))
    fast = kostant_qt((1, 1, 0, 0))
    match = (bf == fast)
    print(f"K_qt((1,1,0,0)) = {fmt_qt(fast)}")
    print(f"   brute force:  {fmt_qt(bf)}")
    print(f"   MATCH: {match}")
    bf = kostant_qt_bruteforce((2, 0, 0, 0))
    fast = kostant_qt((2, 0, 0, 0))
    match = (bf == fast)
    print(f"K_qt((2,0,0,0)) = {fmt_qt(fast)}")
    print(f"   brute force:  {fmt_qt(bf)}")
    print(f"   MATCH: {match}")
    bf = kostant_qt_bruteforce((1, 1, 1, 1))
    fast = kostant_qt((1, 1, 1, 1))
    match = (bf == fast)
    print(f"K_qt((1,1,1,1)) = {fmt_qt(fast)}")
    print(f"   brute force:  {fmt_qt(bf)}")
    print(f"   MATCH: {match}")
    bf = kostant_qt_bruteforce((1, 1, 1, -1))
    fast = kostant_qt((1, 1, 1, -1))
    match = (bf == fast)
    print(f"K_qt((1,1,1,-1)) = {fmt_qt(fast)}")
    print(f"   brute force:  {fmt_qt(bf)}")
    print(f"   MATCH: {match}")
    # The smallest sanity check: highest root (2ρ for D_4 in basis terms is sum of pos roots,
    # but we'll just check a few easy ones).
    print(f"K_qt((1,1,1,-1)) = K_qt((1,1,1,1)) at the matching bidegrees?")
    # (1,1,1,1) and (1,1,1,-1) are related by sign-flip of last coord, which is in W(D_4)
    # only if we flip an EVEN number of signs.  Sign-flipping only coord 4 is NOT in W(D_4),
    # but is in W(B_4) — so K_qt may differ between (1,1,1,1) and (1,1,1,-1).
    # The disparity is informative.
    print()


def weyl_distribution_check(weyl):
    """Print length distribution of W(D_4) and compare to Poincaré poly."""
    lens = Counter(l for _, l, _ in weyl)
    print(f"|W(D_4)| = {len(weyl)} (expected 192)")
    print(f"Length distribution: {dict(sorted(lens.items()))}")
    # Poincaré of W(D_4) = [2]_q[4]_q[6]_q [4]_q (where one [4] is the D-specific
    # exponent).  Actually exponents of D_4 are (1, 3, 3, 5), so
    # Poincaré = [2]_q * [4]_q * [4]_q * [6]_q.
    # Let's compute:
    P = [1]
    def mul_poly(p, q_list):
        out = [0] * (len(p) + len(q_list) - 1)
        for i, a in enumerate(p):
            for j, b in enumerate(q_list):
                out[i + j] += a * b
        return out
    def qbracket(k):
        return [1] * k
    P = mul_poly(P, qbracket(2))
    P = mul_poly(P, qbracket(4))
    P = mul_poly(P, qbracket(4))
    P = mul_poly(P, qbracket(6))
    expected = {i: c for i, c in enumerate(P) if c}
    print(f"Expected from Poincaré [2][4][4][6]: {expected}")
    print(f"Sum check: {sum(P)} == 192? {sum(P) == 192}")
    print()


# ============================================================
# Main pipeline
# ============================================================

def categorize(res):
    """Categorize a result by (acyclic_qt, positive_qt, positive_q)."""
    return (res['acyclic_qt'], res['positive_qt'], res['positive_q'])


def main():
    sanity_tests()

    print("Building W(D_4) ...")
    weyl = weyl_D4()
    weyl_distribution_check(weyl)

    # --- INTEGER PAIRS ---
    print("=" * 70)
    print("INTEGER pairs, λ_1 ≤ 3")
    print("=" * 70)
    print("Note on bigrading: in D_4 (simply-laced), the (q,t)-bigrading L=e_i+e_j,")
    print("S=e_i-e_j is NOT W(D_4)-invariant.  We thus track BOTH the bigraded χ_{q,t}")
    print("and the canonical single-graded χ_q (every root contributes q^1).")
    print()
    int_pairs = enumerate_dominant_integer_pairs(max_lam1=3)
    print(f"Total integer pairs (λ ≥ μ in box, both dominant): {len(int_pairs)}")

    # Bigraded confusion
    int_confusion_qt = defaultdict(int)
    # Single-graded positive vs negative
    int_single_neg = 0
    int_single_pos = 0
    int_nonzero = []
    int_examples = {'all_positive_qt_and_q': [], 'nonpos_qt_pos_q': [], 'neg_q': []}

    for lam, mu in int_pairs:
        res = analyze(lam, mu, weyl=weyl)
        if not res['chi'] and not res['mult_even'] and not res['mult_odd']:
            continue
        int_nonzero.append(res)
        cell = (res['acyclic_qt'], res['positive_qt'])
        int_confusion_qt[cell] += 1
        if res['positive_q']:
            int_single_pos += 1
        else:
            int_single_neg += 1
        # Categorize examples
        if res['positive_qt'] and res['positive_q'] and len(int_examples['all_positive_qt_and_q']) < 5:
            int_examples['all_positive_qt_and_q'].append(res)
        elif not res['positive_qt'] and res['positive_q'] and len(int_examples['nonpos_qt_pos_q']) < 5:
            int_examples['nonpos_qt_pos_q'].append(res)
        elif not res['positive_q'] and len(int_examples['neg_q']) < 5:
            int_examples['neg_q'].append(res)

    print(f"Pairs with nonzero contribution: {len(int_nonzero)}")
    print()
    print("Bigraded confusion (acyclic_qt, positive_qt):")
    for cell in [(True, True), (True, False), (False, True), (False, False)]:
        print(f"  {cell}: {int_confusion_qt[cell]}")
    print(f"  Off-diagonal: (True, False) = {int_confusion_qt[(True, False)]}, "
          f"(False, True) = {int_confusion_qt[(False, True)]}")
    if int_confusion_qt[(True, False)] == 0 and int_confusion_qt[(False, True)] == 0:
        print("  Off-diagonal empty (tautological sanity check passes).")
    print()
    print(f"Single-graded χ_q analysis:")
    print(f"  positive_q = True: {int_single_pos}")
    print(f"  positive_q = False: {int_single_neg}")
    if int_single_neg == 0:
        print("  ALL integer pairs have nonneg single-graded χ_q (consistent with")
        print("  Kazhdan-Lusztig positivity for the simply-laced type D_4).")
    else:
        print(f"  !! {int_single_neg} integer pairs have NEGATIVE single-graded χ_q.")
        print("  This would contradict KL positivity at D_4.")
    print()

    # --- SPIN PAIRS ---
    print("=" * 70)
    print("SPIN pairs, λ_1 ≤ 9/2")
    print("=" * 70)
    spin_pairs = enumerate_spin_pairs(max_lam1_doubled=9)
    print(f"Total spin pairs: {len(spin_pairs)}")

    spin_confusion_qt = defaultdict(int)
    spin_nonzero = []
    cross_lattice_counts = defaultdict(lambda: {
        'nonzero': 0, 'ac_pos_qt': 0, 'nonac_neg_qt': 0,
        'pos_q': 0, 'neg_q': 0,
    })

    spin_single_pos = 0
    spin_single_neg = 0
    spin_examples = {'all_positive_qt_and_q': [], 'nonpos_qt_pos_q': [], 'neg_q': []}

    for lam, mu, lam_type, mu_type in spin_pairs:
        res = analyze(lam, mu, weyl=weyl)
        if not res['chi'] and not res['mult_even'] and not res['mult_odd']:
            continue
        spin_nonzero.append((res, lam_type, mu_type))
        cell = (res['acyclic_qt'], res['positive_qt'])
        spin_confusion_qt[cell] += 1
        ckey = (lam_type, mu_type)
        cross_lattice_counts[ckey]['nonzero'] += 1
        if res['acyclic_qt'] and res['positive_qt']:
            cross_lattice_counts[ckey]['ac_pos_qt'] += 1
        if not res['acyclic_qt'] and not res['positive_qt']:
            cross_lattice_counts[ckey]['nonac_neg_qt'] += 1
        if res['positive_q']:
            cross_lattice_counts[ckey]['pos_q'] += 1
            spin_single_pos += 1
        else:
            cross_lattice_counts[ckey]['neg_q'] += 1
            spin_single_neg += 1
        # Examples
        if res['positive_qt'] and res['positive_q'] and len(spin_examples['all_positive_qt_and_q']) < 5:
            spin_examples['all_positive_qt_and_q'].append((res, lam_type, mu_type))
        elif not res['positive_qt'] and res['positive_q'] and len(spin_examples['nonpos_qt_pos_q']) < 5:
            spin_examples['nonpos_qt_pos_q'].append((res, lam_type, mu_type))
        elif not res['positive_q'] and len(spin_examples['neg_q']) < 5:
            spin_examples['neg_q'].append((res, lam_type, mu_type))

    print(f"Pairs with nonzero contribution: {len(spin_nonzero)}")
    print()
    print("Bigraded confusion (acyclic_qt, positive_qt):")
    for cell in [(True, True), (True, False), (False, True), (False, False)]:
        print(f"  {cell}: {spin_confusion_qt[cell]}")
    print()
    print(f"Single-graded χ_q analysis:")
    print(f"  positive_q = True: {spin_single_pos}")
    print(f"  positive_q = False: {spin_single_neg}")
    if spin_single_neg == 0:
        print("  ALL spin pairs have nonneg single-graded χ_q.")
        print("  (Consistent with KL positivity at simply-laced D_4.)")
    else:
        print(f"  !! {spin_single_neg} spin pairs have NEGATIVE single-graded χ_q.")
    print()
    print("Breakdown by (λ_type, μ_type) — type = sign of last coord (spin1 = +, spin2 = -):")
    for k in sorted(cross_lattice_counts.keys()):
        v = cross_lattice_counts[k]
        print(f"  {k}: nonzero={v['nonzero']}, "
              f"acyclic+pos_qt={v['ac_pos_qt']}, "
              f"nonac+neg_qt={v['nonac_neg_qt']}, "
              f"pos_q={v['pos_q']}, neg_q={v['neg_q']}")
    print()

    # --- EXAMPLES ---
    print("=" * 70)
    print("EXAMPLES (integer)")
    print("=" * 70)
    print("\nPairs with both χ_{q,t} and χ_q nonneg (acyclic-and-positive bigraded):")
    for r in int_examples['all_positive_qt_and_q']:
        print(f"  λ={r['lam']}, μ={r['mu']}")
        print(f"    χ_{{q,t}} = {fmt_qt(r['chi'])}")
        print(f"    χ_q     = {fmt_q(r['chi_q'])}")
    print("\nPairs with bigraded χ_{q,t} NEGATIVE but χ_q nonneg (artifact of bigrading):")
    for r in int_examples['nonpos_qt_pos_q']:
        print(f"  λ={r['lam']}, μ={r['mu']}")
        print(f"    χ_{{q,t}} = {fmt_qt(r['chi'])}")
        print(f"    χ_q     = {fmt_q(r['chi_q'])}")
    print("\nPairs with χ_q NEGATIVE (would contradict KL positivity):")
    if int_examples['neg_q']:
        for r in int_examples['neg_q']:
            print(f"  λ={r['lam']}, μ={r['mu']}")
            print(f"    χ_q     = {fmt_q(r['chi_q'])}")
    else:
        print("  (none — KL positivity holds for all integer pairs.)")
    print()

    print("=" * 70)
    print("EXAMPLES (spin)")
    print("=" * 70)
    print("\nPairs with both χ_{q,t} and χ_q nonneg:")
    for r, lt, mt in spin_examples['all_positive_qt_and_q']:
        print(f"  λ={r['lam']} ({lt}), μ={r['mu']} ({mt})")
        print(f"    χ_{{q,t}} = {fmt_qt(r['chi'])}")
        print(f"    χ_q     = {fmt_q(r['chi_q'])}")
    print("\nPairs with bigraded χ_{q,t} NEGATIVE but χ_q nonneg (artifact of bigrading):")
    for r, lt, mt in spin_examples['nonpos_qt_pos_q']:
        print(f"  λ={r['lam']} ({lt}), μ={r['mu']} ({mt})")
        print(f"    χ_{{q,t}} = {fmt_qt(r['chi'])}")
        print(f"    χ_q     = {fmt_q(r['chi_q'])}")
    print("\nPairs with χ_q NEGATIVE:")
    if spin_examples['neg_q']:
        for r, lt, mt in spin_examples['neg_q']:
            print(f"  λ={r['lam']} ({lt}), μ={r['mu']} ({mt})")
            print(f"    χ_q     = {fmt_q(r['chi_q'])}")
    else:
        print("  (none — KL positivity holds for all spin pairs.)")

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"INTEGER: {len(int_nonzero)} nonzero pairs.")
    print(f"  Bigraded acyclic-and-positive: {int_confusion_qt[(True, True)]}")
    print(f"  Bigraded non-acyclic-and-negative: {int_confusion_qt[(False, False)]}")
    print(f"  Off-diagonal: 0 (tautological)")
    print(f"  Single-graded χ_q nonneg: {int_single_pos}/{len(int_nonzero)}")
    print()
    print(f"SPIN: {len(spin_nonzero)} nonzero pairs.")
    print(f"  Bigraded acyclic-and-positive: {spin_confusion_qt[(True, True)]}")
    print(f"  Bigraded non-acyclic-and-negative: {spin_confusion_qt[(False, False)]}")
    print(f"  Off-diagonal: 0 (tautological)")
    print(f"  Single-graded χ_q nonneg: {spin_single_pos}/{len(spin_nonzero)}")
    print()
    print("CONCLUSION:")
    if int_single_neg == 0 and spin_single_neg == 0:
        print("  The canonical (single-q) KL polynomial is positive for BOTH integer")
        print("  and spin pairs in D_4 — consistent with KL positivity for simply-laced.")
        print("  In D_n there is no canonical (q,t)-bigrading (all roots same length).")
        print("  The B_n integer/spin dichotomy (which uses root-length bigrading)")
        print("  does NOT obviously survive at D_4 because the dichotomy itself")
        print("  requires two root lengths.")
    print()

    return {
        'int_confusion_qt': dict(int_confusion_qt),
        'int_total': len(int_nonzero),
        'int_single_pos': int_single_pos,
        'int_single_neg': int_single_neg,
        'spin_confusion_qt': dict(spin_confusion_qt),
        'spin_total': len(spin_nonzero),
        'spin_single_pos': spin_single_pos,
        'spin_single_neg': spin_single_neg,
        'cross_lattice_counts': dict(cross_lattice_counts),
        'int_examples': int_examples,
        'spin_examples': spin_examples,
    }


if __name__ == "__main__":
    main()
