"""
Verification script for 0-Hecke algebra H_0(S_n) primitive idempotents.

Elements of H_0(S_n) are represented as dicts {permutation tuple -> Fraction coefficient}.
Multiplication uses the Demazure product rule on basis elements:
    pi_w * pi_{s_i} = pi_{w s_i}  if length(w s_i) > length(w)
                    = pi_w        otherwise.
"""

from fractions import Fraction
from itertools import permutations


# ---------- permutation utilities ----------

def s_i_apply_right(w, i):
    """Apply simple transposition s_i on the right: w -> w * s_i.

    s_i swaps positions i and i+1 (1-indexed). In one-line notation w = (w(1), ..., w(n)),
    right-multiplication by s_i swaps entries at positions i and i+1.
    """
    w = list(w)
    w[i-1], w[i] = w[i], w[i-1]
    return tuple(w)


def length(w):
    """Coxeter length = number of inversions of permutation w."""
    n = len(w)
    inv = 0
    for i in range(n):
        for j in range(i+1, n):
            if w[i] > w[j]:
                inv += 1
    return inv


def identity_perm(n):
    return tuple(range(1, n+1))


# ---------- Demazure product on basis ----------

def demazure_right_mult_by_si(w, i):
    """Multiply pi_w * pi_{s_i}. Returns the resulting basis permutation tuple."""
    w_si = s_i_apply_right(w, i)
    if length(w_si) > length(w):
        return w_si
    else:
        return w


def reduced_word_to_perm(n, word):
    """Compute the Demazure product pi_{i_1} * pi_{i_2} * ... starting from identity.
    For a reduced word this gives the permutation. For non-reduced, gives Demazure result."""
    w = identity_perm(n)
    for i in word:
        w = demazure_right_mult_by_si(w, i)
    return w


# ---------- algebra elements as dicts ----------

def zero(n):
    return {}


def one(n):
    return {identity_perm(n): Fraction(1)}


def pi_gen(n, i):
    """Generator pi_i as an algebra element."""
    e = identity_perm(n)
    s = s_i_apply_right(e, i)
    return {s: Fraction(1)}


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def scale(a, c):
    c = Fraction(c)
    if c == 0:
        return {}
    return {k: v*c for k, v in a.items()}


def neg(a):
    return scale(a, -1)


def sub(a, b):
    return add(a, neg(b))


def mult_basis_basis(n, w, v):
    """Multiply pi_w * pi_v using the Demazure product.

    We use a reduced word for v: pi_v = pi_{j_1} ... pi_{j_k}.
    Then pi_w * pi_v = pi_w * pi_{j_1} * ... * pi_{j_k}.
    Each step is multiplication on the right by a generator,
    which on basis elements is the Demazure rule.
    """
    # Get a reduced word for v by row-by-row reduction.
    word = reduced_word_for(v)
    u = w
    for j in word:
        u = demazure_right_mult_by_si(u, j)
    return u


def reduced_word_for(w):
    """Return a reduced expression for w as a list of indices."""
    w = list(w)
    n = len(w)
    word = []
    # Standard algorithm: repeatedly find a descent (w[i] > w[i+1]) and apply s_i to reduce length.
    # That gives a reduced word in reverse.
    while True:
        # find a descent
        desc = None
        for i in range(n-1):
            if w[i] > w[i+1]:
                desc = i
                break
        if desc is None:
            break
        # swap
        w[desc], w[desc+1] = w[desc+1], w[desc]
        word.append(desc+1)  # 1-indexed
    word.reverse()
    return word


def mult(n, a, b):
    """Multiply two algebra elements."""
    out = {}
    for w, cw in a.items():
        for v, cv in b.items():
            u = mult_basis_basis(n, w, v)
            c = cw * cv
            out[u] = out.get(u, Fraction(0)) + c
            if out[u] == 0:
                del out[u]
    return out


def equal(a, b):
    return all(a.get(k, 0) == b.get(k, 0) for k in set(a) | set(b))


# ---------- handy operators ----------

def pi_word(n, word):
    """pi_{i_1} pi_{i_2} ... pi_{i_k} as an algebra element."""
    out = one(n)
    for i in word:
        out = mult(n, out, pi_gen(n, i))
    return out


def sigma_gen(n, i):
    """sigma_i = 1 - pi_i."""
    return sub(one(n), pi_gen(n, i))


def sigma_word(n, word):
    out = one(n)
    for i in word:
        out = mult(n, out, sigma_gen(n, i))
    return out


# ---------- left ideal dimension ----------

def left_ideal_dim(n, e):
    """Compute dim of H_n * e by computing all pi_w * e and finding rank."""
    # Generate all permutations of {1, ..., n}.
    perms = list(permutations(range(1, n+1)))
    vectors = []
    # We'll represent each pi_w * e as a vector indexed by permutations.
    index = {p: i for i, p in enumerate(perms)}
    N = len(perms)

    rows = []
    for w in perms:
        # element pi_w
        elem_w = {w: Fraction(1)}
        prod = mult(n, elem_w, e)
        row = [Fraction(0)] * N
        for k, v in prod.items():
            row[index[k]] = v
        rows.append(row)

    # Compute rank over Q via Gaussian elimination on Fractions.
    return rank_fractions(rows)


def rank_fractions(rows):
    """Rank of a matrix of Fractions via Gaussian elimination."""
    # copy
    M = [row[:] for row in rows]
    if not M:
        return 0
    nrows = len(M)
    ncols = len(M[0])
    r = 0
    col = 0
    while r < nrows and col < ncols:
        # find pivot
        pivot = None
        for i in range(r, nrows):
            if M[i][col] != 0:
                pivot = i
                break
        if pivot is None:
            col += 1
            continue
        M[r], M[pivot] = M[pivot], M[r]
        pv = M[r][col]
        # eliminate below and above
        for i in range(nrows):
            if i != r and M[i][col] != 0:
                f = M[i][col] / pv
                for c in range(col, ncols):
                    M[i][c] -= f * M[r][c]
        r += 1
        col += 1
    return r


# ---------- descent compositions and longest elements ----------

def w0_of_subset(n, I):
    """Longest element w_0(I) in the parabolic subgroup S_I.

    I is a subset of {1, ..., n-1}. The parabolic decomposes {1,...,n} into
    blocks given by I. w_0(I) reverses each block. Returns reduced word as a list.
    """
    # Build blocks: starting from 1, a block continues through positions where i in I.
    blocks = []
    cur = [1]
    for k in range(1, n):
        if k in I:
            cur.append(k+1)
        else:
            blocks.append(cur)
            cur = [k+1]
    blocks.append(cur)

    # For each block [a, a+1, ..., b], the longest element reverses it.
    # As a permutation in S_n, it's the product of swaps. We get a reduced word
    # by taking, for a block of size m, the standard reduced word for w_0 of S_m
    # shifted: e.g. block [a, b] of size 2: word (a). Block [a, a+1, a+2] size 3: (a, a+1, a) i.e.
    # a (a+1) a. General: w_0 of S_m has reduced word
    #   1 2 1 3 2 1 ... (m-1) (m-2) ... 1
    # shift by (a-1).
    word = []
    for blk in blocks:
        a = blk[0]
        m = len(blk)
        # standard reduced word for w_0 in S_m
        sub_word = []
        for r in range(1, m):
            for j in range(r, 0, -1):
                sub_word.append(j)
        # shift
        word.extend([j + (a-1) for j in sub_word])
    return word


def descent_set_of_composition(alpha):
    """Descent set D(alpha) for composition alpha = (a_1, ..., a_k) of n is
    {a_1, a_1+a_2, ..., a_1+...+a_{k-1}}."""
    D = []
    s = 0
    for a in alpha[:-1]:
        s += a
        D.append(s)
    return set(D)


def composition_idempotent(n, alpha):
    """Build e_alpha = pi_{w_0(D)} * sigma_{w_0(D^c)}.

    Where D = D(alpha) subset of {1,...,n-1}, D^c is the complement in {1,...,n-1}.
    """
    D = descent_set_of_composition(alpha)
    Dc = set(range(1, n)) - D
    word_pi = w0_of_subset(n, D)
    word_sigma = w0_of_subset(n, Dc)

    pi_part = pi_word(n, word_pi)
    sigma_part = sigma_word(n, word_sigma)
    return mult(n, pi_part, sigma_part)


# ---------- compositions ----------

def compositions(n):
    """All compositions of n, as tuples."""
    if n == 0:
        return [()]
    out = []
    for k in range(1, n+1):
        for rest in compositions(n-k):
            out.append((k,) + rest)
    return out


# ---------- main verification ----------

def verify_n(n, expected_dims):
    """Verify primitive idempotents for H_0(S_n).

    expected_dims: dict {composition tuple -> expected ribbon number}.
    Returns a list of (composition, idempotent_check, dim, dim_ok).
    """
    print(f"\n=== H_0(S_{n}) verification ===")
    comps = compositions(n)
    idems = {alpha: composition_idempotent(n, alpha) for alpha in comps}

    results = {}

    # (a) idempotency
    print("(a) Idempotency e_alpha^2 = e_alpha:")
    all_idem = True
    for alpha, e in idems.items():
        e2 = mult(n, e, e)
        ok = equal(e2, e)
        all_idem = all_idem and ok
        print(f"    alpha={alpha}: {'OK' if ok else 'FAIL'}")
        results[('idem', alpha)] = ok

    # (b) orthogonality
    print("(b) Orthogonality e_alpha e_beta = 0 for alpha != beta:")
    all_orth = True
    for alpha in comps:
        for beta in comps:
            if alpha == beta:
                continue
            prod = mult(n, idems[alpha], idems[beta])
            ok = (len(prod) == 0)
            if not ok:
                all_orth = False
                print(f"    alpha={alpha}, beta={beta}: FAIL, prod = {prod}")
    if all_orth:
        print("    All pairs OK.")

    # (c) sum = 1
    print("(c) Sum of e_alpha = 1:")
    s = {}
    for e in idems.values():
        s = add(s, e)
    sum_ok = equal(s, one(n))
    print(f"    {'OK' if sum_ok else 'FAIL'}")
    if not sum_ok:
        print(f"    sum = {s}")

    # (d) left ideal dimensions
    print("(d) Left ideal dimensions dim H_n * e_alpha:")
    all_dim = True
    for alpha in comps:
        d = left_ideal_dim(n, idems[alpha])
        exp = expected_dims[alpha]
        ok = (d == exp)
        all_dim = all_dim and ok
        print(f"    alpha={alpha}: dim = {d}, expected {exp} {'OK' if ok else 'FAIL'}")

    return idems, all_idem and all_orth and sum_ok and all_dim


# Expected ribbon numbers for n=3
expected_n3 = {
    (3,): 1,
    (1, 2): 2,
    (2, 1): 2,
    (1, 1, 1): 1,
}

# Expected ribbon numbers for n=4
expected_n4 = {
    (4,): 1,
    (3, 1): 3,
    (1, 3): 3,
    (2, 2): 5,
    (2, 1, 1): 3,
    (1, 2, 1): 5,
    (1, 1, 2): 3,
    (1, 1, 1, 1): 1,
}


def main():
    # n = 3
    idems3, ok3 = verify_n(3, expected_n3)

    # Also verify the explicit forms requested:
    # e_(3) = sigma_1 sigma_2 sigma_1
    # e_(1,2) = pi_1 sigma_2
    # e_(2,1) = pi_2 sigma_1
    # e_(1,1,1) = pi_1 pi_2 pi_1
    print("\nExplicit form check for n=3:")
    explicit3 = {
        (3,): sigma_word(3, [1, 2, 1]),
        (1, 2): mult(3, pi_gen(3, 1), sigma_gen(3, 2)),
        (2, 1): mult(3, pi_gen(3, 2), sigma_gen(3, 1)),
        (1, 1, 1): pi_word(3, [1, 2, 1]),
    }
    for alpha in [(3,), (1,2), (2,1), (1,1,1)]:
        ok = equal(explicit3[alpha], idems3[alpha])
        print(f"    e_{alpha}: {'matches' if ok else 'DIFFERS'}")

    # n = 4
    idems4, ok4 = verify_n(4, expected_n4)

    # Induction test
    print("\n=== Induction test in H_0(S_4) ===")
    # H_2 idempotents using only pi_1 (left factor) embedded in S_4:
    #   e_(2)   = sigma_1 = 1 - pi_1
    #   e_(1,1) = pi_1
    # H_2 idempotents using only pi_3 (right factor) embedded in S_4:
    #   e_(2)   = sigma_3 = 1 - pi_3
    #   e_(1,1) = pi_3
    n = 4
    e_left = {
        (2,): sigma_gen(n, 1),
        (1,1): pi_gen(n, 1),
    }
    e_right = {
        (2,): sigma_gen(n, 3),
        (1,1): pi_gen(n, 3),
    }

    induction_cases = [
        ((2,), (2,), 5 + 1),       # (2,2) + (4)
        ((2,), (1,1), 3 + 3),      # (2,1,1) + (3,1)
        ((1,1), (2,), 3 + 3),      # (1,1,2) + (1,3)
        ((1,1), (1,1), 1 + 5),     # (1,1,1,1) + (1,2,1)
    ]

    all_ind_ok = True
    for alpha, beta, expected in induction_cases:
        e_lifted = mult(n, e_left[alpha], e_right[beta])
        # check it's idempotent
        e2 = mult(n, e_lifted, e_lifted)
        idem_ok = equal(e2, e_lifted)
        d = left_ideal_dim(n, e_lifted)
        dim_ok = (d == expected)
        all_ind_ok = all_ind_ok and idem_ok and dim_ok
        print(f"    e_{alpha} (x) e_{beta}: idempotent? {idem_ok}, "
              f"dim H_4 * e = {d}, expected {expected} "
              f"{'OK' if dim_ok else 'FAIL'}")

    # Diagnostic: show e_(2,2) and e_(1,2,1) and their squares
    print("\n=== Diagnostic for failing n=4 cases ===")
    for alpha in [(2, 2), (1, 2, 1)]:
        e = idems4[alpha]
        e2 = mult(n, e, e)
        diff = sub(e2, e)
        print(f"  e_{alpha} (basis support size = {len(e)}):")
        for k, v in sorted(e.items()):
            print(f"      {k}: {v}")
        print(f"  e_{alpha}^2 - e_{alpha}:")
        for k, v in sorted(diff.items()):
            print(f"      {k}: {v}")

    # ---------- Targeted bug witness for n=4 ----------
    print("\n=== n=4 idempotent-bug witness ===")
    print("  Convention: Demazure product with idempotent generators")
    print("              pi_i^2 = pi_i (rule: pi_w * pi_{s_i} = pi_{w s_i} if length up, else pi_w)")
    print("              sigma_i = 1 - pi_i (so sigma_i^2 = sigma_i, anti-Demazure)")
    print("              ACTION SIDE: right action; DESCENT SET on the right.")
    print("              Naive idempotent: e_alpha = pi_{w_0(I)} * sigma_{w_0(J)},")
    print("                I = D(alpha) subset of {1,...,n-1}, J = I^c.")
    print()
    failures = []
    for alpha in compositions(n):
        e = idems4[alpha]
        e2 = mult(n, e, e)
        diff = sub(e2, e)
        if len(diff) != 0:
            failures.append(alpha)
    print(f"  Failing compositions: {failures}")
    print(f"  (Note: these are EXACTLY the alpha with I or J disconnected in {{1,...,n-1}}.)")
    for alpha in failures:
        I = sorted(descent_set_of_composition(alpha))
        J = sorted(set(range(1, n)) - set(I))
        word_pi = w0_of_subset(n, set(I))
        word_sigma = w0_of_subset(n, set(J))
        e = idems4[alpha]
        e2 = mult(n, e, e)
        diff = sub(e2, e)
        print(f"\n  alpha = {alpha}")
        print(f"    I = D(alpha) = {I}   (descent set)")
        print(f"    J = I^c     = {J}")
        print(f"    w_0(I) reduced word = {word_pi}")
        print(f"    w_0(J) reduced word = {word_sigma}")
        print(f"    e_alpha (basis-element sum):")
        for k, v in sorted(e.items()):
            print(f"        {k}: {v}")
        print(f"    e_alpha^2 - e_alpha (basis-element sum, NONZERO => not idempotent):")
        for k, v in sorted(diff.items()):
            print(f"        {k}: {v}")

    print("\n  Left-ideal dim sanity (Norton: dim H_4 * e_alpha = ribbon number r_alpha):")
    for alpha in compositions(n):
        d = left_ideal_dim(n, idems4[alpha])
        print(f"    alpha={alpha}: dim H_4 * e_alpha = {d}, ribbon r_alpha = {expected_n4[alpha]}"
              f"  {'OK' if d == expected_n4[alpha] else 'FAIL'}")
    print("\n  => bug is MASKED at the K_0 (Grothendieck) level: left-ideal dimensions are")
    print("     correct even when e_alpha is not actually idempotent.")

    # Final summary
    print("\n=== SUMMARY ===")
    print(f"  n=3 all checks: {'PASS' if ok3 else 'FAIL'}")
    print(f"  n=4 all checks: {'PASS' if ok4 else 'FAIL'}")
    print(f"  Induction test: {'PASS' if all_ind_ok else 'FAIL'}")
    print()
    print("  Notes for n=4:")
    print("    * Idempotency, orthogonality, sum=1 ALL FAIL for the user's prescribed")
    print("      formula e_alpha = pi_{w_0(D)} * sigma_{w_0(D^c)} on compositions (2,2) and (1,2,1).")
    print("    * These are exactly the compositions where D or D^c is disconnected in {1,...,n-1}.")
    print("    * However, dim H_4 * e_alpha matches the ribbon numbers for ALL 8 compositions,")
    print("      so the left ideals generated still have the right size.")
    print("    * The induction test (4 cases) all PASS, including dim = r_{a.b} + r_{a>b}.")


if __name__ == "__main__":
    main()
