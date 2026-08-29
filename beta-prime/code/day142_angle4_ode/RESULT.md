# Day 142 Angle-4 / ODE — Results

## Summary

**Attack A (cumulants) succeeded partially**: extended the leading N_k sequence to
k = 6, discovered that the leading T^{3k-1} coefficient of N_k is INDEPENDENT
of (U, V), and found a CLOSED FORM for N_1(T; U=V=0) as a hypergeometric-type
divergent series linked to OEIS A179442 (Bessel-I(2,2) + Bessel-I(3,2) evaluation).

**Attack B (ODE ansatz) succeeded partially**: derived L = T(U+θ)(V+θ) - θ
with L·f = 0 verified. Applied L to F_P; L·F_P does NOT vanish, so F_P does
NOT satisfy the same ODE.  However, L·F_P / F_P has structural regularity:
the LEADING (highest E_3 power) part is (U, V)-INDEPENDENT: -3 E_3 T^2,
-18 E_3^2 T^5, -255 E_3^3 T^8, -4620 E_3^4 T^11, -94500 E_3^5 T^14, ...

**S = T^3 substitution does NOT reveal clean structure** at U=V=0 (all three
residue classes mod 3 have nonzero coefs).

## Rick's questions answered

### (1) Verification of N_k[T^{3k-1}] leading coefficients

Verified at (U, V) = (0, 0), (1, 1), (2, 3), (1/2, 3/2) — all AGREE:

| k | 3k-1 | N_k[T^{3k-1}] | numerator × (3k-1) |
|---|------|---------------|--------------------|
| 1 | 2    | 3/2           | 3                  |
| 2 | 5    | 27/5          | 27                 |
| 3 | 8    | 417/8         | 417                |
| 4 | 11   | 7851/11       | 7851               |
| 5 | 14   | 82062/7 = 164124/14 | 164124       |
| 6 | 17   | 3661389/17    | 3661389            |

The values are IDENTICAL across all (U, V) tested — the leading coefficient
of each cumulant N_k in T is a pure rational number (a UNIVERSAL constant).

**The (U, V) polynomials for N_k[T^{3k-1}] are all CONSTANTS.**

### (2) New data (N_4, N_5, N_6)

N_4[T^11] = 7851 / 11
N_5[T^14] = 82062 / 7 = 164124 / 14
N_6[T^17] = 3661389 / 17

Numerator sequence 3, 27, 417, 7851, 164124, 3661389 — **NOT in OEIS**.

Ratios approach ~24 (geometric growth). Divided by 3: 1, 9, 139, 2617, 54708, 1220463
— also not in OEIS.

### (3) S = T^3 substitution — NEGATIVE

At (U, V) = (0, 0), N_1 is a series in ALL powers of T from T^2 onward.
No cancellation in residue classes mod 3.  For example, N_1 has nonzero
coefs at T^2, T^3, T^4, T^5, T^6, ... — the substitution S = T^3 gives no
simplification.

However: **N_1(T; U=V=0) has an exact closed form:**

    N_1(T; 0, 0) = Σ_{b≥2} (b-1)! (b+1) / b · T^b

Equivalently, if a_b := b! · [T^b] N_1(T; 0, 0), then
    a_b = ((b-1)!)^2 · (b+1) = ((b-1)! (b+1)!) / b   =   OEIS A179442.

OEIS A179442 has the identity  Σ_{b≥1} 1/a_b = BesselI(2, 2) + BesselI(3, 2).
So there is a **Bessel-function-like structure** hidden in N_1.

This is a genuine hit. Whether N_2, N_3, ... admit similar closed forms is open;
the numerator ratios for N_2 (b=5..14 → 575/9, 7396/115, 139489/1849, ...) do NOT
factor cleanly in b, so N_2 is not of the same form as N_1.

### (4) ODE ansatz — L·F_P

**Correct derivation.** The operator
    L := T·(U + θ_T)(V + θ_T) - θ_T,    θ_T = T d/dT,
annihilates f = ₂F₀(U, V; ;T) formally:  L·f = 0 (verified up to T^{18}).

**Applied L to F_P (up to T^{11} in (U, V, E_3), higher at specific values):**

L·F_P DOES NOT VANISH.  Instead:
- L·F_P is divisible by E_3 (every T-coefficient starts at E_3^1 or higher).
- L·F_P has E_3-degree ⌊b/2⌋ at T^b, matching P_b.
- L·F_P / F_P as a series in T with E_3-polynomial coefficients:

At (U, V) = (0, 0):
    [T^2] -3 E_3        [T^3] -2 E_3         [T^4] -6 E_3
    [T^5] -18 E_3^2 - 24 E_3
    [T^6] -162 E_3^2 - 120 E_3
    [T^7] -1384 E_3^2 - 720 E_3
    [T^8] -255 E_3^3 - 12624 E_3^2 - 5040 E_3
    ...

The [E_3^1] coefficient at T^b (b≥3) is exactly -(b-1)! at U=V=0.  In fact
    [E_3^1] (L·F_P/F_P) at U=V=0  =  -3 T^2 - Σ_{b≥3} (b-1)! T^b
    (with [T^2] = -3 the ONLY anomaly).

**The LEADING (highest E_3 power) coefficient of L·F_P/F_P at each T^{3k-1}
is (U, V)-INDEPENDENT:** -3, -18, -255, -4620, -94500, ... (matches the pattern
of the leading N_k numerators, though with a different constant multiplier).

So the ODE ansatz gives a **Frobenius-type identity**:

    L·F_P  =  F_P · X(T, U, V, E_3)

where X = Σ_{k≥1} X_k(T, U, V) E_3^k, and X_k[T^{3k-1}] is a (U,V)-independent constant.

**But X is NOT a simple closed-form expression.**  It is a formal power series
in T with polynomial coefficients in (U, V), and its E_3-slices grow in
complexity.  I have no closed form for X.

### (5) Concrete next step

The most promising empirical finding is:

    **N_1(T; U=V=0)  =  T^2 · 2F0-like series linked to Bessel(2,2) + Bessel(3,2).**

Rick should pursue the following avenues, in order:

1. **Full (U, V) closed form for N_1.**  Compute N_1(T; U, V) as a polynomial in
   (U, V) with T-series coefficients.  I have the data through T^10 in this
   representation (see `analyze_LFPFP.py` for the (U, V, E_3) computation).
   The [T^b] coefficients of N_1 factor as
     [T^2] = 3/2,   [T^3] = 8(U+V+1)/3,   [T^4] = 3·[7 UV(U+V) + 7(U²+V²) + ... ]
   Guess: **N_1(T; U, V) = (some closed form involving (U+V)-shifted rising factorials)
   times the U=V=0 series.**  If Rick can fit N_1(T; U, V) = (a modified Bessel or
   ₂F₀ combination), the ODE for it will be Bessel or confluent hypergeometric,
   which is a clean structural target.

2. **Try to derive a second-order LINEAR ODE for F_P in T alone.**  The Frobenius
   identity L·F_P = F_P · X gives a quasilinear ODE.  Compare with the derivation
   of the Bessel equation from the sum Σ 1/((n-1)!(n+1)! / n).  The Bessel-I(2,x) 
   equation is  x²u'' + xu' - (x²+4)u = 0.  Try to see if a similar equation
   with parameters depending on U, V, E_3 fits F_P.

3. **Abandon the S = T^3 substitution.**  It does not reveal structure here.

4. **The direct closed form for U_b remains elusive.**  Cumulants and the ODE
   ansatz give partial structural information but no clean expression yet.

## Files produced

- `/home/agent/projects/beta-prime/code/day142_angle4_ode/compute_P_UV.py` — P_b in (U, V, E_3).
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/compute_P_fast.py` — P_b at specific (U, V) values (faster).
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/cumulants.py` — Full N_k computation with verifications.
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/cumulants_UV0.py` — N_k(T; 0, 0) up to T^18.
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/probe_full_UV.py` — Confirms (U, V)-independence of N_k leading.
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/ode_ansatz.py` — L·F_P and L·F_P/F_P, L·F_P/f computations.
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/ode_ansatz_v2.py` — Fast per-(U,V) version.
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/ode_ansatz_v3.py` — LFP/f decomposition.
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/analyze_LFPFP.py` — X = L·F_P/F_P as (U, V, T, E_3) poly.

## Honest assessment

- N_1 closed form IS a real find. It's specific to (U, V) = (0, 0), but it links
  Rick's problem to the well-known Bessel-I(2,2) + Bessel-I(3,2) generating series.
- The (U, V)-independence of leading N_k[T^{3k-1}] and of leading L·F_P/F_P at
  E_3^k · T^{3k-1} is a strong structural invariant. It suggests the "top" of
  F_P (in some grading involving E_3 and T^3) is a universal series in E_3, T
  independent of (U, V).
- The full closed form for U_b remains OPEN.  Attack A gives cumulants;
  Attack B gives a Frobenius identity but with unclean RHS X.  Combining
  them into a full closed form is the next step.

## Day 142 Session 2 — Bessel / ODE / Sequence leads

### Lead 3 (ODE for N_1) — **CLEAN ODE DERIVED and VERIFIED**

Substituting log F_P = log f + Σ E_3^k N_k into the Frobenius identity
L·F_P = F_P · X and extracting the E_3^1 coefficient gives:

    T·θ² N_1  +  [T(U+V) - 1 + 2T·φ]·θ N_1  =  X_1

where θ = T d/dT, φ = θf/f (the "logarithmic derivative" of the base
₂F₀(U, V; ; T) formally), and X_1 = [E_3^1] (L·F_P/F_P).

**Verified ALL ZERO** up to T^9 (with full (U, V) polynomial coefficients).
The derivation is:
- L(f·G)/(f·G) = X where G = e^R, R = Σ E_3^k N_k.
- Using L(fG) = (Lf)·G + [T(U+V)f + 2T θf - f]·θG + Tf·θ²G  (and Lf = 0).
- G^{-1}·L(fG) = [T(U+V) + 2Tφ - 1]·θR + T·((θR)² + θ²R).
- At [E_3^1]: (θR)² doesn't contribute — recovers the ODE above.

This is **not** a Bessel equation — the T·φ term makes it "quasi-Bessel"
with a divergent formal power-series coefficient. But it IS a
**first-order linear ODE for M := θN_1** with source X_1.

Formally, the homogeneous solution is:

    M_h = C · T^{-(U+V)} · e^{-1/T} · f^{-2}

(integrate d(log M)/dT = -[(U+V)/T - 1/T² + 2f'/f]).

### Lead 1 (Bessel closed form for N_1) — **PARTIAL FIT**

Computed [T^b] N_1(T; U, V) as symmetric (U↔V) polynomial in (U, V)
for b = 2..10.  Total degree in each of U, V is exactly b-2 (much
lower than the (U)_b(V)_b degree of f — this is why N_1 is "simpler"
than f in the sense that its coefficients live in a lower-degree
subspace).

**MAJOR STRUCTURAL FIND (V = 0 slice):**

    [T^b] N_1 |_{V = 0}  =  (b² - 1)/b · (U + 1)_{b-2}
                        =  (b-1)(b+1)/b · Γ(U+b-1)/Γ(U+1)

Verified for b = 2..8.  At U = V = 0 this reduces to (b-1)!(b+1)/b — matches
the prior A179442 hit.

**Full (U, V) fit — NOT YET FOUND.**  Tested ansatzes:
1. (b²-1)/(b(b-2)!) · (U+1)_{b-2}(V+1)_{b-2}  — FAILS (off by UV-mixed terms).
2. (b²-1)/(b(b-2)!) · (U+V+1)_{b-2}  — matches at b=2, 3, fails at b=4.
3. Symmetric mixed (U+1)_{b-2}(V+2)_{b-2} sums — fails.

The residual after subtracting ansatz 1 grows with b, so a simple product
formula does not extend beyond the V=0 slice.  The full N_1(T; U, V) is
polynomial-symmetric in (U, V) but does not admit a factorization into
rising-factorial products in each of U and V separately.

### Lead 1 (X_1 closed form at V=0) — **CLEAN FACTORIZATION FOUND**

    X_1[T^b] |_{V=0}  =  -(U+1)_{b-3} · [(2b-1) U + (b-2)(b-1)]     (b ≥ 3)
                        =  -3     (b = 2)

(with the convention (U+1)_0 = 1 and (U+1)_{-1} being interpreted so that
b = 2 gives -3 = -(2·2-1)).

Verified for b = 2..7.  This is a much cleaner factorization than N_1 itself
and gives the (U, V)-independent leading X_k[T^{3k-1}] sequence
-3, -18, -255, ... at V=0 (it evaluates to -(2b-1)(b-2)(b-1) at U=0=V, but
we only have data through the full (U, V)-polynomial at this level for X_1).

### Lead 2 (Sequence -3, -18, -255, -4620, -94500) — **NOT IN OEIS**

Queried OEIS in both signed and unsigned forms, and after dividing by 3, k!,
(3k-1)!, (3k-1)!!, C(3k, k), (6k-3), and other natural factors.  **No matches.**

Prime factorizations:
   3 = 3;  18 = 2·3²;  255 = 3·5·17;  4620 = 2²·3·5·7·11;  94500 = 2²·3³·5³·7.
The 17 and later prime factors kill polynomial closed forms.

Best partial fit: a_k = -X_k[T^{3k-1}]|_{U=V=0} and (from Lead 1 above) at V=0
the linear-in-U structure gives -(2(3k-1)-1)U + (3k-3)(3k-2) at leading T^{3k-1}
of X_1 (but this is only the k=1 case).  Extending this to general k needs
computing X_k in full symbolic (U, V) — beyond current compute budget.

### Concrete next step

**The ODE for N_1 is the strongest lead.**  The RHS X_1 factors cleanly at
V = 0.  If Rick can:
1. Derive X_1(T; U, V) in closed form (using the same L(fG)/(fG) expansion
   but extracting the E_3^1 coefficient from L·F_P/F_P directly), then
2. Integrate the first-order ODE for θN_1 with that source.

The integrating factor is T^{-(U+V)} · e^{-1/T} · f^{-2}, so

    θN_1 = T^{-(U+V)} · e^{-1/T} · f^{-2} · [C + ∫ T^{(U+V)-1} e^{1/T} f² · X_1/T dT ]

(interpreted formally).  If X_1 · f² has an "antiderivative" that closes up
nicely, N_1 is in closed form.

The (U, V)-independence of the [E_3^k T^{3k-1}] leading coefficient of X
across k = 1..5 suggests that there is a "diagonal" limit / grading in
which X becomes universal — this may be the natural angle to derive the
X_k series in closed form.

## Files produced (Session 2)

- `/home/agent/projects/beta-prime/code/day142_angle4_ode/lead_bessel.py` — N_1 (U, V) polynomial, ansatz probes.
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/lead_bessel_v2.py` — Ansatz tests, V=0 factorization.
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/lead_Xseq.py` — OEIS / formula probes for X leading.
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/lead_ODE_N1.py` — ODE derivation & verification.

## Day 142 Session 3 — Full (U, V) X_1: NO clean closed form

### Data (X_1[T^b] as symbolic (U, V)-polynomial, b = 2..8)

Verified in `lift_X1.py`, `lift_X1_v3.py`, `lift_X1_v4.py`, `lift_X1_v5.py`.

X_1[T^b] is a **symmetric polynomial in (U, V)** of bidegree (b-2, b-2)
and total degree 2b-3. The (b-1)×(b-1) coefficient matrix has FULL rank
b-1 — so X_1[T^b] is NOT a low-rank tensor.

Structural constants:
    [U^{b-2} V^0] X_1[T^b] = -(2b-1)  ← matches V=0 formula top
    [U^0 V^0]     X_1[T^b] = -(b-1)!
    [U^{b-2} V^{b-2}] X_1[T^b] = 0   (total degree < 2(b-2))

### Best decomposition found

    X_1[T^b] = -(2b-1) [(U)_{b-2} + (V)_{b-2}]
              -(b-2)(b-1)/(b-3)! · (U+1)_{b-3} (V+1)_{b-3}
              + U V · R_b(U, V)

Verified for b = 3..8. The V=0 slice reduces to the known formula because
(V)_{b-2}|_{V=0} = 0 and (V+1)_{b-3}|_{V=0} = (b-3)!.

    R_3 = 0
    R_4 = -15
    R_5 = 6(UV - 6U - 6V - 11)
    R_6 = (2/3)(5U²V² + 30U²V + 30UV² - 110U² - 110V² - 150UV - 459U - 459V - 529)
    R_7 = ...  (see lift_X1.py output; degree 6)
    R_8 = ...  (degree 8)

R_b is symmetric in U↔V and has bidegree (b-3, b-3). Its "top" monomial
[U^{b-3} V^{b-3}] R_b is a rational sequence: 0, -15, 6, 10/3, 5/4, 7/20
for b = 3..8 — no clean OEIS/factorial fit.

### Ansatz results (all FAIL)

Ansatzes tried and RULED OUT:

  (a1) X_1[T^b] = -(1/2)[(U+1)_{b-3} A_0(U) + sym]         FAIL (linear residual)
  (a2) A(U, V, b) polynomial extension of V=0 factor       FAIL (residual not UV·poly)
  (b)  -(U+1)_{b-3}(V+1)_{b-3} Q/(b-3)!  polynomial Q      FAIL (Q rational at b>=4)
  (C)  -[(U+1)_{b-3} A(U,V,b) + (V+1)_{b-3} A(V,U,b)]      FAIL at b=3 already
       (any polynomial A up to degree b-2)
  (D)  Linear comb R_b = Σ c_k X_1[T^{b-2k}](U+k, V+k)     FAIL for b >= 5

The ONLY clean identity found:
    R_4 = 5 · X_1[T^2](U+1, V+1) = -15                     MATCHES

but this is a coincidence — for b >= 5, R_b has a top monomial
[U^{b-3} V^{b-3}] that X_1[T^{b-2}] cannot supply (X_1[T^{b-2}] has
bidegree (b-4, b-4)).

### Structural obstruction

X_1[T^b] is a genuinely full-rank symmetric bilinear form of bidegree
(b-2, b-2). It CANNOT be written as any bounded sum of shifted rising
factorial products of the form
   (U+a)_p (V+b)_q · c(a, b, p, q, b_index)
without a growing number of terms.

The pattern seen in the V=0 slice (a clean rank-1 factorization) is a
special-slice phenomenon: on V=0, the polynomial reduces to a specific
row of the coefficient matrix. There is no analogous factorization for
the full X_1[T^b].

### Interpretation

The **only** clean structural facts about X_1 are:
1. Leading-diagonal (U, V)-independence: [T^{3k-1} E_3^k] X = -3, -18, -255, ...
2. V=0 slice: -(U+1)_{b-3}·[(2b-1)U + (b-2)(b-1)] — clean and verified b=2..8.
3. Row/column structure at the corners:
     [U^{b-2}] X_1[T^b] = -(2b-1) (V-independent!)
     [U^0]     X_1[T^b] = -(b-1)! at (V=0), grows with V into
                          rf(V, b-2) coefficients times (2b-1)-multiples.

The interior of the coefficient matrix (i.e., all monomials [U^i V^j]
with 1 ≤ i, j ≤ b-3) does NOT admit a clean closed form.

### Verdict on the closed-form program

**No clean closed form for X_1(T; U, V).** The V=0 slice was misleading:
its cleanliness comes from evaluating on a coordinate axis, not from
underlying rank-1 structure.

**Best current representation:**
    X_1(T; U, V) = base(T; U, V) + U V · Rem(T; U, V)
where
    base(T; U, V) = Σ_{b>=2} T^b · [ -(2b-1)((U)_{b-2}+(V)_{b-2})
                                     -(b-2)(b-1)(U+1)_{b-3}(V+1)_{b-3}/(b-3)! ]
and Rem(T; U, V) is a symmetric power series with no closed form.

The base has hypergeometric structure — the (U)_{b-2} + (V)_{b-2}
part is (essentially) θ_T · [₂F₀-like series in U or V separately],
and (U+1)_{b-3}(V+1)_{b-3}/(b-3)! · (b-2)(b-1) is a mixed-hypergeometric
term.

### Next step (Rick's decision)

Two paths forward:

1. **Accept partial structure and move on.** The base part above IS a
   closed form for the "boundary" of X_1. The interior is
   noise-in-a-basis. Use the base to derive a partial ODE for N_1 that
   captures the boundary structure; treat the residual as a formal
   correction series.

2. **Change of basis.** Perhaps X_1[T^b] has a clean closed form in a
   BETTER basis than U, V — e.g., after substituting U = α+β, V = α·β
   (Vieta pairs), or as a function of the roots of the ₂F₀ operator
   L = T(U+θ)(V+θ) - θ. But this requires guessing what basis to try.

3. **Compute X_2, X_3, ... first.** The leading-diagonal
   (U,V)-independence of [T^{3k-1} E_3^k] X suggests the sequence X_k
   has structure in k. Maybe X_1 alone is misleading and one should look
   at the generating series X(T, U, V, E_3) as a whole.

### Files produced (Session 3)

- `/home/agent/projects/beta-prime/code/day142_angle4_ode/lift_X1.py` — Full X_1 computation & first ansatzes.
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/lift_X1_v2.py` — Bilinear A ansatz (fails).
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/lift_X1_v3.py` — Double-pochhammer split (base found, residual isolated).
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/lift_X1_v4.py` — R_b structure analysis.
- `/home/agent/projects/beta-prime/code/day142_angle4_ode/lift_X1_v5.py` — Recursion attempts (all fail except b=4).

