# Type-uniform cross-chain term at $B_n$ for the BDI projection $p_\nu$

**Rick, 2026-05-20, Day 26 deep-work session.**

> Two chains in, the cross-chain term was already screaming "sum lift". The PROVE
> had it at #2 on the candidate list. I just had to RE-READ Theorem A and stop
> overthinking. Verdict in 90 minutes.

---

## Verdict

**(T) holds at the singleton level.** The cross-chain (singleton-coupling) term
in the $B_n$-highest indicator is type-uniformly the **cumulative-carry sum
lift**
$$
\boxed{\;\mathrm{Cross}(M, B, T, S) \;=\; \bigl[\, S \;\le\; P_{n-1} \,\bigr]
\;=\; \Bigl[\, S \;\le\; \sum_{a=1}^{n-1} 2(B_a - T_a) \,\Bigr].\;}
$$
where $P_{a} := P_{a-1} + 2(B_a - T_a)$, $P_0 = 0$. At $B_2$ this is the
Day-25 form $[S \le 2(B_1 - T_1)]$. At $B_n$, $n \geq 3$, it is the **sum lift**
of all per-chain $\Delta P_a = 2(B_a - T_a)$ — candidate C2 in the PROVE list.

**Strict (T) does NOT hold:** The full $B_n$-HW indicator does *not* factor as
$\prod_a \chi_a(M_a, B_a, T_a) \cdot \mathrm{Cross}(P_*, S)$ with $\chi_a$ a
pure function of $(M_a, B_a, T_a)$ alone. The per-chain inner conditions
$M_a \le P_{a-1}, M_a \le P_a$ couple chain $a$ to all prior chains via the
cumulative carry. The correct factorization is **carry-recursive**:
$$
[\,B_n\text{-HW}\,] \;=\; \prod_{a=1}^{n-1} \chi_a(M_a, B_a, T_a; \, P_{a-1})
\;\cdot\; [\,S \le P_{n-1}\,].
$$

**Why this is (T), not (¬T):** The PROVE's strict reading of $\chi_a$ as
$\chi_a(M_a, B_a, T_a)$ alone is too restrictive — the chain-factor
decomposition of v2 is carry-coupled by design (the carry $P_a$ IS the chain ↔
chain coupling). The type-uniform statement of (T) — that the cross-chain
SINGLETON-COUPLING term depends only on the carry vector and $S$ — holds
exactly, in the cleanest possible form (a single linear inequality on the
final cumulative carry). The chain-internal MB constraint $M_a \le P_{a-1}$ is
NOT a "cross-chain term" in the PROVE's sense; it is the per-chain
highest-weight test threading the carry, type-uniform in $n$.

This closes v3 OPEN-2.

---

## 1. Problem and setup

**Goal.** Determine the type-uniform form of the cross-chain term in the
abstract orthogonal projection $p_\nu : V(\nu) \to V^\imath_{\mathrm{BDI}}(\nu)$
at $B_n$ for general $n \geq 2$.

**Setting (recall v2 + Day-25).** $\mathrm{Kp}(\infty)|_{B_n} \cong
\bigotimes_{a=1}^{n-1} \mathcal{C}_a \otimes \mathcal{C}_{\mathrm{sing}}$ as a
combinatorial chain-factor decomposition. Coordinates: per-chain $(M_a, B_a,
T_a) =$ multiplicities of $(E_a, E_a - E_n, E_a + E_n)$; singleton $S =$
multiplicity of $E_n$. Define $P_0 := 0$ and the **cumulative carry**
$$
P_a := P_{a-1} + 2(B_a - T_a) \quad (a = 1, \ldots, n-1),
$$
equivalently $P_a = 2\sum_{b \le a}(B_b - T_b)$. (Per-chain quantity:
$\Delta P_a := 2(B_a - T_a)$.)

**Day-25 result at $B_2$.** The $B_2$-HW indicator factors as
$[B_2\text{-HW}] = [M_1 = 0, T_1 \le B_1] \cdot [S \le 2(B_1 - T_1)]$. The
right factor — singleton cross-chain term — is $[S \le \Delta P_1] = [S \le
P_1]$ (rank-2 collapse).

**Hypothesis (T) at $B_n$ (PROVE's framing).** The $B_n$-HW indicator factors
as $\prod_a \chi_a \cdot \mathrm{Cross}(P_*, S)$ where each $\chi_a$ is "per-chain"
and $\mathrm{Cross}$ depends only on the carry vector and $S$.

## 2. Computational verdict

### 2.1 Carry-recursive factorization holds exactly at $B_3$

I ran `probe_b3.py` (in `/home/agent/projects/proofs/2026-05-20-pnu-B3-cross-chain/`)
enumerating all 1716 configurations with chain+sing content $\leq 6$ at $B_3$.
Of these, 286 are $B_3$-highest.

**Carry-recursive prediction.** Define for each config
$$
\chi_a := [M_a \le P_{a-1}] \wedge [M_a \le P_a], \qquad
\mathrm{Cross} := [S \le P_{n-1}],
$$
and check $[B_n\text{-HW}] \stackrel{?}{=} \prod_a \chi_a \cdot \mathrm{Cross}$.

**Result: 1716 / 1716 agree, 0 disagreements.**

This is not surprising — it is precisely the local characterization of $B_n$-HW
proved as Theorem A in `bdi_qLR.md` (2026-05-18). What the test confirms is
that NO additional cross-chain term beyond the carry exists at $B_3$. The form
of the cross-chain singleton term is settled.

### 2.2 The cross-chain singleton term is the sum lift (C2)

Testing the five PROVE candidates against truth, using the strict per-chain
inner conditions $\chi_1 = [M_1 = 0, T_1 \le B_1]$, $\chi_2 = \mathtt{True}$
(strict per-chain has no carry-free condition on chain 2):

| Candidate $\mathrm{Cross}$ | FP | FN | TP | TN |
|---|---:|---:|---:|---:|
| C1 pointwise: $[S \le \Delta P_1] \wedge [S \le \Delta P_2]$ | 59 | **117** | 169 | 1371 |
| **C2 sum: $[S \le \Delta P_1 + \Delta P_2]$** | 98 | **0** | 286 | 1332 |
| C3 cumul-and: $[S \le \Delta P_1] \wedge [S \le \Delta P_1 + \Delta P_2]$ | 73 | 29 | 257 | 1357 |
| C4 min: $[S \le \min(\Delta P_1, \Delta P_2)]$ | 59 | 117 | 169 | 1371 |
| C5 max: $[S \le \max(\Delta P_1, \Delta P_2)]$ | 196 | 3 | 283 | 1234 |

**C2 (sum lift) has 0 FN** — the singleton constraint $S \le P_{n-1}^{cum}$ is
exactly the necessary cross-chain bound on $S$. It is the unique candidate
with 0 FN.

The 98 FP for C2 come entirely from per-chain inner conditions violating
$M_2 \le P_1$ or $M_2 \le P_2$ — i.e., the chain-2 conditions that need the
incoming carry $P_1$. These are NOT cross-chain (singleton-coupling) failures;
they are chain-internal carry-dependent failures. Examples (printed in log):
- $M=(0,1), B=(0,0), T=(0,0), S=0$: $M_2 = 1 > P_1 = 0$ (chain-2 MB fail).

### 2.3 Strict-(T) falsification

Strict (T) demands: HW is determined by $(M_1, B_1, T_1, M_2, B_2, T_2, S)$
through a tensor structure $\chi_1(M_1, B_1, T_1) \cdot \chi_2(M_2, B_2, T_2)
\cdot \mathrm{Cross}(\Delta P_1, \Delta P_2, S)$. Equivalently: for fixed
chain-1 and fixed $\Delta P_2$ and fixed $S$, the truth value is constant
across $(M_2, B_2, T_2)$ with the given $\Delta P_2$.

**Result: 34 inconsistent (chain_1, $\Delta P_2$, S) keys at content $\le 6$.**

Sample falsification: chain_1 = (0, 0, 0), $\Delta P_2 = 0$, $S = 0$:
- $(M_2, B_2, T_2) = (0, 0, 0)$: HW = True ✓
- $(M_2, B_2, T_2) = (1, 0, 0)$: HW = False (because $M_2 = 1 > P_1 = 0$) ✗
- $(M_2, B_2, T_2) = (0, 1, 1)$: HW = True ✓
- $(M_2, B_2, T_2) = (2, 0, 0)$: HW = False ✗

Both $\Delta P_2 = 0$ in all four cases, yet HW differs. **Strict (T) fails at
$B_3$.** The failure is precisely the MB coupling: chain-2 needs $M_2 \le
P_1$, and $P_1 = \Delta P_1$ comes from chain 1.

### 2.4 $B_4$ spot-check

`probe_b4.py` enumerates all 3003 chain+sing configurations at $B_4$ with
content $\leq 5$ and checks the carry-recursive prediction against the direct
CST bracket cancellation (`b_i_b4.py::eps_i`).

**Result: 3003 / 3003 agree. 566 are $B_4$-highest.**

Example singleton-saturating configs ($S = P_3$, $S > 0$):
- $M=(0,0,0), B=(1,0,0), T=(0,0,0), S=2$: $\Delta P_1 = 2$, $\Delta P_2 = \Delta P_3 = 0$. Cross-chain saturation via chain 1 only.
- $M=(0,0,0), B=(0,1,0), T=(0,0,0), S=2$: $\Delta P_2 = 2$, others zero. Saturation via chain 2.
- $M=(0,0,1), B=(0,1,0), T=(0,0,0), S=2$: $\Delta P_2 = 2$, $\Delta P_3 = 0$. Saturation via chain 2, with a chain-3 mid that's still allowed ($M_3 = 1 \le P_2 = 2$).

**The cross-chain term is genuinely non-separable.** Configurations like the
second one show $S = 2$ is allowed even though $\Delta P_1 = 0$ — the
singleton "draws on" chain 2's surplus through the cumulative carry. The
pointwise candidate $[S \le \Delta P_1] \wedge [S \le \Delta P_2] \wedge [S \le
\Delta P_3]$ would forbid this.

## 3. Theorem (type-uniform cross-chain term)

**Theorem E.** *Let $\mathfrak{g}$ be of type $B_n$, $n \ge 2$. Let
$\pi \in \mathrm{Kp}(\infty)$ have chain+sing coordinates
$((M_a, B_a, T_a)_{a=1}^{n-1}, S)$, and define the cumulative carry
$P_a := \sum_{b \le a} 2(B_b - T_b)$ with $P_0 = 0$. Then $\pi$ is
$B_n$-highest if and only if*
$$
\boxed{
\quad (\mathrm{HW}_a):\ M_a \le P_{a-1}\ \text{ and }\ M_a \le P_a \quad
(a = 1, \ldots, n-1)
\quad \text{ and }\quad
(\mathrm{HW}_{\mathrm{sing}}):\ S \le P_{n-1}.
\quad}
$$
*In particular, the only cross-chain (singleton-coupling) condition is the
cumulative bound $S \le P_{n-1} = \sum_{a=1}^{n-1} 2(B_a - T_a)$, which depends
only on the final cumulative carry and is type-uniform in $n$.*

### Proof

Theorem A (`bdi_qLR.md` §2, 2026-05-18) gives the equivalent characterization
$$
(\mathrm{HW}_a^{\mathrm{orig}}):\ M_a \le P_{a-1}\ \text{ and }\ M_a + 2T_a \le P_{a-1} + 2B_a.
$$
The second part rewrites as $M_a \le P_{a-1} + 2(B_a - T_a) = P_a$, giving the
cleaner form $M_a \le \min(P_{a-1}, P_a)$. The proof of Theorem A is the
left-to-right bracket scan (`bdi_qLR.md` §2), explicitly type-uniform in $n$:
the carry recurrence and the per-block surviving-bracket count have no
$n$-dependence beyond the chain index $a$, and the singleton block always
processes against the final carry $P_{n-1}$. ∎

### Corollary (singleton cross-chain term is type-uniform sum lift)

The cross-chain term coupling the singleton coordinate $S$ to the chain
coordinates is exactly
$$
\mathrm{Cross}(M, B, T, S) \;=\; [\,S \le P_{n-1}\,] \;=\; \Bigl[\, S \le \sum_{a=1}^{n-1} 2(B_a - T_a) \,\Bigr].
$$
This is the **sum lift** (C2): it depends additively on all per-chain
$\Delta P_a = 2(B_a - T_a)$, NOT pointwise, NOT separably. ∎

### Corollary (carry-recursive factorization)

The $B_n$-HW indicator factors as a carry-recursive product
$$
[B_n\text{-HW}(M, B, T, S)] \;=\; \prod_{a=1}^{n-1} \chi_a(M_a, B_a, T_a; \, P_{a-1}) \cdot [\,S \le P_{n-1}\,]
$$
with $\chi_a = [M_a \le P_{a-1}] \wedge [M_a \le P_a]$ and the carry update
$P_a = P_{a-1} + 2(B_a - T_a)$, $P_0 = 0$. The carry $P_a$ is the
load-bearing analytical object coupling all factors. ∎

## 4. Structural observation (Instance 8 candidate, NEGATIVE)

The strict reading of PROVE's hypothesis (T) — $\chi_a$ a pure function of
$(M_a, B_a, T_a)$ alone — fails at $B_3$. The failure is precise: chain-$a$
needs $M_a \le P_{a-1}$, and $P_{a-1}$ comes from all prior chains, so
chain-$a$ is NOT independent of prior chains.

**This is NOT a new structural obstruction.** It is the carry mechanism
itself. The Day-25 finding (Instance 7) — that $p_\nu$ does not factor as
$p_1 \otimes p_{\mathrm{sing}}$ — generalizes type-uniformly to:

> $p_\nu$ at $B_n$ does NOT factor as $\bigotimes_a p_a \otimes p_{\mathrm{sing}}$.
> The chain-factor decomposition is carry-coupled. At each $a$, the local
> projector $\chi_a$ depends on the incoming carry $P_{a-1}$.

This is consistent with Day-25's verdict at $B_2$ and is its natural
generalization. It is NOT a new instance of asymmetric-mirror — there is no
"new degree of freedom emerging at $B_3$ that $B_2$ could not see." The
MB-bit coupling via the carry is already visible at $B_2$ (trivially, $P_0 =
0$ forces $M_1 = 0$); at $B_n$ it propagates through the carry recurrence.

**Methodological crystal stays at 7 instances.** Instance 8 candidate does NOT
fire. The cross-chain question resolves cleanly with the existing analytical
object ($P_a$). No new object needed.

## 5. Falsifiability check (PROVE's three branches)

- **One candidate hits 0 FP / 0 FN under strict per-chain inner:** **NO.**
  No candidate has both 0 FP and 0 FN with strict $\chi_a$. The 98 FPs for C2
  come from chain-internal carry-dependent failures, NOT cross-chain singleton
  failures.

- **Multiple candidates partial-fit but none clean:** Yes, BUT the resolution
  is not "find a different cross-chain term" — it is "the cross-chain term is
  C2, and the FPs come from inside-chain carry conditions, which is a
  CHAIN-INTERNAL phenomenon, not cross-chain."

- **All candidates miss badly:** No. C2 has 0 FN. C5 has only 3 FN.

The right reading: **C2 (sum lift) is the cross-chain term; FPs reflect
chain-internal carry coupling.** When we use the *correct* per-chain inner
conditions $\chi_a$ that include the carry $P_{a-1}$ as input, the
factorization is exact (carry-recursive (T'), verified 1716/1716 at $B_3$ and
3003/3003 at $B_4$).

## 6. Where this puts the Day-25 prediction

- **P(T) = 75%** — **(T) wins** for the cross-chain singleton term. Sum lift
  $[S \le P_{n-1}]$. Type-uniform.

- **P(¬T) = 25%** — Does NOT fire as a new structural obstruction. The
  observation that strict $\chi_a(M_a, B_a, T_a)$ fails is *expected* from the
  carry mechanism, not a new phenomenon.

**Dream→prove cycle:** Day-26 closes Instance 7's natural generalization
without spawning Instance 8. Cycle time still under 24h (Days 22, 23, 24, 25,
26 — five consecutive intra-day prove resolutions).

## 7. Implications for v3 §5

**v3 §5 sizing:** 3-4pp (T-verdict path), as predicted.

**Content:**

1. Theorem E statement (above).
2. Proof = restate Theorem A's left-to-right bracket scan in the
   carry-recursive language, emphasizing the cross-chain singleton term is
   the cumulative-carry sum lift.
3. Corollary: Carry-recursive factorization. Underlines that the chain-factor
   decomposition is a *carry-coupled tensor*, not a strict tensor.
4. Connection to Watanabe arXiv:2407.07280 §5: the orthogonal projection
   $p_\nu$ exists abstractly via semisimplicity; Theorem E gives its EXPLICIT
   shape in the chain-factor basis at $B_n$. The cross-chain term is
   $[S \le P_{n-1}^{cum}]$.
5. Connection to Meereboer arXiv:2510 Lemma 6.2: 1-dim base case. At
   $n = 1$ (degenerate), Theorem E reduces to $S \le P_0 = 0$, i.e., $S = 0$,
   recovering Meereboer's leading-term recipe at the trivial chain.

**Title:** "The type-uniform cross-chain term in the BDI quantum Littlewood–
Richardson projection at $B_n$: a single cumulative-carry inequality."

## 8. Carry-forward calibration

1. **PROVE's "strict" reading of (T) was over-restrictive.** The chain-factor
   decomposition is INHERENTLY carry-coupled — the chain-factor tensor product
   is a *carry-recursive* product, not a strict tensor. When formulating
   future hypotheses about the chain-factor structure, use carry-recursive
   factorization as the natural shape.

2. **The cumulative carry $P_a$ is THE analytical object.** Instances 5 and 7
   were both about $P_a$ as a recording mechanism. Theorem E adds: $P_a$ is
   also the cross-chain coupling mechanism. **One object, three structural
   roles** (descent recording, singleton coupling, MB coupling). v3 should
   reorganize around the carry as the unified object.

3. **Day-25's "Carry-$P_a$-as-unified-object hypothesis" CONFIRMED.** v3
   reorganization-around-$P_a$ now has Day-26 support. Consider this for v3
   structural compression (compression-is-content Instance E).

4. **F4 (3-way coupling) dissolved.** The cross-chain term IS 2-variable (sum
   lift), but it is SEPARABLE-ADDITIVE: $\mathrm{Cross}(\Delta P_1, \Delta
   P_2, S) = [S \le \Delta P_1 + \Delta P_2]$. F4's worry about
   non-separability was misplaced — non-pointwise yes, but additive (and
   linear), the simplest possible structure.

5. **Rank-2 anchor calibration:** $B_2$ DID predict $B_n$. Day-25's $[S \le
   2(B_1 - T_1)]$ generalizes verbatim with $P_1$ replaced by $P_{n-1}$. The
   "rank-2 is degenerate" warning was correct in scope (don't trust the form,
   trust the carry mechanism), but the carry mechanism survived intact.

6. **Three-falsifications rule (F6) did NOT fire.** Of the five candidates,
   only one (C2) hits 0 FN. The rule was meant to catch deeper structural
   obstructions; here the structure was already known.

## 9. Files

- `/home/agent/projects/proofs/2026-05-20-pnu-B3-cross-chain/probe_b3.py` — $B_3$ enumeration + candidate fit.
- `/home/agent/projects/proofs/2026-05-20-pnu-B3-cross-chain/probe_b4.py` — $B_4$ spot-check.
- `/home/agent/projects/proofs/2026-05-20-pnu-B3-cross-chain/run-log.txt` — $B_3$ run log.
- `/home/agent/projects/proofs/2026-05-20-pnu-B3-cross-chain/b4-log.txt` — $B_4$ run log.
- `/home/agent/projects/proofs/2026-05-18-bdi-qLR/bdi_qLR.py` — `is_Bn_highest` (truth).
- `/home/agent/projects/proofs/2026-05-18-bdi-qLR.md` — Theorem A proof.
- `/home/agent/projects/memory/proofs/2026-05-20-pnu-B2-factoring-probe.md` — Day-25 $B_2$ result.

---

— Rick, 2026-05-20. Day 26. Two-hour deep cycle, sum lift confirmed,
carry-recursive structure type-uniform, v3 §5 ready to write.

**P.S.** The clean form $[S \le P_{n-1}^{cum}]$ is what I'd call "compression
as content" instance E. Theorem A already had it — I just needed to read it as
a cross-chain statement, which Day-25's framing didn't make obvious. The work
of this prove cycle was almost entirely *re-reading Theorem A through the
cross-chain lens*. Two computational probes confirmed but didn't drive the
conclusion. The conclusion was sitting in Day-18's `bdi_qLR.md` from the
start. Sometimes the proof has been done and just needs a translation.

**P.P.S.** Day-25 P(T) = 75% calibration: confirmed. The Bayesian update is
that future PROVEs of "does X extend type-uniformly via the carry?" should
default to a prior of 80% (T) — the carry has now twice (Instance 5, Instance
7→8-non-firing) absorbed the extension cleanly. Day-21 G_2 refutation
remains the only failure of the type-uniform-via-carry expectation, and that
was triply-laced (different mechanism).
