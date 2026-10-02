# Change-of-base §4.5 step 2 — revised PDF (step 2 now manifestly CCC-free)

- From: scot.macbeth20@gmail.com
- Date: 2026-09-17 10:34:03 UTC
- UID: 281
- Attachments: containers-monads-comonads-change-of-base.pdf (saved /home/agent/mail/attachments/281/)

---

Rick,

Attached is the revised change-of-base paper (14pp; corresponds to scotmacbeth/work-in-progress content-commit 21aef97). It pre-empts exactly the thing you're reading right now: the "closed ⟹ terminal" collapse in the main theorem's step 2 is now factored through a new standalone Lemma 4.2 — "a symmetric monoidal closed category with an initial object ∅ has terminal object [∅,X]", proved from (−)⊗A being a left adjoint so C⊗∅≅∅. Step 2 invokes only that lemma, so it uses neither cartesian-closedness nor unit-connectedness; I've said so in one explicit sentence there. Closedness (existence) and unit-connectedness (fullness) are the two independent axes, as we discussed.

I'd value your read of step 2 under this framing — whether the lemma fully dispels the smuggled-CCC worry, or whether you still see unit-connectedness doing hidden work anywhere in the extension.

MacBeth
