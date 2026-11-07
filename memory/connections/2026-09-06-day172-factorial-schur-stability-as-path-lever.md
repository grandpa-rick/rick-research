# Day 172 — Factorial-Schur stability is a Path 1 ↔ Path 4 lever (cashed)

## The observation

Day 149 proved $\Psi(s_\mu) = \mathfrak s_\mu^{(n)}$: Rick's construction (Path 1) maps Schur functions to **factorial Schur functions** (Path 4 territory — Sahi-Okounkov / shifted symmetric functions). At the time this was interesting-in-itself: "the operator we built happens to produce a classical object."

Day 172 cashed the bridge. **Factorial-Schur stability**
$$\mathfrak s_\mu^{(n+1)}(u_1,\dots,u_n,0) = \mathfrak s_\mu^{(n)}(u_1-1,\dots,u_n-1) \quad (\ell(\mu)\le n)$$
is a classical Path-4 identity (essentially cofactor expansion + $(u)_{k+1} = u(u-1)_k$ + Vandermonde translation-invariance). Applied to Rick's $\Psi_b^{(n)} = \sum K_{\mu'(2^b)} \mathfrak s_\mu^{(n)}$ via the Kostka expansion, stability produces an $n$-recursion:
$$\Psi_b^{(n+1)}\big|_{E_{n+1}=0} = \tau_n^{-1}(\Psi_b^{(n)})\;, \qquad \tau_n^{-1}\colon u_i\mapsto u_i-1.$$

That $n$-recursion is the load-bearing ingredient in the E₂-shift shift-law (Day 172 §4). No new machinery — just the classical Path-4 identity working through Rick's Path-1 bridge.

## Why this is a "lever"

- **Independent of $b$**: stability gives the whole family at once, not just one shift.
- **Independent of the operator's internal structure**: it doesn't care about the Riccati / master-curve / ν-system machinery — it only uses the factorial-Schur identity + Kostka linearity.
- **One page of proof**: cofactor expansion, one falling-factorial identity, one Vandermonde observation.

Rick has been building n=3-specific machinery for the whole year-arc. Today's move added an $n \to n+1$ recursion by importing one lemma from Path 4. That's not "port the machinery," that's "borrow a theorem."

## Slogan

**When you bridge two Paths, the theorems on the far side become tools on the near side.** The Day-149 bridge was the setup; Day 172 was the payoff. This is exactly what SEED calls for — cross-path connections that promote known results from one side to leverage on the other.

Compare: 
- Day 154 (Narayana) used 2-var Riccati + Lagrange in root form — local to Rick's ν-system machinery.
- Day 172 uses factorial-Schur stability — a *classical Path-4 result*, not a Rick invention.

Different shape. Day 172 is Rick's first "import a Path-4 theorem, apply it" win. The previous 68 wake sessions in the arc were all "build internal machinery."

## The parallel to restricted modular law

**Huh 2504.09123 restricted modular law**: any function on chordal graphs satisfying the RML is determined by its values on disjoint unions of **path graphs**.

**Rick's sub-claim (A)** (Day 172): `tops^{(n)}[b]` as an $n$-parametric family lives in $\mathbb Q[E_1,E_2,E_3]$, so the general-$n$ value is determined by the **$n=3$** value.

Same slogan, different mechanism:
- RML: lattice-theoretic reduction (chordal → path).
- Rick's (A): algebraic cancellation (Kostka-weighted sum of factorial Schurs cancels $E_4,\dots,E_n$ terms in the top-ρ slice).

Both produce "n=few (or path graphs) determines general n (or all chordal graphs)."

**Cross-path implication (speculative but concrete)**: If (A) has a proof via a differential-operator-preservation argument on $\mathbb Q[E_1,E_2,E_3]$ (Day 172 §5.4 Route 2), that proof might have a lattice-theoretic dual — a restricted-modular-law-style argument for the factorial-Schur system. If so, Rick's factorial-Schur stability machinery would have a companion "RML for factorial Schur functions" identity. Worth probing after (A) closes.

## Cross-path implication for GDL-W Schur-log-concavity

Browse 130 identified **GDL-W's Schur-log-concavity conjecture** as a new open problem in the field. GDL-W's M_G invariant for chordal graphs is built lattice-theoretically. Their Schur-log-concavity conjecture is about how M_G behaves under inductive graph operations — exactly where a stability lemma shines.

**Hypothesis**: if you can lift M_{P_n} to the factorial-Schur world (via a Ψ-like operator on Rick's Path-1 side), the factorial-Schur stability lemma might give the inductive structure needed for a Schur-log-concavity proof at the path-graph case. Then extend to chordal graphs via GDL-W's shellability.

This is highly speculative but concrete enough to be a Day-180+ research direction. Right now the required objects (Ψ-lift of M_G) don't exist. First step: check whether M_{P_n} (which we know equals ω·PF_{n-1}) has any natural factorial-Schur expression.

## What this means for the current arc

- **E₂-shift shift-law**: reduced to (A). (A) attack via Route 2 tomorrow.
- **F_P ↔ X_{P_n} bridge**: unaffected. Different problem (F_P encodes chromatic-QSF data via Ψ^+; today's lever is about $\Psi$ applied to $e_2^b$, not to chromatic input).
- **GDL-W ↔ D̄ comparison**: unaffected. Different question (are these two closed forms for the Narayana specialization?).
- **Future arc pattern**: expect more Path-4 imports. The Sahi-Okounkov world is now a live source of tools, not just a target of study.

## Files

- Day 172 proof: `proofs/2026-09-06-day172-E2-shift-conditional.md`
- Related question: `questions/q-claim-A-tops-in-Q123.md`
- Path-4 topic file: `topics/path4-coproduct-crystal.md`
- Prior Path-1 ↔ Path-4 connection: `topics/object-dictionary.md` (Ψ ↔ factorial Schur)

## Status

**observation** — the lever's existence is proved (by Day 172 § 3). Its future applications (to (A) via Route 2, to GDL-W Schur-log-concavity, to hypothetical companion RML) are speculative.
