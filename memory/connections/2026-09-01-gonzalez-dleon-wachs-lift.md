# Symmetric function lift of Day 154 — González D'León-Wachs 2608.08692

**Browse 121 (2026-09-01)**

## The connection

Day 154 proved: [T^n]H|_{E_3=0} = C_{n-1} (Catalan).

González D'León-Wachs Theorem 5.9 proves:
$$(-1)^{n-1} M_{P_n}(\mathbf{x}) = \sum_{\pi \in \mathcal{NC}_{n-1}} e_{\lambda(\pi)}(\mathbf{x})$$

Under the specialization η: Sym → ℤ sending e_λ ↦ 1 for all λ, the right side gives |NC_{n-1}| = C_{n-1}.
Under η: e_λ ↦ t^{ℓ(λ)-1}, it gives the Narayana polynomial N_{n-1}(t).

So: Rick's scalar C_{n-1} = M_{P_n}(x) under η ∘ (t→1). Rick's Narayana polynomial N_{n-1}(t) = M_{P_n}(x) under η.

## The key open question

Can [T^n]H|_{d-th E_3 stratum} be lifted to a symmetric function M_G(x) for some graph G?

If yes: by González D'León-Wachs Theorem 7.2, e-positivity of [T^n]H at each stratum follows from chordality of G.

The path graph P_{n-1} handles the top stratum (E_3=0). What graph handles stratum d=1? d=2?

## Evidence for the connection

1. **Forest = free probability.** The equality case in González D'León-Wachs (μ_G(t) = h_{P_G}(t) iff G is a forest) aligns with E_3=0 being the "free" layer of H. Free probability = tree/forest interactions = no cycles = chordal with no triangles.

2. **Lagrange inversion appears in both.** González D'León-Wachs prove N_n(t) = μ_{P_n}(t) via Lagrange inversion of the compositional inverse of Σ (-1)^{n-1}[n]_t y^n. Rick's psi (Day 152) is also a Lagrange kernel. Same mechanism.

3. **Noncrossing partitions appear in both.** NC_{n-1} indexes the e-expansion of M_{P_n}. Rick's Narayana identity (Day 154) has NC_{n-1} as the combinatorial backbone via the lattice structure.

## How to pursue

Small cases:
- Compute [T^2]H and decompose by E_3-degree: the d=0 piece should be C_1=1 (trivially matching M_{P_1}=e_1), the d≥1 pieces are the first new data.
- Compute [T^3]H: d=0 piece = C_2=2, matches M_{P_2}. d=1 piece = first stratum above the base; identify which symmetric function this would lift to.
- Try: does the d=1 stratum of Ψ_{P_n}(x) (not M_{P_n}) match [T^n]H|_{E_3-stratum 1}?

The conjecture: H is a specialization of Ψ_G(x) for some chordal graph G, with E_3 playing the role of the filtration parameter.
