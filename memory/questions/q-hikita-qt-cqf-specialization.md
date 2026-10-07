# Q: Is Rick's F_P the q=1 specialization of Hikita's (q,t)-CQF?

**Opened:** 2026-09-08 (Browse 134, Day 179 dream cycle 2).
**RESOLVED:** 2026-09-08 (Browse 135, Day 180 dream cycle 2). **Question is moot for e-positivity.**
**Priority:** RESOLVED.

## Resolution (Browse 135, Day 180 dream cycle 2)

Hikita 2503.23597 **Theorem B(iv)**: the e-coefficients $c_\lambda(\Gamma; q, t)$ of the (q,t)-CQF are **independent of $q$**. The $q$-direction has no effect on e-expansion.

**Consequence.** Rick's Theorem B computes the definitive e-coefficient layer — there is no richer $(q,t)$-refinement to seek along the $q$-axis. Whether F_P is literally the q=1 slice or a related specialization no longer matters for e-positivity: **both compute the same coefficients**. Question effectively vacated.

**Where a (q,t)-story WOULD be non-trivial:** Schur coefficient basis (Shareshian-Wachs Schur positivity conjecture — still open), HL basis (Kim-Lee-Yoo 2506.23082), Macdonald basis. Rick's arc on e-positivity is orthogonal to these.

**See:** `connections/2026-09-08-hikita-B-iv-closes-qt-question.md`.

---

## Original statement

## Statement

Hikita 2503.23597 ("(q,t)-Chromatic Symmetric Functions") defines a (q,t)-analog of chromatic symmetric functions for unit interval graphs via **level-1 polynomial representations of the affine Hecke algebra of type A**. At q=1 recovers the Shareshian-Wachs CQF (single q-variable, Rick's setting). At q=∞ recovers Hikita's probability distribution (the object Chow's watershed enumerates).

Rick's F_P is the generating function for X_{P_n} across n via the ν-system / Riccati structure. It's a *single-parameter* object (T marks n; s, p mark chromatic and elementary symmetric structure).

**Question**: Does Rick's F_P admit a natural (q,t)-lift matching Hikita's construction on path graphs? Equivalently: is F_P the q=1 slice of some F_P^{(q,t)} living inside affine Hecke?

## Why this is worth investigating

- **Path 3 direct application:** Hikita uses affine Hecke algebras of type A — Rick's Path 3 native quantum-group setting — on Rick's domain (unit interval graphs, specialized to path graphs). Direct hit.
- **(q,t)-lift for free:** If F_P = q=1 of a Hikita (q,t)-object, Rick gets a (q,t) generating function without having to construct one from scratch.
- **Fact 8 in (q,t)-form:** If the (q,t)-lift extends, Fact 8's operator D_n also lifts. The 4-term compact form might reveal a symmetric or interpolation structure only visible in (q,t).
- **FPSAC framing:** would add "affine Hecke algebra representation-theoretic root" to the four-pillar framing.

## Structural check protocol

1. **Read Hikita 2503.23597 §2-3** (definition of (q,t)-CQF, path-graph specialization if written explicitly).
2. **Match objects at q=1**: Hikita's H_n^{(q=1, t)}(x) vs Rick's F_P|_n evaluated at T = t (or appropriate variable substitution). Do they agree as symmetric functions in x?
3. **Sanity check with Theorem B**: Rick's Theorem B expresses X_{P_n}(x, t) algebraically. Hikita's construction is representation-theoretic. If both compute the same q=1 CQF, Rick's Theorem B and Hikita's specialization must land in the same polynomial (verifiable at small n).
4. **Extension check**: does Hikita's (q,t)-CQF for path graphs give a two-parameter refinement of Theorem B's polynomial output?

## Consequences by scenario

- **Match at q=1**: Rick has a natural (q,t)-lift of F_P via Hikita. Substantial extension possible.
- **No natural match**: Rick's F_P is a different object than the q=1 slice of Hikita — perhaps because F_P sums over n while Hikita is n-fixed. Note the distinction and move on.
- **Match after re-indexing**: F_P = generating function of Hikita's per-n objects. Interesting — but requires care about how the sum interacts with (q,t)-lifting.

## Open sub-questions

- Is Hikita's q the same as Shareshian-Wachs' q, or a different Hecke parameter?
- Does the "level-1 representation" have a special structure that matches path graphs specifically? (Unit interval graphs generally correspond to more complex representations; level-1 might BE the path-graph case.)

## Related

- Browse 134 reading log: `reading/2026-09-08.md` § Papers (Hikita) / Connection 5.
- Chow watershed connection: `connections/2026-09-08-chow-watershed-combinatorial-face.md` (Chow's Hikita distribution = q=∞ marginal).
- Path-graphs-generative connection: `connections/2026-09-08-path-graphs-generative-restricted-modular.md`.
- Fact 8: `proofs/2026-09-07-day175-fact8-closed-form-D.md`.
- Theorem B: `proofs/2026-09-05-day170-theorem-B-PROVED.md`.

## Timeline

**Day 180+ wake or dream** (after Chow watershed numerical check, since that's a smaller and more direct verification). Deep-read of Hikita 2503.23597 is the entry-cost.
