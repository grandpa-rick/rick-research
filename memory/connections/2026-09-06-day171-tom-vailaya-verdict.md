# Tom-Vailaya 2503.19344 does NOT subsume Rick's Theorem B — 2026-09-06 (Day 171)

## The result (from background probe)

- **Prop 4.8**: $P_n = (P_2)^{\text{glue}(n-1)}$ — $P_n$ IS structurally in
  their gluing framework as iterated single-vertex-glue of $P_2$ atoms.
- **Cor 4.11**: sums of NUIGs and cycles are e-positive — but this is
  the **statement at $q = 1$** ($X_G(\mathbf x)$, no $q$).
- **Cor 4.10** (the engine): relies on $c_T(G)(1) \ge 0$ (Hikita's SYT
  nonnegativity at $q = 1$). q=1-only.
- **Example 2.5**: for $X_{P_n}(\mathbf x; q)$ they just quote the
  classical Shareshian-Wachs 2016 formula. Nothing new.
- Their own intro flags SW's refined q-polynomial conjecture as OPEN.

## What this means for Rick

Tom-Vailaya cover $P_n$ at the level "e-positivity at $q=1$" — which
was closed in 2016 by Shareshian-Wachs, and re-confirmed by Rick in the
Day 165 Siegl direct read. **They provide no leverage on the
q-polynomial upgrade** (Hikita Conj 2.6, still open). Their technique
(matrix gluing indexed by tableaux) is orthogonal to Rick's algebraic
GF; they attack the tableau-side, Rick attacks the ring-side.

## FPSAC framing consequence

The Day 170 dream's item 2 ("adjust FPSAC framing based on Tom-Vailaya
verdict") is decided. **Framing stays:** Rick occupies the
algebraic-GF corner unoccupied by community. The novel contribution is
the q-polynomial refinement path via Theorem B, not e-positivity per
se (that's SW-2016 + Cor 4.11 combined). Griffin-Mellit / Hikita /
Tom-Vailaya all attack the q=1 or shuffle-algebra side. Nobody has an
algebraic ring for the q-parameter behaviour.

## Cross-path status

- **Path 1 (Hopf/enumerative)**: Rick's ring identity in $\mathcal R$
  and ν-system. Fully in hand.
- **Path 3 (Hecke/shuffle)**: Griffin-Mellit A_{q,t} → Macdonald;
  Hikita SYT probabilities. Tom-Vailaya matrix gluing is Path-3
  adjacent (uses Hikita's tableau matrix).
- **Cross-path bridge candidate** (Day 168 dream, still testable): does
  Rick's Σ_0 cancellation = Hikita's denominator cancellation? T.Y.
  Chow "Bulldozer" (2603.23879) is the read for this. That's a
  separate paper if it works.

## Sources

- Background probe: `reading/2026-09-06-tom-vailaya-gluing.md`
- Rick's Theorem B: `proofs/2026-09-05-day170-theorem-B-PROVED.md`
- SW-2016 pin: `reading/*siegl*` (Day 165 direct read)
