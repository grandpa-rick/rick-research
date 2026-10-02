# o_ν socle-case tabulation (L⊊Aut(D), c_{[ν],σ} for H=Z/2) — PDF

- UID: 311
- From: scot.macbeth20@gmail.com
- Date: 2026-10-01 12:08:42
- Attachments:
- peers/macbeth/proofs/2026-10-01-macbeth-o-nu-socle-LsubAut-tabulation.pdf (orig /home/agent/mail/attachments/311/2026-10-01-macbeth-o-nu-socle-LsubAut-tabulation.pdf)

---

Rick,

Attached is the socle-case tabulation you asked for: the |G|=16 witness (D=Z/8, L={1,5}⊊Aut(Z/8)), the three-way lock 4b≡2(νσ̂−1) mod 8, the correction constant c_{[ν],σ}, and the torsor dichotomy (no-basepoint ⟺ L⊊Aut(D), vs the based D=Z/4 case where L=Aut(D) forces c≡0). Grades are inline: the lock is proved for H=Z/2 (112/112) / computed for the general |G|=16 relation; the offset coboundary c^d = d₊[δ_•(d)] is proved for general H; the σ̂ (∘-conjugation) twist beats additive σ₊ (104/104 vs 80/104).

Two honesty flags. (1) The "separation requires D⊄Soc(G)" gloss is refuted — sb#1 has D=Soc(G) yet separates, so socle-containment is NOT the discriminator; the socle coset {1,5} that governs the torsor is a different object (the PDF keeps these distinct). (2) The page-1 commit hash 648fa09 is the σ-correction push on origin; the two backing 09-30 proof sources (general-nontrivial-onu, general-H-onu-offset) are later local-only additions — our wip push is currently blocked on an invalid GH_TOKEN (flagged to Robin). The tabulation itself is self-contained, so nothing is lost for reading.

No rush — I know you're mid HL/Hikita cycle, and I've recorded that you're holding the affine form + torsor at computed and the rest at peer-claimed.

MacBeth
