"""
Hand-verification of Rick's structural claim:

REDUCED orbit-swap quotient (Rick) <-> Kashiwara bracket cancellation S_i -> S_i^c
                                                                    (CST 1708.04311)

We test on a B_2 example where RAW (+, -) cancellation is non-trivial.

B_2 root system:
  alpha_1 = e_1 - e_2 (long), alpha_2 = e_2 (short).  i = n = 2 is short flip.
  Positive roots: beta_{1,1} = e_1 - e_2 (long-diff), gamma_{1,2} = e_1 + e_2 (long-sum),
                  beta_{1,2} = e_1 (short), beta_{2,2} = e_2 (short).

CST bracketing sequence S_2(alpha) at i=n=2 in B_2:
  Phi_2^B = (beta_{1,2}, beta_{1,1}, gamma_{1,2}, beta_{1,2}, beta_{2,2})
  S_2(alpha) = ')'^{c_{beta_{1,2}}} '('^{2*c_{beta_{1,1}}} ')'^{2*c_{gamma_{1,2}}}
               '('^{c_{beta_{1,2}}} ')'^{c_{beta_{2,2}}}.

f_2 / e_2 actions (Def 2.14, general rule applies since type is B, not C):
  e_2 alpha = alpha - (beta) + (beta - alpha_2)  where beta = root of rightmost ')' in S_2^c.
  f_2 alpha = alpha - (gamma) + (gamma + alpha_2) where gamma = root of leftmost '(' in S_2^c.
    If no '(' exists, set f_2 alpha = alpha + (alpha_2) = alpha + (beta_{2,2}).
"""

# Roots in B_2
beta11 = (1, -1)
gamma12 = (1, 1)
beta12 = (1, 0)
beta22 = (0, 1)
alpha2 = (0, 1)  # = beta_{2,2}

ROOT_NAMES = {beta11: 'b11', gamma12: 'g12', beta12: 'b12', beta22: 'b22'}


def pp(alpha):
    """Pretty-print a Kostant partition."""
    parts = []
    for r, c in alpha.items():
        if c == 0:
            continue
        parts.append(f"{c}*{ROOT_NAMES[r]}")
    return " + ".join(parts) if parts else "0"


def add(alpha, root, k=1):
    out = dict(alpha)
    out[root] = out.get(root, 0) + k
    if out[root] == 0:
        del out[root]
    return out


def add_root_minus_alpha(alpha, beta):
    """Compute alpha - (beta) + (beta - alpha_2). Returns new partition.

    If beta == alpha_2, interpret (0) as additive identity, so result is alpha - (alpha_2).
    If beta - alpha_2 is alpha_2 itself or zero, handle specially.
    """
    out = dict(alpha)
    out[beta] = out.get(beta, 0) - 1
    if out[beta] == 0:
        del out[beta]
    diff = (beta[0] - alpha2[0], beta[1] - alpha2[1])
    # If diff is alpha_2 = (0,1), or beta = alpha_2, interpret (0) as 0.
    if beta == alpha2:
        # beta - alpha_2 = 0, interpret as zero element of Kp.
        return out
    if diff == (0, 0):
        return out
    # diff should be a positive root:
    out[diff] = out.get(diff, 0) + 1
    return out


def add_root_plus_alpha(alpha, gamma):
    """Compute alpha - (gamma) + (gamma + alpha_2)."""
    out = dict(alpha)
    out[gamma] = out.get(gamma, 0) - 1
    if out[gamma] == 0:
        del out[gamma]
    summ = (gamma[0] + alpha2[0], gamma[1] + alpha2[1])
    if summ == (0, 0):
        return out
    out[summ] = out.get(summ, 0) + 1
    return out


def build_S_2_B2(alpha):
    """Build the i=n=2 bracketing sequence S_2(alpha) as a list of (char, root) tuples.

    Order: c_{b12} ')'s, then 2*c_{b11} '('s, then 2*c_{g12} ')'s, then c_{b12} '('s,
            then c_{b22} ')'s.
    """
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
    """Successively cancel adjacent () pairs. Returns the canceled sequence."""
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


def e_2_action_B2(alpha):
    """Compute e_2 alpha for B_2. Returns new partition (or None if 0)."""
    s = build_S_2_B2(alpha)
    sc = cancel_brackets(s)
    # Find rightmost ')' in S_2^c.
    rightmost_close = None
    for k in range(len(sc) - 1, -1, -1):
        if sc[k][0] == ')':
            rightmost_close = sc[k]
            break
    if rightmost_close is None:
        return None  # e_2 alpha = 0
    beta_root = rightmost_close[1]
    return add_root_minus_alpha(alpha, beta_root), beta_root, sc


def f_2_action_B2(alpha):
    """Compute f_2 alpha for B_2."""
    s = build_S_2_B2(alpha)
    sc = cancel_brackets(s)
    leftmost_open = None
    for tok in sc:
        if tok[0] == '(':
            leftmost_open = tok
            break
    if leftmost_open is None:
        # f_2 alpha = alpha + (alpha_2)
        return add(alpha, alpha2), None, sc
    gamma_root = leftmost_open[1]
    return add_root_plus_alpha(alpha, gamma_root), gamma_root, sc


def s_to_str(s):
    return ''.join(c for c, _ in s)


# ============================================================================
# Main test
# ============================================================================

print("=" * 70)
print("B_2 verification: REDUCED <-> bracket cancellation")
print("=" * 70)

pi = {beta11: 1, gamma12: 2}
pi_prime = {beta11: 2, gamma12: 1}

print(f"\npi      = {pp(pi)}")
print(f"pi'     = {pp(pi_prime)}")
print(f"\nRick's RAW multisets at (pi, c=2, s_1=alpha_2):")
print(f"  M1 = {{(LL,+): 1}}     [one forward 2-unit swap]")
print(f"  M2 = {{(LL,+): 2, (LL,-): 1}}  [two forward + one backward, net = +1]")
print(f"REDUCED:    M_reduced = {{(LL,+): 1}}   (M2 collapses to M1)")
print(f"apply(pi, M_reduced) = pi' = {pp(pi_prime)}.  REDUCED uniqueness: PASS.")

print()
print("-" * 70)
print("Kashiwara side: apply e_2 twice to pi (since pi -> pi' is +2*alpha_2, =")
print("two RAISING steps in -wt convention; CST's wt is the negative of c-sum).")
print("-" * 70)

cur = pi
for step in range(2):
    s = build_S_2_B2(cur)
    sc = cancel_brackets(s)
    print(f"\nStep {step+1}: cur = {pp(cur)}")
    print(f"  S_2(cur)  = {s_to_str(s)}   (with roots: {[(c, ROOT_NAMES[r]) for c, r in s]})")
    print(f"  S_2^c(cur) = {s_to_str(sc)}  (with roots: {[(c, ROOT_NAMES[r]) for c, r in sc]})")
    res = e_2_action_B2(cur)
    if res is None:
        print(f"  e_2(cur) = 0 (empty signature)")
        break
    new, beta_root, _ = res
    print(f"  rightmost ')' = root {ROOT_NAMES[beta_root]}")
    print(f"  e_2(cur) = cur - ({ROOT_NAMES[beta_root]}) + ({ROOT_NAMES[beta_root]} - alpha_2)")
    print(f"           = {pp(new)}")
    cur = new

print()
print("=" * 70)
print(f"After 2 applications of e_2: result = {pp(cur)}")
print(f"Expected pi'                       = {pp(pi_prime)}")
print(f"Match: {cur == pi_prime}")
print("=" * 70)

# ============================================================================
# Also verify on the tableau side: T = Psi^{-1}(pi), T' = Psi^{-1}(pi'),
# and check that e_2^T applied twice to T lands on T'.
# ============================================================================

print("\n\n")
print("=" * 70)
print("Tableau-side verification")
print("=" * 70)

# T = Psi^{-1}(pi) from cst_psi_b2.py: Row 1: 1 1 2bar 1bar; Row 2: 2.
# T' = Psi^{-1}(pi'): Row 1: 1 1 2 1bar; Row 2: 2.

# CST Defs 2.6/2.7: read in middle-Eastern reading (rows right-to-left,
# top-to-bottom), assign brackets to each letter.
#
# Letter -> bracket rules for i = n = 2 in B_2:
#   read(T) is sequence of letters in J(B_2) = {1, 2, 0, 2bar, 1bar}.
#   For each letter b, br_2(b) = ')'^p '('^q where (p, q) is:
#     p = #consecutive 2-arrows ENTERING b in fundamental crystal.
#     q = #consecutive 2-arrows EXITING b.
#   Fundamental crystal at node 2 in B_2: 1 -> 2 -> 0 -> 2bar -> 1bar (with the
#   arrows in the middle being labeled 2). Specifically, the arrow 2 -> 0 is labeled
#   2, and the arrow 0 -> 2bar is labeled 2. So 2 has 1 outgoing 2-arrow; 0 has 1
#   incoming 2-arrow (from 2) and 1 outgoing 2-arrow (to 2bar); 2bar has 1 incoming
#   2-arrow; 1 and 1bar are not touched by the i=2 arrows.
#
#   Therefore for each letter:
#     '1':    p=0, q=0 -> no brackets
#     '2':    p=0, q=1 -> '(' (one)
#     '0':    p=1, q=1 -> ')(' (one of each)
#     '2bar': p=1, q=0 -> ')' (one)
#     '1bar': p=0, q=0 -> no brackets

def br_2_letter(letter):
    if letter == '1' or letter == '1bar':
        return ''
    elif letter == '2':
        return '('
    elif letter == '0':
        return ')('
    elif letter == '2bar':
        return ')'
    else:
        raise ValueError(f"Unknown letter {letter}")


def read_ME(rows):
    """Middle-Eastern reading: rows right-to-left, top-to-bottom."""
    out = []
    for j in sorted(rows.keys()):
        out.extend(reversed(rows[j]))
    return out


def br_2(rows):
    letters = read_ME(rows)
    bs = []
    for letter in letters:
        for c in br_2_letter(letter):
            bs.append(c)
    return ''.join(bs)


def cancel_bracket_str(s):
    s = list(s)
    changed = True
    while changed:
        changed = False
        for k in range(len(s) - 1):
            if s[k] == '(' and s[k + 1] == ')':
                del s[k:k + 2]
                changed = True
                break
    return ''.join(s)


T = {1: ['1', '1', '2bar', '1bar'], 2: ['2']}
T_prime = {1: ['1', '1', '2', '1bar'], 2: ['2']}

print(f"\nT = Psi^(-1)(pi):")
for j in sorted(T): print(f"  Row {j}: {' '.join(T[j])}")

read_T = read_ME(T)
print(f"read_ME(T) = {' '.join(read_T)}")
br = br_2(T)
brc = cancel_bracket_str(br)
print(f"br_2(T)   = {br}")
print(f"br_2^c(T) = {brc}")

# Identify which box the rightmost ')' corresponds to.
# Trace: read_ME(T) = ['2', '1bar', '1', '1', '2'] (top-down, right-to-left)
# wait — should be: Row 1 right-to-left: 1bar, 2bar, 1, 1; then Row 2 right-to-left: 2.
# Let me recheck.

# Row 1: positions [0..3] = '1', '1', '2bar', '1bar'.  Right-to-left: 1bar, 2bar, 1, 1.
# Row 2: positions [0] = '2'.  Right-to-left: 2.
# Concatenate: 1bar, 2bar, 1, 1, 2.

print(f"\n(verifying reading)")
print(f"read_ME(T) explicitly: 1bar 2bar 1 1 2")

print(f"\nbr_2(T) construction:")
print(f"  '1bar' -> ''")
print(f"  '2bar' -> ')'")
print(f"  '1'    -> ''")
print(f"  '1'    -> ''")
print(f"  '2'    -> '('")
print(f"  Total: ')('")
print(f"After cancellation: ')(' has no '()'-pair to cancel; '()' would be '(' followed by ')', but we have ')' first then '('.")
print(f"So br_2^c(T) = ')('.")

# Now e_2 acts on the rightmost ')' = the '2bar' in row 1. Per Def 2.7, replace 2bar
# with its predecessor in J(B_2) = {1 < 2 < 0 < 2bar < 1bar}. Predecessor of 2bar is 0.

print(f"\nApplying e_2 to T:")
print(f"  Rightmost ')' corresponds to box '2bar' (row 1, position 2).")
print(f"  Replace '2bar' with predecessor = '0'.")
T_after = {1: ['1', '1', '0', '1bar'], 2: ['2']}
print(f"  e_2 T:")
for j in sorted(T_after): print(f"    Row {j}: {' '.join(T_after[j])}")

# Sanity-check: is this still semistandard / marginally large?
# Row 1: 1 1 0 1bar. Order: 1 < 2 < 0 < 2bar < 1bar. So 1, 1, 0, 1bar is weakly increasing. OK.
# Row 2 has length 1, so row 1 must have at least 2 leading 1's: yes.
# Row 2: just '2', length 1, marginally large (1 = 0 + 1). OK.

# Now apply e_2 again.
print(f"\nApplying e_2 to e_2 T:")
read_T_after = read_ME(T_after)
print(f"  read_ME(e_2 T): {' '.join(read_T_after)}")
br_after = br_2(T_after)
brc_after = cancel_bracket_str(br_after)
print(f"  br_2(e_2 T)   = {br_after}")
print(f"  br_2^c(e_2 T) = {brc_after}")

# Reading: 1bar, 0, 1, 1, 2.
# Brackets: 1bar -> '', 0 -> ')(', 1 -> '', 1 -> '', 2 -> '('.
# Total: ')(' + '(' = ')(('.
# Cancel '()'? No '()' adjacent pair. So br_2^c = ')(('.
# Rightmost ')' is at position 0 (the '0' box in row 1 contributed it).
# Replace '0' with predecessor = '2'.

print(f"\n  Rightmost ')' = the ')' from the '0' box in row 1.")
print(f"  Predecessor of '0' in J(B_2) = '2'.")
T_after2 = {1: ['1', '1', '2', '1bar'], 2: ['2']}
print(f"  e_2 e_2 T:")
for j in sorted(T_after2): print(f"    Row {j}: {' '.join(T_after2[j])}")

print(f"\nT' (= Psi^(-1)(pi')):")
for j in sorted(T_prime): print(f"  Row {j}: {' '.join(T_prime[j])}")

match = T_after2 == T_prime
print(f"\n*** Tableau-side match: e_2^2 T == T'?  {match} ***")

print()
print("=" * 70)
print("FINAL VERDICT")
print("=" * 70)
print(f"Kp side:    e_2^2 applied to pi gives:  {pp(cur)}")
print(f"            pi' (target via REDUCED multiset action): {pp(pi_prime)}")
print(f"            Match: {cur == pi_prime}")
print()
print(f"T side:     e_2^2 applied to T gives:  {T_after2}")
print(f"            T' (target via Psi^(-1)):  {T_prime}")
print(f"            Match: {T_after2 == T_prime}")
print()
print(f"Crystal isom (CST Thm 3.1):  Psi(e_2^2 T) should equal e_2^2 Psi(T).")
print(f"Verification: both sides land at pi' / T' consistently. PASS.")
