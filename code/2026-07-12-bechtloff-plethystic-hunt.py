#!/usr/bin/env python3
"""
OQ-BECHTLOFF-PLETHYSTIC hunt.

Goal: find pairs of partitions (alpha, beta) such that in the ring Lambda of
symmetric functions,

    s_alpha[S_+] * s_beta[S_-]  =  e_2^j * p_1^{n-2j}

where
    S_+ = sum_{k>=0} h_{2k}   (even h's, including h_0 = 1)
    S_- = sum_{k>=0} h_{2k+1} (odd h's)

Degrees: |alpha| grades with base weight 2? No -- deg h_{2k} = 2k so the
degree-n part of s_alpha[S_+] is finite. In fact deg(s_alpha[S_+]) is at
least 0 (since h_0 = 1 makes S_+ have a constant term).

We work in the power-sum basis. Plethysm rule:
    p_k[f]  = f with each p_i replaced by p_{k*i}.
    (f g)[h] = f[h] * g[h],   (f + g)[h] = f[h] + g[h].

A symmetric function of homogeneous degree n is represented as a dict
{ partition_tuple : rational_coefficient } giving its expansion
    f = sum_mu c_mu p_mu
where partition_tuple is a strictly decreasing tuple? No -- use weakly
decreasing tuple representing the partition.

We truncate every computation to total degree <= N (say N = 8 to cover n up
to 8 comfortably).
"""

from fractions import Fraction
from functools import lru_cache
from itertools import product
from collections import defaultdict


# ------------------------------------------------------------------
# Partitions and characters
# ------------------------------------------------------------------

def partitions(n, max_part=None):
    """All partitions of n as tuples in weakly decreasing order."""
    if n == 0:
        yield ()
        return
    if max_part is None:
        max_part = n
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def all_partitions_up_to(N):
    """All partitions of 0..N."""
    out = {}
    for n in range(N + 1):
        out[n] = list(partitions(n))
    return out


def z_mu(mu):
    """z_mu = prod i^{m_i} m_i! where m_i is the multiplicity of i in mu."""
    from collections import Counter
    c = Counter(mu)
    result = 1
    for i, m in c.items():
        # i^m * m!
        result *= (i ** m)
        for k in range(1, m + 1):
            result *= k
    return result


# Character table via Murnaghan-Nakayama recursion.
#
# chi^lambda_mu = sum over rim hooks r of length mu[0] in lambda
#                     of (-1)^{ht(r)} * chi^{lambda \ r}_{mu[1:]}
#
# Base: chi^{()}_{()} = 1.

def rim_hooks(lam, k):
    """Yield (new_lambda, height) for each rim hook of size k in lam.

    lam is a tuple weakly decreasing (partition). height = (# rows of hook) - 1.
    Approach: iterate over all subsets of border cells... use the standard
    algorithm via beta-numbers.
    """
    # Use beta-numbers: for partition lam of length ell, define
    #   beta_i = lam_i + (ell - i) for i = 1..ell.
    # A rim hook of size k <-> decreasing beta_i by k, provided the result
    # is still a strict set of nonneg integers of size ell.
    # Height of the hook = (# beta_j strictly between new_beta_i and old_beta_i).
    if not lam:
        return
    lam = list(lam)
    ell = len(lam)
    # Pad with zeros to allow rim hooks that extend to a new row? Actually
    # for k <= |lam| we never need to extend; but rim hooks can touch the
    # bottom. Use ell rows only (no extra padding needed if lam has enough
    # trailing structure). Actually rim hooks can be a single row that
    # "extends past the bottom" only if we allow ell+? -- no, rim hook must
    # be inside lambda. So we're fine.
    beta = [lam[i] + (ell - 1 - i) for i in range(ell)]
    # beta strictly decreasing, beta[-1] >= 0.
    beta_set = set(beta)
    for i in range(ell):
        new_val = beta[i] - k
        if new_val < 0:
            continue
        if new_val in beta_set:
            continue
        # Height = # of j != i with beta[j] between new_val and beta[i] exclusive.
        # (Standard formula.)
        height = sum(1 for j in range(ell) if j != i and new_val < beta[j] < beta[i])
        new_beta = list(beta)
        new_beta[i] = new_val
        # Convert back to partition: sort descending, subtract (ell-1-i).
        new_beta_sorted = sorted(new_beta, reverse=True)
        new_lam = tuple(new_beta_sorted[i] - (ell - 1 - i) for i in range(ell))
        # Drop trailing zeros.
        new_lam = tuple(x for x in new_lam if x > 0) + tuple()
        # Remove trailing zeros properly:
        while new_lam and new_lam[-1] == 0:
            new_lam = new_lam[:-1]
        yield new_lam, height


@lru_cache(maxsize=None)
def chi(lam, mu):
    """Character chi^lambda evaluated on conjugacy class mu."""
    if lam == () and mu == ():
        return 1
    if sum(lam) != sum(mu):
        return 0
    if mu == ():
        return 1 if lam == () else 0
    # Peel off the largest part of mu (or any part; convention: use mu[0]).
    k = mu[0]
    rest = mu[1:]
    total = 0
    for new_lam, height in rim_hooks(lam, k):
        total += ((-1) ** height) * chi(new_lam, rest)
    return total


# ------------------------------------------------------------------
# Symmetric functions in the p-basis, truncated.
# ------------------------------------------------------------------
#
# A "SymFn" is a dict { partition_tuple : Fraction } representing
#   sum_mu c_mu * p_mu
# where partition_tuple is a weakly decreasing tuple.
# The degree is |mu| = sum(mu). We work truncated to total degree <= N.

def sf_zero():
    return {}


def sf_one():
    return {(): Fraction(1)}


def sf_add(f, g, N=None):
    out = dict(f)
    for mu, c in g.items():
        if N is not None and sum(mu) > N:
            continue
        out[mu] = out.get(mu, Fraction(0)) + c
        if out[mu] == 0:
            del out[mu]
    return out


def sf_scale(f, c):
    if c == 0:
        return {}
    return {mu: v * c for mu, v in f.items()}


def sf_mul(f, g, N):
    """Multiply two SymFns, truncating at degree N."""
    out = defaultdict(Fraction)
    for mu, cf in f.items():
        if sum(mu) > N:
            continue
        for nu, cg in g.items():
            deg = sum(mu) + sum(nu)
            if deg > N:
                continue
            combined = tuple(sorted(list(mu) + list(nu), reverse=True))
            out[combined] += cf * cg
    return {k: v for k, v in out.items() if v != 0}


def sf_pow(f, k, N):
    """f^k, truncated."""
    result = sf_one()
    for _ in range(k):
        result = sf_mul(result, f, N)
    return result


# ------------------------------------------------------------------
# Building blocks: h_n, e_n, p_n, s_lambda in p-basis.
# ------------------------------------------------------------------

def p_n(n):
    """p_n."""
    if n == 0:
        return sf_one()
    return {(n,): Fraction(1)}


@lru_cache(maxsize=None)
def h_n_partitions(n):
    """Return h_n as SymFn in p-basis: h_n = sum_{mu |- n} p_mu / z_mu."""
    if n == 0:
        return sf_one()
    out = {}
    for mu in partitions(n):
        out[mu] = Fraction(1, z_mu(mu))
    return out


@lru_cache(maxsize=None)
def e_n_partitions(n):
    """e_n = sum_{mu |- n} (-1)^{n - ell(mu)} / z_mu * p_mu."""
    if n == 0:
        return sf_one()
    out = {}
    for mu in partitions(n):
        sign = (-1) ** (n - len(mu))
        out[mu] = Fraction(sign, z_mu(mu))
    return out


def schur_p(lam, N=None):
    """s_lambda in the p-basis: s_lam = sum_{mu |- |lam|} chi^lam_mu / z_mu * p_mu."""
    n = sum(lam)
    if N is not None and n > N:
        return {}
    out = {}
    for mu in partitions(n):
        c = chi(lam, mu)
        if c == 0:
            continue
        out[mu] = Fraction(c, z_mu(mu))
    return out


# ------------------------------------------------------------------
# Plethysm.
# ------------------------------------------------------------------
#
# Given f (SymFn) and g (SymFn), compute f[g] truncated to degree <= N.
#
# f is a polynomial in the p_i's:
#     f = sum_mu c_mu * p_mu = sum_mu c_mu * prod_i p_{mu_i}
# So
#     f[g] = sum_mu c_mu * prod_i (p_{mu_i}[g])
# And p_k[g] = g with every p_j replaced by p_{k*j}.

def p_k_of(g, k, N):
    """Compute p_k[g]: replace every p_j in g by p_{k*j}, truncate to deg <= N."""
    out = {}
    for mu, c in g.items():
        # New partition: multiply each part by k, resort.
        new_mu = tuple(sorted([j * k for j in mu], reverse=True))
        if sum(new_mu) > N:
            continue
        out[new_mu] = out.get(new_mu, Fraction(0)) + c
    return {k2: v for k2, v in out.items() if v != 0}


def plethysm(f, g, N):
    """Compute f[g] truncated to total degree <= N."""
    out = sf_zero()
    for mu, c in f.items():
        # Compute prod_i p_{mu_i}[g].
        term = sf_one()
        for k in mu:
            pkg = p_k_of(g, k, N)
            term = sf_mul(term, pkg, N)
            if not term:
                break
        out = sf_add(out, sf_scale(term, c), N)
    return out


# ------------------------------------------------------------------
# Degree truncation & extraction.
# ------------------------------------------------------------------

def sf_degree_n(f, n):
    """Extract the degree-n part."""
    return {mu: c for mu, c in f.items() if sum(mu) == n}


def sf_equal(f, g):
    keys = set(f) | set(g)
    for k in keys:
        if f.get(k, Fraction(0)) != g.get(k, Fraction(0)):
            return False
    return True


def sf_str(f):
    if not f:
        return "0"
    items = sorted(f.items(), key=lambda kv: (sum(kv[0]), kv[0]))
    parts = []
    for mu, c in items:
        parts.append(f"{c} * p{list(mu)}")
    return " + ".join(parts)


# ------------------------------------------------------------------
# The hunt.
# ------------------------------------------------------------------

def build_S_plus(N):
    """S_+ = sum_{k>=0} h_{2k} truncated to degree <= N."""
    out = sf_zero()
    k = 0
    while 2 * k <= N:
        out = sf_add(out, h_n_partitions(2 * k), N)
        k += 1
    return out


def build_S_minus(N):
    """S_- = sum_{k>=0} h_{2k+1} truncated to degree <= N."""
    out = sf_zero()
    k = 0
    while 2 * k + 1 <= N:
        out = sf_add(out, h_n_partitions(2 * k + 1), N)
        k += 1
    return out


def target(n, j):
    """e_2^j * p_1^{n-2j} truncated to degree n (it is homogeneous of degree n)."""
    e2 = e_n_partitions(2)
    p1 = p_n(1)
    lhs = sf_pow(e2, j, n)
    rhs = sf_pow(p1, n - 2 * j, n)
    return sf_mul(lhs, rhs, n)


def hunt(n, j, alpha_beta_bound, verbose=False):
    """Search for (alpha, beta) with s_alpha[S+] * s_beta[S-] = target in degree n."""
    N = n
    Splus = build_S_plus(N)
    Sminus = build_S_minus(N)
    tgt = target(n, j)
    # Enumerate alpha, beta with |alpha| + |beta| <= alpha_beta_bound.
    # But actually the degree of s_alpha[S_+] can range across many degrees
    # (because S_+ has multiple degree components). What we need is that
    # deg(s_alpha[S_+] * s_beta[S_-]) has a degree-n component matching target.
    #
    # Bound: to have degree-n contribution, we need s_alpha[S_+] to have some
    # component of degree d <= n, and s_beta[S_-] of degree n - d. Now
    # s_alpha[S_+] evaluated at a partition of Sym has "size" = |alpha| * ??? Actually,
    # since h_0 = 1, S_+ has p_0-like constant term = ??? Actually h_0 = 1 in Lambda
    # has degree 0. Then s_alpha[S_+] evaluated: the lowest-degree contribution
    # depends on alpha. If alpha = (), s_alpha = 1 and s_alpha[S_+] = 1 has
    # degree 0. Generally s_alpha[S_+] has terms of all degrees >= 0 in general.
    #
    # For efficiency, only enumerate |alpha|, |beta| <= alpha_beta_bound.
    matches = []
    all_alpha = []
    for k in range(alpha_beta_bound + 1):
        all_alpha.extend(partitions(k))
    all_beta = list(all_alpha)
    # Cache plethysms.
    salpha_Splus_cache = {}
    for alpha in all_alpha:
        salpha = schur_p(alpha, N)
        salpha_Splus_cache[alpha] = plethysm(salpha, Splus, N)
    sbeta_Sminus_cache = {}
    for beta in all_beta:
        sbeta = schur_p(beta, N)
        sbeta_Sminus_cache[beta] = plethysm(sbeta, Sminus, N)
    for alpha in all_alpha:
        A = salpha_Splus_cache[alpha]
        for beta in all_beta:
            B = sbeta_Sminus_cache[beta]
            prod = sf_mul(A, B, N)
            deg_n = sf_degree_n(prod, n)
            if sf_equal(deg_n, tgt):
                matches.append((alpha, beta))
                if verbose:
                    print(f"  MATCH n={n} j={j}: alpha={alpha}, beta={beta}")
    return matches, tgt


def main():
    print("=" * 70)
    print("OQ-BECHTLOFF-PLETHYSTIC hunt")
    print("=" * 70)
    print()
    print("Environment: Python 3 + sympy fractions (SageMath not available).")
    print("All computations in Lambda = Q[p_1, p_2, ...] truncated to deg <= n.")
    print()

    # Sanity: for n=2, j=1, target = e_2 = (1/2)(p_1^2 - p_2).
    print("Sanity: e_2 =", sf_str(e_n_partitions(2)))
    print("Sanity: e_2 * p_1^0 (n=2, j=1):", sf_str(target(2, 1)))
    print("Sanity: h_2 =", sf_str(h_n_partitions(2)))
    print("Sanity: p_1^2 (n=2, j=0):", sf_str(target(2, 0)))
    print()

    # Character check: chi^{(2)} should be [1,1] on classes [(2),(1,1)].
    print("chi^(2) on (2):", chi((2,), (2,)))
    print("chi^(2) on (1,1):", chi((2,), (1, 1)))
    print("chi^(1,1) on (2):", chi((1, 1), (2,)))
    print("chi^(1,1) on (1,1):", chi((1, 1), (1, 1)))
    print("chi^(3) on (3):", chi((3,), (3,)))
    print("chi^(2,1) on (3):", chi((2, 1), (3,)))
    print("chi^(2,1) on (2,1):", chi((2, 1), (2, 1)))
    print("chi^(2,1) on (1,1,1):", chi((2, 1), (1, 1, 1)))
    print()

    # Plethysm sanity: p_2[h_1] = p_2 (since h_1 = p_1, p_2[p_1] = p_2).
    print("p_2[h_1] =", sf_str(plethysm(p_n(2), h_n_partitions(1), 4)))
    print("h_2[p_1] =", sf_str(plethysm(h_n_partitions(2), p_n(1), 4)))
    print()

    # Main hunt.
    for n in range(2, 8):
        print(f"--- n = {n} ---")
        for j in range(n // 2 + 1):
            if 2 * j > n:
                continue
            # Bound on |alpha|, |beta|. Choose generously.
            bound = n
            matches, tgt = hunt(n, j, alpha_beta_bound=bound, verbose=False)
            print(f"  n={n}, j={j}, target = e_2^{j} p_1^{n-2*j}")
            print(f"    target =", sf_str(tgt))
            if matches:
                # Sort by (|alpha|, |beta|, alpha, beta) and dedupe.
                matches_sorted = sorted(matches, key=lambda ab: (sum(ab[0]) + sum(ab[1]), ab[0], ab[1]))
                print(f"    {len(matches_sorted)} match(es):")
                for a, b in matches_sorted[:20]:
                    print(f"      alpha={a}, beta={b}")
                if len(matches_sorted) > 20:
                    print(f"      ... and {len(matches_sorted) - 20} more")
            else:
                print("    NO MATCHES.")
        print()


if __name__ == "__main__":
    main()
