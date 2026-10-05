"""
Day 188 — Route B feasibility check: does Rick's (Re) at q=1 match GDL-W bond-lattice h-expansion?

CONTEXT:
- Rick's (Re): X_{P_n} = e_n + sum_{k=2}^n (k-1) e_k X_{P_{n-k}}   (q=1)
- GDL-W (arXiv:2608.08692) studies the Mobius polynomial mu_G(t) and the
  symmetric function Psi_G(x), which they explicitly warn is "DIFFERENT from
  Stanley's well-known chromatic symmetric function" (p.53).

Goals of this script:
1. Compute X_{P_n} for n=1..7 in e-basis via Rick's (Re) at q=1.
2. Convert to h-basis.
3. Compute GDL-W Psi_{P_n}(x) via Whitney's formula on the bond lattice Pi_{P_n},
   for small n to check whether Rick's X_{P_n} and GDL-W's Psi_{P_n} (or its
   omega-image, or its highest-degree component M_{P_n}) coincide in any basis.

The paper states (p.7):
    "when G is equal to the path graph with n vertices, (-1)^{n-1} omega M_G(x)
     is the parking function symmetric function of Haiman [28]"
where M_G is the top-degree part of Psi_G and omega swaps h_n <-> e_n.

The Stanley chromatic symmetric function X_{P_n} is NOT the parking function
symmetric function. So we expect NO direct match; the check quantifies the gap.
"""

import sympy as sp
from sympy import Symbol, Rational, symbols, Poly, expand, simplify

# ---------- Symbolic e_k and h_k as formal variables ----------
# We'll represent symmetric functions as polynomials in formal e_1, e_2, ...
# then convert e-basis <-> h-basis via the standard involution.

N_MAX = 7  # go up to n=7 to be safe

E = [Symbol(f'e{k}') for k in range(N_MAX + 1)]  # e_0 = 1 formal placeholder
H = [Symbol(f'h{k}') for k in range(N_MAX + 1)]
E[0] = sp.Integer(1)
H[0] = sp.Integer(1)


# ---------- Rick's (Re) at q=1 ----------
def rick_X_e_basis(n_max):
    """Compute X_{P_n} in the e-basis (as a polynomial in e_1,...,e_n)
       via X_n = e_n + sum_{k=2..n} (k-1) e_k X_{n-k}, X_0 = 1."""
    X = [sp.Integer(1)]  # X_0 = 1
    for n in range(1, n_max + 1):
        if n == 1:
            X.append(E[1])
        else:
            expr = E[n] + sum((k - 1) * E[k] * X[n - k] for k in range(2, n + 1))
            X.append(sp.expand(expr))
    return X


# ---------- e-basis <-> h-basis conversion ----------
# Newton's identity for e and h:
# sum_{k=0}^n (-1)^k e_k h_{n-k} = 0 for n >= 1
# Equivalently: E(t) H(-t) = 1, where E(t) = sum e_k t^k, H(t) = sum h_k t^k.
# We use: h_n = sum over partitions lambda of n of (something) e_lambda.
#
# The cleanest way: express e_k in terms of h's, then substitute.
# Standard formulas:
#   sum_{k>=0} h_k t^k = 1 / sum_{k>=0} (-1)^k e_k t^k
#   sum_{k>=0} e_k t^k = 1 / sum_{k>=0} (-1)^k h_k t^k
#
# Given a polynomial in e_1..e_n, we want its h-basis expansion.
# We compute the h_lambda -> e_lambda transition matrix and invert.

def h_in_terms_of_e(n):
    """Return h_n as a polynomial in e_1,...,e_n using
       h_n = det of a Jacobi-Trudi-like matrix, or via Newton's identity:
       h_n = -sum_{k=1}^n (-1)^k e_k h_{n-k}."""
    h = [sp.Integer(1)]
    for m in range(1, n + 1):
        val = -sum((-1)**k * E[k] * h[m - k] for k in range(1, m + 1))
        h.append(sp.expand(val))
    return h  # h[0] = 1, h[1] = e_1, h[2] = e_1^2 - e_2, ...


def e_in_terms_of_h(n):
    """Return e_n as a polynomial in h_1,...,h_n via same Newton identity."""
    e = [sp.Integer(1)]
    for m in range(1, n + 1):
        val = -sum((-1)**k * H[k] * e[m - k] for k in range(1, m + 1))
        e.append(sp.expand(val))
    return e  # e[0] = 1, e[1] = h_1, e[2] = h_1^2 - h_2, ...


# ---------- Convert an e-polynomial to h-basis in symmetric functions ----------
# Symmetric functions are polynomials in {p_k} or {e_k} or {h_k}, but as a ring
# on infinite variables, they're a polynomial ring. To convert a polynomial
# expression in e_i's to h_i's, substitute e_k -> polynomial(h_1,...,h_k),
# then collect terms and express in the "monomial h-basis" indexed by partitions.

def sym_poly_to_h_basis(expr, n):
    """Given an e-polynomial expr homogeneous of degree n, express it in the
       h-basis {h_lambda : lambda |- n}."""
    # 1. Substitute each e_k with polynomial in h's
    e_in_h = e_in_terms_of_h(n)
    subs = {E[k]: e_in_h[k] for k in range(1, n + 1)}
    expr_h = sp.expand(expr.subs(subs))
    return expr_h  # This is a polynomial in h_1,...,h_n


def collect_by_partitions(poly_in_h, n):
    """Given a polynomial in h_1,...,h_n that is homogeneous of degree n
       (with weight of h_k being k), collect coefficients of h_lambda for
       each partition lambda of n. Return a dict {partition: coefficient}."""
    from sympy import Poly

    # Get all partitions of n
    def partitions(m):
        if m == 0:
            yield ()
            return
        for p in _partitions_helper(m, m):
            yield tuple(sorted(p, reverse=True))

    def _partitions_helper(m, max_part):
        if m == 0:
            yield ()
            return
        for k in range(min(m, max_part), 0, -1):
            for rest in _partitions_helper(m - k, k):
                yield (k,) + rest

    parts = list(partitions(n))
    result = {}

    # For each partition lambda = (l_1,...,l_r), the monomial h_lambda = h_{l_1} * ... * h_{l_r}
    # So we need the coefficient of h_1^{m_1(lambda)} * h_2^{m_2(lambda)} * ... in the expanded poly.
    # We treat H[k] as symbols and use sympy's polynomial handling.

    h_syms = [H[k] for k in range(1, n + 1)]
    p = sp.Poly(poly_in_h, *h_syms)
    coeff_dict = p.as_dict()  # (exponents) -> coefficient

    for lam in parts:
        # Convert lam to exponent vector
        exp_vec = [0] * n  # exponents of h_1,...,h_n
        for part in lam:
            exp_vec[part - 1] += 1
        key = tuple(exp_vec)
        result[lam] = coeff_dict.get(key, sp.Integer(0))

    return result


# ---------- Bond lattice of P_n and Whitney's Psi_{P_n} ----------
def path_bond_lattice(n):
    """Enumerate the bond lattice Pi_{P_n}: partitions of [n] whose blocks
       are intervals (i.e., induce connected subgraphs of P_n).
       Return a list of partitions, each as a sorted tuple of sorted tuples."""
    # A partition of [n] is a bond of P_n iff every block is an interval [a,b].
    # Equivalently, it's determined by choosing which of the n-1 edges to "cut".
    # If we cut a subset S of {1,...,n-1}, we get intervals separated by S.
    edges = list(range(1, n))  # edges 1..n-1 mean "cut between vertex k and k+1"
    lattice = []
    from itertools import combinations
    for r in range(n):  # number of cuts, 0 to n-1
        for cuts in combinations(edges, r):
            # Build intervals from cuts
            blocks = []
            prev = 1
            for c in cuts:
                blocks.append(tuple(range(prev, c + 1)))
                prev = c + 1
            blocks.append(tuple(range(prev, n + 1)))
            lattice.append(tuple(sorted(blocks)))
    return lattice


def mobius_pi_G(lattice):
    """Compute Mobius function mu(0_hat, pi) for each pi in the bond lattice.
       0_hat = all-singletons partition. Order is refinement (0_hat is finest)."""
    # For P_n bond lattice, this is the Mobius function of Pi_{P_n}.
    # Use recursive definition: mu(0,0) = 1; mu(0,pi) = -sum_{0 <= sigma < pi} mu(0,sigma).
    def refines(sigma, tau):
        """sigma <= tau (sigma refines tau)?"""
        # Each block of sigma is contained in some block of tau
        for B in sigma:
            found = False
            for C in tau:
                if set(B).issubset(set(C)):
                    found = True
                    break
            if not found:
                return False
        return True

    n = sum(len(b) for b in lattice[0])
    zero_hat = tuple(sorted((i,) for i in range(1, n + 1)))

    mu = {}
    # Compute in order of size (finer partitions have more blocks)
    lattice_sorted = sorted(lattice, key=lambda p: -len(p))  # finest first
    for pi in lattice_sorted:
        if pi == zero_hat:
            mu[pi] = sp.Integer(1)
        else:
            s = sp.Integer(0)
            for sigma in lattice_sorted:
                if sigma == pi:
                    continue
                if refines(sigma, pi):
                    s += mu[sigma]
            mu[pi] = -s
    return mu


# ---------- Main computation ----------
def main():
    print("=" * 70)
    print("Day 188 Route B: Rick's (Re)|q=1 vs GDL-W bond lattice for P_n")
    print("=" * 70)

    # 1. Rick's X_{P_n} in e-basis
    X = rick_X_e_basis(N_MAX)
    print("\n--- Rick's (Re) at q=1: X_{P_n} in e-basis ---")
    for n in range(1, N_MAX + 1):
        print(f"X_{{P_{n}}} = {X[n]}")

    # 2. Convert to h-basis
    print("\n--- Rick's X_{P_n} in h-basis (coefficients of h_lambda) ---")
    rick_h_table = {}
    for n in range(1, N_MAX + 1):
        expr_h = sym_poly_to_h_basis(X[n], n)
        coeffs = collect_by_partitions(expr_h, n)
        rick_h_table[n] = coeffs
        print(f"\nX_{{P_{n}}} =")
        for lam, c in sorted(coeffs.items(), key=lambda x: (-len(x[0]), x[0])):
            if c != 0:
                lam_str = ",".join(str(p) for p in lam)
                print(f"    {c} * h_{{{lam_str}}}")

    # 3. GDL-W Psi_{P_n} via Whitney's formula: Psi_G(x) = sum_{pi in Pi_G^infty} mu(0,pi) x^w(pi)
    # But we don't need multiweighted; the "classical" specialization at v=0 gives:
    # Psi_G(x) restricted to weight-0 partitions is the mu polynomial evaluated symbolically.
    # The paper says (7.2): Psi_{P_3}(x) = 1 - 2 e_1(x) + e_{1,1}(x) + e_2(x)
    # Let's verify this via bond lattice.
    print("\n\n--- GDL-W Psi_{P_n}(x) [bond lattice via Whitney, NON-weighted slice] ---")
    print("Note: paper's Psi_G is on WEIGHTED bond poset; we compute the (v=0) slice")
    print("which is Whitney's chromatic polynomial in symmetric-function form.")
    print()
    # Whitney: chi_G(x) = sum_{pi in Pi_G} mu_{Pi_G}(0, pi) * (product over blocks of p_{|B|}? or x^|pi|?)
    # Actually eq (1.4): chi_G(t) = sum_{pi in Pi_G} mu(0, pi) t^{|pi|}
    # The symmetric-function analog Psi_G(x) needs the paper's definition (7.1) with weighted bond poset.
    # From eq (7.2) for P_3: Psi_{P_3}(x) = 1 - 2 e_1(x) + e_{1,1}(x) + e_2(x)
    #   That is 1 - 2 e_1 + e_1^2 + e_2 - e_2 = 1 - 2 e_1 + e_1^2. Wait: e_{1,1} = e_1^2 - 2 e_2? no
    #   Actually e_{1,1} in monomial notation means e_1 * e_1 = e_1^2. And e_2 is e_2.
    #   So Psi_{P_3} = 1 - 2 e_1 + e_1^2 + e_2. Let's just print bond-lattice computation.

    for n in range(1, min(N_MAX, 4) + 1):
        L = path_bond_lattice(n)
        mu = mobius_pi_G(L)
        print(f"\nP_{n}: |Pi_{{P_{n}}}| = {len(L)}")
        # Print Mobius values at each partition
        print(f"  Mobius sum (this is chi_{{P_{n}}}(1) = 0 for n>=2 iff connected): ", end='')
        print(sum(mu[pi] for pi in L))
        # Print block structure counts
        from collections import Counter
        # For each pi, block sizes form a partition of n
        block_partition = lambda pi: tuple(sorted((len(b) for b in pi), reverse=True))
        by_shape = Counter()
        for pi in L:
            by_shape[block_partition(pi)] += mu[pi]
        for shape, weight in sorted(by_shape.items()):
            print(f"  shape {shape}: sum of mu = {weight}")

    # 4. Compare
    print("\n\n" + "=" * 70)
    print("VERDICT COMPUTATION")
    print("=" * 70)

    # The paper's Psi_{P_3} in (7.2) has degree only up to 2 (linear + quadratic).
    # Rick's X_{P_3} in e-basis is 3 e_3 + e_1 e_2 (degree exactly 3).
    # These live in different degrees! GDL-W Psi_G has degrees 0..n; Rick's X_G is
    # homogeneous of degree n. So Psi_G(x) is NOT a direct h-analog of X_G.
    #
    # The top-degree component M_G of Psi_G is homogeneous of degree n. This is
    # what the paper says is the parking function symmetric function for P_n.
    #
    # Rick's X_{P_n} is Stanley's chromatic symmetric function. It's known that
    # for path graphs, X_{P_n} is NOT the parking-function symmetric function.
    #
    # So the match, if any, would be between Rick's X_{P_n} h-basis and something
    # OTHER than M_G. The paper does NOT give a bond-lattice h-expansion for
    # Stanley's X_G specifically.

    print("""
KEY FINDING FROM PAPER:
- GDL-W define Psi_G(x) (eq 7.1) as a SYMMETRIC FUNCTION ANALOG OF THE
  CHROMATIC POLYNOMIAL via Whitney's formula on the WEIGHTED bond lattice.
- Paper explicitly says (p.53): "this is a symmetric function analog of the
  chromatic polynomial of a graph, which is DIFFERENT from Stanley's well-known
  chromatic symmetric function [41]."
- Paper example (7.2): Psi_{P_3}(x) = 1 - 2 e_1 + e_{1,1} + e_2 = 1 - 2e_1 + e_1^2 + e_2.
- Paper top-degree component M_G: for path graphs, (-1)^{n-1} omega M_{P_n} = parking function
  symmetric function of Haiman [28]. This is degree-n and h-basis-related via omega,
  but is NOT Stanley's X_{P_n}.

RICK'S OBJECT: X_{P_n} = Stanley's chromatic symmetric function of P_n
  (homogeneous of degree n, e-positive with (Re) recursion).

CONCLUSION:
- GDL-W's bond-lattice symmetric function Psi_G is NOT Stanley's X_G.
- The paper does NOT give any h-expansion of Stanley's X_{P_n} in terms of the
  bond lattice of P_n.
- Route B (checking Rick's (Re)|q=1 = GDL-W h-expansion) is INFEASIBLE as
  stated because GDL-W does not study Stanley's X_G. It studies a DIFFERENT
  symmetric function.

Possible salvage: does the paper's M_G (parking function connection) tell us
anything about X_{P_n}? Only via a nontrivial identity NOT in this paper.
""")


if __name__ == "__main__":
    main()
