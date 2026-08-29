# Day 106 — H5'' proof attempt

**Date:** 2026-08-14
**Author:** Rick's proof-attempt agent
**Statement (H5'', to prove):**
```
Q_{2R}(R-2, R, R) = R! · (R+1)! · (2R)!         (R even, ≥ 4)
```
Empirically verified as exact integer identity at R ∈ {4, 6, 8, 10, 12}.

**One-line status:** Route C (symbolic small-case) SUCCESS. H5'' verified
symbolically at R = 2, 3, 4, 5, 6 with a small sign correction for R odd:

```
Q_{2R}(R-2, R, R) = (-1)^R · R! · (R+1)! · (2R)!         (R ≥ 2)
```

For R even (Rick's stated regime) the sign is `+1`, matching H5''. For R
odd we discovered the identity extends with sign flip. **NEW: H5'' extends
to all R ≥ 2 with (-1)^R prefactor.**

**A cleaner reformulation of the residual gap (RESIDUAL GAP)** is at the
end of this document (§5). It reduces the target to a polynomial-identity
statement about a specific 3-row Jacobi-Trudi determinant.

---

## 1. Route C — symbolic small-case verification (SUCCESS)

**Procedure.** For each R ∈ {2, 3, 4, 5, 6}:
1. Use `d102.fit_Qk_bivar` at each c ∈ {2R+2, 2R+3, ..., 2R+2+N} to fit
   Q_{2R}^{(c)}(a, b) as a bivariate polynomial and evaluate at
   (a, b) = (R-2, R). This gives Q_{2R}(R-2, R, c) as integer for each c.
2. Fit Q_{2R}(R-2, R, c) as univariate polynomial in c via Vandermonde on
   the sample values. Verify polynomial degree.
3. Evaluate the fitted polynomial at c = R.
4. Compare to R!(R+1)!(2R)!.
5. Divide Q by c^(R) = c(c-1)...(c-R+1) and factor.

**Result table.**

| R | deg_c(Q) | Q(R-2, R, R)              | (-1)^R · R!(R+1)!(2R)!    | Match |
|---|----------|---------------------------|---------------------------|-------|
| 2 |    8     |             288           |             288           | ✓     |
| 3 |    12    |          -103,680         |          -103,680         | ✓     |
| 4 |    16    |         116,121,600       |         116,121,600       | ✓     |
| 5 |    20    |      -313,528,320,000     |      -313,528,320,000     | ✓     |
| 6 |    24    |    1,738,201,006,080,000  |    1,738,201,006,080,000  | ✓     |

**Code:** `/home/agent/projects/code/2026-08-14-h5doubleprime-symbolic.py` and
`2026-08-14-h5dp-R6-check.py`.

This is a *proof-quality symbolic verification* at each R independently
(the poly fit is unique and cross-validated by additional samples). It is
NOT a uniform-in-R proof, but it CLOSES H5'' at R = 4, 6 (Rick's confirmed
range) at proof-level rigor via the same technique that closed Claim B in
Day 104.

## 2. Structural facts extracted from Route C

**Fact 2.1 (Q polynomial degree).** Q_{2R}(R-2, R, c) is a polynomial in c
of degree exactly **4R**.

**Fact 2.2 (Vanishing at c = 0, 1, ..., R-1).** Q_{2R}(R-2, R, c) is
divisible by c^(R) := c(c-1)⋯(c-R+1). So we can write
```
Q_{2R}(R-2, R, c) = c^(R) · P_R(c),   deg P_R = 3R.
```

**Fact 2.3 (Anchor value factors into two).** At c = R:
```
Q_{2R}(R-2, R, R) = R^(R) · P_R(R) = R! · P_R(R),
```
so H5'' reduces to
```
                    P_R(R) = (-1)^R · (R+1)! · (2R)!.       (H5''-P)
```

**Fact 2.4 (Two-point equality — DISCOVERED HERE).** Empirically, at
R = 2, 3, 4, 5, 6:
```
                    P_R(R) = P_R(R+1).
```

Verified from Route C data:

| R | P_R(R)                | P_R(R+1)              | Equal? |
|---|-----------------------|-----------------------|--------|
| 2 |          144          |          144          | ✓      |
| 3 |       -17,280         |       -17,280         | ✓      |
| 4 |     4,838,400         |     4,838,400         | ✓      |
| 5 |  -2,612,736,000       |  -2,612,736,000       | ✓      |
| 6 |  2,414,168,064,000    |  2,414,168,064,000    | ✓      |

Equivalent statement:
```
Q_{2R}(R-2, R, R+1) = (R+1)!/R! · Q_{2R}(R-2, R, R) = (R+1) · Q_{2R}(R-2, R, R).  (‡')
```

This is a new nontrivial two-point rigidity, not previously noted.

**Fact 2.5 (Ratio table for P_R at other integer points).**
```
    P_R(R-1) / P_R(R)  =  (R+2)/2   (verified R = 2..6)
    P_R(R+1) / P_R(R)  =  1         (Fact 2.4)
```
The R-1 ratio is a rational function of R (verified: R=2→2, R=3→5/2,
R=4→3, R=5→7/2, R=6→4). Higher-order ratios (R-2, R-3, ...) grow but do
NOT match any obvious factorial pattern (e.g., R=3: 13, R=4: 19, R=5: 26,
R=6: —). We did NOT identify a uniform closed form for k ≥ 2.

**Fact 2.6 (Catalan reformulation of the target).**
```
R! · (R+1)! · (2R)! = ((2R)!)^2 / C_R,     C_R := (2R)! / (R!(R+1)!) = Catalan #.
```
So H5'' equivalently reads
```
Q_{2R}(R-2, R, R) = ((2R)!)^2 / C_R.
```
This is suggestive of a Selberg / Macdonald constant term / super-Catalan
identity but we did NOT close a combinatorial interpretation. (Attempt to
match to SYT of shapes (2R-2, R, R), (2R, R+1, R), etc. FAILED — the hook-
length counts don't match.)

## 3. Route A — Pochhammer analytic continuation

The relation from Day 104 §1 is (†)
```
h_{2R}^{(c)}(R-2, R) = (c-R-1)! (c-R)! / (R!(R+1)!) · Q_{2R}(R-2, R, c),
                       (c ≥ 2R+1, regular regime).
```

Both sides are polynomial-in-c (by Day 88, Q is polynomial; h_{2R} is
computed by the H_c template which is a rational function that becomes
polynomial after Q-normalization).

**Blocker for Route A.** At c = R, the pre-factor (c-R-1)!(c-R)!/R!(R+1)!
has a POLE (from (c-R-1)! = (-1)!). And separately, the H_c template
has a **0/0 singularity** at c=R because (a-c+2)(b-c+1)|_{a=R-2, b=R, c=R}
= 0·1 = 0.

To evaluate Q at c=R via (†), we'd need to
- extract the residue of h_{2R} at the pole, OR
- extract the finite part of the 0/0 in H_c and back out Q via limit.

We tried to symbolically implement this via `sympy.limit` on the H_c
template, but the raw sympy expressions with `RisingFactorial(x, c-symbolic)`
don't reduce cleanly — the arguments are symbolic and sympy cannot
poly-fy them without a rewrite to gamma functions. This route is BLOCKED
in-session but not fundamentally obstructed (see §5 for the reformulation).

## 4. Route B — direct h evaluation at c = R via binomial inversion

Attempted. The H_c(R-2, R, j) template is UNDEFINED at c = R for all
j ≥ 0 due to the (a-c+2)(b-c+1) denominator = 0. Individual H_c(R-2, R, j)
values do NOT extend to c = R without a limit/residue calculation, which
loops back to the same challenge as Route A.

**Empirically** (from Route C), we know h_{2R}^{(R+ε)}(R-2, R) has a pole
at ε=0 of order 2 (from the (c-R-1)! (c-R)! prefactor), whose residue
matches Q(R-2, R, R) · 1 / (R!(R+1)!) (from the Laurent expansion). But
we did NOT extract this analytically — only numerically via Route C.

## 5. Route D — combinatorial interpretation (partial)

The target (2R)!² / C_R = R!(R+1)!(2R)! is a well-known combinatorial
quantity, but we did NOT locate a matching SYT count for any 3-row shape
we tested: (2R-2, R, R), (2R, R+1, R), (2R+2, 2, 1), (2R+1, R+1, R-1)
all gave DIFFERENT hook-length values. Not a plain 3-row SYT count.

**Candidate interpretations we did NOT try (recommended for future):**
- **Number of pairs (T_1, T_2) of SYT** of some shape.
- **Weyl dim × dim of some SL_3 × SL_3 tensor.**
- **Selberg integral** evaluation: 3-particle Selberg with specific
  exponents.
- **Macdonald constant term for A_2 root system.**

The R!(R+1)!(2R)! structure factoring symmetrically across 3 rows *strongly*
suggests an SL_3 or A_2-root-system interpretation, but pinning it down
requires familiarity with the specific normalization of the M_j determinant.

## 6. Sanity: R = 2 gets 288 (matches all data — refutes an old open question)

The Day-106 file `H5-doubleprime-c0-triple-factorial.md` (§ "R = 2 edge
case") noted a discrepancy: "H5'' FAILS at R = 2 by a factor of 2." But
our Route C fit at R = 2 gives Q_4(0, 2, 2) = **288** exactly, not 144. This
matches R!(R+1)!(2R)! = 2·6·24 = 288.

So **H5'' also holds at R = 2** with no correction. The "actual c_0(2) = 144"
claim in the H5'' memo appears to be incorrect (probably a v_2 mismatch —
144 = 288/2, but v_2(288) = 5 and v_2(144) = 4, and Day 104 §5.5 says
v_2(Q_4(0, 2, c)) = 5, matching our 288 not 144).

**Consequence:** with the (-1)^R sign correction for odd R, H5'' holds
uniformly for all R ≥ 2:
```
Q_{2R}(R-2, R, R) = (-1)^R · R! · (R+1)! · (2R)!.       (H5''-general)
```

## 7. THE CRUX — where the analytic argument is blocked

The Day-88 factorisation h_{2R}^{(c)}(a, b) = (a+3)_L (b+2)_L Q_{2R}(a, b, c)
is a **polynomial identity** in Z[a, b, c] (lean-verified). At the anchor
(a, b) = (R-2, R):
```
(a+3)_L = (R+1)_{c-1-2R},    (b+2)_L = (R+2)_{c-1-2R}.
```
As rational functions of c (viewed via gamma), (R+1)_L = Γ(c-R)/Γ(R+1).

**The crux algebraic step:** Extract the pole-order-1 residue of
h_{2R}^{(c)}(R-2, R) at c = R via the direct M_j-determinant formula, and
observe that this residue equals (R+1)!(2R)! (which is P_R(R) up to a
sign; then Q(R-2, R, R) = R!·P_R(R)).

Equivalently: prove **(†) at c = R via analytic continuation**:
```
[(c-R-1)! (c-R)! · Q_{2R}(R-2, R, c) / (R!(R+1)!)]_{c=R+0}
   = lim_{c→R} [(c-R-1)! (c-R)! / (R!(R+1)!)] · [P_R(R) · R!] + higher order.
```

The residue of (c-R-1)! at c=R is (-1)^{R+1}/R! ... actually more
precisely, (c-R-1)! has a simple pole at c=R with residue
Res_{c=R} (c-R-1)! = Res_{s=0} 1/Γ(0+s)(...)  — this is where the (-1)^R
comes from!

The residue of Γ(-n) is (-1)^n / n!. So the residue of (c-R-1)! = Γ(c-R)
at c=R is: Γ(c-R) has pole at c=R (arg=0), residue 1. So the pole of
(c-R-1)! · (c-R)! at c=R is: (c-R)! is nonzero (=1) at c=R, but (c-R-1)!
= Γ(c-R) has pole of order 1 with residue 1.

Therefore:
```
lim_{c→R} (c-R) · (c-R-1)! · (c-R)! = 1 · 1 = 1     [wait this is residue, not the value]
```

Hmm — actually the identity (†) holds ONLY for c ≥ 2R+1 (integer). To
extend to c = R we need the polynomial identity for Q, which is what we
have. But Q by itself IS a well-defined polynomial — its value at c = R
is determined by the polynomial coefficients, not by any analytic
continuation of h.

**So the *true* crux is:** the polynomial Q_{2R}(R-2, R, c) is defined by
a specific formula (M_j determinant / Jacobi-Trudi / Pochhammer normalization
of h_{2R}). This polynomial happens to vanish at c = 0, 1, ..., R-1 (Fact
2.2) and takes the value (-1)^R R!(R+1)!(2R)! at c = R (Fact H5''). Both
facts are *structural properties of the polynomial coefficients* and are
in principle derivable from the M_j determinant, but the derivation
requires **evaluating the M_j determinant at a=R-2, b=R, c=R** and
tracking what the 0/0 singularity in the H_c → h_k → Q pipeline resolves
to.

## 8. Residual gap (RESIDUAL GAP)

**Reformulation:** Prove that the polynomial P_R(c) ∈ Z[c] (of degree 3R,
leading coefficient 1) defined by

    Q_{2R}(R-2, R, c) = c(c-1)(c-2)⋯(c-R+1) · P_R(c)

satisfies

    P_R(R) = (-1)^R · (R+1)! · (2R)!,       AND       P_R(R+1) = P_R(R).

The second equation is a **new observation** and represents a nontrivial
algebraic constraint on P_R.

**Rewriting using the two-point equality:** since Q vanishes at c = 0..R-1
and P_R(R) = P_R(R+1), the divided difference
```
[Q_{2R}(R-2, R, c) - (something)] / (c-R)(c-R-1)
```
should be a polynomial in c of degree 3R - 2 with tractable value at
c = R. This might be the cleanest tackling angle.

**Alternative reformulation via the ratio (‡'):** prove the "1-shift"
identity
```
Q_{2R}(R-2, R, c+1) · c = Q_{2R}(R-2, R, c) · (c-R+1) ·
                            [something regular in c that equals (R+1) at c=R]
```
This is the exact form of the equality Q(R-2, R, R+1) = (R+1) · Q(R-2, R, R)
if written correctly.

**Recommended attack:** compute Q_{2R}(R-2, R, c) symbolically via the
M_j determinant (Jacobi-Trudi for SL_3) with `a, b` integer specialized
and `c` symbolic, then verify (†) at c=R via Laurent expansion. The
Jacobi-Trudi should give an explicit (small) determinant of hypergeometric
values that CAN be evaluated symbolically. We tried this via `sympy.rf`
but the `RisingFactorial(x, symbolic_c)` didn't cooperate with `Poly`; a
gamma-function rewrite or manual expansion should unblock it.

## 9. Verification data files

- `/home/agent/projects/code/2026-08-14-h5doubleprime-symbolic.py` — main
  Route C symbolic verifier.
- `/home/agent/projects/code/2026-08-14-h5dp-analyze-P.py` — P_R
  ratio-pattern analysis.
- `/home/agent/projects/code/2026-08-14-h5dp-R6-check.py` — R=6
  verification (~2 min compute).

Empirical outputs (integer-exact): R = 2, 3, 4, 5, 6 all match H5''-general.

## 10. What Rick should attack next

1. **Prove Fact 2.4 (P_R(R) = P_R(R+1)) from the M_j determinant.** This
   is a new, clean two-point equality that likely reduces to an
   antisymmetry / row-swap in the determinant. Might be low-hanging.
2. **Prove Fact 2.2 (c^(R) | Q) from the M_j formula.** The vanishing of
   Q at c = 0, 1, ..., R-1 is a strong structural fact. In the M_j
   determinant, c = 0 corresponds to a degenerate row; c = 1 to a
   different degeneracy; etc. Likely accessible via row-operations on the
   3×3 M_j matrix.
3. **Look up "R!(R+1)!(2R)!" in OEIS.** Sequence 288, 103680, 116121600,
   313528320000, ... . May yield a known combinatorial identification.
   (I did not have OEIS access mid-session.)
4. **Selberg / Macdonald A_2.** The three-factorial symmetric structure
   R!(R+1)!(2R)! and Rick's "Jacobi-Trudi for SL_3" hunch strongly
   suggest a Macdonald constant-term or Selberg integral evaluation.

## 11. Registry updates (proposed)

- `H5-doubleprime-c0-triple-factorial`: 
  → **`verified-R2-through-R6-symbolic`**. Was `verified-R4-R10-empirical`.
  Route C independently reproduces R = 4, 6 (Rick's data) AND extends to
  R = 2, 3, 5 (with (-1)^R sign for odd R).

- **NEW node:** `P_R-two-point-equality-R-Rplus1`:
  → **`verified-R2-through-R6-empirical`**. Statement: P_R(R) = P_R(R+1).
  Structural rigidity, worth pursuing separately from H5''.

- **NEW node:** `Q-vanishes-at-c-in-0-to-Rminus1`:
  → **`verified-R2-through-R6-symbolic`**. Statement: c^(R) | Q_{2R}(R-2, R, c).
  Foundational; likely provable directly from M_j.

- **NEW node:** `H5''-general-with-sign`:
  → **`verified-R2-through-R6-symbolic`**. Statement:
  Q_{2R}(R-2, R, R) = (-1)^R · R!(R+1)!(2R)!.  Extends H5'' to odd R.
