# Q57: Theorem K beyond type C. Part 1 is FALSE as stated; it is TRUE for minuscule quotients (Theorem M)

PROVE 269 (session dated 2026-11-01, file named as PROVE.md asked). Bounded jewel: proofs/ and registry only. The draft
(9be3ae3), the FPSAC cut (6dbecb8) and the 11-04 note (39c11e7) are untouched.
Scripts are in `proofs/prove269/thmK/` (`k1.py` … `k11.py`, with `k7.out`). `k1,k2,k3,k11` run from `proofs/prove268/`
(full-group engine of q55.py). `k4`–`k10` run from `proofs/prove269/` (W^J-only engine of q_cominuscule_scout.py).

## Verdict

Labels follow the scout: (a) [x,y]_{W^J} is Boolean; (b) P^{J,q}_{x,y} = 1; (c) y = u·x with u a product of distinct,
pairwise commuting simple reflections and ℓ(y) = ℓ(u)+ℓ(x); (d) [x,y]_W ⊆ W^J. (PROVE.md's "Part 1" is (b)⇔(d).)

1. **(b)⇒(d) holds for every Coxeter system and every J.** This is already proved: PROVE 268, Theorem K0 + Lemma G1.
2. **(d)⇒(b) is FALSE in general.** There are three counterexamples, in increasing order of how much they hurt:
   - J = ∅. Here (d) is vacuous, and P^{∅,q} = P, which is not always 1.
   - A4 with J = {s1}, x = e, y = s3s2s4s3. This is proved by hand in §2.
   - **E6 with J = S∖{α4}, a maximal parabolic.** x = s6s2s4s5s1s3s2s4 and y = s4s5s6s3s2s4s5s1s3s2s4 (Bourbaki labels).
     [x,y]_W has 10 elements, all in W^J, with rank sizes 1,4,4,1. P_{x,y} = P^{J,q}_{x,y} = **1+q**. This is COMPUTED,
     by two independent engines (§2.3). There are 24 such pairs.

   So "maximal parabolic" is not the hypothesis either. The scout's controls never reached an example like this: their
   largest non-minuscule maximal case was E6 node 2.
3. **Theorem M (PROVED).** Suppose W is a Weyl group and λ is a minuscule dominant weight with stabiliser W_J. Then
   (b)⇔(c)⇔(d), and they imply (a). In that case [x,y]_W = {u'x : u' ≤ u} ≅ 2^{supp u}. The proof uses Min and the
   sign a_{st} ≤ 0, and nothing else; it does not need simply-laced. Every cominuscule (W,J) is covered, because the
   Coxeter data coincide: LG(n,2n) is the B_n spinor quotient, and the B_n quadric is C_n's ω_1.
4. **Prop E (PROVED, any Coxeter system, any J).** If y = w_0(L)·x with x minimal in W_L x and lengths adding, then
   (d) and (b) hold, and [x,y]_W = W_L x ≅ (W_L, Bruhat). (c) is the case where L is commuting. **The hexagon is
   L = {s2,s3} of type A2.** That answers Part 3: Boolean needs L commuting. Under Min, the commuting is forced, because
   left descents of elements of W^J pairwise commute.
5. **(a)⇒(d) in Theorem M** is proved for type C (PROVE 268 Theorem C) and for chains. For general minuscule λ it is
   only computed, or follows by citing Proctor's ideal model, which I have not deep-read. This is the GAP, §6.
6. What Part 2 actually uses is Min (minuscule), not distributivity. Distributivity is a consequence of Min (Proctor),
   and it is never used in the proof.

---

## 0. Conventions and imported facts

(W,S) is a Coxeter system and J ⊆ S. W^J is the set of minimal left-coset representatives (ℓ(zt) > ℓ(z) for all
t ∈ J). D_L(w) is the set of left descents. Imported facts:
- (LA) BB05 Prop 2.4.4; (SW) the subword property, BB05 Thm 2.2.2.
- (Z) the lifting property, BB05 Prop 2.2.7, in two forms. First: if u < w and s ∈ D_L(w)∖D_L(u), then su ≤ w and
  u ≤ sw. Second: if s ∈ D_L(u) ∩ D_L(w), then u ≤ w ⇔ su ≤ sw.
- (L1) KL79 (2.3.g) / BB05 Prop 5.1.8 (locator from memory). If s ∈ D_L(y), then P_{x,y} = P_{sx,y} for all x. The
  printed version is right-handed; apply P_{x,y} = P_{x^{-1},y^{-1}}.
- **Prop 1 / G1 / G2 / K0** (PROVE 266, PROVE 268; proved, any Coxeter system). For x ≤ y in W^J the following are
  equivalent: (d); xt ≰ y for all t ∈ J; dn(y, xW_J) = x. Under them P^{J,q}_{x,y} = P_{x,y}. Also
  P^{J,q}_{x,y}(0) = [(d)]. G2's first claim, mirrored by inversion: for x ∈ ^LW, u ↦ ux is an order isomorphism from
  W_L onto W_L x.

Two elementary facts about W^J. Both are proved here.
- (PS) W^J is closed under right factors. If y ∈ W^J and y = ab with ℓ(y) = ℓ(a)+ℓ(b), then b ∈ W^J. *Proof.* If
  bt < b with t ∈ J, then ℓ(yt) ≤ ℓ(a)+ℓ(b)−1, so t ∈ D_R(y). Contradiction.
  It is also closed under left-descent removal: z ∈ W^J and sz < z imply sz ∈ W^J. *Proof.* If (sz)t < sz, then
  ℓ(zt) ≤ 1+ℓ(szt) = ℓ(z)−1. Contradiction.
- (F3) Let x ≤ y in W^J satisfy (d), let s ∈ D_L(y), and let z ∈ [x,y]. Then sz ∉ zW_J∖{z}, i.e. sz ≠ zt for every
  t ∈ J. *Proof.* If sz = zt, then sz > z by (LA). Lifting gives sz ≤ y, so sz ∈ [x,y]∖W^J. ∎

**(L3) Descent transfer (any Coxeter system, any J).** Let x ≤ y in W^J satisfy (d), and let s ∈ D_L(x) ∩ D_L(y).
Then sx ≤ sy lie in W^J, and the pair (sx, sy) again satisfies (d).
*Proof.* sx ≤ sy holds by (Z), second form, and both lie in W^J by (PS). Let t ∈ J. By (LA), ℓ(sx·t) = ℓ(sx)+1 = ℓ(x),
and ℓ(xt) = ℓ(x)+1. Since xt = s·(sxt), we get s ∈ D_L(xt). By (Z), second form, sxt ≤ sy ⇔ xt ≤ y, and the right-hand
side is false by Prop 1. So sxt ≰ sy for every t ∈ J, and Prop 1 gives (d) for (sx, sy). ∎

## 1. (b) ⇒ (d): already done

P^{J,q}_{x,y} = 1 forces P^{J,q}_{x,y}(0) = 1, and K0 then gives dn = x, which is (d) by G1. This works for any
Coxeter system and any J. Nothing new is needed here.

## 2. (d) ⇏ (b): counterexamples

**2.1 J = ∅.** W^∅ = W and (d) always holds, but P^{∅,q} = P.

**2.2 A4, J = {s1} (proved by hand).** Put K = {s2,s3,s4}, x = e, y = s3s2s4s3. Every element of [e,y] is a subword
product (SW), so it lies in W_K. No element of W_K has a right descent in J = {s1}, so [e,y] ⊆ W^J, which is (d).
In W_K ≅ S_4 the element y is the permutation 3412 (relabel s2,s3,s4 as σ1,σ2,σ3; y = σ2σ1σ3σ2). KL polynomials
of a standard parabolic subgroup are its own. So P_{e,y} = P_{e,3412} = 1+q, the textbook singular Schubert variety
(machine: `k10.py` A3 control prints (1,1)). By K0, P^{J,q}_{e,y} = 1+q.
`k1.py` counts, over all J, the (d)-pairs with P ≠ 1: A3 J=∅: 6; B3 J=∅: 106; A4: 394 (J=∅), 20/12/12/20 (|J|=1),
0 (|J|≥2); C4: J=∅ 13476, |J|=1 734/374/274/282, and **|J|=2 already fails**: J={s1,s3}: 6, J={s1,s4}: 12, J={s2,s4}: 12
(0-based (0,2),(0,3),(1,3)). Every maximal parabolic in these four groups has 0 failures.

**2.3 E6, J = S∖{α4}, a maximal parabolic (COMPUTED).** The pair is
x = s6 s2 s4 s5 s1 s3 s2 s4 (ℓ = 8) and y = s4 s5 s6 s3 s2 s4 s5 s1 s3 s2 s4 (ℓ = 11).
- `k10.py` builds [x,y]_W by enumerating all 2^11 subwords of the reduced word of y (SW) and keeping those ≥ x. It finds
  10 elements, with rank sizes 1,4,4,1, and each has right descent set exactly {s4}, so (d) holds. It then computes
  P_{x,y} from the full-group R-recursion and the inversion formula on that interval, getting **1+q**. The same code
  reproduces P_{s2,s2s1s3s2} = 1+q and the hexagon P = 1 in A3.
- `k8.py`/`k9.py` find the same 24 pairs independently, from the W^J-only engine and the recursion of §5.3. The
  diagnosis there is N = 0, so P = 1+q.
- By K0, P^{J,q}_{x,y} = P_{x,y} = 1+q. The second listed pair, x = s3s2s4s5s4s1s3s2s4 and
  y = s5s6s4s3s2s4s5s4s1s3s2s4, behaves the same way.
- `k5.py` checks (b)⇔(d) with the parabolic R-recursion and finds 0 failures on every node of F4, B4, B5, D5 and A6,
  and on E6 node 3. `k7.out` shows which maximal parabolics even allow the dangerous configuration ("doubly stuck" with
  gap ≥ 3, §5.3): only E6 node 4 does (24 pairs), among F4, B4, C4, D5, A5, B5, D6 and E6.
- Grade: COMPUTED, not proved by hand. A hand proof would need the 10-element interval and its R-polynomials.

## 3. Prop E: a sufficient condition for any Coxeter system and any J

**Prop E.** Let x, y ∈ W^J and L ⊆ S with W_L finite. Assume sx > x for all s ∈ L (so x ∈ ^LW), and
y = w_0(L)·x with ℓ(y) = ℓ(w_0(L)) + ℓ(x). Then:
(i) [x,y]_W = W_L x, and u ↦ ux is a poset isomorphism (W_L, ≤) → [x,y];
(ii) [x,y]_W ⊆ W^J, i.e. (d) holds;
(iii) P_{x,y} = P^{J,q}_{x,y} = 1.
*Proof.* Since x ∈ ^LW, ℓ(ux) = ℓ(u)+ℓ(x) for u ∈ W_L (mirror of LA). Each s ∈ L lies in D_L(y), because
s w_0(L) < w_0(L) and lengths add.

*W_L acts on [x,y].* Let z ∈ [x,y] and s ∈ L. If sz > z, then z < y and s ∈ D_L(y)∖D_L(z), so lifting gives sz ≤ y,
and sz > z ≥ x. If sz < z, then sz < z ≤ y. Also z ≠ x, because the descent sets differ, so x < z with
s ∈ D_L(z)∖D_L(x), and lifting gives x ≤ sz.

*(i).* For z ∈ [x,y] let z_0 be the minimum of W_L z, which is in [x,y] by the action. Then w_0(L) z_0 ∈ [x,y] has
length ℓ(w_0(L)) + ℓ(z_0) ≤ ℓ(y), so ℓ(z_0) ≤ ℓ(x). Since z_0 ≥ x, z_0 = x. Hence [x,y] = W_L x, and G2 (mirrored)
gives the order isomorphism.

*(ii).* z = ux is a right factor of y = (w_0(L)u^{-1})·(ux), with lengths adding, so z ∈ W^J by (PS).

*(iii).* L ⊆ D_L(y), so by (L1) P_{z,y} = P_{sz,y} for all z and all s ∈ L. Hence P_{·,y} is constant on the orbit
W_L x, and P_{x,y} = P_{y,y} = 1. By (ii) and K0, P^{J,q}_{x,y} = P_{x,y}. ∎

**Corollary E′. (c) ⇒ (a), (b), (d) for any Coxeter system and any J.** If y = ux as in (c), set L = supp u, so that
w_0(L) = u. Then x ∈ ^LW, because y = (us)(sx) forces ℓ(sx) ≥ ℓ(y)−ℓ(us) = ℓ(x)+1. Prop E applies, and
[x,y]_{W^J} = [x,y]_W ≅ (Z/2)^L with subset order (subword property), which is Boolean. ∎

## 4. Theorem M: minuscule quotients

**Setting.** Φ is a finite crystallographic root system with Weyl group W, simple roots α_s, coroots α_s^∨ and
a_{ts} := ⟨α_s, α_t^∨⟩ ≤ 0 for t ≠ s. λ is a dominant weight, J = {s : ⟨λ,α_s^∨⟩ = 0}, and Stab_W(λ) = W_J
(Humphreys, *Lie algebras* 10.3; standard). For z ∈ W^J put c_s(z) := ⟨zλ, α_s^∨⟩. **(Min)**: λ is minuscule, so
c_s(z) ∈ {−1,0,1} for all z and s. (The proof works verbatim for Kac–Moody realisations.)

- (C) c_t(sz) = c_t(z) − c_s(z) a_{ts}, and c_s(sz) = −c_s(z). This is immediate from s·μ = μ − ⟨μ,α_s^∨⟩α_s.
  (When sz ∉ W^J, apply it to the orbit point szλ = (sz)^J λ. We only use it when sz ∈ W^J.)
- (F1) Let z ∈ W^J. If c_s(z) > 0, then sz > z and sz ∈ W^J. If c_s(z) = 0, then sz = zt with t ∈ J. If c_s(z) < 0,
  then sz < z and sz ∈ W^J.
  *Proof.* sz > z ⇔ z^{-1}α_s > 0, and c_s(z) = ⟨λ, (z^{-1}α_s)^∨⟩, which is ≥ 0 when z^{-1}α_s > 0 and ≤ 0 otherwise.
  c_s(z) = 0 ⇔ z^{-1}sz fixes λ ⇔ z^{-1}sz ∈ W_J. Then sz = zt' with t' ∈ W_J a reflection, and ℓ(zt') = ℓ(z)+ℓ(t') =
  ℓ(z) ± 1 by (LA), so t' ∈ J. If c_s(z) ≠ 0 and sz > z with sz ∉ W^J, the exchange condition on (sz)t < sz forces
  sz = zt, which is excluded. The case sz < z is (PS). ∎

**Lemma D (Min).** For y ∈ W^J, D_L(y) is pairwise commuting.
*Proof.* Let s ≠ t lie in D_L(y). Then c_s(y) = c_t(y) = −1 by (F1) and Min, and sy ∈ W^J. By (C),
c_t(sy) = −1 + a_{ts} ≥ −1 by Min, so a_{ts} = 0, which means m_{st} = 2. ∎

**Lemma NS ("no stuck pairs", Min).** Let x < y in W^J satisfy (d). Then some s ∈ D_L(y) has c_s(x) > 0, i.e. sx > x.
*Proof.* Suppose not, and pick a counterexample (x,y) with ℓ(y) minimal. y ≠ e, so D_L(y) ≠ ∅. For every s ∈ D_L(y),
c_s(x) ≠ 0 by (F3)+(F1), so c_s(x) = −1. Fix s ∈ D_L(y). By (L3), (sx, sy) satisfies (d), and sx < sy because the length
gap is the same. Since ℓ(sy) < ℓ(y), minimality gives r ∈ D_L(sy) with c_r(sx) > 0, so c_r(sx) = 1 by Min. r ≠ s,
because c_s(sy) = +1. By (C), 1 = c_r(sx) = c_r(x) − c_s(x)a_{rs} = c_r(x) + a_{rs}, so c_r(x) = 1 − a_{rs} ≥ 1. By Min,
a_{rs} = 0 and c_r(x) = 1. Then (C) gives c_r(y) = c_r(sy) + 0 < 0, so r ∈ D_L(y) and c_r(x) > 0. This contradicts the
choice of (x,y). ∎

**Theorem M.** Under Min, for x ≤ y in W^J: (b) ⇔ (c) ⇔ (d), and these imply (a), with [x,y]_W = {u'x : u' ≤ u}
Boolean.
*Proof.* (b)⇒(d) is §1. (c)⇒(a),(b),(d) is Cor E′.
(d)⇒(c): start at x_0 = x. While x_i ≠ y, Lemma NS gives s_i ∈ D_L(y) with s_i x_i > x_i. By lifting, x_{i+1} := s_i x_i
lies in [x_i, y] ⊆ W^J, so (x_{i+1}, y) satisfies (d). The process ends at y, with y = s_{g−1}⋯s_0 x and lengths adding.
All s_i lie in D_L(y), which is commuting by Lemma D. A reduced word in an elementary abelian Coxeter group has
distinct letters, so u := s_{g−1}⋯s_0 is as in (c). ∎
(This also gives a second proof of (d)⇒(b): (L1) along the chain gives P_{x,y} = P_{y,y}.)

**Scope.** W^J depends only on (W,J), and W(B_n) = W(C_n). Theorem M therefore covers:
- type A Grassmannians;
- D_n nodes 1, n−1, n; E6 nodes 1, 6; E7 node 7;
- B_n node n, using the minuscule ω_n of B_n. This quotient is C_n's LG. Theorem K of PROVE 268 is the special case.
- C_n node 1, using the minuscule ω_1 of C_n. This quotient is the B_n quadric.
It covers all the cominuscule cases of the scout table. Chains (G2, I2(m), and the quotients above) are also trivial
directly: a (d)-pair in a chain W^J has gap ≤ 1, because length-2 Bruhat intervals have 4 elements.

## 5. Part 3: sharpness, and what each hypothesis does

**5.1 The hexagon, by hand.** A3, J = {s2}, x = s1, y = s2s3s2s1 = w_0(L)·s1 with L = {s2,s3}, and s2x, s3x > x.
- Prop E gives [x,y]_W = W_L x = {s1, s2s1, s3s1, s3s2s1, s2s3s1, s2s3s2s1}, with ranks 1,2,2,1 and ≅ S_3 in Bruhat
  order (a hexagon).
- All six elements lie in W^J. Their right descents are {s1} or {s1,s3}, never s2, so (d) holds.
- P^{J,q} = P_{x,y} = 1. It is not Boolean: 6 ≠ 8, and the rank-2 sizes are 2 ≠ 3.
- Consistency with Prop 1: xs2 = s1s2 is not a subword of any reduced word of y (in every reduced word of y, the letter
  s1 comes last or only before the final s3), so s1s2 ≰ y.

**5.2 Which hypothesis does what.**
- *(c) and (a) are about the shape L*: Boolean ⇔ L commuting. Lemma D says Min forces this for L ⊆ D_L(y).
- *(d) ⇒ (b) is about whether collapse terminates*: Lemma NS. Min is used twice in NS: at c_r(sx) = 1, and to force
  a_{rs} = 0. When Min fails, (d) can hold without the left-descent collapse reaching y. Prop E covers that case when the
  collapse finishes in one W_L-coset, as the hexagon does.
- E6 node 4 is the case where it neither finishes nor recovers (§5.3).
- Distributivity of W^J is never used.

**5.3 The stuck recursion (remark, any Coxeter system, any J).** Let (x,y) satisfy (d) and s ∈ D_L(x) ∩ D_L(y).
- If x ≰ sy, the KL recursion (c = 1; the second and third terms need x ≤ sy) gives P_{x,y} = P_{sx,sy}, and (L3) keeps
  the pair (sx,sy) inside (d).
- If x ≤ sy =: v, assume all (d)-pairs with smaller top have P = 1. The recursion gives P_{x,y} = 1 + q(1 − N), where
  N = #{z : x ≤ z ⋖ v, sz < z}. The terms are: P_{sx,v} = 1, because (sx, v) satisfies (d) by the L3 argument;
  P_{x,v} = 1; and μ(z,v) ≠ 0 only for covers.
- For gap ≤ 2, P = 1 automatically (degree bound). The E6 node-4 pairs have gap 3 and N = 0 for every s ∈ D_L(y)
  (`k8.py`), hence P = 1+q.

## 6. Gaps (precise)

1. **(a) ⇒ (d) under Min, for general minuscule λ.**
   - Proved for type C LG (PROVE 268 Thm C, in-house shapes) and for chains.
   - For type A, D and E minuscule quotients it follows from Proctor's model: minuscule W^J ≅ J(P), with Bruhat order =
     inclusion. Then Lemma I (PROVE 268) gives Boolean ⇔ the skew is an antichain ⇔ (c). Locator is second-hand only:
     Proctor thesis Prop V.2 via Miura; not deep-read.
   - Computed with 0 failures on every scout cominuscule case (E7 node 7: 1463 pairs).
   - I tried an in-house induction. Its 0-pairing case (c_s(x) = 0 forces a 3-chain [x, srx]_{W^J}) works. The all-(−1)
     case did not close in this session.
2. **E6 node 4 is computed, not hand-proved.**
3. (L1) and the stabiliser/descent facts are cited from memory. They are textbook-standard (KL79, BB05, Humphreys).
4. No novelty claimed. Theorem M is very likely folklore near Proctor, Stembridge, Brenti and Boe.

## 7. Verification log

| script | what | result |
|---|---|---|
| k1.py | all J of A3, B3, A4, C4: (d)-pairs with P ≠ 1 | maximal J: 0 everywhere; fails for J = ∅, |J| = 1 (A4, C4) and |J| = 2 (C4) |
| k2.py / k3.py | "stuck" pairs (D_L(y) ⊆ D_L(x)) | occur for every non-minuscule J; in A3–C4 maximal J they are covers only |
| k4.py / k7.py (k7.out) | W^J-only, maximal J of F4, B4, C4, D5, A5, B5, D6, E6 | minuscule nodes: 0 stuck pairs (Lemma NS); doubly-stuck with gap ≥ 3: only E6 node 4 (24) |
| k5.py | (b) ⇔ (d) via parabolic R-recursion | 0 failures on all nodes of F4, B4, D5, B5, A6, and on E6 node 3 |
| k8.py, k9.py | E6 node 4 doubly-stuck pairs | N = 0 for every s; full-W R-polys give P = 1+q |
| k10.py | independent subword-interval + full-W KL | E6 pairs: 10 elements, ranks 1,4,4,1, all in W^J, P = 1+q; controls OK |
| k11.py | Prop E over all J of A3, B3, D4, A4 (1628 pairs) | 0 failures of (d) & P = 1 & [x,y] = W_D x |
