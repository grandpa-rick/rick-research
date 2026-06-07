"""
Revised projection pi_2 : AII n=2 → BDI n=2 that IS surjective.

pi_2(m_2, m_23, m_14, m_123, m_124) = (M_1, B_1, T_1, S) where
  M_1 = 0
  B_1 = m_2 + m_23                (= m_2 + m_14 since m_14 = m_23)
  T_1 = m_23 - m_124              (≥ 0 since m_124 ≤ m_23)
  S   = m_123 + 2 m_124

Lands in BDI cone:
  T_1 ≤ B_1 ⟺ -m_124 ≤ m_2 ✓
  S ≤ 2(B_1 - T_1) = 2(m_2 + m_124) ⟺ m_123 ≤ 2 m_2 ✓ (from AII m_123 ≤ m_2)

Surjective: section sigma(0, B_1, T_1, S) =
  m_124 = max(0, S - (B_1 - T_1))
  m_23 = T_1 + m_124
  m_2 = B_1 - T_1 - m_124
  m_123 = S - 2 m_124
  m_14 = m_23
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
    B_1 = m_2 + m_23
    T_1 = m_23 - m_124
    S = m_123 + 2*m_124
    return (M_1, B_1, T_1, S)

def sigma_2(q):
    M_1, B_1, T_1, S = q
    m_124 = max(0, S - (B_1 - T_1))
    m_23 = T_1 + m_124
    m_2 = B_1 - T_1 - m_124
    m_123 = S - 2*m_124
    m_14 = m_23
    return (m_2, m_23, m_14, m_123, m_124)


def verify(N):
    # Test pi_2(AII) ⊂ BDI for all AII points up to weight N
    n_aii = 0
    n_bad_pi = 0
    image = set()
    for m_2 in range(N+1):
        for m_23 in range(N+1):
            m_14 = m_23
            for m_123 in range(m_2 + 1):
                for m_124 in range(m_23 + 1):
                    p = (m_2, m_23, m_14, m_123, m_124)
                    tot = sum(p)
                    if tot > N: continue
                    if not aii_feasible(p): continue
                    n_aii += 1
                    q = pi_2(p)
                    if not bdi_feasible(q):
                        n_bad_pi += 1
                        if n_bad_pi < 3:
                            print(f"  BAD pi: {p} -> {q}")
                    image.add(q)

    # Test sigma_2(BDI) ⊂ AII and pi_2 ∘ sigma_2 = id for all BDI points up to N
    n_bdi = 0
    n_bad_sigma = 0
    n_bad_roundtrip = 0
    for B_1 in range(N+1):
        for T_1 in range(B_1 + 1):
            for S in range(2*(B_1 - T_1) + 1):
                q = (0, B_1, T_1, S)
                if B_1 + T_1 + S > N: continue
                if not bdi_feasible(q): continue
                n_bdi += 1
                p = sigma_2(q)
                if not aii_feasible(p):
                    n_bad_sigma += 1
                    if n_bad_sigma < 3:
                        print(f"  BAD sigma: {q} -> {p}")
                if pi_2(p) != q:
                    n_bad_roundtrip += 1
                    if n_bad_roundtrip < 3:
                        print(f"  BAD roundtrip: {q} -> {p} -> {pi_2(p)}")

    not_covered = 0
    for B_1 in range(N+1):
        for T_1 in range(B_1 + 1):
            for S in range(2*(B_1 - T_1) + 1):
                if B_1 + T_1 + S > N: continue
                q = (0, B_1, T_1, S)
                if q not in image:
                    not_covered += 1

    print(f"N={N}: AII pts {n_aii}, bad pi: {n_bad_pi}, BDI pts {n_bdi}, bad sigma: {n_bad_sigma}, "
          f"bad roundtrip: {n_bad_roundtrip}, BDI not covered: {not_covered}")


if __name__ == "__main__":
    for N in [5, 10, 15, 20]:
        verify(N)
