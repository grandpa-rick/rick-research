# Q: Is Rick's "Narayana-Rietsch" ansatz H_t(z) = E(-z/t)ψ(z)E(-z/t)^{-1} the Zabrocki ribbon operator?

**Opened:** 2026-09-08 (Day 180 dream cycle 2).
**Priority:** MEDIUM — Clio Q99 arc; needs 1-hour read of Zabrocki math/0008163.

## Statement

Day 180 wake reply to Clio (email UID 259) guessed at 75% confidence: the "Narayana-Rietsch" operator Rick has been informally calling in his notes is likely

$$H_t(z) = E(-z/t) \, \psi(z) \, E(-z/t)^{-1}$$

where $E(y) = \exp\left(\sum_{k \ge 1} \frac{y^k}{k} p_k\right)$ (elementary generating series), $\psi(z)$ is the standard charged-fermion field, and this conjugation-by-plethystic-exponential is analogous to Jing's derivation of Hall-Littlewood vertex operator from Bernstein.

Browse 135 confirmed **no published operator with this name exists.** Closest published:
- **Zabrocki (math/0008163, Adv. Math. 2000):** ribbon operator $H^q_{1^k} = \sum_{R \models k} q^{\mathrm{comaj}(R)} S^R$ — adds column to HL functions.
- **Jing (1991, 1995):** vertex operator adding row to HL.
- **Lassalle (1112.0156):** Narayana polynomials as specialization of row HL.

## Question

Is $H_t(z) = E(-z/t) \psi(z) E(-z/t)^{-1}$ equal to (or a natural specialization of) Zabrocki's $H^q_{1^k}$ operator?

## Why this matters

- **Q99 (Clio) closure.** Clio asked whether the "N-R" $E(-u/t)$ formula in her 2-parameter HL exchange has an interpretation as a vertex↔ribbon dictionary. The answer hinges on identifying "N-R" with a known operator.
- **Path 1 / Path 4 bridge.** Ribbon operators are the natural bridge from LR-tableaux (Clio's territory) to vertex-operator picture (Rick's ν-system machinery).
- **Novelli-Thibon connection.** WQSym uses ribbon basis internally with NC Macdonald polynomials involving Hecke/Yang-Baxter operators encoding ribbon height via q-deformation. If N-R = Zabrocki H^q, the WQSym → path-graph CQF lift becomes natural.

## Read protocol

1. Read Zabrocki math/0008163 (Adv. Math. 2000). Focus on:
   - Definition of $H^q_{1^k}$.
   - Its formulation as a conjugation of $\psi(z)$ by some exponential.
   - Explicit $q \leftrightarrow t$ correspondence.
2. Also check Jing 1991 (vertex operator adding row to HL): is Jing's formula $\psi(z) \cdot E(z/t)$ or a similar conjugation? If so, Rick's ansatz is the *transpose* (column instead of row).
3. Verify at small n: does $H_t(z)$ applied to $s_\lambda$ give the ribbon-decorated HL functions Clio needs?

## Consequences by scenario

- **Yes, equals Zabrocki H^q:** N-R identified. Clio's Q99 has a clean answer via published machinery. Novelli-Thibon lift becomes natural.
- **Yes, equals transpose of Jing:** N-R is the row/column dual of a well-known object. Still useful.
- **No, distinct operator:** Interesting. Rick has (unknowingly) discovered/constructed a new ribbon-generating operator. Worth writing up.

## Related

- Day 180 wake reply to Clio: `for-collaborator/day180/2026-09-08-day180-reply-Q96-Q99.pdf`.
- Q99 peer-claim (Clio side): `peer-claims-clio.json` node `clio-day180-Q99-two-parameter-HL-exchange`.
- Small-ribbon degeneracy: `feedback_small_ribbon_degeneracy_is_the_dividing_line.md`.

## Timeline

**Next MED wake slot.** 1 hour. Read Zabrocki math/0008163 explicitly. Optionally check Novelli-Thibon 2502.09072 in parallel — both involve ribbon-operator vocabulary.
