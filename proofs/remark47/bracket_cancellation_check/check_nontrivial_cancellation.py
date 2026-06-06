"""
A SECOND B_2 example, this time with non-trivial Kashiwara bracket cancellation
WITHIN a single e_2 step.

Setup: pi = 2*b11 + 2*g12 (more cancellation room).
At simple s_1 = alpha_2, c = +2 (one forward 2-unit orbit-swap on LL):
  RAW multisets:  M1 = {(LL,+): 1}
                  M2 = {(LL,+): 2, (LL,-): 1}
                  M3 = {(LL,+): 3, (LL,-): 2}  [up to donor capacity = 2]
  All net to (LL, +): 1, so REDUCED = {(LL,+): 1}.
  Apply REDUCED: pi' = 3*b11 + 1*g12. Wait need to check donor capacity.

  Actually for (LL,+) with multiplicity m: donor is gamma_{1,2}, need pi(g12) >= m.
  For (LL,-): donor is beta_{1,1}, need pi(b11) >= m.
  So M3 needs pi(g12) >= 3 (we have 2 -- FAIL). M2 needs pi(g12) >= 2 (OK, equal), and pi(b11) >= 1 (we have 2, OK).

  Let me try (pi(b11), pi(g12)) = (2, 2):
    Net +1 swap multisets, capacity-respecting:
    M1 = {(LL,+): 1, (LL,-): 0}  net +1.  Cap: g12>=1 OK, b11>=0 OK.  pi' = 3*b11 + 1*g12.
    M2 = {(LL,+): 2, (LL,-): 1}  net +1.  Cap: g12>=2 OK, b11>=1 OK.  pi' = same.
    No M3 since (LL,+):3 needs g12>=3 fail.

  So 2 RAW multisets, both net to {(LL,+): 1}.

Tableau side: pi = 2*b11 + 2*g12.
  Need: c_{b11}=2, c_{b12}=0, c_{g12}=2, c_{b22}=0.
  Decomposition: row 1 needs both unpaired '2's and '2bar's, so we use '1bar' boxes.
  min(2, 2) = 2 '1bar' boxes. Then unpaired_2 = 0, unpaired_2bar = 0.
  Row 1 = [shaded 1's] + [1bar, 1bar].
  Row 2 = [shaded 2] = [2].
  Row 1 shaded count = len(Row 2) + 1 = 2.  So Row 1 = '1 1 1bar 1bar', Row 2 = '2'.

  Check Psi: pair-matching of (2, 2bar) in row 1 = 0. No '0'. Unpaired '2' = 0, unpaired '2bar' = 0.
  Number of '1bar' in row 1 = 2: each contributes (b11 + g12).  Total: 2*b11 + 2*g12. ✓

Now apply e_2 twice and check.
"""

# Same machinery from main_check.py
beta11 = (1, -1)
gamma12 = (1, 1)
beta12 = (1, 0)
beta22 = (0, 1)
alpha2 = (0, 1)

ROOT_NAMES = {beta11: 'b11', gamma12: 'g12', beta12: 'b12', beta22: 'b22'}


def pp(alpha):
    parts = [f"{c}*{ROOT_NAMES[r]}" for r, c in alpha.items() if c > 0]
    return " + ".join(parts) if parts else "0"


def build_S_2_B2(alpha):
    s = []
    c_b12 = alpha.get(beta12, 0)
    c_b11 = alpha.get(beta11, 0)
    c_g12 = alpha.get(gamma12, 0)
    c_b22 = alpha.get(beta22, 0)
    for _ in range(c_b12):
        s.append((')', beta12))
    for _ in range(2 * c_b11):
        s.append(('(', beta11))
    for _ in range(2 * c_g12):
        s.append((')', gamma12))
    for _ in range(c_b12):
        s.append(('(', beta12))
    for _ in range(c_b22):
        s.append((')', beta22))
    return s


def cancel_brackets(s):
    s = list(s)
    changed = True
    while changed:
        changed = False
        for k in range(len(s) - 1):
            if s[k][0] == '(' and s[k + 1][0] == ')':
                del s[k:k + 2]
                changed = True
                break
    return s


def s_to_str(s):
    return ''.join(c for c, _ in s)


def add(alpha, root, k=1):
    out = dict(alpha)
    out[root] = out.get(root, 0) + k
    if out[root] == 0:
        del out[root]
    return out


def e_2(alpha):
    s = build_S_2_B2(alpha)
    sc = cancel_brackets(s)
    rightmost = None
    for k in range(len(sc) - 1, -1, -1):
        if sc[k][0] == ')':
            rightmost = sc[k]
            break
    if rightmost is None:
        return None, None, s, sc
    beta = rightmost[1]
    out = dict(alpha)
    out[beta] = out.get(beta, 0) - 1
    if out[beta] == 0:
        del out[beta]
    diff = (beta[0] - alpha2[0], beta[1] - alpha2[1])
    if diff != (0, 0):
        out[diff] = out.get(diff, 0) + 1
    return out, beta, s, sc


# ====== Test ======
pi = {beta11: 2, gamma12: 2}
pi_prime_expected = {beta11: 3, gamma12: 1}

print(f"pi = {pp(pi)}, pi' (expected after e_2^2) = {pp(pi_prime_expected)}")

cur = pi
for step in range(2):
    new, beta, s, sc = e_2(cur)
    print(f"\nStep {step+1}: cur = {pp(cur)}")
    print(f"  S_2  = {s_to_str(s)}")
    print(f"  S_2^c = {s_to_str(sc)}")
    print(f"  rightmost ')' root = {ROOT_NAMES[beta]}")
    print(f"  e_2(cur) = {pp(new)}")
    cur = new

print(f"\nFinal: {pp(cur)}, expected {pp(pi_prime_expected)}")
print(f"Match: {cur == pi_prime_expected}")
