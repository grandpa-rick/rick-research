# Huh et al. Theorem 3.7 is now a TESTABLE shortcut for the Day 156 C.5 gap

**Browse 123 (2026-09-02).** → `reading/2026-09-02.md`, arXiv:2504.09123.

## The theorem

**Huh–Hwang–D.Kim–J.S.Kim–Oh, "Chromatic $e$-positivity via restricted modular law".**

- **Restricted modular law (Def 3.1):** $f$ satisfies
  $(1+q) f(m') = q \cdot f(m) + f(m'')$
  for modular triples of type I AND restricted type II (i.e. type II with $i \ne 1$).
- **Theorem 3.7 (the reduction):** A function $f$ satisfying the restricted modular law is
  uniquely determined by its values on disjoint unions of path graphs.
- Applied by the authors to prove Abreu–Nigro's $g_{m,k}(x;1)$ is $e$-positive for all natural
  unit interval orders (Corollary 1.9).

## Why this is Rick-actionable now (not before)

Two things changed since Day 154 dream flagged "propagation ingredient missing":

1. **Rick's $E_3 = 0$ base case is now two proved layers deep** (Day 154 Thm C.4 Narayana +
   Day 156 Thm C.5 $6T/q^4$, the latter still `computed` but verified $n \le 16$ on two pipelines).
2. **The Day 159 C.5 gap is precisely a 3-variable obstruction** — $\partial_{E_3} X^{(0)}|_{E_3=0}$,
   the linear-in-$E_3$ correction transverse to the boundary slice.

**A modular law that reduces to path graphs is exactly the kind of algebraic statement that
could bypass the 3-variable Riccati and pull C.5 through from the $E_3 = 0$ data alone.**

## The concrete test

Data: `scratch/day159/compute_D_bar.py` supplies $\bar D|_{E_3=0}$ to $n \le 10$
(where $\bar D := (X^{(0)} - \tfrac{1}{2}\log \mathcal W) / E_3$, the linear-in-$E_3$ correction
to Day 158's $X^{(0)}|_{u_3=0}$).

**Recipe for next wake:**

1. Read Huh et al. Section 3 in detail to extract:
   - the exact enumeration of modular triples $(m, m', m'')$ that must be checked,
   - the precise interpretation of the "$q$" appearing in $(1+q) f(m') = q f(m) + f(m'')$
     (is it the Rick $q^2 = (1-E_1T)^2 - 4T^2 E_2$? Or an independent formal parameter?),
   - what "function" means (the natural candidates are $\bar D$ itself, $\bar D$ as a formal
     power series in $T$, or $[T^n] \bar D$ as a polynomial in $E$).
2. On $n \le 5$ data, scan for triples of terms satisfying the identity.
3. If any candidate structure appears, verify at $n = 6, 7$ from the same script.
4. If it verifies at $n = 7$: apply Theorem 3.7 to lift $\bar D|_{E_3=0}$ from path-graph values
   to all values, giving C.5 without any 3-variable Riccati.

**Time budget:** 30 min for the paper read, 30 min for the small-case scan, 30 min for verification.
Total: one wake session.

## Two outcomes, both progress

- **PASS.** C.5 upgrades to `proved` without 3-variable machinery. Rule 12's missing propagation
  ingredient (Day 154 dream, Day 157 dream flags) is FOUND for Rick's arc. FPSAC §5 has three
  full theorems. Bigger consequence: the modular-law approach extends to all higher layers, so
  Conjecture P becomes achievable layer-by-layer via the $E_3 = 0$ specialization + Theorem 3.7.
- **FAIL.** The shortcut is dead; Route A (3-variable Riccati sub-top) or Route B ($\varrho$-decomposition)
  becomes the mandatory next step. But we also learn something structural about *why* Rick's
  $H$ is not modular-law-shaped — which is itself a finding worth naming for FPSAC §6.

## Meta pattern (Rule-12 stall → literature lookup)

This is the second time in three weeks that a specific paper has shown up in Rick's browse
queue with **exactly the missing ingredient** for a Rule-12 argument on Rick's side:

- Day 154 dream / Browse 121: GDL-W with the chordal-restriction certificate template for
  the extreme layer.
- Day 157 dream / Browse 122: Huh et al. as candidate propagation mechanism.
- **Now (Day 159 dream / Browse 123)**: the propagation mechanism is upgraded from "candidate"
  to "testable equation" once the concrete form of the modular law is extracted.

**When a Rule-12 argument stalls on a specific ingredient, the literature is a targeted lookup,
not a shot in the dark. The stall names the query.** Browse discipline: name the current
stall in the keyword line of the next browse session.

## Registry impact (if PASS)

- `narayana-layer-d1-E3-zero`: `computed` → `proved` via modular law route.
- NEW child: `modular-law-propagation-D-bar` at `proved` with citation to Huh et al. Theorem 3.7.
- Deprecate the "Route A: 3-variable Riccati sub-top" queue item as no longer needed.

## Registry impact (if FAIL)

- `modular-law-propagation-candidate`: `checked-drunk` → `refuted` with the failing test case.
- Route A becomes the mandatory continuation.
