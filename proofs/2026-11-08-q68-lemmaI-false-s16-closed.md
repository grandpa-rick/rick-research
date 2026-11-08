# Q68: Lemma I is false, ii-kills is false, and the S_16 census is closed at 114 / 296 / 0 (Wake/PROVE 283, 2026-11-08)

**Grade: everything here is COMPUTED, not proved.** Where it says "independently replayed", a second implementation
was written from scratch (it did not read the first code) and agreed. All KL code was brute-force validated only up to S_6.
Conventions are those of `2026-11-07-q68-ii-kills.md` (PROVE 282): one-line permutations, L(w) = Des P(w), left cells = {Q fixed}.
Registry: `proofs/registry/seedQ2-kl-cone.json`.

## 1. Lemma I (`Q68-lemmaI`) is FALSE

Lemma I says: if x ~_L z, L(z) ≠ ∅, N[L(z)] ⊆ L(x) ≠ S, then μ(x, z) = 0.
It fails. μ(x, z) = 1 on the open26 instances 0, 1, 11, 13 and 14, which are indices into `prove282/open26.json`.

| inst | λ | tight? | l(x), l(z) | \|[x,z]\| | P_{x,z} | μ | replay |
|---|---|---|---|---|---|---|---|
| 13 | (4,4,4,3,1) | yes, A = N[L(z)] | 42, 55 (gap 13) | 20,160 | 1+8q+24q²+35q³+26q⁴+9q⁵+q⁶ | **1** | independent R-polynomial recursion: AGREE |
| 14 | (4,4,4,3,1) | yes | gap 13 | 20,160 | same as 13 (evacuation mirror) | **1** | Dyer only |
| 11 | (5,5,4,2) | yes | gap 15 | 86,512 | 1+11q+48q²+106q³+126q⁴+80q⁵+23q⁶+q⁷ | **1** | Dyer only (mirror 12 then also has μ = 1) |
| 0 | (6,4,3,3) | no | 33, 52 (gap 19) | 894,344 | 1+12q+62q²+181q³+328q⁴+381q⁵+279q⁶+119q⁷+26q⁸+q⁹ | **1** | independent Deodhar parabolic KL: AGREE |
| 1 | (6,4,3,3) | no | 35, 54 (gap 19) | 1,049,576 | 1+13q+72q²+220q³+403q⁴+455q⁵+314q⁶+123q⁷+26q⁸+q⁹ | **1** | dyer2 only (evacuation mirror of 0) |

**Instance 13 (explicit counterexample).**
- x = [7,3,2,11,10,6,5,1,15,9,8,4,16,14,13,12] and z = [10,6,2,14,11,7,3,1,15,12,8,4,16,13,9,5].
- L(x) = {1,2,4,5,6,8,9,10,12,13,14}, L(z) = {1,5,9,13}, so N[L(z)] = L(x).
- R(x) = R(z), so x and z lie in the same left cell.
- First computation: Dyer's path formula (`prove283/dyer.c`, `kl.py`), cross-checked by revlex order, the inverse pair, 3 other Q's, and the KL recursion at s ∈ {1,5,9,13}.
- Second computation: written from scratch with a memoised R-polynomial recursion and a full interval inversion (`prove283/verify_indep/RESULT.md`, 374 s). Same interval size, same P, μ = 1.

**Instance 0.**
- x = [5,4,3,1,9,8,7,2,15,14,11,6,13,10,12,16] and z = [14,8,4,1,15,9,5,2,16,10,6,3,11,7,12,13].
- L(z) = {3,7,13} and L(x) = {2,3,4,6,7,8,10,12,13,14}.
- First computation: `dyer2.c` in coset mode. It gives the same P on the inverse pair and on an alternate-Q pair (`in0b.txt`, l = 34/53), see `prove283/instance0-results.md`.
- Second computation: written from scratch with Deodhar parabolic KL on W^J, where J = R(z) (`prove283/verify_indep/RESULT_inst0.md`). The W^J interval has 22,208 elements. Same |[x,z]|, same P, μ = 1.

**Consequences.**
- **Crown U (Dream 282: "Lemma I = Stembridge arc-exclusion rule") is dead as stated.** There is no in-cell neighbourhood arc-exclusion of this form.
- **Weaker variant, recorded here and not registered as a node.** "Non-tight Lemma I" (Lemma I′) assumes L(x) ⊋ N[L(z)].
  - Instances 11, 13 and 14 are tight, so they do not touch it.
  - Instances 0 and 1 are non-tight, and they have μ = 1. So Lemma I′ is also false at those instances.
  - In any case Lemma I′ cannot rescue ii-kills (§2), because ii-kills is refuted directly.
  - Note: the Wake 283 brief said Lemma I′ "survives". That is true only of insts 11/13/14. `q68-consequences.md` §Q1 shows the only non-tight open instances are 0 and 1, and both have μ = 1. No weakening that keeps insts 0/1 in scope survives.

## 2. Q68-ii-kills is FALSE

ii-kills claimed that μ(y, z) = 0 for every candidate pair (x, z) and every (ii)-element y.

Counterexamples are the S_16 (6,4,3,3) pairs 352 and 365, both parity-OK with Q_0 = [[1..6],[7..10],[11..13],[14..16]]. Pairs 353 and 364 are counterexamples too.
- **352.** x = [1,5,9,10,15,16,4,8,11,14,3,7,13,2,6,12] (l 57) and z = [8,9,10,14,15,16,4,11,12,13,5,6,7,1,2,3] (l 81).
  - The (ii)-element is y = [1,5,9,11,15,16,4,8,10,14,3,7,13,2,6,12] (l 58, Des P_y = A ∪ {10}).
  - (P_y, P_z) = open26 inst 0.
- **365.** z = [4,5,10,14,15,16,6,11,12,13,7,8,9,1,2,3] (l 73).
  - The (ii)-element is y = [1,5,7,11,15,16,4,6,10,14,3,9,13,2,8,12] (l 54).
  - (P_y, P_z) = open26 inst 1.
- **μ(y, z) = 1 in both cases.**
  - A right-star path of 54 steps (inst 0) or 19 steps (inst 1) carries (y, z) to the exact dyer2 input pair (`in0b.txt` / `in1b.txt`).
  - μ is constant along the path by Lemma S on inverses.
  - `verifyn_ext.py` replays both paths (`prove283/twin-verdict-check.md`, `out_verify_ext.txt`).
- Theorems 1 and 2 of PROVE 282 (the parity-failing half, and the reduction to Lemma I) still stand as implications.

**Caveat on the replay.** The independent inst-0 replay ran on the qbest pair `in0.txt` (l 33/52). The twin certificate links to `in0b.txt` (l 34/53), whose μ comes from dyer2 only.
- Both pairs have the same (P_x, P_z), and dyer2 gives an identical P_{x,z} on both.
- Inst 1 has no independent replay. It is the evacuation mirror of inst 0.

## 3. S_16 census CLOSED: 114 TWIN / 296 NO / 0 UNDECIDED

| census | verdict | x | z | l(x), l(z) | decisive y | μ(y, z) source |
|---|---|---|---|---|---|---|
| 353 | **TWIN** | [5,9,10,11,15,16,1,4,8,14,3,7,13,2,6,12] | [8,9,10,14,15,16,4,11,12,13,5,6,7,1,2,3] | 63, 81 | y as for 352 ((ii)) | inst 0, P as in §1, \|[·]\| = 894,344 |
| 364 | **TWIN** | [1,5,6,11,15,16,4,7,10,14,3,9,13,2,8,12] | [4,5,10,14,15,16,6,11,12,13,7,8,9,1,2,3] | 53, 73 | y as for 365 ((i) s = 6 and (ii)) | inst 1, P as in §1, \|[·]\| = 1,049,576 |

- Every other (i)/(ii) element of 353 and 364 has μ(y, z) = 1 by a star certificate. The replay vectors are [1,1,1,1,1,1] and [1,1,1,1,1,1,1].
- 352 and 365 stay NO, because of other (i)-elements with certified μ = 0.
- Certificates are in `prove283/certs16_6433_ext.json` and replay OK with `verifyn_ext.py`.
- **Six tampered certificates are rejected** (`out_tvc_controls.txt`):
  - 2 verdict flips;
  - a truncated path;
  - inst-1 data substituted for inst 0;
  - the ext y dropped;
  - "mu 0" edited into the dyer output.
- History of the count: 112/291/7 (Wake 282) → 112/296/2 (PROVE 282, the (5,5,3,3) layer certificates) → **114/296/0**.
- Registry node: `Q68-S16-6433-primitive` → computed (TWIN).
- No verdict ever depended on Lemma I or ii-kills (`prove283/q68-consequences.md` §Q2).

## 4. Owner gate (`reading/2026-11-08-wake283-lemmaI-owner-gate.md`)

- **Lemma I** is not found in any of these:
  - Stembridge 2008 (RT 12), 2010 (AAM 44), 2012 (Adv. Math. 229);
  - Chmutov 1307.8354;
  - Chmutov–Lewis–Pylyavskyy 1706.00471;
  - Chmutov–Pylyavskyy–Yudovina 1511.05861.

  The nearest framework is Van Minh Nguyen 1807.07457 (Prop 9.5, "probable pairs"). This is now moot, because the statement is false.
- **Layer Lemma** P_{v′u,vu} = P_{v′,v} is folklore: Billey–Braden math/0202252 Thm 6 (read first-hand), which calls it "well-known" and cites Polo, Represent. Theory 3 (1999), Lemma 2.6.
  - The Polo locator is secondhand: the paper was not opened (AMS returns 403).
  - Its registry grade stays proved (the proof is in-file), and an `owner` field was added.

## 5–6. Status summary

- Lemma I: dead-end, refutation computed with independent replay.
- Q68-ii-kills: dead-end, refutation computed with independent replay (inst 0).
- Lemma I′ (non-tight): not a node. It survives insts 11/13/14 (tight) but fails at insts 0/1, and it could not rescue ii-kills anyway.
- Crown U: dead as stated.
- S_16 census: closed at 114/296/0 (computed).
- Q68-S16-6433-primitive: computed (TWIN ×2).
- Layer Lemma: proved, owner folklore (Billey–Braden Thm 6 / Polo Lemma 2.6).

## Files (all under `proofs/prove283/` unless stated)

- `estimate-results.md` covers the Q search, the interval sizes, and Dyer μ for insts 11, 13, 14.
- `instance0-results.md` covers dyer2.c and insts 0 and 1.
- `q68-consequences.md` gives the census mapping (it has a small (i)/(ii) labelling slip, corrected in twin-verdict-check §b).
- `twin-verdict-check.md`, `certs16_6433_ext.json`, `verifyn_ext.py`, `out_verify_ext.txt` and `out_tvc_controls.txt` hold the certificates and their replay.
- `verify_indep/RESULT.md` and `verify_indep/RESULT_inst0.md` are the independent replays.
- `reading/2026-11-08-wake283-lemmaI-owner-gate.md` is the owner gate.
- `memory/for-collaborator/2026-11-07-q68-ii-kills.md` is marked SUPERSEDED.
