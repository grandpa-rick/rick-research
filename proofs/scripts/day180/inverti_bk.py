"""
Zabrocki INVERTi criterion applied to Rick's b_k sequence.

Reference: arXiv:2505.06941 (Zabrocki et al.). The stated theorem:
  A graded free NC-cocomm connected Hopf algebra with dimension sequence
  (a_n)_{n>=0}, a_0 = 1, exists  iff  the INVERTi transform of a is
  nonnegative.

OEIS INVERT convention (standard):
  Let A(x) = sum_{n>=1} a_n x^n  (OGF of the input, no constant term).
  Then INVERT(a) = b where
     1 + sum_{n>=1} b_n x^n  =  1 / (1 - A(x))
  equivalently  B(x) = A(x) / (1 - A(x))  with B(x) = sum_{n>=1} b_n x^n.

INVERTi is the inverse. If we are GIVEN a sequence (a_n)_{n>=1} thought of
as the "1 + sum a_n x^n" coefficients of some series F(x), i.e.
  F(x) = 1 + sum_{n>=1} a_n x^n = 1/(1 - B(x)),
then INVERTi(a)_n = b_n where
  B(x) = 1 - 1/F(x) = sum_{n>=1} b_n x^n.

Zabrocki's condition "INVERTi(a) >= 0 componentwise" is the classical
Grinberg / free-Hopf existence criterion (Krob-Thibon dimension formulas)
and matches the OEIS INVERTi convention.

We test Rick's sequence
   b_k = 3, 27, 417, 7851, 164124
under two natural framings:

  Convention A:  a = (1, 3, 27, 417, 7851, 164124), i.e. a_0=1 is the
                 Hopf-algebra ground field and a_k = b_k for k>=1.
                 Then INVERTi is applied to (3, 27, 417, 7851, 164124)
                 (equivalently, F(x) = 1 + 3 x + 27 x^2 + ...).
                 This is the Zabrocki convention.

  Convention B:  a = (3, 27, 417, 7851, 164124) treated directly as
                 (a_0, a_1, ...), i.e. F(x) = 3 + 27 x + 417 x^2 + ...
                 Not natural for Hopf existence (a_0 != 1) but included
                 as sanity check.
"""

from fractions import Fraction


def inverti_from_1_plus(a_pos):
    """INVERTi where input represents (a_1, a_2, ...) inside F(x) = 1 + a_1 x + a_2 x^2 + ...
    Returns (b_1, b_2, ...) with 1/F(x) = 1 - B(x), i.e. B(x) = 1 - 1/F(x).
    """
    N = len(a_pos)
    # Compute reciprocal G(x) = 1/F(x) as a power series up to x^N.
    # F(x) = 1 + a_1 x + a_2 x^2 + ...   G(x) = g_0 + g_1 x + ...
    # F * G = 1  =>  g_0 = 1;  for n>=1:  sum_{k=0..n} f_k g_{n-k} = 0
    #    where f_0 = 1, f_k = a_k.
    f = [Fraction(1)] + [Fraction(x) for x in a_pos]
    g = [Fraction(0)] * (N + 1)
    g[0] = Fraction(1)
    for n in range(1, N + 1):
        s = Fraction(0)
        for k in range(1, n + 1):
            s += f[k] * g[n - k]
        g[n] = -s  # since f_0 = 1
    # B(x) = 1 - G(x)  =>  b_0 = 0, b_n = -g_n for n>=1
    b = [-g[n] for n in range(1, N + 1)]
    return b


def invert_check(a_pos, b_pos):
    """Verify INVERT(b) == a, i.e. round-trip. Uses OEIS INVERT: A = B/(1-B)."""
    N = len(b_pos)
    # 1 - B(x)
    denom = [Fraction(1)] + [Fraction(-x) for x in b_pos]
    # 1/(1 - B(x)) = sum h_n x^n
    h = [Fraction(0)] * (N + 1)
    h[0] = Fraction(1)
    for n in range(1, N + 1):
        s = Fraction(0)
        for k in range(1, n + 1):
            s += denom[k] * h[n - k]
        h[n] = -s
    # a_reconstructed = (h_1, h_2, ...)
    return [h[i] for i in range(1, N + 1)]


rick = [3, 27, 417, 7851, 164124]

print("=" * 72)
print("Zabrocki INVERTi criterion on Rick's b_k sequence")
print("=" * 72)
print(f"Rick's sequence: {rick}")
print()

# ----- Convention A -----
print("Convention A: F(x) = 1 + 3 x + 27 x^2 + 417 x^3 + 7851 x^4 + 164124 x^5")
print("             (Zabrocki: a_0 = 1, a_k = b_k for k>=1)")
print("             INVERTi applied to (3, 27, 417, 7851, 164124)")
inv_A = inverti_from_1_plus(rick)
print(f"INVERTi(A) = {[str(x) for x in inv_A]}")
# Check integrality
all_int_A = all(x.denominator == 1 for x in inv_A)
print(f"All integer?  {all_int_A}")
# Sign check
signs_A = [int(x) for x in inv_A]
neg_A = [(i + 1, s) for i, s in enumerate(signs_A) if s < 0]
print(f"Nonneg?       {len(neg_A) == 0}")
if neg_A:
    print(f"  Negative terms (index, value): {neg_A}")
# Round trip
recon = invert_check(rick, inv_A)
recon_int = [int(x) for x in recon]
print(f"Round-trip INVERT(INVERTi(a)) = {recon_int}  (should equal {rick})")
assert recon_int == rick, "round-trip failure -- bug"
print()

# ----- Convention B -----
print("Convention B: F(x) = 3 + 27 x + 417 x^2 + 7851 x^3 + 164124 x^4")
print("             (a_0 = 3, not 1 -- not natural for Hopf existence)")
print("             We normalize by dividing F by 3, then apply INVERTi to")
print("             the resulting (a_1, a_2, ...) inside 1 + ...")
# F(x)/3 = 1 + 9 x + 139 x^2 + 2617 x^3 + 54708 x^4
a_pos_B = [Fraction(x, 3) for x in rick[1:]]
print(f"F/3 tail: {[str(x) for x in a_pos_B]}")


def inverti_from_1_plus_frac(a_pos):
    N = len(a_pos)
    f = [Fraction(1)] + list(a_pos)
    g = [Fraction(0)] * (N + 1)
    g[0] = Fraction(1)
    for n in range(1, N + 1):
        s = Fraction(0)
        for k in range(1, n + 1):
            s += f[k] * g[n - k]
        g[n] = -s
    return [-g[n] for n in range(1, N + 1)]


inv_B = inverti_from_1_plus_frac(a_pos_B)
print(f"INVERTi(F/3) = {[str(x) for x in inv_B]}")
signs_B = [x for x in inv_B]
neg_B = [(i + 1, s) for i, s in enumerate(signs_B) if s < 0]
print(f"Nonneg?       {len(neg_B) == 0}")
if neg_B:
    print(f"  Negative terms (index, value): {neg_B}")
print()

# ----- Extra: raw (no a_0 = 1) direct application if someone insists ------
print("Extra: some references define INVERTi purely on (a_1, a_2, ...)")
print("       treating F(x) = 1 + sum a_i x^i implicitly. That is exactly")
print("       Convention A above -- no separate computation needed.")
print()

print("=" * 72)
print("SUMMARY")
print("=" * 72)
print(f"Convention A INVERTi = {[int(x) if x.denominator==1 else str(x) for x in inv_A]}")
print(f"  All nonneg? {len(neg_A) == 0}")
print(f"Convention B INVERTi = {[str(x) for x in inv_B]}")
print(f"  All nonneg? {len(neg_B) == 0}")

verdict_A = "CONSISTENT with a graded free NC-cocomm connected Hopf algebra" if len(neg_A) == 0 else "INCONSISTENT (some INVERTi term is negative)"
print(f"\nZabrocki verdict (Convention A, the natural one): {verdict_A}")
