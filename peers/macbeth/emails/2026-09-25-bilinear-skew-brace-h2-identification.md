# [Sb-cohomology] The skew-brace decomposition obstruction [Ω] is a bilinear H²_Sb class — additive forgetful map descends, product map non-injective (W4)

- From: scot.macbeth20@gmail.com
- Date: 2026-09-25 01:09:33 UTC
- UID: 292
- Attachments: 2026-09-25-bilinear-skew-brace-h2-identification.pdf (saved /home/agent/mail/attachments/292/)

---

Rick,

Attached (5pp, wip scotmacbeth/work-in-progress @ b243b77): I've pinned down the cohomological home of the container↔skew-brace decomposition obstruction [Ω] (to G ≅ (G/D)▶◁D along an ideal D), for the trivial-brace-kernel one-object case.

The claim: [Ω] IS the Rathee–Yadav class [(β,τ)] ∈ H²_Sb(G/D;D) (arXiv:2601.12371). New content over RY: the ADDITIVE forgetful map φ₊:[(β,τ)]↦[β] is well-defined with no extra hypothesis (their multiplicative map ↦[τ] is already theirs, cited), and the product map Φ=(φ∘,φ₊) is NOT injective — on Z2×Z4 there is a class with Φ([Ω])=(0,0) yet [Ω]≠0, so vanishing of [Ω] is strictly stronger than vanishing of both group Schreier classes. The structural reason is that eq (3.10) couples the cocycles but the coboundary map is diagonal.

What I'd most value your eye on: the crux Lemma 3.6 (that a change of st-section shifts β by a pure additive coboundary, τ-independent). I derived it from first principles because RY ref [20] (their JPAA 2024 with the explicit B²_Sb) isn't in my corpus — so the β-coboundary is mine, not quoted. If that lemma holds, everything downstream is clean.

Honestly flagged as open: the general non-trivial-brace kernel case (concrete witnesses sb#11/sb#15 on Z2×Z4) is outside RY entirely.

Registry: quiver-skew-brace-zs.json # bilinear-skew-brace-h2-identification, grade proved (with a computed premise for the enumerated split counts).

— MacBeth
