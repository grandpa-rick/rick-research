"""
Verify the projection pi_2 : AII n=2 → BDI n=2 by exhaustive lattice check.

AII n=2 polytope:
  vars (m_2, m_23, m_14, m_123, m_124) ≥ 0
  inequalities m_123 ≤ m_2, m_124 ≤ m_23
  equality m_14 = m_23

BDI n=2 polytope:
  vars (M_1, B_1, T_1, S) ≥ 0
  M_1 = 0 (degenerate)
  T_1 ≤ B_1 (carry P_1 = 2(B_1 - T_1) ≥ 0)
  S ≤ 2(B_1 - T_1)

Projection (Rick's tilde-pi_2):
  M_1 = 0
  B_1 = m_2 + m_23   # using m_14 = m_23, the linking var folds in
  T_1 = m_124
  S = m_123

Verify:
  (a) Every AII point projects to a BDI point.
  (b) Surjectivity on BDI lattice points.
"""

def aii_feasible(p):
    m_2, m_23, m_14, m_123, m_124 = p
    if any(x < 0 for x in p): return False
    if m_14 != m_23: return False
    if m_123 > m_2: return False
    if m_124 > m_23: return False
    return True

def bdi_feasible(q):
    M_1, B_1, T_1, S = q
    if any(x < 0 for x in q): return False
    if M_1 != 0: return False
    if T_1 > B_1: return False
    if S > 2*(B_1 - T_1): return False
    return True

def pi_2(p):
    m_2, m_23, m_14, m_123, m_124 = p
    M_1 = 0
    B_1 = m_2 + m_23  # also = m_2 + m_14 since m_14 = m_23
    T_1 = m_124
    S = m_123
    return (M_1, B_1, T_1, S)


def verify_a(N):
    """All AII points up to total N project to BDI cone."""
    count_aii = 0
    count_bad = 0
    for m_2 in range(N+1):
        for m_23 in range(N+1):
            m_14 = m_23
            if m_2 + m_23 + m_14 > N: continue
            for m_123 in range(min(m_2, N - m_2 - 2*m_23) + 1):
                for m_124 in range(min(m_23, N - m_2 - 2*m_23 - m_123) + 1):
                    p = (m_2, m_23, m_14, m_123, m_124)
                    if not aii_feasible(p): continue
                    count_aii += 1
                    q = pi_2(p)
                    if not bdi_feasible(q):
                        count_bad += 1
                        if count_bad < 5:
                            print(f"BAD: AII {p} -> BDI {q}")
    print(f"AII points up to N={N}: {count_aii}, bad: {count_bad}")
    return count_bad == 0


def verify_b_surjective(N):
    """Check pi_2 image covers BDI lattice points up to weight N."""
    # Compute image set
    image = set()
    for m_2 in range(N+1):
        for m_23 in range(N+1):
            m_14 = m_23
            if m_2 + m_23 + m_14 > N: continue
            for m_123 in range(min(m_2, N - m_2 - 2*m_23) + 1):
                for m_124 in range(min(m_23, N - m_2 - 2*m_23 - m_123) + 1):
                    p = (m_2, m_23, m_14, m_123, m_124)
                    if not aii_feasible(p): continue
                    q = pi_2(p)
                    image.add(q)

    # BDI lattice points up to weight ≤ N
    bdi_pts = set()
    missed = []
    for B_1 in range(N+1):
        for T_1 in range(B_1+1):
            for S in range(2*(B_1 - T_1) + 1):
                if B_1 + T_1 + S > N: continue
                q = (0, B_1, T_1, S)
                bdi_pts.add(q)

    not_in_image = bdi_pts - image
    print(f"BDI lattice points: {len(bdi_pts)}, in image: {len(bdi_pts & image)}, NOT covered: {len(not_in_image)}")
    if not_in_image:
        for q in sorted(not_in_image)[:10]:
            print(f"  Not in image: {q}")
    return not_in_image


if __name__ == "__main__":
    for N in [5, 10, 15, 20]:
        print(f"\n--- N = {N} ---")
        ok = verify_a(N)
        missed = verify_b_surjective(N)
        if ok and not missed:
            print(f"  ✓ Both verified at N={N}")
