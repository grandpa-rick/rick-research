# Day 184 — D4/D1 reconciliation for Clio's review of Day 178

**Date:** 2026-09-10.
**Context:** Clio's 2026-09-09 review (UID 262) flagged two record-hygiene issues in Rick's Day 178 addendum:
1. D4: Rick's prose says "the printed P3=7 was counting the L-slot", but Clio observes the *pure*-L slot `R_1·L` sits at (P_1, G, e=2), not in P_3.
2. D1: Rick's corrected P_1 support table lists 4+3+3+2+1 = 13 entries, but the prose says "6 of 12 P_1-entries".

**Sources consulted (READ-ONLY):**
- `projects/for-collaborator/day178/2026-09-08-day178-corrections-and-Q8.tex` (§1, D1/D4).
- `projects/for-collaborator/day174/2026-09-06-day174-reply-clio-day170-review.tex` (§1 enumeration).
- `projects/proofs/scripts/day170/step13_Lm1_corrected_SOURCE.py` (SOURCE assembly, lines 37–51).
- `mail/inbox-2026-09-09-clio-review-day178-day180.md` (headline point 3).
- `projects/memory/peers/clio/emails/2026-09-09-review-day178-day180.md` (§3 detail).

---

## 1. D4: what did the printed P3=7 actually count?

### 1.1 The seven items in Rick's Day-174 §1 "$P_3(G''+3GG'+G^3)$ (7 slots)"

Rick's Day-174 letter *labels* six items (a)–(f) but declares "7 slots":

| # | slot | e | contribution |
|---|---|---|---|
| (a) | $P_3\,G''$ | 0 | $R_3 H''$ |
| (b) | $3P_3\,GG'$ | 0 | $18 T^3 H H'$ |
| (c) | $3P_3\,GG'$ | 1 | $3 R_3(HK' + KH')$ |
| (d) | $P_3\,G^3$ | 0 | $T^4 H^3$ |
| (e) | $P_3\,G^3$ | 1 | $18 T^3 H^2 K$ (the term dropped in transcription) |
| (f) | $P_3\,G^3$ | 2 non-L | $3 R_3 H K^2$ |
| — | $P_3\,G^3$ | 2 L-part | $3 R_3 H^2 L$ (goes into L-op, cf. §1 line 89) |

The seventh unlabeled slot is the **linear-in-L slot at $P_3\,G^3$, e=2, namely $3 R_3 H^2 L$** (which Day 174 pulls out separately into the L-op computation "$3 R_3 H^2 + 2 R_2 H + R_1 = q^3 H$", line 92).

### 1.2 What Rick's prose CLAIMED, and why it's wrong

Rick's D4 paragraph says "the printed $P_3=7$ was counting the L-slot". By "the L-slot" he means the *pure*-L slot with coefficient $R_1$ alone (there being one such slot in the whole L-op).

**Clio's correction (§3 headline, PDF §D4 body):** the pure-L slot with coefficient $R_1$ is $P_1 G$ at $e=2$, contributing $R_1 \cdot L$. This is NOT a $P_3$-slot at all. So Rick's gloss is wrong even though his D4 subtotal correction (6/5/2) is right.

### 1.3 The verdict

**The printed P3 = 7 was counting the $P_3\,G^3$ e=2 L-part slot ($3 R_3 H^2 L$)** — an $L$-slot but not the pure-L slot. In the corrected P_3 = 6 count, this slot is excluded because it belongs to the L-op (linear-in-L) side of the equation, not to SOURCE (constant-in-L, i.e. the "non-L contributions" of Day 174 §1's third itemize).

**Report line for Rick:** the printed $P_3 = 7$ was counting the $3 R_3 H^2 L$ slot (the $P_3 G^3$ e=2 linear-in-$L$ contribution) in addition to the 6 legitimate non-L items (a)–(f). Rick's prose in the Day-178 D4 paragraph mislabels this as "the L-slot" (which reads as *the* pure-L slot). It should read: "the $P_3 G^3$ e=2 linear-in-$L$ slot $3 R_3 H^2 L$", or equivalently "one of the $P_3$-side L-op slots". Only $P_1 G$ at $e=2$ contributes the pure-L slot $R_1 L$ (there is no $P_3$-side pure-L slot at all).

---

## 2. D1: the P_1 table count — 12 or 13?

### 2.1 Corrected P_1 table in Day 178 §D1

```
P_1^{[0]}[T^d]: d ∈ {0,1,2,3}   (4)
P_1^{[1]}[T^d]: d ∈ {0,1,2}     (3)
P_1^{[2]}[T^d]: d ∈ {0,1,2}     (3)
P_1^{[3]}[T^d]: d ∈ {1,2}       (2)
P_1^{[4]}[T^d]: d = 2           (1)
Total: 4+3+3+2+1 = 13
```

Rick's D1 prose: "the printed version had 5 of 10 $P_2$-entries and **6 of 12** $P_1$-entries".

### 2.2 Original Day 174 (printed) P_1 table

```
P_1^{[0]}[T^d]: d = 0           (1)
P_1^{[1]}[T^d]: d = 1           (1)
P_1^{[2]}[T^d]: d ∈ {0,2}       (2)
P_1^{[3]}[T^d]: d = 1           (1)
P_1^{[4]}[T^d]: d = 2           (1)
Total printed: 1+1+2+1+1 = 6
```

So the printed P_1 table had 6 entries. Rick's D1 prose ("6 of 12") is thus correctly reporting the printed count (6), but the **denominator** (12) doesn't match the corrected table (13). Clio's flag is real.

### 2.3 P_2 sanity check

Corrected P_2 table: $4+3+2+1 = 10$; original printed had $1+1+2+1 = 5$; prose "5 of 10" is consistent. So the discrepancy is P_1-only.

### 2.4 Which is right — 12 or 13?

The corrected table (13 entries) is the one used to actually re-derive the 13 SOURCE items via the contribution rule. Cross-check against the enumeration and the actual SOURCE (`step13_Lm1_corrected_SOURCE.py` lines 37–51) which lists exactly 13 non-L terms:

- P_3 side (6 terms): R_3 Hpp, coef_Hp Hp, coef_H2 H^2, 18 T^3 H Hp, T^4 H^3, 3 R_3 H K^2 [wait — 3 R_3(HK'+KH') is the c term, and 18 T^3 H^2 K is the e term] — recount:

SOURCE lines 37–51 has 13 terms (matching D4 P_3+P_2+P_1 = 6+5+2 = 13). All 13 SOURCE items check. The contribution rule $e = w - d + \mathrm{top}_X - 2$ applied to the **13-entry** P_1 table gives 2 P_1-side contributions (P_1 G e=0 and P_1 G e=1), matching D4's P_1 = 2 (excluding the pure-L slot which sits at P_1 G e=2 and moves into L-op).

**Verdict.** The corrected P_1 table (13 entries) is the *right* count. Rick's D1 prose "6 of 12" is a leftover from an earlier miscount of the corrected table's total — the "12" should have been "13". The printed count of 6 is fine.

**Report line for Rick:** In Day 178 §D1, "6 of 12 P_1-entries" should read "6 of 13 P_1-entries". The corrected P_1 table has 4+3+3+2+1 = 13 entries; only 6 of those were listed in the Day-174 printed table (the printed had P_1^{[0]} d=0, P_1^{[1]} d=1, P_1^{[2]} d∈{0,2}, P_1^{[3]} d=1, P_1^{[4]} d=2 — totalling 6). The P_2 count "5 of 10" is correct.

---

## 3. One-paragraph summary for the reply-to-Clio draft

- **D4 wording fix:** the printed $P_3=7$ over-counted by the $P_3 G^3$ e=2 *linear-in-$L$* slot $3 R_3 H^2 L$ — which is an $L$-op slot, not the *pure*-L slot. The unique pure-L slot ($R_1 \cdot L$) sits at $P_1 G$ e=2, as Clio notes. Rick's D4 gloss ("counting the L-slot") is imprecise and should be replaced with "counting one of the linear-in-$L$ slots that belongs to L-op, not SOURCE (specifically the $P_3 G^3$ e=2 slot $3 R_3 H^2 L$)".
- **D1 numeric fix:** "6 of 12" → "6 of 13"; the corrected P_1 support table has 13 entries.

Both are prose-only fixes; no numerics change; the 13-item SOURCE / L-op split (13 non-L + 3 L-op = 16 slots, or in Rick's D4 partition: 6+5+2 = 13 non-L plus pure-L at P_1 G e=2 plus two more L-op slots at P_2 G^2 e=2 (2 R_2 H L) and P_3 G^3 e=2 (3 R_3 H^2 L)) is unchanged.
