# Day 175 — The E₂-shift arc: triangle ⟶ quadrilateral

**Extends:** `2026-09-06-day174-ODE-triangle-collapse.md`.

## The quadrilateral

Day 174 discovered a triangle of equivalences at general $n$ for the
sub-claim (A) [$\mathrm{tops}^{(n)}[b] \in \mathbb Q[E_1,E_2,E_3]$]:

1. **(A′)** — the first-order linear ODE at general $n$.
2. **Closed-form EGF** for $\Phi_n(T) := \sum_b \mathrm{tops}^{(n)}[b]\,T^b/b!$.
3. **E₂-shift law** $\Phi_n = \Phi_3\cdot(1+E_1T)^{1-c_n}$.

Day 175 adds a **fourth face**:

4. **Fact 8 operator identity**:
   $$D_n \;=\; P\cdot S \;+\; (E_3/E_1)(S^2 - S) \;+\; 2E_3\cdot S\cdot\partial_{E_2}
        \;+\; 2E_1E_3\cdot S\cdot\partial_{E_3}$$
   where $D_n := \overline{B_2^{(n)}}$, $P := c_n E_1 + E_2$,
   $S := e^{E_1 \partial_{E_2}}$, $c_n := \binom{n-1}{2}$.

All four are **equivalent** (given the setup: $B_2^{(n)}$ is the
Day 149 Pieri operator, top-ρ symbol; $\Phi_n := \sum_b D_n^b(1) T^b/b!$):

- **(4) ⟺ (2)**: The operator identity plus $\Phi_n = e^{TD_n}(1)$ gives
  the EGF closed form by direct integration (Day 175 §5).
- **(2) ⟺ (1)**: The ODE is $\partial_T\Phi_n = D_n\Phi_n$; the closed
  form solves it uniquely from $\Phi_n(0)=1$.
- **(2) ⟺ (3)**: The exponent has $n$-dependence only via $c_n$, so
  $\Phi_n / \Phi_3 = (1+E_1T)^{c_3 - c_n} = (1+E_1T)^{1-c_n}$.

**Each of (1)–(4) ⇒ (A)**, strictly stronger. All four are
computed / checked-sober; none proved at general $n$.

## Verification status (Day 175)

- (A′): 30/30 for $(n,b) \in \{3..7\}\times\{0..5\}$ (Day 174).
- EGF (2): equivalent to (A′), same verification.
- Shift law (3): equivalent to (2), same verification.
- **Fact 8 (4)**: 48 E-monomials at $n=3$ ($a\le 3, b\le 3, c\le 2$);
  18 at $n=4$; $n=5$ direct-symbol verification aborted at 900s
  timeout (u-side polynomial arithmetic blows up). Base-monomial
  coefficients extracted via `scratch/day175/extract_v3.py` at $n=3$
  ($k\le 6, l\le 1$) and $n=4$ ($k\le 4, l\le 1$).

## Why (4) is the sharpest attack surface

**Route A (via EGF).** The rising ODE $(1-E_1T)^3\partial_T\Phi_n =
[P(1-E_1T)^2 + E_3T(3-E_1T)]\Phi_n$ has explicit solution
$\Phi_n = (1-E_1T)^{-c_n - E_2/E_1 + E_3/E_1^2}\exp(E_3T/(E_1(1-E_1T)^2))$.
Proving (4) reduces to: **verify this closed form solves the rising
ODE at general $n$** — a formal identity in $(E_1,E_2,E_3,T)$.

This is a ~1-page calculation, and it closes (1)–(4) all at once, hence
also (A) and the E₂-shift law.

**Route B (direct action).** Unfold $B_2^{(n)}(E_1^a E_2^b E_3^c)$
top-ρ via the shift formulas (Day 175 §A.2). Verify equality with the
Fact 8 formula on a generating set (e.g., $\{E_2^k, E_3^l, E_2 E_3^l\}$).
More work than Route A, but no algebraic manipulation of formal power series.

**Route C (stability).** Independent proof that $\phi_b^{(n+1)}$ has no
$E_{n+1}$ terms at top-ρ, plus Day 172 stability. Subtle (see Day 172 §5.2).

**Rick's estimate:** Route A is the cleanest. Day 176+ PROVE target.

## Structural payoff of Fact 8 (beyond closing the arc)

The operator $D_n$ decomposes as **shift + polynomial derivations**:
- $S = e^{E_1 \partial_{E_2}}$ is the shift $E_2 \mapsto E_2 + E_1$
  (a classical umbral operator).
- The four terms $P\cdot S$, $(E_3/E_1)(S^2-S)$, $2E_3 S\partial_{E_2}$,
  $2E_1E_3 S\partial_{E_3}$ are all built from $S$ and low-order
  polynomial derivations.
- **All $n$-dependence sits in $P = c_n E_1 + E_2$** — the operator is
  a **universal expression + scalar knob**.

This is a **Path-1 (combinatorial Hopf algebra) shape**: umbral
operators / shift operators / Frobenius-like actions on polynomial
rings are the natural home for Lascoux/Rota/Roman-style theory.
No paper found (Browse 132 web research) with this specific
combination of shift and differential parts in the chromatic-QSF /
top-ρ context — Fact 8's operator form appears to be new.

## FPSAC 2027 framing consequence

Rick's algebraic-GF corner has two independent frames:

- **BM&J catalytic-variable side** (Bouvel's territory — invited talk,
  Browse 132): $F_P$ satisfies a functional equation of BM&J type;
  Riccati / ν-system structure → Theorem B (Day 170).
- **Umbral / shift-operator side** (Lascoux, Rota): $D_n$ has a
  compact closed operator form (Fact 8, Day 175). Algebraic skeleton
  on the **recursion-operator** side while BM&J is on the
  **functional-equation** side.

Both frames are absent from the immediate community (SW / Hikita /
Griffin-Mellit / Huh-Hwang all sit in Carlsson-Mellit or geometric
frames; Bouvel's methods have not yet been aimed at chromatic QSFs).

## Path-1 probe (Day 176 or later)

Is $D_n$ a **Hopf-algebra derivation + shift knob** on the divided-
power Hopf structure $\Delta(E_k) = \sum_i \binom{k}{i} E_i \otimes E_{k-i}$?
(Memory: `feedback_hopf_structure_picks_the_filtration.md` — divided-
power is the structure for which wt is coradical.)

If yes, Fact 8 becomes **the Hopf-algebraic skeleton of the Pieri
operator's top-ρ symbol on divided-power symmetric functions** —
which is a Path-1 statement, not just a Path-2 (β') statement.

30-min structural check: does $S$ satisfy $\Delta \circ S = (S \otimes 1)
\circ \Delta$ or similar? If so, Fact 8 gains Hopf-algebraic content.

## Files

- Day 175 proof: `proofs/2026-09-07-day175-fact8-closed-form-D.md`
- Day 174 proof (setup): `proofs/2026-09-06-day174-A-reduction-to-ODE.md`
- Day 174 triangle connection: `connections/2026-09-06-day174-ODE-triangle-collapse.md`
- Question status: `questions/q-claim-A-tops-in-Q123.md`
- Related feedback: `feedback_second_differences_reveal_shifts.md`
  (the $2^k$ second-difference fingerprint that pinned $d_k = 2^k + 2k - 1$).

## Status

**observation + reduction + closed form.** The four-face equivalence
is proved (§ above). What remains open is any ONE of (1)–(4) at general
$n$ — closing any one closes all four plus (A). Route A (verify EGF
solves rising ODE at general $n$) is the cleanest attack.

## Slogan

**A triangle of equivalences becomes a quadrilateral when the ODE's
right-hand-side operator itself has a compact closed form.** Day 174
found the ODE. Day 175 found the operator. The quadrilateral collapses
the whole E₂-shift arc into a single ~1-page algebraic-identity check.
