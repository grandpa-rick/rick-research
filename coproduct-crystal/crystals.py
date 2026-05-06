"""
Crystal bases for type A_{n-1} on semistandard Young tableaux.

Reading word convention: COLUMN reading, columns RIGHT-TO-LEFT, each
column TOP-TO-BOTTOM. (This is one of the standard "column word"
conventions.) Together with the signature rule below, this preserves
SSYT-ness automatically when applying crystal operators.

Signature rule (for crystal index i, on a word w):
  - replace each occurrence of i by '+', each i+1 by '-'.
  - cancel adjacent '+-' pairs ('+' immediately followed by '-') iteratively.
  - the surviving sequence has the form '-...-+...+'.
  - f_i: change the LEFTMOST surviving '+' (an i) to i+1.
  - e_i: change the RIGHTMOST surviving '-' (an i+1) to i.

Tensor product: word(T (x) S) = word(T) ++ word(S); apply the same rule.
"""

from itertools import product
from collections import defaultdict


# ---------- Partitions / shapes ----------

def parts(lam):
    """Trim trailing zeros."""
    lam = list(lam)
    while lam and lam[-1] == 0:
        lam.pop()
    return tuple(lam)


# ---------- SSYT enumeration ----------

def ssyt(lam, n):
    """All SSYT of shape lam with entries in {1,...,n}.
    Tableaux are stored as tuples of tuples (rows)."""
    lam = parts(lam)
    if not lam:
        return [()]
    rows = list(lam)
    # Fill cells in row-major order. Constraints: weakly increasing along
    # rows, strictly increasing down columns.
    cells = [(r, c) for r in range(len(rows)) for c in range(rows[r])]
    out = []

    def rec(idx, T):
        if idx == len(cells):
            out.append(tuple(tuple(row) for row in T))
            return
        r, c = cells[idx]
        lo = 1
        if c > 0:
            lo = max(lo, T[r][c-1])           # weakly >= left neighbor
        if r > 0:
            lo = max(lo, T[r-1][c] + 1)       # strictly > above neighbor
        for v in range(lo, n+1):
            T[r][c] = v
            rec(idx+1, T)
            T[r][c] = 0

    T = [[0]*rows[r] for r in range(len(rows))]
    rec(0, T)
    return out


# ---------- Reading word ----------

def reading_word(T):
    """Column reading: columns right-to-left, each column top-to-bottom."""
    if not T:
        return ()
    ncols = max((len(r) for r in T), default=0)
    w = []
    for c in reversed(range(ncols)):
        col = [T[r][c] for r in range(len(T)) if c < len(T[r])]
        # top-to-bottom
        for v in col:
            w.append(v)
    return tuple(w)


def weight(T, n):
    """Composition counting occurrences of 1..n."""
    wt = [0]*n
    for row in T:
        for v in row:
            wt[v-1] += 1
    return tuple(wt)


# ---------- Signature rule on a word ----------

def signature(word, i):
    """For crystal index i, return the list of (pos, sign) of surviving
    +/- after cancellation of '+-' adjacent pairs.
    + is letter i, - is letter i+1.
    Surviving sequence has the form - ... - + ... + (minuses left of pluses)."""
    stack = []  # list of (pos, sign)
    for pos, v in enumerate(word):
        if v == i:
            stack.append((pos, '+'))
        elif v == i+1:
            if stack and stack[-1][1] == '+':
                stack.pop()
            else:
                stack.append((pos, '-'))
    return stack


# ---------- Crystal operators on tableaux ----------

def _word_pos_to_cell(T):
    """Map index in reading_word(T) -> (r, c) cell.
    Matches reading_word: columns right-to-left, each column top-to-bottom."""
    mapping = []
    if not T:
        return mapping
    ncols = max(len(r) for r in T)
    for c in reversed(range(ncols)):
        rows_in_col = [r for r in range(len(T)) if c < len(T[r])]
        for r in rows_in_col:
            mapping.append((r, c))
    return mapping


def f_i(T, i):
    """Apply f_i: change leftmost surviving + (an i) to i+1, or None."""
    w = reading_word(T)
    sig = signature(w, i)
    pluses = [p for p in sig if p[1] == '+']
    if not pluses:
        return None
    pos = pluses[0][0]
    cells = _word_pos_to_cell(T)
    r, c = cells[pos]
    newT = [list(row) for row in T]
    newT[r][c] = i+1
    out = tuple(tuple(row) for row in newT)
    if not is_ssyt(out):
        return None
    return out


def e_i(T, i):
    """Apply e_i: change rightmost surviving - (an i+1) to i, or None."""
    w = reading_word(T)
    sig = signature(w, i)
    minuses = [p for p in sig if p[1] == '-']
    if not minuses:
        return None
    pos = minuses[-1][0]
    cells = _word_pos_to_cell(T)
    r, c = cells[pos]
    newT = [list(row) for row in T]
    newT[r][c] = i
    out = tuple(tuple(row) for row in newT)
    if not is_ssyt(out):
        return None
    return out


def is_ssyt(T):
    """Check SSYT conditions."""
    for row in T:
        for j in range(len(row)-1):
            if row[j] > row[j+1]:
                return False
    for r in range(len(T)-1):
        for c in range(len(T[r+1])):
            if c < len(T[r]) and T[r][c] >= T[r+1][c]:
                return False
    return True


# ---------- Crystal graph ----------

def crystal_graph(lam, n):
    """Return (vertices, edges) where edges is dict (T, i) -> f_i(T)."""
    V = ssyt(lam, n)
    Vset = set(V)
    E = {}
    for T in V:
        for i in range(1, n):
            T2 = f_i(T, i)
            if T2 is not None and T2 in Vset:
                E[(T, i)] = T2
    return V, E


# ---------- Tensor product ----------

def tensor_reading_word(T, S):
    """Concatenate reading words: word(T) then word(S).
    Convention: for tensor T (x) S, signature acts on this concatenation,
    which corresponds to the standard tensor product rule."""
    return reading_word(T) + reading_word(S)


def f_i_tensor(T, S, i):
    """f_i applied to T (x) S using concatenated reading word."""
    wT = reading_word(T)
    wS = reading_word(S)
    w = wT + wS
    sig = signature(w, i)
    pluses = [p for p in sig if p[1] == '+']
    if not pluses:
        return None
    pos = pluses[0][0]
    if pos < len(wT):
        # acts on T
        cells = _word_pos_to_cell(T)
        r, c = cells[pos]
        newT = [list(row) for row in T]
        newT[r][c] = i+1
        out = tuple(tuple(row) for row in newT)
        if not is_ssyt(out):
            return None
        return (out, S)
    else:
        cells = _word_pos_to_cell(S)
        r, c = cells[pos - len(wT)]
        newS = [list(row) for row in S]
        newS[r][c] = i+1
        out = tuple(tuple(row) for row in newS)
        if not is_ssyt(out):
            return None
        return (T, out)


def e_i_tensor(T, S, i):
    wT = reading_word(T)
    wS = reading_word(S)
    w = wT + wS
    sig = signature(w, i)
    minuses = [p for p in sig if p[1] == '-']
    if not minuses:
        return None
    pos = minuses[-1][0]
    if pos < len(wT):
        cells = _word_pos_to_cell(T)
        r, c = cells[pos]
        newT = [list(row) for row in T]
        newT[r][c] = i
        out = tuple(tuple(row) for row in newT)
        if not is_ssyt(out):
            return None
        return (out, S)
    else:
        cells = _word_pos_to_cell(S)
        r, c = cells[pos - len(wT)]
        newS = [list(row) for row in S]
        newS[r][c] = i
        out = tuple(tuple(row) for row in newS)
        if not is_ssyt(out):
            return None
        return (T, out)


# ---------- Tensor decomposition ----------

def is_highest_weight_pair(T, S, n):
    for i in range(1, n):
        if e_i_tensor(T, S, i) is not None:
            return False
    return True


def tensor_weight(T, S, n):
    wT = weight(T, n)
    wS = weight(S, n)
    return tuple(a+b for a, b in zip(wT, wS))


def tensor_decomposition(lam, mu, n):
    """Return {nu: multiplicity} where nu are partitions appearing in
    B(lam) (x) B(mu)."""
    A = ssyt(lam, n)
    B = ssyt(mu, n)
    out = defaultdict(int)
    for T in A:
        for S in B:
            if is_highest_weight_pair(T, S, n):
                wt = tensor_weight(T, S, n)
                # weight of HW element = the partition nu (since in type A,
                # HW elements have partition weight)
                out[parts(wt)] += 1
    return dict(out)


# ---------- Restriction (coproduct side) ----------

def is_restricted_highest_weight(T, m, n):
    """Check whether T is highest-weight for the gl_m x gl_n action,
    i.e., e_i(T) = None for all i in {1,...,m+n-1} \\ {m}."""
    total = m + n
    for i in range(1, total):
        if i == m:
            continue
        if e_i(T, i) is not None:
            return False
    return True


def restricted_weight(T, m, n):
    """Return (mu, nu) where mu is the partition formed by entries <=m
    and nu is the partition formed by entries >m (re-indexed).
    Returns the raw composition; caller can trim trailing zeros."""
    mu = [0] * m
    nu = [0] * n
    for row in T:
        for v in row:
            if v <= m:
                mu[v-1] += 1
            else:
                nu[v-m-1] += 1
    return parts(mu), parts(nu)


def restrict(lam, m, n):
    """Decompose B(lam) under the gl_m x gl_n branching.
    Returns {(mu, nu): multiplicity} where mu, nu are partitions."""
    out = defaultdict(int)
    for T in ssyt(lam, m + n):
        if is_restricted_highest_weight(T, m, n):
            mu, nu = restricted_weight(T, m, n)
            out[(mu, nu)] += 1
    return dict(out)


# ---------- Expected coproduct from LR coefficients ----------

def sub_partitions(lam, max_rows):
    """Yield all partitions mu with mu \\subseteq lam (componentwise),
    with at most max_rows parts."""
    lam = parts(lam)
    if max_rows == 0:
        yield ()
        return
    L = list(lam) + [0] * max(0, max_rows - len(lam))
    L = L[:max_rows] if len(L) >= max_rows else L
    # We need all mu = (m_1 >= m_2 >= ... >= m_{max_rows} >= 0) with
    # m_i <= lam_i (taking lam_i = 0 if i > len(lam)).
    bounds = [lam[i] if i < len(lam) else 0 for i in range(max_rows)]

    def rec(idx, prev, acc):
        if idx == max_rows:
            yield parts(acc)
            return
        upper = min(prev, bounds[idx])
        for v in range(upper, -1, -1):
            yield from rec(idx + 1, v, acc + [v])
    # prev starts at infinity (use a large number)
    yield from rec(0, max(bounds) if bounds else 0, [])


def all_partitions_up_to_size(N, max_rows):
    """Yield all partitions with sum <= N and at most max_rows parts."""
    def rec(remaining, prev, acc):
        yield parts(acc)
        if len(acc) >= max_rows:
            return
        for v in range(1, min(prev, remaining) + 1):
            yield from rec(remaining - v, v, acc + [v])
    yield from rec(N, N, [])


def expected_coproduct(lam, m, n):
    """Compute expected {(mu, nu): mult} from LR coefficients:
       Delta(s_lam) = sum_{mu subseteq lam, |mu| <= m rows}
                       sum_{nu, |nu| <= n rows} c^lam_{mu,nu} s_mu (x) s_nu.
       We use tensor_decomposition over a sufficiently large alphabet to
       extract LR coefficients c^lam_{mu, nu} = mult of nu' in
       B(lam-skew?) — but actually our tensor_decomposition computes
       c^{rho}_{mu, sigma}: nu in B(mu)(x)B(sigma) gives c^nu_{mu,sigma}.

       Strategy: for each pair (mu, nu) with mu subseteq lam (rows <= m)
       and len(nu) <= n with |mu|+|nu|=|lam|, compute
       c^lam_{mu, nu} = coefficient of s_lam in s_mu * s_nu via
       tensor_decomposition(mu, nu, big_n)[lam]."""
    lam = parts(lam)
    size = sum(lam)
    big_n = max(len(lam), m + n) + 2  # ensure all relevant partitions fit
    out = {}
    # Iterate mu subseteq lam with at most m rows.
    for mu in sub_partitions(lam, m):
        mu = parts(mu)
        rem = size - sum(mu)
        if rem < 0:
            continue
        # nu has |nu| = rem, at most n rows.
        for nu in all_partitions_up_to_size(rem, n):
            nu = parts(nu)
            if sum(nu) != rem:
                continue
            # c^lam_{mu, nu} = coefficient of lam in B(mu) (x) B(nu)
            d = tensor_decomposition(mu, nu, big_n)
            c = d.get(lam, 0)
            if c > 0:
                out[(mu, nu)] = out.get((mu, nu), 0) + c
    return out


def verify_coproduct(lam, m, n, expected=None):
    """Run restrict(lam, m, n) and compare to expected_coproduct.
    Returns (ok, got, expected)."""
    got = restrict(lam, m, n)
    if expected is None:
        expected = expected_coproduct(lam, m, n)
    # Normalize
    got_n = {(parts(k[0]), parts(k[1])): v for k, v in got.items()}
    exp_n = {(parts(k[0]), parts(k[1])): v for k, v in expected.items()}
    ok = (got_n == exp_n)
    return ok, got_n, exp_n


def tensor_decomposition_multi(shapes, n):
    """Iterate tensor product B(lam_1) (x) ... (x) B(lam_k).
    For multiple factors, we successively tensor; an element
    (T1, T2, ..., Tk) is highest-weight iff every left-prefix tensor is."""
    # We model as iterated: start with B(shapes[0]), then tensor each
    # subsequent factor and re-decompose.
    if len(shapes) == 1:
        return {parts(shapes[0]): 1}
    cur = {parts(shapes[0]): 1}
    for s in shapes[1:]:
        nxt = defaultdict(int)
        for nu, m in cur.items():
            d = tensor_decomposition(nu, s, n)
            for rho, k in d.items():
                nxt[rho] += m * k
        cur = dict(nxt)
    return cur


# ---------- Tests ----------

def fmt(d):
    return {tuple(k): v for k, v in sorted(d.items(), key=lambda x: (-sum(x[0]), x[0]))}


def run_tests():
    tests = []

    # Test 1
    expected1 = {(3,1): 1, (2,2): 1, (2,1,1): 1}
    got1 = tensor_decomposition((2,1), (1,), 3)
    tests.append(("B((2,1)) (x) B((1)) over n=3", expected1, got1))

    # Test 2
    expected2 = {
        (4,2): 1, (4,1,1): 1, (3,3): 1, (3,2,1): 2,
        (3,1,1,1): 1, (2,2,2): 1, (2,2,1,1): 1
    }
    got2 = tensor_decomposition((2,1), (2,1), 4)
    tests.append(("B((2,1)) (x) B((2,1)) over n=4", expected2, got2))

    # Test 3
    expected3 = {(4,): 1, (3,1): 1, (2,2): 1}
    got3 = tensor_decomposition((2,), (2,), 3)
    tests.append(("B((2)) (x) B((2)) over n=3", expected3, got3))

    # Test 4
    expected4 = {(3,): 1, (2,1): 2, (1,1,1): 1}
    got4 = tensor_decomposition_multi([(1,), (1,), (1,)], 3)
    tests.append(("B((1)) (x) B((1)) (x) B((1)) over n=3", expected4, got4))

    n_pass = 0
    for name, exp, got in tests:
        # Normalize keys
        exp_n = {parts(k): v for k, v in exp.items()}
        got_n = {parts(k): v for k, v in got.items()}
        ok = (exp_n == got_n)
        status = "PASS" if ok else "FAIL"
        if ok:
            n_pass += 1
        print(f"[{status}] {name}")
        print(f"   expected: {fmt(exp_n)}")
        print(f"   computed: {fmt(got_n)}")
        if not ok:
            extra = {k: v for k, v in got_n.items() if exp_n.get(k, 0) != v}
            missing = {k: v for k, v in exp_n.items() if got_n.get(k, 0) != v}
            print(f"   diff (extras): {extra}")
            print(f"   diff (missing/wrong-mult): {missing}")
        print()
    print(f"Tensor-decomposition tests: {n_pass}/{len(tests)} passed.")
    print()

    # ---------- Restriction (coproduct) tests ----------
    print("=" * 60)
    print("Restriction / coproduct tests:")
    print("=" * 60)
    print()

    rtests = [
        ((2, 1), 1, 2),
        ((2, 1), 2, 1),
        ((2, 2), 2, 2),
        ((3, 1), 2, 2),
    ]

    def fmt_pair(d):
        return {(tuple(k[0]), tuple(k[1])): v
                for k, v in sorted(d.items(),
                                   key=lambda x: (sum(x[0][0]), x[0][0],
                                                  sum(x[0][1]), x[0][1]))}

    n_rpass = 0
    for lam, m, n in rtests:
        ok, got, exp = verify_coproduct(lam, m, n)
        status = "PASS" if ok else "FAIL"
        if ok:
            n_rpass += 1
        print(f"[{status}] restrict(lam={lam}, m={m}, n={n})")
        print(f"   expected: {fmt_pair(exp)}")
        print(f"   computed: {fmt_pair(got)}")
        if not ok:
            extra = {k: v for k, v in got.items() if exp.get(k, 0) != v}
            missing = {k: v for k, v in exp.items() if got.get(k, 0) != v}
            print(f"   diff (extras): {extra}")
            print(f"   diff (missing/wrong-mult): {missing}")
        print()
    print(f"Restriction tests: {n_rpass}/{len(rtests)} passed.")
    print()
    print(f"OVERALL: {n_pass + n_rpass}/{len(tests) + len(rtests)} tests passed.")


if __name__ == "__main__":
    run_tests()
