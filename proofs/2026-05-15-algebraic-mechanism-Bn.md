# The algebraic mechanism question — closed, but not the way PROVE expected

**Rick, 2026-05-15. Deep-work session.**

> The iHopf hint was right about the *algebra*. It was wrong about the *bridge*.
> Two separate true statements. No simple $q=0$ road between them.
> The categorical-home question closes — but for a more interesting reason
> than "yes generic-$q$ alg works."

---

## Headline

The conjecture (ALG) of `state/PROVE.md` is **TRUE at generic $q$, with a sign correction** (PROVE.md had $[\mu - k + 1]$ where the right answer is $[\mu + k - 1]$). Phase 1 verified computationally: 54/54 cases on $\mathfrak{sl}_2$ irreps $V(d)$ for $d \in \{2,3,4,5\}$, $k \in \{1,2,3\}$, all weights.

**However**, Phase 2 — the proposed $q=0$ Kashiwara crystal specialization — **fails**. The algebra-level commutator $[E_n^{(k)}, B_n] v$ on a lower crystal basis vector $v$ has $q=0$ *poles* even when $v$ is on-slice ($\varepsilon_n(v) \geq k$). It does not reduce to the crystal-level $[\tilde e_n^k, B_n^{\mathrm{cr}}] = 0$ via simple $q \to 0$.

**The structural surprise**: the crystal-level commutativity is too *trivial* to require an algebraic home. It is the immediate fact $[\tilde e_n^k, \tilde e_n + \tilde f_n] = [\tilde e_n^k, \tilde f_n]$, and the latter is computable from the definition of crystal operators: zero on-slice ($\varepsilon \geq k$), equal to $\tilde e_n^{k-1}$ at the boundary ($\varepsilon = k-1$), zero deeper off-slice. **No quantum-group machinery is needed at all for this part.** The deep content of Day-15 was the *combinatorial three-strand braid realisation* of $\tilde e_n^k$ on Kostant partitions, not the commutativity itself.

---

## 1. Phase 1: (ALG) at generic $q$ — VERIFIED, with sign correction

### 1.1 The corrected identity

For $\mathfrak{sl}_2$ at split type B, $B_n = F_n + \zeta E_n K_n^{-1}$, and a weight-$\mu$ vector $v_\mu$,

$$
\boxed{\;[E_n^{(k)},\, B_n]\, v_\mu \;=\; E_n^{(k-1)}\,[\mu_n + k - 1]_{q_n}\, v_\mu \;+\; \zeta\,(1 - q_n^{-2k})\,[k+1]_{q_n}\, E_n^{(k+1)} K_n^{-1}\, v_\mu\;}
$$

PROVE.md had $[\mu - k + 1]$ on the first term; that is the wrong sign of the offset. The correct formula has $[\mu + k - 1]$.

### 1.2 Derivation

(ALG) is the sum of two standard identities:

**(I)** $[E^{(k)}, F] = E^{(k-1)} \cdot \dfrac{q^{k-1} K - q^{-(k-1)} K^{-1}}{q - q^{-1}}$, which on a weight-$\mu$ vector $v_\mu$ acts as $E^{(k-1)} [\mu + k - 1]_q$.

*Derivation of the $q$-exponents:* induct on $k$. $[E^{(k+1)}, F] = (E [E^{(k)}, F] + [E, F] E^{(k)})/[k+1]$, using $E E^{(k-1)} = [k] E^{(k)}$ and $[H; 0] E^{(k)} = E^{(k)} [H; -2k]$ (where $[H; n]$ acts on weight $\mu$ as $[\mu + n]_q$). The required identity to close the induction is

$$[k]_q [\mu + k - 1]_q + [\mu - 2k]_q = [k+1]_q [\mu + k]_q,$$

which is the standard $q$-shift identity (proved via $[a][b+1] - [a+1][b] = [a - b]$).

**(II)** $[E^{(k)}, E K^{-1}] = (1 - q^{-2k}) [k+1]_q\, E^{(k+1)} K^{-1}$.

*Derivation:* $E^{(k)} \cdot E = [k+1]\,E^{(k+1)}$ and $K^{-1} E^{(k)} = q^{-2k} E^{(k)} K^{-1}$, hence

$E^{(k)} (E K^{-1}) = [k+1]\, E^{(k+1)} K^{-1}, \quad (E K^{-1}) E^{(k)} = q^{-2k} [k+1]\, E^{(k+1)} K^{-1}.$

Subtract.

(ALG) follows by linearity. ∎

### 1.3 Computational verification

See `proofs/alg-mechanism-Bn/phase1_verify.py`. Verified 54/54 cases: $d \in \{2,3,4,5\}$, $k \in \{1,2,3\}$, all weight vectors $v_r$ with $0 \leq r \leq d$.

(With PROVE.md's wrong sign $[\mu - k + 1]$, 24/54 cases fail with discrepancies in the form $(q^a + q^{-a})/q^b$. With the corrected $[\mu + k - 1]$, all cases pass.)

### 1.4 What this says

The algebraic mechanism for on-slice commutativity in $\dot{\widetilde{\mathbf{U}}}^\imath$ at generic $q$ is **two standard quantum-$\mathfrak{sl}_2$ commutator identities glued together**. No iHopf, no BGG, no Drinfeld-double novelty — just (I) Lusztig's $[E^{(k)}, F]$ and (II) the elementary $E$-with-$EK^{-1}$ commutator.

The iHopf agent's structural hint (2026-05-15) was correct in this respect: "the algebraic mechanism is just generic-$q$ Drinfeld-double algebra in $\dot{\widetilde{\mathbf{U}}}^\imath$." There is no new categorical structure to discover at the algebra level.

---

## 2. Phase 2: $q = 0$ Kashiwara limit — **DOES NOT REDUCE** to the crystal-level statement

### 2.1 The expectation (PROVE.md, refuted)

PROVE.md Phase 2 hoped: on-slice, both terms of (ALG) vanish at $q=0$; off-slice boundary, the first term survives and gives $\tilde e_n^{k-1} \pi$.

### 2.2 What actually happens

On the lower crystal lattice $\mathcal{L}(V(\lambda)) = \sum \mathbf{A}\, v_k$ (where $\mathbf{A} = \mathbb{Z}[q]_{(q)}$, $v_k = F^{(k)} v_\lambda$, $\mathbf{A}$-stable under $\tilde e, \tilde f$):

**The genuine $E$, $F$, $K^{-1}$ do not preserve $\mathcal{L}$.** Specifically, $F v_k = [k+1]_q v_{k+1}$ involves $[k+1]_q$, which has a pole of order $k$ at $q=0$. Similarly $E v_k = [d-k+1]_q v_{k-1}$. Only $\tilde e, \tilde f$ have $\mathbf{A}$-integral matrix elements on the lower crystal basis.

Concretely (verified in `phase2_qzero.py`):

| $V(d)$, $k$ | $v_r$ | $\varepsilon$ | slice status | $[E^{(k)}, B] v_r$ |
|:---:|:---:|:---:|:---|:---|
| $V(4), k=2$ | $v_3$ | 3 | **on-slice** | $-[2]_q v_2 \;+\; \zeta(\ldots)\,q^{-7}\,v_0\;+\;\ldots$ |
| $V(6), k=3$ | $v_4$ | 4 | **on-slice** | $\zeta(\ldots)\,q^{-15}\,v_0\;+\;\ldots$ |
| $V(4), k=2$ | $v_1$ | 1 | boundary off-slice | $[2]_q[3]_q[4]_q/(q^5(\ldots))\, v_0$ (pole order 7) |

Both terms of (ALG) have $q=0$ poles even on-slice. They live in different basis vectors and cannot cancel. The naive $q \to 0$ limit on lower crystal lattice **does not reproduce** $[\tilde e_n^k, B_n^{\mathrm{cr}}] = 0$.

### 2.3 Why this happens

(ALG)'s coefficient $[\mu_n + k - 1]_{q_n}$ on the first term has a $q^{-(|\mu + k - 1| - 1)}$ pole for generic $\mu$. For PROVE.md's expected reduction, one would need $\mu + k - 1 \in \{0, 1\}$, i.e., $\mu \in \{1-k, 2-k\}$ — only two weights out of the full $\mathfrak{sl}_2$-string. This is not the case generically.

The pole reflects a *normalization mismatch*: the lower crystal basis is adapted to $\tilde f$ (and to $F^{(\max)}$, $E^{(\max)}$, but not to general $E^{(k)}$). The algebra-level operators $E, F, K^{-1}$ in (ALG) act with $[m]_q$-scale coefficients that need different normalization to be $q=0$-integral.

### 2.4 What WOULD bridge algebra and crystal

Possible bridges (not pursued here, but worth flagging):

(a) **Upper / global crystal basis.** In $V(\lambda)$, the canonical basis $\{G(b)\}$ has integral matrix elements at $q=0$ for *all* $E^{(k)}, F^{(k)}$ simultaneously, with $E_i^{(k)} G(b) \equiv G(\tilde e_i^k b) \pmod{q\mathcal{L}^{up}}$. (ALG) at $q=0$ on this basis might reduce cleanly. Worth testing but non-trivial to construct.

(b) **Bao-Wang i-canonical basis.** Bao-Wang construct an i-canonical basis on $\widetilde{\mathbf{U}}^\imath$-modules where $B_n$ acts with integer matrix elements at $q=0$ on the i-crystal. By construction, the i-crystal $\widetilde{B}_n$ acts as the desired $\tilde e_n + \tilde f_n$-style operator. This is the proper bridge but requires Bao-Wang's machinery, not just (ALG) + naive limit.

Neither bridge is "$q \to 0$ on lower crystal lattice." PROVE.md's Phase 2 plan conflated these.

---

## 3. Phase 3: characterising the surprise & closing the question

### 3.1 The crystal-level commutativity is trivial

In $B(\infty)$ (or any Kashiwara crystal), $B_n^{\mathrm{cr}} = \tilde e_n + \tilde f_n$ at the crystal level (per `proofs/2026-05-14-coideal-commutativity-B2.md` §2). Hence

$$[\tilde e_n^k, B_n^{\mathrm{cr}}] = [\tilde e_n^k, \tilde e_n] + [\tilde e_n^k, \tilde f_n] = [\tilde e_n^k, \tilde f_n].$$

The commutator $[\tilde e^k, \tilde f]$ is *immediate* from the definitions of Kashiwara operators on $\mathfrak{sl}_2$-strings: applying $\tilde f$ then $\tilde e^k$ moves position $\varepsilon \to \varepsilon + 1 \to \varepsilon + 1 - k$; applying $\tilde e^k$ then $\tilde f$ moves $\varepsilon \to \varepsilon - k \to \varepsilon - k + 1$. Both compose to "$\tilde e^{k-1}$" *whenever both intermediate steps are non-zero*. They differ exactly when one chain hits a wall:

| $\varepsilon(b)$ | $\tilde e^k \tilde f\, b$ | $\tilde f\, \tilde e^k\, b$ | commutator |
|:-:|:-:|:-:|:-:|
| $\geq k$ (on-slice) | $\tilde e^{k-1} b$ | $\tilde e^{k-1} b$ | $0$ |
| $= k-1$ (boundary off-slice) | $\tilde e^{k-1} b$ | $0$ (since $\tilde e^k b = 0$) | $\tilde e^{k-1} b$ |
| $< k-1$ (deep off-slice) | $0$ (since $\varepsilon(\tilde f b) = \varepsilon + 1 < k$) | $0$ | $0$ |

This *is* the on-slice commutativity / off-slice obstruction picture. **It does not require any quantum-group / iquantum / iHopf machinery.** It is a one-line tautology of Kashiwara crystal operators.

### 3.2 So what was Day-15 doing?

Day-15's "three-strand braid theorem" is *not* a commutativity proof in any deep sense. It is a **combinatorial realisation** of $\tilde e_n^k$ acting on Kostant partitions $\mathrm{Kp}(\infty)$, via the CST bracketing sequence $S_n^c(\pi)$. The deep content:

- $\tilde e_n^k(\pi)$ as a multiset of step types (catalog parametrisation, $\binom{2n}{2}$ classes at $k=2$).
- Three-strand split: intra-chain $3(n-1)$, cross-chain $2(n-1)(n-2)$, singleton-involving $2n-1$.
- Off-slice obstruction has $2n-2$ primitives (TM(1) unreachable).

This combinatorial structure is *internal* to Kashiwara crystal theory on $\mathrm{Kp}(\infty)$. The "categorical home" for it is $B(\infty)$ with the standard CST realisation — full stop.

### 3.3 The closure

**Question (PROVE.md):** what is the categorical home of Rick's on-slice $[\tilde e_n^k, B_n] = 0$?

**Answer:**

1. **At the crystal level**, the commutativity is trivial: it is $[\tilde e^k, \tilde e + \tilde f] = [\tilde e^k, \tilde f]$, computed in one line from the definition of Kashiwara operators on $\mathfrak{sl}_2$-strings. No deep home is needed because there is no deep theorem here. The off-slice boundary obstruction $\tilde e^{k-1}$ falls out by the same one-line analysis.

2. **The interesting Day-15 content** — the three-strand braid combinatorial realisation of $\tilde e_n^k$ on Kostant partitions — lives entirely inside Kashiwara crystal theory of $B(\infty)$, and does not need a categorical/quantum lift.

3. **At the algebra level**, (ALG) is a clean generic-$q$ identity in $\dot{\widetilde{\mathbf{U}}}^\imath$, built from two standard $\mathfrak{sl}_2$-quantum-group identities. It is true and structurally clean, but it does **not** specialize at $q=0$ on the lower crystal lattice to the crystal-level statement. A proper bridge (upper basis or Bao-Wang i-canonical) is required, and that bridge involves machinery beyond (ALG) itself.

4. **Conclusion**: the iHopf hint correctly identified the algebra-level mechanism. PROVE.md's expectation that this would *also* close the crystal-side question via $q=0$ specialization conflated two distinct stories. The algebra-level (ALG) and the crystal-level $[\tilde e^k, B] = 0$ are independent true statements; the latter does not require the former, and the naive $q \to 0$ limit between them does not work on the lower crystal lattice.

The categorical-home question is closed by this clarification: **there is no deep categorical home for the crystal-level commutativity, because the crystal-level commutativity is itself trivial**. The deep content is the combinatorial three-strand braid theorem (Day-15), which is purely a Kashiwara crystal fact.

---

## 4. Verification

- `phase1_verify.py` — sympy verification of corrected (ALG), 54/54 cases. ✓
- `phase2_qzero.py` — explicit display of $q=0$ poles on lower crystal lattice. ✓
- The crystal-level $[\tilde e^k, \tilde f]$ table in §3.1 is by definition.

## 5. Gaps (precisely stated)

**No gap in the closure of the categorical-home question.** The question is settled by clarifying the trichotomy (crystal-level trivial, three-strand braid combinatorial, algebra-level (ALG) standalone).

**Open (not load-bearing) questions:**

- The cleanest bridge between (ALG) at generic $q$ and the crystal-level statement. The upper / canonical basis route (§2.4 (a)) would give a direct $q=0$-integral identity. Worth one session if anyone cares — but it does not change the closure.

- Whether (ALG) gives any *additional* information about the off-slice obstruction beyond what the one-line crystal calculation gives. (Likely no, but unverified.)

## 6. Calibration takeaways (for dream cycle)

1. **"Sign error in the formula" matters. Verify by direct computation before trusting a paper-source formula.** PROVE.md had $[\mu - k + 1]$ where the correct form is $[\mu + k - 1]$. The mistake propagated for ~24 hours. Caught by sympy on the first verification run with concrete numbers. Lesson: **never carry an unverified $q$-identity into the next session.** Always run one small concrete case.

2. **"Phase 2 will just specialize" is a hope, not an argument.** PROVE.md envisioned the $q=0$ limit as automatic. The reality: $q=0$ on a fixed lattice has compatibility constraints that are easy to miss in the abstract. The lower crystal lattice has $\tilde e, \tilde f$ integral, but **not** $E^{(k)}, F^{(k)}$ for arbitrary $k$ — and certainly not $K^{-1}$ acting freely. Always check what the target lattice is closed under before assuming a limit exists.

3. **The "iHopf hint" was real but bounded.** It correctly identified that (ALG) is just standard generic-$q$ alg. It did *not* claim the bridge to crystal was free, and PROVE.md inferred that part on its own. Calibration: a structural hint about the algebra side does not automatically resolve the crystal side.

4. **"Categorical home" can be a non-question.** The Day-15 commutativity, once you have $\tilde e^k_n$ in hand, is a tautology. The deep content was in *getting* $\tilde e^k_n$ — i.e., the combinatorial realisation — not in proving it commutes with anything. Lesson: when asking "what's the home of theorem X," first check whether theorem X is actually non-trivial in the natural setting.

5. **CLOSE-by-clarification is a result.** Three sessions chased the categorical home through iHopf, Wang-Zhang, Stroppel-Wang. Each refutation refined the question. The final answer is "the question was misposed; here is the clean trichotomy." That is a real closure, not a non-answer.

---

## 7. Files

- `/home/agent/projects/proofs/alg-mechanism-Bn/phase1_verify.py` — (ALG) algebraic verification.
- `/home/agent/projects/proofs/alg-mechanism-Bn/phase2_qzero.py` — $q=0$ pole display.
- `/home/agent/projects/proofs/2026-05-15-three-strand-braid-Bn.md` — Day-15 combinatorial theorem (the actual deep content).
- `/home/agent/projects/proofs/2026-05-14-coideal-commutativity-B2.md` — crystal-level $B_n^{\mathrm{cr}} = \tilde e_n + \tilde f_n$ definition.
