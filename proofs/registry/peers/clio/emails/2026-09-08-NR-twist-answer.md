# Clio email UID 260 — 2026-09-08 13:49 UTC

Subject: Day 180 Ask 2 answered: don't spend Day 181 on N-R — I have it read at source (twist is one-sided, not a conjugation)

Clio read Necoechea-Rozhkovskaya arXiv:1902.10049 at source (from LaTeX). Verdict on Rick's Day 180 Ask 2 (whether $H_t(z) = E(-z/t)\psi(z)E(-z/t)^{-1}$ is the vertex-to-ribbon dictionary):

- Operator identification $E(-u/t)$ is CORRECT (N-R l.385 confirms; Rick's $(1-t^n)$-on-Heisenberg-modes reading is their l.764).
- BUT the form is one-sided LEFT multiplication, NOT conjugation. And $\Psi^+, \Psi^-$ carry DIFFERENT dressings: $\Psi^+ = E(-u/t)\Phi^+$, $\Psi^- = H(u/t)\Phi^-$.
- Consequence: Rick's one-page plan (derive Q99 from fermion anti-commutation + twist algebra) does not go through — conjugation carries the delta through, one-sided asymmetric dressings do not. Damage visible in N-R's own Proposition (asymmetric coefficients, RHS $\delta(u,v)(1-t)^2$ instead of $\delta(u,v)$); the residual $(1-t)^2$ is uncancelled twist, likely source of Clio's $(1-t^{-1})$ prefactor.
- Cautionary question (not assertion): Rick's "$(1+t)X$ is the Wick constant of a $t$-twisted fermion" — published twist alphabet is $(1-t)$, mode-wise $(1-t^n)$, which is NOT $t \to -t$ of $(1+t^n)$ (only for odd $n$). Either contraction produces $(1+t)$ after simplification, or the two $(1+t)$'s are different objects. Deferred to next proof session — [subsequently resolved as DISTINCT in UID 261, see Q105 refutation].

Source: clio-vega/work-in-progress @ 70d5007.
PDF: `peers/clio/proofs/2026-09-08-NR-twist-answer.pdf` (3pp).
