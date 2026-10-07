# Does [T^n]H|_{E_3-stratum d} lift to M_G(x) for some chordal graph G?

**Opened:** Day 154 dream (2026-09-01).
**Source:** González D'León-Wachs 2608.08692 Theorem 7.2 + connection `2026-09-01-gonzalez-dleon-wachs-lift.md`.

## The question

González D'León-Wachs prove: for connected perfectly labeled **chordal** $G$, the chromatic-analog symmetric function $\Psi_G(\mathbf x)$ has every stratum (indexed by degree $d \in \{0,\dots,n-k\}$) alternating $e$-positive:
$$(-1)^d \Psi_G(\mathbf x)|_{\deg d} = \sum_{|\pi| = n-d} (-1)^d M_{G|_\pi}(\mathbf x) \in \mathbb Z_{\ge 0}[e_\lambda].$$

**Rick's version:** $[T^n]H$ is filtered by $E_3$-degree; layer $d = 0$ is $(n+1) W_n(u_1,u_2)$ (Narayana, Day 154). Empirically all layers appear to be $E$-positive (Conjecture P; verified layer $d = 0$ to $Y^{33}$ on Day 151).

**The question:** is there a chordal graph $G_n$ (or a family $G_{n,d}$) such that
$$[T^n]H|_{E_3\text{-stratum } d} = \phi\bigl(\Psi_{G_n}(\mathbf x)|_{\deg d}\bigr)$$
for some ring homomorphism $\phi$ (candidate: $\eta: e_\lambda \mapsto$ some scalar)?

If yes: Conjecture P is a corollary of González D'León-Wachs Theorem 7.2 + chordality of $G_n$.

## Evidence

**Positive:**
- Day 154 base case: $[T^n]H|_{E_3=0}|_{u_1=u_2=1} = C_{n-1} = $ specialisation of $M_{P_n}(\mathbf x)$ under $\eta = (t \to 1) \circ (e_\lambda \mapsto t^{\ell(\lambda)-1})$. So the top stratum for $G_n = P_n$ works.
- Forest = free probability. The equality case $\mu_G(t) = h_{\mathcal P_G}(t)$ iff $G$ is a forest matches $E_3 = 0$ = "no triple interactions."
- Both frameworks use Lagrange inversion at the base case.

**Negative / caution:**
- The specialisation $\eta$ that gives $C_{n-1}$ loses ALL structure — $\eta(e_\lambda) = 1$ is not a lift, it's a projection. Need to find a richer $\phi$ that preserves both $u_1, u_2$ information AND $E_3$-stratum information.
- Two-variable case only: González D'León-Wachs' $M_G$ lives in Sym in *infinitely many* variables; Rick's $u_1, u_2, u_3$ is three-variable. Restriction to three variables may be lossy.
- No papers cross-reference. Two communities that don't talk to each other. That has led to false convergences before (Rule 6 v2 fires 11 times).

## Small-case test (do this in the next wake session)

**Step 1.** Compute $[T^2]H$ and $[T^3]H$ symbolically in $E_1, E_2, E_3$, then decompose by $E_3$-degree.

**Step 2.** Predict from González D'León-Wachs:
- $[T^2]H|_{E_3 = 0}$: from Day 154, this is $3 W_1(u_1, u_2) = 3(u_1 + u_2)$. Symmetric function shadow: $M_{P_2}(\mathbf x) = -e_{11}$? Check.
- $[T^3]H|_{E_3 = 0}$: from Day 154, this is $4 W_2(u_1, u_2)$. Small.
- $[T^n]H|_{E_3 = k > 0}$: no prediction yet — this is exactly what the test would reveal.

**Step 3.** Look up $M_G(\mathbf x)$ for small chordal $G$ (paths $P_n$, cycles fail chordality but chords fix it, tree-like graphs). The paper has tables. Try:
- $G = P_n$ for various $n$ (already know top stratum).
- $G = $ path with one added chord.
- $G = $ tree of small size.

**Step 4.** If any match found: check that $\tau = $ mult by $e_3$ (Day 149 Theorem 3) corresponds to a chordal-preserving graph operation.

**Falsifier:** if $[T^3]H|_{E_3 = 1}$ does not appear in any small $M_G$ table, the lift doesn't exist, and the connection to González D'León-Wachs is limited to the top stratum only.

## Priority

**High.** This is the concrete new lead of Browse 121 and would close Conjecture P if it works. Small-case test is cheap.

## Related

- `connections/2026-09-01-gonzalez-dleon-wachs-lift.md` — the base connection.
- `connections/2026-09-01-rule12-external-validation.md` — the meta pattern.
- `questions/q-lagrange-kernel-psi.md` — the parallel arc (identify the sequence $1,2,5,34,334,\dots$).

## Status

**REFUTED for the naive path-graph lift, Day 155 (2026-09-01).**

Day 155 computed $[T^n]H$ by $E_3$-stratum for $n = 2, 3, 4, 5$ from the raw definition of $F_P$ (script: `/home/agent/projects/scratch/day155/compute_strata.py`, tables: `.../strata.txt`).

**The result of the small-case test.** The naive "$[T^n]H|_{d=0} = (n+1) M_{P_{n+1}}$" hypothesis matches at $E_3 = 0$ (the Day 154 Narayana result) but breaks as soon as $E_3$ enters:

- **n=3, $E_3$ coefficient:** Rick has 8, path-graph prediction gives $(n+1)|\text{NC}_n \text{ of type }(3)| = 4 \cdot 1 = 4$. Ratio 2.
- **n=4, $E_1 E_3$ coefficient:** Rick has 45, path-graph prediction gives $(n+1) \cdot 4 = 20$. Discrepancy 25 comes from an *extra* contribution: picking one "$Y^4$" from $\psi$ (which contributes $E_1 E_3$) contributes 5, and the "$Y^3$" contribution is *doubled* (since $[Y^3]\psi = 2 E_3$, not $E_3$) giving 40 instead of 20. Total 45.
- **Terms with no size-3 or size-≥4 parts (n=2,3,4 verified):** MATCH exactly.

**Mechanism of failure.** Rick's $\psi = 1 + E_1 Y + E_2 Y^2 + 2 E_3 Y^3 + E_1 E_3 Y^4 + 2 E_2 E_3 Y^5 + (E_1 E_2 E_3 + 5 E_3^2) Y^6 + \ldots$ is NOT the ordinary generating function of elementary symmetric functions. If it were, $[Y^n]\psi^{n+1} = (n+1)\sum_{\pi \in NC_n} e_{\lambda(\pi)} = (n+1)(-1)^n M_{P_{n+1}}$. Rick's higher-order corrections (starting at $[Y^3]\psi = 2 E_3$, not $E_3$) produce a strictly larger polynomial. So the top stratum is a Lagrange inversion of a *decorated* $\psi$, not of the classical $E(Y) = \sum e_i Y^i$.

**What this rules out.** The "single chordal graph $G$ per stratum" hypothesis is dead for paths. It could still be revived by
(i) a family of graphs $G_n$ growing with $n$, chosen so their $M_{G_n}$ has the extra multiplicities on size-3 blocks (e.g. graphs with triangles);
(ii) allowing $\phi$ to be a non-obvious ring map that absorbs the correction;
(iii) $\psi$ itself being some $\Psi_G$-like object.

Options (i)–(iii) are speculative and NOT enough evidence to pursue further this cycle. **Downgrade priority to LOW.** Retain the E_3=0 slice connection to $M_{P_n}$ (still real).

## Related update
- The E_3=0 slice = Narayana connection stands.
- The full-stratum "single graph $G$" story dies.
- Rule 12 external validation stands (three papers, unchanged).

## Day 159 dream update — the parking function bridge

**Browse 123 (2026-09-02) turned up GDL-W Theorem 5.9**:
$$(-1)^{n-1} M_{P_n}(\mathbf x) \;=\; \omega \cdot PF_{n-1}(\mathbf x) \;=\; \sum_{\pi \in NC_{n-1}} e_{\lambda(\pi)}(\mathbf x)$$
where $PF_{n-1}$ is the parking-function symmetric function.

**This bridges Rick's two arcs at the path-graph slice.** The b_k arc (Day 148 solved) uses
Rick's $\psi$ producing Narayana via Lagrange inversion; the Conjecture P arc uses $H$ with
its $E_3$-filtered $E$-positivity. At $E_3 = 0$ (= path graphs), *both* arcs land on the same
polynomial, and GDL-W Thm 5.9 identifies that common landing zone with a parking-function
symmetric function summed over NC partitions.

**New open sub-question.** Is there a natural bijection between the Lyndon trees $T \in N_{P_n}$
(GDL-W Thm 6.18) and the noncrossing partitions $\pi \in NC_{n-1}$ that respects the type map
$\lambda(T) = \lambda(\pi)$? If yes, it would explain WHY Rick's Lagrange route to Narayana
and GDL-W's shellability route to $M_{P_n}$ produce the same polynomial: they enumerate the
same combinatorial structure by different names.

**Priority remains LOW for the "single graph G per stratum" question.** But the parking function
bridge is worth logging as a fact for FPSAC §6 open-problems.

