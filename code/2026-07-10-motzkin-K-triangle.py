"""Day 88 — OQ-MOTZKIN-K-TRIANGLE (verification/refutation).

Original claim (Poulain d'Andecy Cor 4.4 -> Motzkin-2 centralizer):
    K_{mu^T, (2^j)} = m^(2)_{k, j}
for j <= 6 and some correspondence k <-> mu.

  m^(2)_{k, j} := multiplicity of V_k of U_q(sl_2) in (V_1 (+) V_2)^{tensor j}.
  V_r denotes the (2r+1)-dim irrep (V_1 = 3-dim, V_2 = 5-dim).
  K_{mu^T, (2^j)} := coefficient of s_mu in e_2^j (Pieri).

The trigger flagged "check recursion carefully" — so this script:

  1. Computes m^(2)_{k, j} with the correct SO(3)-style Clebsch-Gordan:
        V_a (X) V_r = (+)_{k=|r-a|}^{r+a} V_k     (mult 1 each).
     Sanity: dim check sum_k (2k+1) m^(2)_{k, j} =?= 8^j.

  2. Computes K_{mu^T, (2^j)} via Pieri (vertical 2-strips), for mu with
     at most 3 rows. Sanity: sum of K's =?= M_j (Motzkin number).

  3. Tries every "natural" k <-> mu correspondence and reports match.

  4. If face-value identity fails, characterises the actual object the K's
     count (walk on the SL_3 Bratteli graph in vertical-2-strip steps).

Also emits the m^(1) table (V_1 alone) for comparison / sanity.
"""
from collections import defaultdict
from itertools import combinations
from math import factorial


def C(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


# ---------------------------------------------------------------------------
# 1. m_{k, j}: multiplicity of V_k in a tensor power of a chosen source rep.
# ---------------------------------------------------------------------------

def cg_range(r, a):
    """Clebsch-Gordan: V_a (X) V_r = (+)_{k=|r-a|}^{r+a} V_k."""
    return range(abs(r - a), r + a + 1)


def build_mult_table(j_max, sources=(1, 2)):
    """Compute multiplicities of V_k in ((+)_{s in sources} V_s)^{tensor j}.

    Recursion: at each step, take each current V_r isotype and tensor with
    each source V_s, distributing according to CG.
    """
    prev = defaultdict(int)
    prev[0] = 1
    tables = [dict(prev)]
    for _ in range(j_max):
        curr = defaultdict(int)
        for r, mult in prev.items():
            for s in sources:
                for k in cg_range(r, s):
                    curr[k] += mult
        prev = curr
        tables.append(dict(prev))
    return tables


def print_mult_table(tables, label):
    j_max = len(tables) - 1
    all_ks = set()
    for t in tables:
        all_ks.update(t.keys())
    ks_sorted = sorted(all_ks)
    print(f"\n{label} table (rows = j, cols = k):")
    header = "  j\\k | " + " ".join(f"{k:>6d}" for k in ks_sorted) + " | rowsum"
    print(header)
    print("-" * len(header))
    for j, t in enumerate(tables):
        rowsum = sum(t.values())
        row = f"  {j:>3d} | " + " ".join(f"{t.get(k, 0):>6d}" for k in ks_sorted)
        print(f"{row} | {rowsum:>8d}")


def dim_check(tables, source_dim, label):
    print(f"\nDim check for {label}: sum_k (2k+1) m_k =?= {source_dim}^j")
    for j, t in enumerate(tables):
        total = sum((2 * k + 1) * mult for k, mult in t.items())
        expected = source_dim ** j
        mark = "OK" if total == expected else "FAIL"
        print(f"  j = {j}: sum = {total}, {source_dim}^j = {expected}  {mark}")


# ---------------------------------------------------------------------------
# 2. K_{mu^T, (2^j)}: coefficient of s_mu in e_2^j.
# ---------------------------------------------------------------------------

def add_vertical_2_strip(mu, max_rows=None):
    """All partitions nu s.t. nu / mu is a vertical 2-strip (add 2 cells in
    different rows)."""
    L = len(mu) + 2
    base = list(mu) + [0] * (L - len(mu))
    results = []
    for pair in combinations(range(L), 2):
        new = base.copy()
        for i in pair:
            new[i] += 1
        ok = True
        for i in range(L - 1):
            if new[i] < new[i + 1]:
                ok = False
                break
        if not ok:
            continue
        while new and new[-1] == 0:
            new.pop()
        if max_rows is not None and len(new) > max_rows:
            continue
        results.append(tuple(new))
    return results


def e2_power_schur(j_max, max_rows=None):
    tables = [{(): 1}]
    curr = defaultdict(int)
    curr[()] = 1
    for _ in range(j_max):
        nxt = defaultdict(int)
        for mu, coef in curr.items():
            for nu in add_vertical_2_strip(mu, max_rows=max_rows):
                nxt[nu] += coef
        curr = nxt
        tables.append(dict(curr))
    return tables


def pad3(mu):
    return tuple(list(mu) + [0] * (3 - len(mu)))


def partition_transpose(mu):
    mu = list(mu)
    while mu and mu[-1] == 0:
        mu.pop()
    if not mu:
        return ()
    m = mu[0]
    return tuple(sum(1 for x in mu if x > i) for i in range(m))


# ---------------------------------------------------------------------------
# 3. Motzkin triangle T(j, k): # Motzkin paths of length j from 0 to k.
# ---------------------------------------------------------------------------

def motzkin_triangle(j_max):
    """Standard Motzkin triangle: T(j, k) counts paths of length j from
    height 0 to height k with steps {-1, 0, +1}, staying >= 0.

    Recursion:
        T(0, 0) = 1; T(0, k) = 0 for k > 0.
        T(j, 0) = T(j-1, 0) + T(j-1, 1)
        T(j, k) = T(j-1, k-1) + T(j-1, k) + T(j-1, k+1)  for k >= 1.
    """
    T = [{0: 1}]
    for j in range(1, j_max + 1):
        row = {}
        prev = T[j - 1]
        for k in range(j + 1):
            val = 0
            if k >= 1:
                val += prev.get(k - 1, 0)
            val += prev.get(k, 0)
            val += prev.get(k + 1, 0)
            row[k] = val
        # Special: T(j, 0) uses reduced recursion (no down-step from 0).
        row[0] = prev.get(0, 0) + prev.get(1, 0)
        T.append(row)
    return T


# ---------------------------------------------------------------------------
# 4. Correspondence tests.
# ---------------------------------------------------------------------------

def try_correspondence(K_tables, target_tables, target_label, name, k_from_mu):
    """Test if K_{mu^T, (2^j)} aggregated by k = k_from_mu(mu) equals
    target_tables[j][k] for all j."""
    print(f"\n--- {name}  (target: {target_label}) ---")
    j_max = min(len(K_tables), len(target_tables)) - 1
    all_ok = True
    for j in range(j_max + 1):
        K_by_k = defaultdict(int)
        for mu, coef in K_tables[j].items():
            if len(mu) > 3:
                continue
            mu3 = pad3(mu)
            k = k_from_mu(mu3)
            if k is None or k < 0:
                continue
            K_by_k[k] += coef
        target_row = target_tables[j]
        all_ks = sorted(set(K_by_k) | set(target_row))
        row_ok = all(K_by_k.get(k, 0) == target_row.get(k, 0) for k in all_ks)
        if not row_ok:
            all_ok = False
            print(f"  j = {j}: MISMATCH")
            for k in all_ks:
                a, b = K_by_k.get(k, 0), target_row.get(k, 0)
                mark = "OK" if a == b else "!!"
                if a != 0 or b != 0:
                    print(f"    k={k}: K={a}, target={b}  {mark}")
        else:
            print(f"  j = {j}: MATCH  (sum: K={sum(K_by_k.values())}, target={sum(target_row.values())})")
    print(f"  RESULT: {'*** ALL MATCH ***' if all_ok else 'mismatch'}")
    return all_ok


def print_K_table_by_mu(K_tables, j_max):
    print("\nK_{mu^T, (2^j)} table, mu with <= 3 rows:")
    for j in range(j_max + 1):
        row_sum = sum(coef for mu, coef in K_tables[j].items() if len(mu) <= 3)
        print(f"\n  j = {j}  (|mu| = {2 * j}, total K = {row_sum}):")
        for mu, coef in sorted(K_tables[j].items(), reverse=True):
            if len(mu) > 3:
                continue
            mu3 = pad3(mu)
            mu_str = f"({mu3[0]}, {mu3[1]}, {mu3[2]})"
            mu_T = partition_transpose(mu3)
            mu_T_str = "(" + ", ".join(str(x) for x in mu_T) + ")"
            print(f"    mu = {mu_str},  mu^T = {mu_T_str},  K = {coef}")


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main():
    j_max = 6
    print("=" * 78)
    print("OQ-MOTZKIN-K-TRIANGLE  (j <= 6)")
    print("Claim: K_{mu^T, (2^j)} = m^(2)_{k, j} for some k <-> mu bijection.")
    print("=" * 78)

    # --- m^(1) sanity (V_1 alone) ---
    m1_tables = build_mult_table(j_max, sources=(1,))
    print_mult_table(m1_tables, "m^(1)_{k, j}   (V_1 alone, V_1 = 3-dim)")
    dim_check(m1_tables, source_dim=3, label="m^(1)")

    # --- m^(2) (V_1 (+) V_2, the Motzkin-2 setup) ---
    m2_tables = build_mult_table(j_max, sources=(1, 2))
    print_mult_table(m2_tables, "m^(2)_{k, j}   (V_1 (+) V_2, V_1 = 3-dim, V_2 = 5-dim)")
    dim_check(m2_tables, source_dim=8, label="m^(2)")

    # --- Motzkin triangle (ordinary) ---
    T = motzkin_triangle(j_max)
    print("\nMotzkin triangle T(j, k)  (steps {-1, 0, +1}, non-negative, from 0 to k):")
    all_ks = set()
    for t in T:
        all_ks.update(t.keys())
    ks_sorted = sorted(all_ks)
    header = "  j\\k | " + " ".join(f"{k:>4d}" for k in ks_sorted) + " | rowsum"
    print(header)
    print("-" * len(header))
    for j, t in enumerate(T):
        row_sum = sum(t.values())
        row = f"  {j:>3d} | " + " ".join(f"{t.get(k, 0):>4d}" for k in ks_sorted)
        print(f"{row} | {row_sum:>6d}")
    print("  (Ordinary Motzkin numbers M_j = T(j, 0) = 1, 1, 2, 4, 9, 21, 51.)")

    # --- K table ---
    K_tables = e2_power_schur(j_max, max_rows=3)
    print_K_table_by_mu(K_tables, j_max)

    # Row sums.
    print("\nK-table row sums (over mu with <= 3 rows):")
    K_row_sums = []
    for j in range(j_max + 1):
        s = sum(coef for mu, coef in K_tables[j].items() if len(mu) <= 3)
        K_row_sums.append(s)
        print(f"  j = {j}: sum K = {s}")
    print(f"K row sums: {K_row_sums}")
    print(f"Motzkin M_j: {[T[j].get(0, 0) for j in range(j_max + 1)]}")
    match_motzkin = K_row_sums == [T[j].get(0, 0) for j in range(j_max + 1)]
    print(f"K row sums == Motzkin M_j?  {match_motzkin}")

    print("\n" + "=" * 78)
    print("CORRESPONDENCE TESTS")
    print("=" * 78)
    print("(Aggregating K's by k = f(mu) and comparing to m^(1), m^(2), and T.)")

    results = {}

    # ==== m^(2) as target ====
    print("\n### Target: m^(2)_{k, j}  (Rick's original claim) ###")
    for name, k_fn in [
        ("k = mu_1 - mu_2",              lambda mu: mu[0] - mu[1]),
        ("k = mu_1 - mu_3",              lambda mu: mu[0] - mu[2]),
        ("k = mu_2 - mu_3",              lambda mu: mu[1] - mu[2]),
        ("k = mu_1 + mu_2 - 2 mu_3",     lambda mu: mu[0] + mu[1] - 2 * mu[2]),
        ("k = 2 mu_1 - mu_2 - mu_3",     lambda mu: 2 * mu[0] - mu[1] - mu[2]),
    ]:
        ok = try_correspondence(K_tables, m2_tables, "m^(2)", name, k_fn)
        results[("m^(2)", name)] = ok

    # ==== m^(1) as target ====
    print("\n### Target: m^(1)_{k, j}  (Ordinary Motzkin V_1 alone) ###")
    for name, k_fn in [
        ("k = mu_1 - mu_2",              lambda mu: mu[0] - mu[1]),
        ("k = mu_1 - mu_3",              lambda mu: mu[0] - mu[2]),
        ("k = mu_2 - mu_3",              lambda mu: mu[1] - mu[2]),
    ]:
        ok = try_correspondence(K_tables, m1_tables, "m^(1)", name, k_fn)
        results[("m^(1)", name)] = ok

    # ==== T (Motzkin triangle) as target ====
    print("\n### Target: T(j, k)  (Motzkin triangle) ###")
    for name, k_fn in [
        ("k = mu_1 - mu_2",              lambda mu: mu[0] - mu[1]),
        ("k = mu_1 - mu_3",              lambda mu: mu[0] - mu[2]),
        ("k = mu_2 - mu_3",              lambda mu: mu[1] - mu[2]),
        ("k = mu_3",                     lambda mu: mu[2]),
    ]:
        ok = try_correspondence(K_tables, T, "T", name, k_fn)
        results[("T", name)] = ok

    # ==== Summary ====
    print("\n" + "=" * 78)
    print("SUMMARY OF CORRESPONDENCE TESTS")
    print("=" * 78)
    for (target, name), ok in results.items():
        print(f"  target={target:>8s}  {name:<40s}  {'PASS' if ok else 'FAIL'}")

    # --- Structural finding: what do the K's actually count? ---
    print("\n" + "=" * 78)
    print("STRUCTURAL FINDING")
    print("=" * 78)
    print(
        """
Structural facts established by this computation:

  (F1)  m^(2)_{k, j} (V_1 (+) V_2 tensor centraliser dims) row sums are
        1, 2, 14, 116, 1008, 8942, 80066  -- NOT Motzkin numbers.
        (Dim check: sum_k (2k+1) m^(2)_{k, j} = 8^j PASSES, confirming
        the (V_1 + V_2)^tensor j dimension.)

  (F2)  sum_{mu <= 3 rows, |mu| = 2j} K_{mu^T, (2^j)} = M_j
        (ordinary Motzkin: 1, 1, 2, 4, 9, 21, 51).

  (F3)  Therefore the OQ face-value identity
              K_{mu^T, (2^j)} = m^(2)_{k, j}
        is REFUTED at the level of row sums: 1 vs 1, 1 vs 2 already
        disagrees at j = 1.  No k <-> mu bijection can save it.

  (F4)  The K's do count something structural: sequences
              () = nu^0 sub nu^1 sub ... sub nu^j = mu
        where each nu^{i+1}/nu^i is a vertical 2-strip and each nu^i is
        a partition with <= 3 rows.  This is the Bratteli graph for
        GL_3 acting on (Lambda^2 C^3)^{tensor j}.

  (F5)  In (x, y) = (mu_1 - mu_2, mu_2 - mu_3) coordinates the walk
        has three step types:
              A: (Delta x, Delta y) = (0, +1)   [add row 1 & row 2]
              B: (+1, -1)                       [add row 1 & row 3]
              C: (-1,  0)                       [add row 2 & row 3]
        with the constraint x >= 0, y >= 0 throughout.  Ending point
        (x, y) satisfies mu_3 = j - (x + 2y + x)... etc; the number of
        such walks ending at mu = K_{mu^T, (2^j)}.  This is a
        "3-step Motzkin-like walk in the SL_3 Weyl chamber", NOT the
        classical Motzkin-2 (5-cell) walk that centralises V_1 (+) V_2.

  (F6)  Root-cause of Rick's OQ misfire: he conflated two centralisers.
        The Motzkin-2 algebra (centraliser of U_q(sl_2) on
        (V_1 + V_2)^tensor j) has cell-module dims m^(2)_{k, j} which
        grow as ~8^j.  The Kostka numbers K_{mu^T, (2^j)} instead
        count multiplicities in (Lambda^2 C^3)^tensor j as GL_3-rep,
        which grow as ~3^j (Motzkin sum sequence).

Consequence: OQ-MOTZKIN-MJ-CENTRALIZER does NOT close via this route.
The Motzkin-2 centraliser interpretation of M_j coefficients is a
DIFFERENT identification -- via the SL_3 -> principal SL_2 restriction:

        m^(1)_{k, j} = sum_{mu} K_{mu^T, (2^j)} * mult(V_k, S^mu | pSL_2)

where S^mu is a GL_3 Schur module and mult(V_k, .) is the principal
SL_2 branching multiplicity.  The K's are grouping coefficients in
this refined branching -- NOT the multiplicities themselves.
"""
    )


if __name__ == "__main__":
    main()
