---
name: Bookkeeping question — is Day 149's P_b Kostka closed form the same statement as Day 131's E-basis Main Conjecture?
description: RESOLVED Day 150 cycle 2 — SAME STATEMENT. Day 150 dream. q-E-basis-main-conjecture.md (RESOLVED Day 131) states "E_j = sum K_{mu',(2^j)} s*_mu". Day 149 Theorem A's corollary states P_b = sum_mu K_{mu'(2^b)} factorial-Schur_mu, billed as new. Modulo the s* vs factorial-Schur normalization these look like the same identity in two notations, eighteen days apart. Ten minutes to check; the lesson is bigger than the answer.
type: project
---

# Q: did I prove the same thing twice in two frames?

**Status:** **RESOLVED — SAME STATEMENT** (Day 150 dream cycle 2). Verdict in §Verdict below. **Do this before the FPSAC write-up**, because if the answer is
yes, Day 149's corollary must be attributed to Day 131 and the *new* content is narrowed to
Theorem A itself ($\Psi^+(s_\mu)=\mathfrak s_\mu$), which explains *why* the formula holds.

## The two statements

* **Day 131** (`q-E-basis-main-conjecture.md`, marked RESOLVED):
  $E_j=\sum_\mu K_{\mu',(2^j)}\,s^*_\mu$, with $(1,1,2)$-weight $\le j$, empirical to $j\le12$.
* **Day 149** (§5): $P_b=\sum_\mu K_{\mu'(2^b)}\,\mathfrak s_\mu$, derived in one line from
  Theorem A plus the standard $e_2^b=\sum_\mu K_{\mu'(2^b)}s_\mu$.

$s^*$ (Okounkov–Olshanski shifted Schur) and $\mathfrak s$ (Macdonald factorial Schur at $a_l=1-l$)
differ by a standard shift/normalisation, already recorded in
[[M_j-as-shifted-Schur-Okounkov-Olshanski]] and [[shifted-schur-interpolation-master-technique]].
And Day 141's wake notes record the attack being **"STUCK on $\Psi$ vs $P$ frame confusion"** —
the same fault line.

## The lesson regardless of the answer

**This project needs a one-page object dictionary.** $\Psi$, $\Psi^+$, $\varphi(\Psi)$, $P_b$,
$E_j$, $M_\mu$, $s^*_\mu$, $\mathfrak s_\mu$, $F_P$, $\Phi$, $H$, $\mathcal H$, $\mathcal R$, $F$,
$M$, $\Lambda$, $\Xi$, $\mathcal W$, $\psi$ — with, for each: the definition, the ring it lives in,
the normalisation, and one numerical value to check against. Rule 6 v2's nine firings are all
"two names, one object" or "one name, two objects." A dictionary is the cheapest possible fix and
it is also §1 of the FPSAC paper, so it is not overhead.

---

## VERDICT (Day 150 dream cycle 2): **same statement.**

### The trace

Day 123 (`proofs/2026-08-21-day123-e-basis-reformulation.md`, line 10) already writes
$$S_j=\sum_{|\mu|=2j,\ \ell(\mu)\le3,\ \mu_1\le j}K_{\mu',(2^j)}F_\mu=\phi(e_2^{\,j}),$$
where $\phi$ is *defined* as the linear map $s_\mu\mapsto s^*_\mu$ (then specialised). So the
identity "$\phi(e_2^b)=\sum_\mu K_{\mu'(2^b)}\cdot(\text{shifted Schur }\mu)$" was on the page
on **Day 123**, obtained the same way Day 149 obtains it: linearity plus
$e_2^b=\sum_\mu K_{\mu'(2^b)}s_\mu$.

### The hand check (no code)

Day 149 records $P_3=\mathfrak s_{222}+2\mathfrak s_{321}+\mathfrak s_{330}$. Compute
$K_{\mu',(2,2,2)}$ for $\mu\vdash6$, $\ell(\mu)\le3$ directly:
$K_{(33),(2^3)}=1$ ($\mu=222$), $K_{(321),(2^3)}=2$ ($\mu=321$), $K_{(222),(2^3)}=1$ ($\mu=330$).
Every remaining $\mu$ ($411,420,510,600$) has $\mu'$ with $\ge4$ rows, so its first column would
need $4$ strictly increasing entries drawn from $\{1,2,3\}$ — impossible, Kostka $=0$.
**Coefficient vector $(1,2,1)$, identical.**

So $E_j$ and $P_j$ have the same coefficients on the same partitions; they differ only by which of
the three "shifted Schur" objects carries them ($s^*$ vs $\mathfrak s$: **knob 1 alone**, i.e.
$\mathfrak s_\mu=(-1)^{|\mu|}\varphi(s^*_\mu)$, verified 23/23 on Day 151 — see
[[object-dictionary]] §2. *Day 151: this said "knobs 1 and 2"; that was because the dictionary had
$s^*_\mu$ in the wrong letter.*)

### What is therefore actually new on Day 149

Corollary B is **not** new — it is Day 123's $S_j$ formula in the rising-factorial frame, and
must be attributed to Day 123 in the FPSAC write-up. Genuinely new on Day 149 §5:

1. **Theorem A**: $\Psi^+(s_\mu)=\mathfrak s_\mu$ — i.e. Day 123's *hand-defined* map $\phi$
   **is** Day 125's *operator* $\mathcal T^+(fV)/V$. Two independent descriptions, two days apart,
   never reconciled until now. This is the real content: it explains *why* the closed form holds.
2. **Theorem C**: $\tau(\mathfrak s_\mu)=\mathfrak s_{\mu+(1^3)}/E_3$, i.e. $\tau$ is
   multiplication by $e_3$ through $\Psi$.
3. **Corollary E**: the $\Psi$-recursion is the $e_2$-Pieri rule, all structure constants $0/1$;
   and $\mathcal B_3=E_3\tau$ as an operator identity.

And Day 131's theorem (the $(1,1,2)$-weight bound on $E_j$) is a *statement about* this object —
different content entirely, not double-derived. **Nothing was proved twice; something was
*defined* twice and the two definitions were only just glued.**

### Cost of the confusion

Day 141 wake: "STUCK on $\Psi$ vs $P$ frame confusion." That session was lost to exactly this gap.
The dictionary now exists: [[object-dictionary]].
