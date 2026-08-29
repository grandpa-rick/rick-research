"""Day 120 — Search for a Garsia-Milne style involution on {mu : |mu|=2j, ell<=3}
that would explain [t^d] S_j = 0.

Candidate involutions to test:
  (A) mu <-> mu' (conjugate). No -- flips shape but changes ell.
  (B) row-swap in some canonical way.
  (C) (a, b, c) -> (a, c+1, b-1) or similar "slide" that preserves |mu|.
  (D) Bender-Knuth on conjugate.
  (E) Pair (a, b, c) with (a, b+1, c-1) or (a, b-1, c+1) (parity flip).
  (F) Cyclic pairing on the (b, c) plane.

For each candidate involution I:
  Test: does K_{mu', (2^j)} * [t^d] s*_mu + K_{I(mu)', (2^j)} * [t^d] s*_{I(mu)}
        = 0 for each d? (With appropriate sign)

Or weaker: does I preserve K_{mu', (2^j)}? Does it flip (mu_2 - mu_3) parity?
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')

from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts
from compute_bar_s import s_star_mu
from route_v_probe import substitute_sigma_pi, sig, pi
from sympy import expand, Integer, symbols, Poly

u, y, c = symbols('u y c')
t, s = symbols('t s')


def eval_ts(mu):
    f = s_star_mu(mu)
    fsub = substitute_sigma_pi(f)
    return expand(fsub.subs({u: t, sig: s, pi: t}))


def parity(mu):
    return (mu[1] - mu[2]) % 2


def valid(mu):
    return len(mu) == 3 and mu[0] >= mu[1] >= mu[2] >= 0


# ================== Candidate involutions ==================

def cand_bc_swap(mu):
    """(a, b, c) -> (a, b+1, c-1) if valid -- flips (b-c) parity by ±2 doesn't help.
    Actually (b-c) parity changes by 2, so no flip.
    Try (a, b, c) <-> (a', b', c') where b - c flips parity by shifting one box."""
    a, b, c = mu
    # For flipping parity, move a box between rows in a way that changes b - c mod 2.
    return None


def cand_shift_bc(mu):
    """Move a box from row 3 to row 2, or vice versa, preserving partition:
    (a, b, c) -> (a, b+1, c-1) if c >= 1 and b+1 <= a  [b - c changes by 2, parity same]
    NOT useful.

    Move a box between row 1 and row 3:
    (a, b, c) -> (a-1, b, c+1) if a > b and c < b [b - c changes by 1 -> parity FLIPS]
    But |mu| preserved!
    """
    a, b, c = mu
    # try (a-1, b, c+1)
    nu = (a - 1, b, c + 1)
    if valid(nu) and sum(nu) == sum(mu):
        return nu
    return None


def cand_shift_ac(mu):
    """(a, b, c) -> (a+1, b, c-1). Parity flips (b-c changes by 1)."""
    a, b, c = mu
    nu = (a + 1, b, c - 1)
    if valid(nu) and sum(nu) == sum(mu):
        return nu
    return None


def cand_row1_to_row2(mu):
    """(a, b, c) -> (a-1, b+1, c). Parity of (b-c) flips."""
    a, b, c = mu
    nu = (a - 1, b + 1, c)
    if valid(nu) and sum(nu) == sum(mu):
        return nu
    return None


def cand_row2_to_row1(mu):
    """(a, b, c) -> (a+1, b-1, c). Parity flips."""
    a, b, c = mu
    nu = (a + 1, b - 1, c)
    if valid(nu) and sum(nu) == sum(mu):
        return nu
    return None


# ================== Analysis of parity classes ==================

def parity_classes(j):
    """For each j, list mu in support by parity."""
    twoj = 2 * j
    ev, od = [], []
    for mu in all_mu_3parts(twoj):
        K = kostka_mu_prime_2j(mu)
        if K == 0:
            continue
        (ev if parity(mu) == 0 else od).append((mu, K, d_mu(mu)))
    return ev, od


def try_row1_row2_pairing(j):
    """Test pairing mu = (a, b, c) with I(mu) = (a-1, b+1, c)."""
    print(f"\n=== j={j}: row1<->row2 pairing (a-1, b+1, c) ===")
    twoj = 2 * j
    all_mu = [(mu, kostka_mu_prime_2j(mu)) for mu in all_mu_3parts(twoj)]
    all_mu = [(mu, K) for mu, K in all_mu if K > 0]
    print(f"  Support size: {len(all_mu)}")
    paired = set()
    for mu, K in all_mu:
        if mu in paired:
            continue
        nu = cand_row1_to_row2(mu)
        if nu is None:
            print(f"  mu={mu} K={K} d_mu={d_mu(mu)}: UNPAIRED")
            paired.add(mu)
            continue
        Knu = kostka_mu_prime_2j(nu)
        # Check parity flip
        p1 = parity(mu)
        p2 = parity(nu)
        print(f"  mu={mu} K={K} d={d_mu(mu)} p={p1}  <-> nu={nu} K={Knu} d={d_mu(nu)} p={p2}"
              + ("  [parity flip!]" if p1 != p2 else ""))
        paired.add(mu)
        paired.add(nu)


def try_delta_pairing(j):
    """Compute [t^d] contribution and compare mu vs (a-1, b+1, c)."""
    print(f"\n=== j={j}: [t^d] cancellation test for (a,b,c) <-> (a-1, b+1, c) ===")
    twoj = 2 * j
    mu_evals = {}
    for mu in all_mu_3parts(twoj):
        K = kostka_mu_prime_2j(mu)
        if K == 0:
            continue
        mu_evals[mu] = (K, eval_ts(mu))
    d_max = max(d_mu(mu) for mu in mu_evals)
    for d in range(j+1, d_max + 1):
        print(f"  d={d}:")
        checked = set()
        residual = Integer(0)
        for mu, (K, ev) in mu_evals.items():
            if mu in checked:
                continue
            checked.add(mu)
            p = Poly(ev, t, s)
            cd = sum(coef * s**ds for (dt, ds), coef in p.terms() if dt == d)
            cd = expand(cd)
            if cd == 0:
                continue
            nu = cand_row1_to_row2(mu)
            if nu is not None and nu in mu_evals:
                Knu, evnu = mu_evals[nu]
                pnu = Poly(evnu, t, s)
                cdn = sum(coef * s**ds for (dt, ds), coef in pnu.terms() if dt == d)
                cdn = expand(cdn)
                pair_sum = expand(K * cd + Knu * cdn)
                sign_pair_sum = expand(K * cd - Knu * cdn)
                status = "cancel" if pair_sum == 0 else ("sign-cancel" if sign_pair_sum == 0 else f"nope, sum={pair_sum}")
                print(f"    mu={mu} K={K} cd={cd}, nu={nu} K={Knu} cd={cdn}: pair_sum={pair_sum}  {status}")
                checked.add(nu)
                residual += pair_sum
            else:
                print(f"    mu={mu} K={K} cd={cd}: unpaired, contrib K*cd = {expand(K*cd)}")
                residual += K * cd
        print(f"    residual (after pairing) = {expand(residual)}")


if __name__ == "__main__":
    for j in [3, 4, 5, 6, 7]:
        try_row1_row2_pairing(j)
    for j in [3, 4, 5]:
        try_delta_pairing(j)
