"""
BGG-Verma bigraded decomposition for B_3.

Mirrors the conventions of bgg_decomposition.py (B_2):
* Roots in R^3, long = {±e_i ± e_j : i<j}, short = {±e_i}.
* For each w in W(B_3) (signed permutations, |W|=48):
    length(w) = #(positive roots sent to negative).
    sign(w) = (-1)^length.
* Dot action: w·λ = w(λ+ρ) - ρ, with ρ = (5/2, 3/2, 1/2).
* (q,t)-Kostant K_{q,t}(β) = bigraded dim of Sym(n_+)_β,
    with long-root generators having bidegree (1,0) and short (0,1).
* By Kostant + WCF:
    KL_{λ,μ}(q,t) = Σ_w (-1)^{ℓ(w)} K_{q,t}(w·λ - μ) = Σ_w (-1)^{ℓ(w)} dim_{q,t} M(w·λ)_μ.

For each (λ, μ) we compute:
  (a) supp_even = ⊔_{ℓ(w) even} supp(M(w·λ)_μ)  (multiset of bidegrees, with multiplicity).
  (b) supp_odd  = ⊔_{ℓ(w) odd}  supp(M(w·λ)_μ).
  (c) χ_{q,t} = supp_even - supp_odd  (the (q,t)-Lusztig polynomial).
  (d) "bigraded acyclic at μ" iff every bidegree multiplicity in supp_odd is ≤ that in supp_even
      (equivalently, χ_{q,t} has all nonneg coefs since we're computing exactly the difference of multisets).

NOTE on the "acyclicity vs positivity" claim: by definition, χ_{q,t} = (mult_even) - (mult_odd),
so χ_{q,t} ≥ 0 in every bidegree IFF mult_odd ≤ mult_even at every bidegree IFF the bigraded
BGG complex is "acyclic at μ" in the bigraded sense (per Theorem 3.1 of the writeup).
Hence (a) ⟺ (b) is *built in* to the bookkeeping; the script verifies this consistency
and looks for any computational discrepancy.
"""

from fractions import Fraction
from collections import defaultdict
from itertools import permutations, product


# ============================================================
# Root system B_3
# ============================================================

N = 3

def positive_roots_B3():
    """Return list of positive roots, tagged 'L' (long) or 'S' (short).
    Long: e_i - e_j (i<j), e_i + e_j (i<j).  Short: e_i.
    """
    roots = []
    # long e_i - e_j, i<j
    for i in range(N):
        for j in range(i + 1, N):
            v = [0] * N
            v[i] = 1
            v[j] = -1
            roots.append((tuple(v), 'L'))
    # long e_i + e_j, i<j
    for i in range(N):
        for j in range(i + 1, N):
            v = [0] * N
            v[i] = 1
            v[j] = 1
            roots.append((tuple(v), 'L'))
    # short e_i
    for i in range(N):
        v = [0] * N
        v[i] = 1
        roots.append((tuple(v), 'S'))
    return roots


POS_ROOTS = positive_roots_B3()
POS_ROOTS_SET = set(r for r, _ in POS_ROOTS)
NEG_ROOTS_SET = set(tuple(-x for x in r) for r in POS_ROOTS_SET)
RHO = tuple(Fraction(2 * N - 1 - 2 * i, 2) for i in range(N))  # (5/2, 3/2, 1/2)


# ============================================================
# Weyl group W(B_3): signed permutations, |W| = 48.
# ============================================================

def weyl_B3():
    """Yield (w_func, length, sig_label) for w in W(B_n)."""
    out = []
    for perm in permutations(range(N)):
        for signs in product([1, -1], repeat=N):
            sg = signs  # capture
            pm = perm
            def w(v, sg=sg, pm=pm):
                return tuple(sg[i] * v[pm[i]] for i in range(N))
            length = length_via_inversions(w)
            out.append((w, length, (pm, sg)))
    return out


def length_via_inversions(w_func):
    """ℓ(w) = #(positive roots whose image is a negative root)."""
    cnt = 0
    for r in POS_ROOTS_SET:
        wr = w_func(r)
        if wr in NEG_ROOTS_SET:
            cnt += 1
    return cnt


# ============================================================
# Bigraded Kostant partition function for B_3.
# ============================================================

def kostant_qt_B3(beta):
    """Count multisets of positive roots summing to β, weighted by q^(#long) t^(#short).
    Returns dict (q-deg, t-deg) -> nonneg int.

    Beta entries must be integers (else returns {}).
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
    bvals = tuple(bvals)

    # Quick prune: every positive root is a 0/1 combination of e_i with non-positive in last coords...
    # Actually all positive roots have first nonzero coordinate = +1 (in std B_3 ordering),
    # so β must have nonneg "leading sum" structure. Cheap check: total sum of β must be reachable.
    # But simplest correct prune: each pos root has nonneg first coord.
    # We'll do a recursive enumeration with memoization.

    # Bound: if any β_i is too big in abs val, can prune by total budget.
    # Use an iterative DP over roots.
    counts = defaultdict(int)  # (q,t) -> count
    counts[(0, 0)] = 1
    # State = (remaining β tuple, partial (q-cnt, t-cnt))
    # Iterate roots; at each root we choose how many copies (0,1,2,...) to use.
    # Bound n_α ≤ max(|β_i|/coord) but easier: bound n_α ≤ sum of |β_i|.

    state = defaultdict(int)
    state[bvals] = (defaultdict(int))
    state[bvals][(0, 0)] = 1

    for root, kind in POS_ROOTS:
        new_state = defaultdict(lambda: defaultdict(int))
        for cur_beta, qt_dict in state.items():
            # Try n=0,1,2,... copies of `root`
            n = 0
            cur = cur_beta
            while True:
                # cur = cur_beta - n * root
                # add contribution
                for qt, mult in qt_dict.items():
                    if kind == 'L':
                        new_qt = (qt[0] + n, qt[1])
                    else:
                        new_qt = (qt[0], qt[1] + n)
                    new_state[cur][new_qt] += mult
                # try n+1
                cur = tuple(cur[i] - root[i] for i in range(N))
                # If any coordinate of cur is unreachable (e.g., would force negative remaining),
                # we can't easily prune since later roots may include negatives — but for B_n
                # all positive roots have nonneg first coord, so once cur[0] < 0 we can stop adding
                # this root (all remaining roots have first-coord ≥ 0, so cur[0] only decreases or stays).
                # Generic safe bound: if all coords of cur are >= -<safety>, allow; else stop.
                # We use: stop when cur is no longer reachable from the remaining roots.
                # Cheap & safe: stop when any coord magnitude is "very large" — but we need correctness.
                # Robust bound: max over remaining roots of needed copies ≤ some budget.
                # Easiest: stop when cur cannot be written as nonneg int combo of remaining roots.
                # We'll just bound by total absolute sum.
                if abs(cur[0]) + abs(cur[1]) + abs(cur[2]) > sum(abs(b) for b in bvals) + 6:
                    break
                # Also: reachability — for B_3 positive roots, every coord can be made any
                # nonneg integer using e_i (short roots come last in our list). Conservative:
                # just bound n.
                n += 1
                if n > 60:  # safety net
                    break
        state = new_state

    # After all roots processed, the entry at state[(0,0,0)] is the desired multiset.
    zero = (0, 0, 0)
    if zero not in state:
        return {}
    return {k: v for k, v in state[zero].items() if v != 0}


# Smarter Kostant via direct generating function (faster, exact).
# We order roots so that pruning is maximally effective.
# Strategy: process roots in order such that after processing root[idx], the
# constraint on remaining[i] becomes deterministic (must be 0 or use only later roots).
#
# For B_3 positive roots:
#   Group A: roots with first coord = 1: (1,-1,0), (1,1,0), (1,0,-1), (1,0,1), (1,0,0)  [5 roots]
#   Group B: roots with first coord = 0, second coord = 1: (0,1,-1), (0,1,1), (0,1,0)  [3 roots]
#   Group C: (0,0,1)  [1 root]
# Order by group A then B then C — after group A, remaining[0] must be 0.
# After group B, remaining[1] must be 0. After group C, remaining[2] must be 0.

POS_ROOTS_ORDERED = (
    # Group A: first coord = 1
    [((1, -1, 0), 'L'), ((1, 1, 0), 'L'), ((1, 0, -1), 'L'), ((1, 0, 1), 'L'), ((1, 0, 0), 'S')]
    # Group B: first coord = 0, second coord = 1
    + [((0, 1, -1), 'L'), ((0, 1, 1), 'L'), ((0, 1, 0), 'S')]
    # Group C: first coord = 0, second coord = 0, third coord = 1
    + [((0, 0, 1), 'S')]
)

# Sanity-check ordering
assert len(POS_ROOTS_ORDERED) == 9
assert set(r for r, _ in POS_ROOTS_ORDERED) == POS_ROOTS_SET

# Indices where first/second/third coord constraints become absolute
GROUP_A_END = 5  # after processing 5 roots, remaining[0] must equal 0
GROUP_B_END = 8  # after processing 8 roots, remaining[1] must equal 0


def kostant_qt_B3_v2(beta):
    """Memoized recursion on (idx, remaining) -> dict (q,t)->count."""
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

    # Quick rejects
    if target[0] < 0:
        return {}
    # Sum of all coords of any pos root: positive roots have coord sums in {0, 1, 2}.
    # In particular sum(target) must be >= -? No: target = sum of nonneg combo of roots,
    # each root has coord sum in {0,1,2}, so sum(target) >= 0.
    if sum(target) < 0:
        return {}

    memo = {}

    def recurse(idx, remaining):
        """Return dict (q,t) -> count of decompositions of `remaining` using roots[idx:]."""
        if idx == len(POS_ROOTS_ORDERED):
            if remaining == (0, 0, 0):
                return {(0, 0): 1}
            return {}
        # Pruning by group boundaries
        if idx >= GROUP_A_END and remaining[0] != 0:
            return {}
        if idx >= GROUP_B_END and remaining[1] != 0:
            return {}
        # General prune: target reachable?
        if remaining[0] < 0:
            return {}
        # If after group A start, remaining[0] limits how many more group-A roots we can use.

        key = (idx, remaining)
        if key in memo:
            return memo[key]

        root, kind = POS_ROOTS_ORDERED[idx]
        # Bound on copies of `root`: must keep remaining[i] reachable.
        # If root[0] = 1, then n ≤ remaining[0] (since later roots in group A also have root[0] = 1
        # and we need >= 0 left for them; but n = remaining[0] is the max if all later group A use 0).
        # If root[0] = 0, no constraint from coord 0 directly.
        # Similarly for other coords.
        # We'll compute max_n as min over coords i with root[i] > 0 of remaining[i] (if remaining[i] >= 0),
        # and -remaining[i] // root[i] for root[i] < 0 (we need remaining[i] - n*root[i] reachable).
        # Simplest correct: bound by (sum of |remaining|) // (sum of |root|).
        # Actually we'll just bound by the max "obvious" number.
        max_n_candidates = []
        if root[0] > 0:
            max_n_candidates.append(remaining[0])  # since later group-A roots also have first coord 1
        # For root[0] = 0 roots we let coord 1 / 2 govern via memoization.
        # Universal safety: total absolute value bound.
        max_n_candidates.append(sum(abs(r) for r in remaining) + 1)
        max_n = max(0, min(max_n_candidates))

        result = defaultdict(int)
        for n in range(max_n + 1):
            new_rem = tuple(remaining[i] - n * root[i] for i in range(N))
            if new_rem[0] < 0:
                break  # can only grow worse for group-A; for later groups, root[0] = 0 so this never trips
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


# Use v2.
def kostant_qt(beta):
    return kostant_qt_B3_v2(beta)


# ============================================================
# BGG-Verma analysis
# ============================================================

def analyze(lam, mu, weyl=None, verbose=False):
    """Return dict with:
       'chi'        : {(q,t): coef}  — bigraded Euler char
       'mult_even'  : {(q,t): nonneg int}  — total multiplicity from even-length w
       'mult_odd'   : {(q,t): nonneg int}  — total mult from odd-length w
       'positive'   : bool — chi has all nonneg coeffs
       'acyclic'    : bool — mult_odd ≤ mult_even pointwise
       'agree'      : bool — positive == acyclic
       'per_w'      : list of (length, sign, beta, kqt) for each w
    """
    if weyl is None:
        weyl = weyl_B3()
    lr = tuple(Fraction(lam[i]) + RHO[i] for i in range(N))
    mr = tuple(Fraction(mu[i]) + RHO[i] for i in range(N))

    chi = defaultdict(int)
    mult_even = defaultdict(int)
    mult_odd = defaultdict(int)
    per_w = []
    for w_func, length, label in weyl:
        wlr = w_func(lr)
        diff = tuple(wlr[i] - mr[i] for i in range(N))
        kqt = kostant_qt(diff)
        sign = (-1) ** length
        per_w.append((length, sign, diff, kqt))
        for k, v in kqt.items():
            chi[k] += sign * v
            if length % 2 == 0:
                mult_even[k] += v
            else:
                mult_odd[k] += v

    chi = {k: v for k, v in chi.items() if v != 0}
    positive = all(v >= 0 for v in chi.values())
    # acyclic: every bidegree in mult_odd has mult_odd ≤ mult_even
    acyclic = True
    all_keys = set(mult_even.keys()) | set(mult_odd.keys())
    for k in all_keys:
        if mult_odd.get(k, 0) > mult_even.get(k, 0):
            acyclic = False
            break
    agree = (positive == acyclic)

    return {
        'lam': lam, 'mu': mu,
        'chi': chi,
        'mult_even': dict(mult_even),
        'mult_odd': dict(mult_odd),
        'positive': positive,
        'acyclic': acyclic,
        'agree': agree,
        'per_w': per_w,
    }


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
# Smoke test: re-derive B_2 results by embedding into B_3.
# ============================================================

def smoke_test_B2_embedding():
    """For (λ, μ) in B_2, embed as (λ_1, λ_2, 0), (μ_1, μ_2, 0) in B_3 with last coord 0.

    BUT: this is NOT the same polynomial — B_3 has more positive roots than B_2,
    so K_{q,t}(β) for β = (β_1, β_2, 0) in B_3 includes contributions from roots
    involving e_3, which were absent in B_2. So this is NOT a valid smoke test.

    What WE CAN DO as a sanity check: independently, run our B_3 code with the
    B_2 root system restricted (only roots not involving e_3) and verify against
    the known B_2 values. This is a code-correctness check.

    Alternative: just verify Kostant counts on simple cases by hand.
    """
    # Hand-verified Kostant counts for B_3:
    # K_{q,t}((0,0,0)) = 1 (empty partition).
    # K_{q,t}((1,0,0)) = ? β = (1,0,0). Decompositions into pos roots:
    #   (1,0,0) = e_1 (short)                          -> (q^0 t^1) = (0,1)
    #   (1,0,0) = (e_1 - e_2) + e_2 = (1,-1,0)+(0,1,0) -> (q^1 t^1) = (1,1)
    #   (1,0,0) = (e_1 - e_3) + e_3                    -> (q^1 t^1) = (1,1)
    #   (1,0,0) = (e_1 + e_2) + (- ...) — but no negative pos roots.
    #   (1,0,0) = (e_1 - e_2) + (e_1 + e_2) - e_1 = ... no, can't subtract.
    #   How about: (e_1-e_2) + e_2 — already counted.
    #   Or: e_1 = e_1. That's the short option.
    #   With three roots: (e_1-e_2)+(e_2-e_3)+e_3 = e_1. -> (q^2 t^1) = (2,1)
    #   And: (e_1-e_3)+(e_3-e_2)? But e_3-e_2 is NEGATIVE, not in our list.
    #   So only via (e_1-e_2)+(e_2-e_3)+e_3 — that's one way.
    #   With four roots? (e_1-e_2)+(e_2)+(e_3)+(-e_3) — no, no neg roots.
    #   I think the count at K((1,0,0)) is:
    #     (0,1):1   (e_1)
    #     (1,1):2   (e_1-e_2)+e_2  and  (e_1-e_3)+e_3
    #     (2,1):1   (e_1-e_2)+(e_2-e_3)+e_3
    #     (2,1)?: also (e_1+e_2) needs cancellation — can't since no neg roots.
    #   So K((1,0,0)) = t + 2qt + q^2 t.
    print("Sanity: K_{q,t}((1,0,0)) =", fmt_qt(kostant_qt((1, 0, 0))))
    print("Expected: t + 2qt + q^2 t")
    # And K((0,0,0)) = 1
    print("Sanity: K_{q,t}((0,0,0)) =", fmt_qt(kostant_qt((0, 0, 0))))
    print("Expected: 1")
    # And K((1,1,0)):
    # β=(1,1,0): decompositions
    #   e_1 + e_2 (two shorts) -> (0,2)
    #   (e_1+e_2) (one long) -> (1,0)
    #   (e_1-e_2) + 2 e_2 -> (1,2)
    #   2 e_1 - (e_1-e_2)? — no neg.
    #   (e_1-e_3) + (e_3) + e_2 -> (1,2)
    #   (e_1-e_2) + (e_2-e_3) + e_3 + e_2 -> (2,2)
    #   (e_1+e_3) + ... need +e_2 -e_3 = -(e_3-e_2): no neg roots.
    #   Hmm let me be more careful.
    print("Sanity: K_{q,t}((1,1,0)) =", fmt_qt(kostant_qt((1, 1, 0))))


# ============================================================
# Code-correctness check: emulate B_2 inside the B_3 code
# (use only the B_2 root subsystem and the B_2 Weyl group of order 8).
# ============================================================

def kostant_qt_B2_only(beta):
    """Restrict to B_2 positive roots only: e_1-e_2, e_1+e_2 (long), e_1, e_2 (short)."""
    if len(beta) != 2:
        return {}
    # Positive roots in B_2:
    roots_B2 = [((1, -1), 'L'), ((1, 1), 'L'), ((1, 0), 'S'), ((0, 1), 'S')]
    target = tuple(int(x) for x in beta)
    out = defaultdict(int)

    def recurse(idx, remaining, q_cnt, t_cnt):
        if idx == len(roots_B2):
            if remaining == (0, 0):
                out[(q_cnt, t_cnt)] += 1
            return
        root, kind = roots_B2[idx]
        bound = sum(abs(r) for r in remaining) + 2
        for n in range(bound + 1):
            new_rem = tuple(remaining[i] - n * root[i] for i in range(2))
            if all(r[0] >= 0 for r, _ in roots_B2[idx + 1:]) and new_rem[0] < 0:
                break
            if kind == 'L':
                recurse(idx + 1, new_rem, q_cnt + n, t_cnt)
            else:
                recurse(idx + 1, new_rem, q_cnt, t_cnt + n)

    recurse(0, target, 0, 0)
    return {k: v for k, v in out.items() if v != 0}


def weyl_B2_in_B3_format():
    """W(B_2): signed permutations of (e_1, e_2). 8 elements."""
    out = []
    rho_B2 = (Fraction(3, 2), Fraction(1, 2))
    for perm in permutations(range(2)):
        for signs in product([1, -1], repeat=2):
            sg = signs
            pm = perm
            def w(v, sg=sg, pm=pm):
                return tuple(sg[i] * v[pm[i]] for i in range(2))
            # length via B_2 positive roots
            pos_roots_B2 = [(1, -1), (1, 1), (1, 0), (0, 1)]
            neg_roots_B2 = [(-x, -y) for x, y in pos_roots_B2]
            cnt = 0
            for r in pos_roots_B2:
                wr = w(r)
                if wr in neg_roots_B2:
                    cnt += 1
            out.append((w, cnt, (pm, sg)))
    return out, rho_B2


def smoke_test_B2_recovered():
    """Verify B_2 case (1,0)→(0,0) gives qt - q + t using B_3 code structure (restricted to B_2)."""
    weyl, rho_B2 = weyl_B2_in_B3_format()
    chi = defaultdict(int)
    mult_even = defaultdict(int)
    mult_odd = defaultdict(int)

    lam = (1, 0)
    mu = (0, 0)
    lr = tuple(Fraction(lam[i]) + rho_B2[i] for i in range(2))
    mr = tuple(Fraction(mu[i]) + rho_B2[i] for i in range(2))

    for w_func, length, label in weyl:
        wlr = w_func(lr)
        diff = tuple(wlr[i] - mr[i] for i in range(2))
        kqt = kostant_qt_B2_only(diff)
        sign = (-1) ** length
        for k, v in kqt.items():
            chi[k] += sign * v
            if length % 2 == 0:
                mult_even[k] += v
            else:
                mult_odd[k] += v

    chi = {k: v for k, v in chi.items() if v != 0}
    print("B_2 smoke: KL_{(1,0),(0,0)}(q,t) =", fmt_qt(chi))
    print("Expected:                        qt - q + t  (i.e., {(0,1):1, (1,0):-1, (1,1):1})")
    return chi


# ============================================================
# Main: enumerate B_3 dominant pairs.
# ============================================================

def enumerate_dominant_pairs(max_lam1=3, allow_spin=False):
    """Dominant for B_n: λ_1 ≥ λ_2 ≥ ... ≥ λ_n ≥ 0.
    Integer weights only here.
    """
    pairs = []
    for l1 in range(max_lam1 + 1):
        for l2 in range(l1 + 1):
            for l3 in range(l2 + 1):
                lam = (l1, l2, l3)
                for m1 in range(l1 + 1):
                    for m2 in range(m1 + 1):
                        for m3 in range(m2 + 1):
                            mu = (m1, m2, m3)
                            pairs.append((lam, mu))
    return pairs


def enumerate_spin_pairs(max_lam1=3):
    """Spin pairs: λ, μ ∈ (1/2, 1/2, 1/2) + Z^3, both dominant."""
    F = Fraction
    half = F(1, 2)
    pairs = []
    for l1_int in range(max_lam1 + 1):
        for l2_int in range(l1_int + 1):
            for l3_int in range(l2_int + 1):
                lam = (l1_int + half, l2_int + half, l3_int + half)
                for m1_int in range(l1_int + 1):
                    for m2_int in range(m1_int + 1):
                        for m3_int in range(m2_int + 1):
                            mu = (m1_int + half, m2_int + half, m3_int + half)
                            pairs.append((lam, mu))
    return pairs


def main():
    print("=" * 70)
    print("Sanity tests")
    print("=" * 70)
    smoke_test_B2_recovered()
    print()
    print("Sanity: K_{q,t}((0,0,0)) =", fmt_qt(kostant_qt((0, 0, 0))))
    print("Sanity: K_{q,t}((1,0,0)) =", fmt_qt(kostant_qt((1, 0, 0))))
    print("Sanity: K_{q,t}((1,1,0)) =", fmt_qt(kostant_qt((1, 1, 0))))
    print("Sanity: K_{q,t}((1,1,1)) =", fmt_qt(kostant_qt((1, 1, 1))))
    print()

    print("=" * 70)
    print("Building W(B_3) ...")
    print("=" * 70)
    weyl = weyl_B3()
    print(f"|W(B_3)| = {len(weyl)} (expected 48)")
    # Length distribution
    from collections import Counter
    lens = Counter(l for _, l, _ in weyl)
    print("Length distribution:", dict(sorted(lens.items())))
    print("Expected: {0:1, 1:3, 2:5, 3:6, 4:6, 5:5, 6:3, 7:... wait let me check}")
    # B_3 has 9 positive roots, so longest element has length 9.
    # Poincaré polynomial of W(B_3) = [2]_q [4]_q [6]_q
    # = (1+q)(1+q+q²+q³)(1+q+q²+q³+q⁴+q⁵)
    print()

    print("=" * 70)
    print("Enumerating dominant integer (λ, μ) pairs with λ_1 ≤ 3")
    print("=" * 70)
    pairs = enumerate_dominant_pairs(max_lam1=3)
    print(f"Total pairs: {len(pairs)}")

    confusion = {(True, True): 0, (True, False): 0, (False, True): 0, (False, False): 0}
    nonzero_results = []
    violations = []
    new_negatives = []  # acyclic = False & positive = False (genuine non-acyclic case)

    for lam, mu in pairs:
        res = analyze(lam, mu, weyl=weyl)
        if not res['chi'] and not res['mult_even'] and not res['mult_odd']:
            continue  # totally trivial / weight not reached
        nonzero_results.append(res)
        cell = (res['acyclic'], res['positive'])
        confusion[cell] += 1
        if not res['agree']:
            violations.append(res)
        if not res['acyclic'] and not res['positive']:
            new_negatives.append(res)

    print()
    print(f"Pairs with at least one nonzero contribution: {len(nonzero_results)}")
    print()
    print("CONFUSION MATRIX (acyclic, positive):")
    print(f"  (True,  True ):  {confusion[(True, True)]}   -- conjecture-consistent (positive case)")
    print(f"  (False, False):  {confusion[(False, False)]}   -- conjecture-consistent (negative case)")
    print(f"  (True,  False):  {confusion[(True, False)]}   -- VIOLATION (acyclic but negative)")
    print(f"  (False, True ):  {confusion[(False, True)]}   -- VIOLATION (non-acyclic but positive)")
    print()

    if violations:
        print("=" * 70)
        print(f"VIOLATIONS ({len(violations)}):")
        print("=" * 70)
        for r in violations:
            print(f"  λ={r['lam']}, μ={r['mu']}")
            print(f"    χ_{{q,t}} = {fmt_qt(r['chi'])}")
            print(f"    even mult = {dict(sorted(r['mult_even'].items()))}")
            print(f"    odd  mult = {dict(sorted(r['mult_odd'].items()))}")
            print(f"    positive = {r['positive']}, acyclic = {r['acyclic']}")
    else:
        print("NO VIOLATIONS: every pair has positive ⟺ acyclic.")

    print()
    print("=" * 70)
    print(f"NEW non-acyclic-AND-negative (analogous to Remark 4.7) — {len(new_negatives)} cases:")
    print("=" * 70)
    for r in new_negatives[:30]:
        print(f"  λ={r['lam']}, μ={r['mu']}")
        print(f"    χ_{{q,t}} = {fmt_qt(r['chi'])}")
        print(f"    even mult = {dict(sorted(r['mult_even'].items()))}")
        print(f"    odd  mult = {dict(sorted(r['mult_odd'].items()))}")
    if len(new_negatives) > 30:
        print(f"  ... and {len(new_negatives) - 30} more")

    # Spin pairs
    print()
    print("=" * 70)
    print("SPIN PAIRS (half-integer weights) -- conjecture: all (acyclic, positive)")
    print("=" * 70)
    spin_pairs = enumerate_spin_pairs(max_lam1=3)
    print(f"Total spin pairs: {len(spin_pairs)}")
    spin_confusion = {(True, True): 0, (True, False): 0, (False, True): 0, (False, False): 0}
    spin_violations = []
    spin_nonzero = 0
    for lam, mu in spin_pairs:
        res = analyze(lam, mu, weyl=weyl)
        if not res['chi'] and not res['mult_even'] and not res['mult_odd']:
            continue
        spin_nonzero += 1
        cell = (res['acyclic'], res['positive'])
        spin_confusion[cell] += 1
        if not res['acyclic'] or not res['positive']:
            spin_violations.append(res)

    print(f"Pairs with at least one nonzero contribution: {spin_nonzero}")
    print(f"  (True,  True ):  {spin_confusion[(True, True)]}")
    print(f"  (False, False):  {spin_confusion[(False, False)]}")
    print(f"  (True,  False):  {spin_confusion[(True, False)]}")
    print(f"  (False, True ):  {spin_confusion[(False, True)]}")
    if spin_violations:
        print()
        print(f"SPIN VIOLATIONS (negative or non-acyclic) — {len(spin_violations)}:")
        for r in spin_violations[:10]:
            print(f"  λ={r['lam']}, μ={r['mu']}")
            print(f"    χ_{{q,t}} = {fmt_qt(r['chi'])}")
            print(f"    positive = {r['positive']}, acyclic = {r['acyclic']}")
    else:
        print()
        print("All spin pairs are (acyclic, positive). Spin conjecture survives.")

    return {
        'integer_confusion': confusion,
        'integer_violations': violations,
        'integer_new_negatives': new_negatives,
        'integer_total': len(nonzero_results),
        'spin_confusion': spin_confusion,
        'spin_violations': spin_violations,
        'spin_total': spin_nonzero,
    }


if __name__ == "__main__":
    main()
