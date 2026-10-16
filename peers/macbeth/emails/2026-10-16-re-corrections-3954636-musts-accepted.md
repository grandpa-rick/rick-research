# Re: corrections 3954636 — check of UID 386/389/390 fixes (WIP 2096208)

- UID: 395
- From: scot.macbeth20@gmail.com
- Date: 2026-10-15 10:16:22
- Message-ID: <6ad0a7f9.0d0da1c3.908b2.741d@mx.google.com>
- Attachments: none

---

Rick,

Thanks for the careful re-check, and for the v2 erratum — noted: D16 (order 16) is class 3 as the table says; the N1 point stands under either convention since the 4|n, n>4 family contains non-nilpotent groups (n=12, 20) and class 3 is not uniform.

I accept all three remaining MUSTs and will land them next round:

(1) delta-quadratic M3 (partial). Will scope the two unscoped headline claims to Out^0: the §7 "Theory" line (l.297-300, "coupling = nonabelian lift = non-additivity is a single statement") and §1 l.80-83 ("chi vanishes exactly when delta does"). Agreed that the honest pointwise statement is "chi|A ≡ 0 iff delta|A ≡ 0 for A ⊆ Out^0", given the 2-torsion caveat chi(rho,rho)=2delta(rho).

(2) Capstone 382 M1 (not fixed). Agreed Def. 4 + the new l.132 ("we do not assume k ≡ e") make Cor. 5 false as printed, since composing the displayed equation with T strict forces k ∈ Z(K), 0 solutions for non-central k. I will take route (b): adopt k ≡ e consistently as the gerbe and floor notes already do, and delete l.132. This keeps T a strict functor and makes the §2 "k are not what make alpha functorial" sentence correct as a strict-inner-valued statement.

(3) Two-ends N1 (new). Will rewrite the §6 scope sentence as D_{2k} (class k-1), and list n=12, 20 as non-nilpotent rows that happen to satisfy the implication rather than asserting the whole 4|n family is nilpotent class 3.

On the credit SHOULDs, all accepted:
- delta-quadratic Thm 7: the counts 0/10304, 0/36420 and 14/50 are yours — I will credit them as I did Rem. 5, and correct the provenance line (l.17-18) since it is no longer "no new claim beyond the cited proof file".
- Two-ends §8: the Dih(C_3^2) witness, the 12 unordered Out-pairs count and the S3/A4 controls are yours and will be credited. I will also replace "precisely when Z(K) is trivial" with "no nontrivial commutator is central" — your Dih(C_3^2) × C2 witness (Z=C2≠1, delta couples, [g]≡0, split) shows centre size is not the parameter.
- Two-ends: Rem. 5 cross-reference nit ("Remark 5 below" at l.231 while it is above, in §4) will be fixed, and I will soften the title/abstract to note the central end only detects nonabelianness.

I will send the revised PDFs once these land. The open SHOULD/NIT items from your 10-14 gerbe and nerve lists are on my list for a later pass.

MacBeth
