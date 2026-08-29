"""Day 120 — More involution candidates.

The candidate (a,b,c) <-> (a-1, b+1, c) works for SOME mu but leaves many unpaired.

Let's try MORE candidates:
  (I1) (a, b, c) <-> (a, b+1, c-1)  -- flips (b-c) by 2, NO parity flip
  (I2) (a, b, c) <-> (a-1, b, c+1) -- flips (b-c) by 1, parity flips  [row1 -> row3]
  (I3) (a, b, c) <-> (a+1, b-1, c) -- reverse of (a-1, b+1, c)
  (I4) Multi-step: (a, b, c) <-> conjugate then swap rows
  (I5) (a, b, c) <-> (a - k, b + k, c) for some k (multi-slide)
"""

import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')

from kostka import kostka_mu_prime_2j, d_mu, all_mu_3parts


def parity(mu):
    return (mu[1] - mu[2]) % 2


def valid(mu):
    return len(mu) == 3 and mu[0] >= mu[1] >= mu[2] >= 0


def involution_scan(j, involution_fn, name):
    """For each mu in support, apply involution and check parity flip + Kostka relation."""
    twoj = 2 * j
    support = {}
    for mu in all_mu_3parts(twoj):
        K = kostka_mu_prime_2j(mu)
        if K > 0:
            support[mu] = K
    print(f"\n=== j={j}: involution '{name}' ===")
    print(f"  Support: {len(support)} mu's")
    unpaired = []
    fixed = []
    paired_flip_ok = []
    paired_no_flip = []
    seen = set()
    for mu, K in support.items():
        if mu in seen:
            continue
        nu = involution_fn(mu)
        if nu == mu:
            fixed.append((mu, K))
            seen.add(mu)
            continue
        if nu is None or not valid(nu) or nu not in support:
            unpaired.append((mu, K))
            seen.add(mu)
            continue
        # Check involution property: involution_fn(nu) should be mu
        nu2 = involution_fn(nu)
        if nu2 != mu:
            unpaired.append((mu, K, "not involution", nu, nu2))
            seen.add(mu)
            continue
        Knu = support[nu]
        parity_flip = parity(mu) != parity(nu)
        if parity_flip:
            paired_flip_ok.append((mu, nu, K, Knu))
        else:
            paired_no_flip.append((mu, nu, K, Knu))
        seen.add(mu)
        seen.add(nu)
    print(f"  Fixed points: {len(fixed)}: {fixed}")
    print(f"  Unpaired (I sends outside support): {len(unpaired)}: {unpaired}")
    print(f"  Paired with parity flip: {len(paired_flip_ok)}")
    for mu, nu, K, Knu in paired_flip_ok:
        print(f"    {mu}(K={K}, p={parity(mu)}, d={d_mu(mu)}) <-> {nu}(K={Knu}, p={parity(nu)}, d={d_mu(nu)}) ")
    print(f"  Paired WITHOUT parity flip: {len(paired_no_flip)}")
    for mu, nu, K, Knu in paired_no_flip:
        print(f"    {mu}(K={K}) <-> {nu}(K={Knu})")


def I_a_bplus_cminus(mu):
    a, b, c = mu
    if c >= 1 and b + 1 <= a:
        return (a, b + 1, c - 1)
    return None


def I_reverse(mu):
    """Involution that reverses I_a_bplus_cminus: (a, b, c) -> (a, b-1, c+1)."""
    a, b, c = mu
    if b >= 1 and c + 1 <= b - 1:
        return (a, b - 1, c + 1)
    return None


def I_symmetric_bc(mu):
    """Combine both: check whether pairing is self-inverse when we choose canonically."""
    a, b, c = mu
    # If we can go to (a, b+1, c-1), do it. Otherwise if we can go to (a, b-1, c+1), do that.
    up = (a, b + 1, c - 1)
    if valid(up) and up[0] >= up[1]:
        return up
    dn = (a, b - 1, c + 1)
    if valid(dn) and dn[1] >= dn[2]:
        return dn
    return None


def I_row1_row3(mu):
    """(a, b, c) -> (a - 1, b, c + 1) if valid."""
    a, b, c = mu
    nu = (a - 1, b, c + 1)
    if valid(nu) and sum(nu) == sum(mu):
        return nu
    return None


def I_row3_row1(mu):
    """Reverse: (a, b, c) -> (a + 1, b, c - 1)."""
    a, b, c = mu
    nu = (a + 1, b, c - 1)
    if valid(nu) and sum(nu) == sum(mu):
        return nu
    return None


def I_symm_row1_row3(mu):
    """Try to always move a box between row 1 and row 3."""
    a, b, c = mu
    # Attempt (a-1, b, c+1)
    up = (a - 1, b, c + 1)
    if valid(up):
        return up
    dn = (a + 1, b, c - 1)
    if valid(dn):
        return dn
    return None


def I_row1_row2_symm(mu):
    """Try to always pair row1 <-> row2."""
    a, b, c = mu
    up = (a - 1, b + 1, c)
    if valid(up):
        return up
    dn = (a + 1, b - 1, c)
    if valid(dn):
        return dn
    return None


if __name__ == "__main__":
    for j in [4, 5, 6, 7, 8]:
        # involution_scan(j, I_a_bplus_cminus, "(a, b+1, c-1)")
        # involution_scan(j, I_symmetric_bc, "symmetric bc")
        involution_scan(j, I_symm_row1_row3, "row1<->row3 (symm)")
        involution_scan(j, I_row1_row2_symm, "row1<->row2 (symm)")
