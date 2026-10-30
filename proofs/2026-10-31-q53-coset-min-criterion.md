# Q53 — the coset-minimum criterion, and Lemma A as its type-C corollary

PROVE 266, 2026-10-30. This is a bounded jewel: it goes in proofs/ and the registry only. The draft stays FROZEN.
Scripts: `proofs/prove266/check.py` (general), `proofs/prove266/checkC.py` (type C). Outputs are in `check.out`, `checkC.out`.

**Verdict.** Both halves are PROVED. The general half is a 4-line Coxeter lemma, provided we add the hypothesis
`z ≤ w` that the PROVE statement left out. The type-C half is the "key step" of the printed Rem 4.22 at 9be3ae3. I
re-derived it cold below, with every case checked, and it survives. So Lemma A = (Prop 1) + (Prop 2) + the rotation
dictionary (Lemma 3), and Crown N's "one root" is literal. The root is Property Z / the lifting property
[BB05 Prop 2.2.7], together with length-additivity on `W^J × W_J` [BB05 Prop 2.4.4] and the subword property
[BB05 Thm 2.2.2].

---

## 0. Conventions

`(W,S)` is a Coxeter group, `J ⊆ S`, and `W^J` is the set of minimal left-coset representatives (`ℓ(zs) > ℓ(z)` for
every `s ∈ J`). We use two standard facts.

- **(LA)** [BB05 Prop 2.4.4] For `z ∈ W^J` and `v ∈ W_J`, `ℓ(zv) = ℓ(z) + ℓ(v)`.
- **(SW)** [BB05 Thm 2.2.2] `x ≤ y` iff some (equivalently every) reduced word of `y` contains a subword that
  multiplies to `x`. In particular, a prefix of a reduced word of `y` is `≤ y`.

Put `C(w,z) := {u ∈ zW_J : u ≤ w}` and `dn(w, zW_J) := max C(w,z)` when the max exists (Deodhar). Put `E(z,w) := {s ∈ J : zs ≤ w}`.

## 1. The general criterion (Prop 1)

**Prop 1.** Let `z ∈ W^J` and `w ∈ W`. The following are equivalent:
(a) `dn(w, zW_J) = z`, meaning that `z ∈ C(w,z)` and `z` is the maximum of `C(w,z)`;
(b) `C(w,z) = {z}`;
(c) `z ≤ w` and `zs ≰ w` for every `s ∈ J`.

*Correction to the PROVE statement.* The hypothesis `z ≤ w` must be stated. If `z ≰ w`, then (c)'s second clause
can hold vacuously while `C(w,z) = ∅` and `dn` is undefined. Every `u ∈ zW_J` has `u ≥ z` by (LA)+(SW), since `z`
is a prefix. So `C(w,z) ≠ ∅` iff `z ≤ w`. In the type-C application `ρ ⊆ λ` gives `z_λ ≤ z_ρ`, so nothing is lost.

*Proof.* (a)⇒(b): every `u ∈ C(w,z)` satisfies `u ≤ z` by (a), and `z ≤ u` because `z` is a prefix of `u`
((LA)+(SW)). So `u = z`.
(b)⇒(c): `z ∈ C(w,z)` gives `z ≤ w`. If `zs ≤ w` for some `s ∈ J`, then `zs ∈ C(w,z) = {z}`, but
`ℓ(zs) = ℓ(z)+1`, a contradiction.
(c)⇒(b): `z ∈ C(w,z)`. Suppose `u = zv ∈ C(w,z)` with `v ∈ W_J`, `v ≠ e`. Pick a left descent `s` of `v`. Then
`s ∈ J`, because the descents of an element of `W_J` lie in `J` (a reduced word of `v` uses only letters of `J`).
Write `v = s v'` with `ℓ(v') = ℓ(v) − 1`. By (LA), `ℓ(u) = ℓ(z) + 1 + ℓ(v')`, so concatenating reduced words of `z`,
`s` and `v'` gives a reduced word of `u` with prefix `zs`. By (SW), `zs ≤ u ≤ w`, which contradicts (c).
(b)⇒(a) is trivial. ∎

Note that the existence of `dn` in general (Deodhar) is not used: Prop 1 characterises when `z` *is* the maximum.

*Literature.* This is folklore-level and is the printed "E-criterion" of Rem 4.22. I have not located it as a
numbered statement in BB05 Ch. 2 from memory. No browsing this session, so the locator check is deferred. It needs
no citation beyond (LA)+(SW).

## 2. The type-C translation

**Setting.** Type `C_m` with signed permutations. `s_c` (`c<m`) swaps coordinates `c, c+1`, and `s_m` negates
coordinate `m`. `J = S∖{s_m}`, so `W_J ≅ S_m` is the stabiliser of `ω = (1,…,1)`. For a strict partition `η` with parts
`≤ m`, `w_η ∈ W^J` is the minimal representative with `w_η ω = v_η` (`−1` exactly at positions `m+1−k`, `k ∈ η`).
`D(η)` is the shifted diagram `{(a,b) : 0 ≤ a, a ≤ b ≤ a+η_a−1}` inside the staircase `{0 ≤ a ≤ b ≤ m−1}`. The boxes
are ordered by `(a,b) ≤ (a',b')` iff `a ≤ a'` and `b ≤ b'`.

Two facts come from the draft, Lemma bonds (`lem:bonds`). They are re-checked by machine here, and the first is
re-derived in §2.1:
- `ℓ(w_η) = |η|`;
- Bruhat order on `{w_η}` is inclusion of diagrams.

### 2.1 Elementary facts

**(O) Shapes are order ideals.** The shifted diagrams in the staircase are exactly the order ideals of the staircase
poset. *Proof.* Let `I` be an order ideal. Row `a` of `I` is an interval starting at `(a,a)`, since
`(a,a) ≤ (a,b)`. Also `(a+1,b) ∈ I` implies `(a,b) ∈ I`, so row `a+1` ends no later than row `a`. Since it starts one
column later, it is strictly shorter or empty. The converse is clear. Consequently `b` is *removable* from `η`
(`D(η)∖b` is a shape) iff `b` is maximal in `D(η)`. And `b ∉ D(η)` is *addable* iff every box below `b` lies in
`D(η)`. On each diagonal `{(a,a+d)}` the boxes of `D(η)` form an initial segment, because
`(a,a+d) < (a+1,a+1+d)`.

**(T) Trichotomy** for a shape `η` and colour `c` (box `(a,a+d)` has colour `c = m−d`). Let `μ = v_η`.
- If `c<m` and `μ_c = μ_{c+1}`, then `s_c μ = μ`. So `s_c w_η = w_η u` with `u ∈ W_J∖{e}`. By (LA),
  `ℓ = |η|+ℓ(u) = |η| ± 1`, so `u = s_j` for some `j ≠ m`. This is **(iii)**.
- If `c<m` and `(μ_c, μ_{c+1}) = (+,−)`, swapping changes the part `m−c = d` into `d+1`. That adds the box at the end of
  the row of length `d`, which is on diagonal `d`, i.e. colour `c`. Then `s_c w_η` lies in the coset of `η+b`, which
  has minimal length `|η|+1`, and its own length is `|η| ± 1`. So it is the minimal representative: `s_c w_η = w_{η+b}`.
  This is **(i)**.
- `(−,+)` is (i) applied to `η − b` and gives `s_c w_η = w_{η−b}`. This is **(ii)**.
- For `c = m`, flipping `μ_m` adds or removes the part 1, i.e. the diagonal box. So `s_m` is always (i) or (ii).

The cases are mutually exclusive, because they are decided by `(μ_c, μ_{c+1})`. Hence a shape never has both an
addable and a removable box of the same colour.

**(Z) Lifting / Property Z** [BB05 Prop 2.2.7 and its corollary]. Suppose `sw < w`. Then:
if `sv > v`, `v ≤ w ⇔ v ≤ sw`; if `sv < v`, `v ≤ w ⇔ sv ≤ sw`.
(For the first: `⇐` is trivial. For `⇒`, `v ≠ w` because their descents differ, so `v < w`, and Prop 2.2.7 gives
`v ≤ sw`.)

### 2.2 Key step (Prop 2)

**Prop 2.** For shapes `η ⊆ ν`: `E(w_η, w_ν) = ∅` iff `ν/η := D(ν)∖D(η)` is an antichain.

*Proof.* Induct on `|ν|`. If `ν = η`, then `ν/η = ∅` is an antichain, and `w_η s_j ≰ w_η` for length reasons. Now
let `ν ≠ η`. We use a removable box `b` of `ν` of colour `c` and set `s = s_c`, so `s w_ν = w_{ν−b} < w_ν` by (T)(ii).
Throughout, `v = w_η s_j` has length `|η|+1` by (LA).

*Antichain ⇒ E = ∅.* Pick any removable `b` of `ν`.
- `b ∈ η`. Then `b` is maximal in `η ⊆ ν`, so by (O) it is removable in `η`, and (T) gives `s w_η = w_{η−b}`. So
  `sv = w_{η−b}s_j` has length `|η| < ℓ(v)`, and (Z) gives `v ≤ w_ν ⇔ w_{η−b}s_j ≤ w_{ν−b}`. Hence
  `E(w_η,w_ν) = E(w_{η−b},w_{ν−b})`, with skew `(ν−b)/(η−b) = ν/η`.
- `b ∉ η`. Every box below `b` lies in `ν`. It is not in `ν/η`, by the antichain property, so it lies in `η`. Hence
  `b` is addable to `η` (O), and `s w_η = w_{η+b}`. So `ℓ(sv) = |η|+2 > ℓ(v)`, and (Z) gives
  `E(w_η,w_ν) = E(w_η,w_{ν−b})`. The skew `(ν−b)/η = ν/η ∖ b` is an antichain, and `η ⊆ ν−b`.
In both cases induction gives `E = ∅`.

*Not antichain ⇒ E ≠ ∅.* Take `x < y` in `ν/η`, and choose `b ≥ y` maximal in `ν/η`.
- `b` is removable in `ν`. If `b' > b` were in `ν`, then `b' ∉ η`, since otherwise `b ∈ η`. So `b' ∈ ν/η`, which
  contradicts maximality.
- `b ∉ η`, and `b` is not addable to `η`, because `x < b` and `x ∉ η`.
Apply (T) to `η` and `c`:
- **(iii)** `s w_η = w_η s_j`. Take this `j`: `v = s w_η`, so `sv = w_η < v`. Then (Z) gives
  `v ≤ w_ν ⇔ w_η ≤ w_{ν−b}`, which holds since `η ⊆ ν−b`. So `j ∈ E`.
- **(i)** `s w_η = w_{η+b'}`, with `b'` addable of colour `c` and `b' ≠ b`. Write `b' = (k,k+d)`, the first non-`η`
  box on diagonal `d`, and `b = (a,a+d)` with `a ≥ k`, so `a > k`. For every `j`, `ℓ(sv) = |η|+2`, so (Z) gives
  `E(w_η,w_ν) = E(w_η,w_{ν−b})`. Now `b' < b'+(0,1) = (k,k+d+1) ≤ (k+1,k+1+d) ≤ b`, and `b'+(0,1) ≠ b`. Both boxes
  are in `ν−b` and not in `η`. So `(ν−b)/η` is not an antichain, and induction gives `E ≠ ∅`.
- **(ii)** `s w_η = w_{η−b''}`, with `b''` removable of colour `c`. Write `b'' = (k−1,k−1+d)`, the last `η`-box on
  diagonal `d`, and `b = (a,a+d)` with `a ≥ k`. For every `j`, `ℓ(sv) = |η| < ℓ(v)`, so (Z) gives
  `E(w_η,w_ν) = E(w_{η−b''},w_{ν−b})`, with `η−b'' ⊆ ν−b`. Now `b'' < b''+(0,1) = (k−1,k+d) ≤ (k,k+d) ≤ b`, and they
  are not equal. `b''+(0,1) ∉ η`, since `b''` is maximal in `η`. Both boxes lie in `(ν−b)/(η−b'')`, which is
  therefore not an antichain, and induction gives `E ≠ ∅`.
(Boundary: in (i) and (ii), diagonal `d` contains two distinct boxes `b' ≠ b` (resp. `b'' ≠ b`), so `d ≤ m−2` and
`+(0,1)` stays in the staircase.) ∎

### 2.3 The dictionary (Lemma 3) and Lemma A

**Lemma 3.** Let `κ^∨` be the strict partition with parts `[m]∖κ`, and `z_κ := w_{κ^∨}`, the minimal representative
with `z_κ ω = −v_κ`. Then `D(κ^∨) = rot(stair ∖ D(κ))`, where `rot(a,b) = (m−1−b, m−1−a)`. This is an
order-*reversing* involution of the staircase that preserves diagonals.
*Proof.* `(a,b) ∈ D(κ)` iff `κ_a ≥ d+1` (`d = b−a`), iff `N_d := #{k ∈ κ : k ≥ d+1} ≥ a+1`, since κ is strict. The
rotated box `(m−1−b, m−1−a)` has offset `d` and row `m−1−a−d`. It lies in `D(κ^∨)` iff
`#{k ∉ κ : d+1 ≤ k ≤ m} = (m−d) − N_d ≥ m−a−d`, iff `N_d ≤ a`, iff `(a,b) ∉ D(κ)`. ∎

**Corollary (Lemma A).** For `ρ ⊆ λ`: `dn(z_ρ, z_λ W_J) = z_λ` ⇔ `D(λ)∖D(ρ)` is an antichain.
*Proof.* `ρ ⊆ λ` ⇔ `η := λ^∨ ⊆ ν := ρ^∨`, so `z_λ ≤ z_ρ`. By Prop 1, `dn = z_λ` ⇔ `E(w_η,w_ν) = ∅`. By Prop 2 this
holds ⇔ `ν/η` is an antichain. By Lemma 3, `ν/η = rot(D(λ)∖D(ρ))`, and `rot` maps antichains to antichains. ∎

## 3. Verification (machine, from the stated claims; not from draft code)

`check.py` is a generic engine. It builds groups from the geometric representation, computes Bruhat order as the
transitive closure of `u → ut` with `ℓ(ut) < ℓ(u)` (the reflection definition, independent of (Z)), and checks
Prop 1 (a)⇔(b)⇔(c) and the existence of Deodhar's max for **every J ⊆ S**, every `z ∈ W^J`, and every `w ≥ z`:

| group | triples | failures | control `sz` (left mult) disagreements |
|---|---|---|---|
| A3 | 825 | 0 | 142 |
| A4 | 21681 | 0 | 3602 |
| B3 | 3025 | 0 | 414 |
| B4 | 208433 | 0 | 25024 |
| D4 | 54229 | 0 | 8392 |
| H3 | 18265 | 0 | 1954 |
| I2(5) | 121 | 0 | 14 |
| I2(8) | 289 | 0 | 24 |

`checkC.py`, type `C_m` with `m ≤ 5`, signed permutations. It also asserts `ℓ(w_η) = |η|`, Bruhat on `W^J` =
inclusion, `z_κ = w_{κ^∨}`, and Lemma 3.

| m | pairs ρ⊆λ | E=∅ (antichain) | Lemma A fails | Prop 2 fails | ctrl: only s_{m−1} | ctrl: "row-strip" |
|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 3 | 0 |
| 2 | 10 | 7 | 0 | 0 | 0 | 1 |
| 3 | 35 | 17 | 0 | 0 | 4 | 4 |
| 4 | 126 | 41 | 0 | 0 | 29 | 14 |
| 5 | 462 | 99 | 0 | 0 | 146 | 45 |

The pair counts 3/10/35/126/462 match the Wake 266 referee. The controls fire from `m = 3` on. At `m = 2` the
"only `s_{m−1}`" control is not a control, because `J = {s_1}`. At `m = 1` it is vacuous. Both are degenerate, as
expected.

Side observation, computed only (not chased; jewel discipline): the antichain-pair counts 3, 7, 17, 41, 99 follow
the Pell recurrence `a_m = 2a_{m−1} + a_{m−2}`.

## 4. Gaps

None in the logic. Cited premises: BB05 Prop 2.2.7, Prop 2.4.4 and Thm 2.2.2, all standard textbook. The deferred
item is only a *locator*: whether Prop 1 appears as a numbered statement (BB05 Ch. 2 exercises or Deodhar 1977).
Without browsing it is unverified, and it does not affect correctness.
