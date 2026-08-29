"""Use Jacobi-Trudi to get closed form for K_{mu', (2^j)} where mu = 3-part partition.

Row JT: s_mu = det [ h_{mu_i - i + j} ]_{i, j = 1..3}
where mu = (m1, m2, m3).

For mu 3-part:
  s_mu = det [[ h_{m1},   h_{m1+1}, h_{m1+2}],
              [ h_{m2-1}, h_{m2},   h_{m2+1}],
              [ h_{m3-2}, h_{m3-1}, h_{m3}]]

Now K_{mu', (2^j)} = coefficient of s_{(2^j)} in s_mu (Kostka wrt content).

We want < s_mu, s_{(2^j)}^* >. Wait no: K_{lambda, nu} = # SSYT of shape lambda, content nu
  = coefficient of x^nu in s_lambda(x).
  = < s_lambda, m_nu > (with some normalization) ... hmm

Actually K_{lambda, nu} = < s_lambda, h_nu > where <,> is Hall inner product with h_nu ~ dual to m_nu.
Wait: <s_lambda, h_mu> = K_{lambda, mu} (yes).

So K_{mu', (2^j)} = <s_{mu'}, h_{(2^j)}> = <s_{mu'}, h_2^j>.

By omega involution: s_{mu'} = omega(s_mu). Omega sends h_k -> e_k.
So <s_{mu'}, h_2^j> = <omega(s_mu), h_2^j> = <s_mu, omega(h_2^j)> = <s_mu, e_2^j>.

So K_{mu', (2^j)} = <s_mu, e_2^j> = [s_mu] e_2^j (Kostka is #SSYT of shape mu, content ...)
Wait <s_mu, e_2^j>: since {s_lambda} is orthonormal, this equals coefficient of s_mu in e_2^j.

e_2^j = sum_lambda c_lambda s_lambda where c_lambda = # ways to build lambda by vertical 2-strips.
For lambda 3-part: c_lambda = K_{lambda', (2^j)}.

That's how we compute it! So our compute is correct.

Now: for CLOSED FORM.
Substitute h_k = C(x, k) evaluated at some x (this is the principal specialization).
Actually the "e_2 -> ..." trick: we want [s_mu] e_2^j.

Consider power sums: e_2 = (p_1^2 - p_2) / 2.
Or use character formula:
  [s_mu] e_2^j = <s_mu, e_2^j> = <s_mu, sum_lambda K_{lambda, ...} ...>

Actually easier: use Frobenius formula / Muller for symmetric function.

Or: use Weyl character on Grassmannian.

Let's try: [s_mu] e_2^j =  1/(3!) sum_{sigma} sgn(sigma) [monomial] via characters.

Hmm let me try direct: for 3-part mu, JT expansion of s_mu into h's.

Let me just compute [s_mu] e_2^j via a formula. Recall:
  e_2^j = sum_{lambda: |lambda|=2j, lambda' has all parts <=2} K_{lambda', (2^j)} s_lambda
(vertical 2-strip repeated)

Actually [s_mu] e_2^j is what we want. Let me try another approach:

Use the formula: [s_mu] p_lambda / z_lambda ... = chi^mu(lambda), and e_2 = sum p_lambda ...

e_r = sum_{|lambda|=r} (-1)^{r - ell(lambda)} p_lambda / z_lambda
e_2 = (-1)^{2-2}/2 p_{(1,1)} + (-1)^{2-1}/2 p_2 ... actually:
z_{1,1} = 2, z_2 = 2. So e_2 = p_{1,1}/2 - p_2/2 = (p_1^2 - p_2)/2. Good.

So e_2^j = ((p_1^2 - p_2)/2)^j = 1/2^j sum_{k=0}^j C(j,k) (-1)^k p_1^{2(j-k)} p_2^k.

Then [s_mu] p_1^a p_2^b = chi^mu(1^a 2^b) — character value.

For 3-part mu, character values can be computed via Frobenius formula or Murnaghan-Nakayama.

Actually the simpler approach: chi^mu at (2^k, 1^{2j-2k}) is the "signed count of border-strip tableaux".

For our case, we want:
  [s_mu] e_2^j = 1/2^j sum_k C(j,k) (-1)^k chi^mu(1^{2(j-k)} 2^k)

where chi^mu(1^a 2^b) is the character of mu evaluated at conjugacy class 1^a 2^b.

Hmm this is getting complex. Let me try a direct symbolic computation for small cases and see if the sum simplifies.
"""

import sympy as sp
from sympy import symbols, expand, factorial, binomial, Rational, Sum, simplify, S


def h_poly(k, x):
    """h_k = C(x, k) evaluated? No, we want h_k as a formal symbol.
    For computing power series expansions, we use h_k(x_1, ...) via Newton's identities."""
    pass


def jt_kostka(mu, j):
    """Compute K_{mu', (2^j)} directly via JT and power-sum expansion."""
    # e_2 = (p1^2 - p2)/2
    # e_2^j = 1/2^j sum_k C(j,k) (-1)^k p1^{2(j-k)} p2^k
    # <s_mu, p1^a p2^b> = chi^mu(1^a 2^b)  (character value)
    # For 3-part mu, chi^mu can be computed via MN rule.

    # First: compute chi^mu(1^a 2^b) for a + 2b = 2j.
    # Iterate k = 0..j: a = 2(j-k), b = k.
    total = Rational(0)
    for k in range(j+1):
        a = 2*(j-k)
        b = k
        c = character_value(mu, (2,)*b + (1,)*a)
        total += Rational(sp.binomial(j, k) * (-1)**k) * c
    return total / (2**j)


def character_value(mu, cycle_type):
    """Compute chi^mu(cycle_type) via Murnaghan-Nakayama.
    mu, cycle_type: tuples."""
    if not mu:
        return 1 if not cycle_type else 0
    mu = tuple(sorted([m for m in mu if m > 0], reverse=True))
    cycle_type = tuple(sorted([c for c in cycle_type if c > 0], reverse=True))
    if not cycle_type:
        return 1 if not mu else 0
    r = cycle_type[0]
    rest = cycle_type[1:]
    total = 0
    for strip, sign in border_strips(mu, r):
        total += sign * character_value(strip, rest)
    return total


def border_strips(mu, r):
    """Enumerate border strips of size r that can be removed from mu.
    Return (mu_after_removal, sign) where sign = (-1)^(height of strip)."""
    # A border strip of size r is a connected skew shape mu/lambda that contains no 2x2 square.
    # For 3-part mu, we can enumerate more easily.
    # Height = # rows - 1.
    n_rows = len(mu)
    padded = list(mu) + [0] * (3 - len(mu))
    results = []
    # Enumerate all lambda subset mu with |mu| - |lambda| = r, mu/lambda is a border strip.
    from itertools import product
    # Try all possible removals: for each row i, remove some cells from the right
    # such that: (a) result is a partition (b) mu/lambda is connected and has no 2x2 square.
    # Border strip has cells (i,j) with i - j = const... no that's ribbon. Ribbon = border strip.
    #
    # Better: use the fact that removing a border strip is same as picking a "rim hook" of length r.
    # A rim hook can be described by its start row i and start column j, then extends along the rim.
    #
    # For 3-part mu = (m1, m2, m3), let's enumerate:
    # Rim hooks are: pick a "corner" and go down and left, staying on the rim.

    # Let's do brute force: enumerate all subshapes lambda <= mu with |lambda| = |mu| - r,
    # and check if mu/lambda is a ribbon (connected, no 2x2).
    m1, m2, m3 = padded[0], padded[1], padded[2]
    for l1 in range(m1 + 1):
        if l1 > m1: continue
        for l2 in range(min(m2, l1) + 1):
            for l3 in range(min(m3, l2) + 1):
                if m1 + m2 + m3 - (l1 + l2 + l3) != r:
                    continue
                if not (l1 >= l2 >= l3 >= 0):
                    continue
                # skew shape mu / (l1, l2, l3)
                skew = []
                for i, (m, l) in enumerate(zip([m1, m2, m3], [l1, l2, l3])):
                    for j in range(l, m):
                        skew.append((i, j))
                if not skew:
                    continue
                # check connected & no 2x2
                if not is_ribbon(skew):
                    continue
                # compute height
                rows_used = set(c[0] for c in skew)
                height = len(rows_used) - 1
                # simplify lambda
                new_lam = [l for l in [l1, l2, l3] if l > 0]
                results.append((tuple(new_lam), (-1)**height))
    return results


def is_ribbon(cells):
    """Check if cells form a connected skew shape with no 2x2 square."""
    cell_set = set(cells)
    # no 2x2 square
    for (i, j) in cells:
        if (i, j+1) in cell_set and (i+1, j) in cell_set and (i+1, j+1) in cell_set:
            return False
    # connected (via edges)
    visited = {cells[0]}
    stack = [cells[0]]
    while stack:
        i, j = stack.pop()
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            n = (i+di, j+dj)
            if n in cell_set and n not in visited:
                visited.add(n)
                stack.append(n)
    return len(visited) == len(cells)


def kostka_via_jt(mu):
    j = sum(mu) // 2
    return jt_kostka(mu, j)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')
    from kostka import kostka_mu_prime_2j
    print("=== Cross-check JT-based Kostka vs direct ===\n")
    for mu in [(2,2,2), (4,3,3), (4,4,2), (6,4,4), (6,5,3), (6,6,2), (8,5,5), (8,6,4)]:
        K_jt = kostka_via_jt(mu)
        K_direct = kostka_mu_prime_2j(mu)
        ok = "OK" if K_jt == K_direct else "!!!"
        print(f"  mu={mu}: JT={K_jt}, direct={K_direct}  {ok}")
