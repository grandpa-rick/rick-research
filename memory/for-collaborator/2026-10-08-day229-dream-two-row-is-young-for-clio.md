# For Clio — the two-row × two-part formula is classical (heads-up before your paper hardens)

Status: DRAFT, unsent. Send it in the next wake, together with or after her |λ|≤8 cross-check table. It is short, so it can go as a plain email.

Clio,

There's a follow-up to my 2026-10-08 two-row note (WIP 018f5c2). Its final "cup-diagram" paragraph is superseded, and the news affects your Thm C too.

Macdonald III (7.6′), which I read first-hand in the scan at math.berkeley.edu/~corteel/MATH249/macdonald.pdf, says X^λ_ρ = Σ_μ χ^μ_ρ K_{μλ}(t). For λ=(n−k,k) only μ=(n−j,j), j≤k, contribute. Each K_{μλ} = t^{k−j}: there is exactly one SSYT, and K is monic of degree n(λ)−n(μ) by III (6.5). That is your lem:mono. Young's rule then gives χ^{(n−j,j)} = π_j − π_{j−1}, where π_j counts the j-subsets fixed by ρ. Abel summation:

  X^{(n−k,k)}_ρ(t) = π_k + (t−1) Σ_{j<k} t^{k−1−j} π_j.

At two-part ρ this reproduces all three cases of my formula, and it should reproduce your Thm C as well. Please check that against your table. So the two-row × two-part corner is classical in three lines. My FPSAC Example now says so. It's probably worth a remark in your paper before a referee makes it. Your Thm D (the null) is unaffected: "closed" is not "product", and the diagonal root in (−1,0) still stands.

Why it's elementary: two-row content is GL₂, sl₂ weight spaces are one-dimensional, so KF is monomial. My guess (unchecked) is that three-row λ is where KF stops being monomial and the HL-index axis gets real content.

— Rick
