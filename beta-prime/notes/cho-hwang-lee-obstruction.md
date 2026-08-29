# Cho-Hwang-Lee (arXiv:2603.03886) — where it breaks for NCSF immaculate

Day 139. Read the paper. Six pages, one involution, done. Question: does it lift to
Benedetti-Sagan's open problem for S(S_alpha) in the immaculate basis? Answer below —
short version: **no, and the failure is not sign-tracking. It's that the coproduct on
S_alpha does not close on the immaculate basis, so there is no target set to build an
involution on.**

## 1. Their setup, tersely

Sym, Schur basis. Coproduct on skew Schurs:
  Delta(s_{lambda/mu}) = sum_{mu subset nu subset lambda} s_{nu/mu} tensor s_{lambda/nu}.
Iterate. Takeuchi with the projection pi (kills degree 0) forces STRICT inclusions:

  S(s_{lambda/mu}) = sum_k (-1)^k sum_{mu = lam_0 subsetneq ... subsetneq lam_k = lambda}
                          s_{lam_1/lam_0} * s_{lam_2/lam_1} * ... * s_{lam_k/lam_{k-1}}.       (2.1)

Each product s_{lam_i/lam_{i-1}} is a generating function for SSYT. So the whole thing is
a signed sum over

  X^lambda_mu = { (T^(1), ..., T^(k)) : T^(i) in SSYT(lam_i/lam_{i-1}), chain strict }.

Sign = (-1)^k = (-1)^{length}. Weight = product of x^{T^(i)} = one big monomial in the
concatenated multiset of entries. Since Sym is commutative and each factor is a plain
Schur (not skew of a fancier thing), the weight collapses to a monomial depending only on
the multiset of entries in the concatenated tableau T = (T^(1) | ... | T^(k)).

## 2. The involution Phi

Total order on cells: primary by entry value, secondary by column (left-to-right), ternary
by row (bottom-to-top, i.e., "reading order" biased). Given a chain-tuple T, look at each
cell c in T^(i), classify:

- SPLITTABLE: c is the largest cell in T^(i) AND |T^(i)| > 1.
  Operation: peel c off T^(i), insert singleton {c} as a NEW factor between T^(i) and T^(i+1).
  Length goes k -> k+1. Sign flips.

- MERGEABLE: |T^(i)| = 1 (say T^(i) = {c}), i > 1, T^(i-1) sqcup T^(i) is semistandard
  as a skew tableau, AND c is larger (in the total order) than every cell of T^(i-1).
  Operation: merge {c} into T^(i-1). Length k -> k-1. Sign flips.

Take the LARGEST cell (in the total order) that is either splittable or mergeable; if
none, T is a fixed point. Phi(T) = split or merge that cell.

Lemma 2 (the whole content): split and merge are mutual inverses and no other cell of
higher priority becomes splittable/mergeable after the move. Two-page argument, elementary.

**Fixed points** = every T^(i) is a singleton AND enumerating cells c_1 < c_2 < ... in the
total order gives c_{ell - i + 1} in T^(i). I.e., the singletons are stacked in REVERSE
order of the total order. Read this off the shape: the concatenation is a
**row-strict plane partition** on the skew shape (rows strictly decreasing,
columns weakly decreasing) — bijection with RSPP(lambda/mu).

Reverse the order on the alphabet: RSPP -> SSYT of the CONJUGATE shape. So

  S(s_{lambda/mu}) = (-1)^{|lambda|-|mu|} s_{lambda^t / mu^t}.

Done.

## 3. What their involution uses about Sym-Schur

Load-bearing structural facts:

**(A) Coproduct closes on the same basis.** Delta(s_{lambda/mu}) is a sum of
s_{nu/mu} tensor s_{lambda/nu} — the tensor factors are still (skew) Schurs. Iterating
(k-1) times keeps you inside "skew Schurs indexed by chains of partitions."

**(B) Skew Schurs have monomial expansions with combinatorial cells.**
s_{lambda/mu} = sum_{T in SSYT(lam/mu)} x^T. Each summand is a MONOMIAL indexed by a
cell-filling. So the k-fold product s_{lam_1/lam_0} * ... * s_{lam_k/lam_{k-1}} expands
as a sum over TUPLES of SSYT and the sign is on the tuple, not smeared inside a
signed expansion of each factor.

**(C) Commutativity of Sym.** Weight(T) depends only on the concatenated MULTISET of
entries. The involution changes T from being a chain-tuple to a chain-tuple of different
length, keeps the multiset of entries fixed, and that is enough to keep the weight fixed.
No monomial-vs-monomial cancellation *within* a single Schur summand is needed.

**(D) Order on cells is well-defined.** Two-dimensional shape (rows, columns) gives a
natural lex-type total order. The tie-breaking (i) entry value (ii) column L->R
(iii) row bottom-up is exactly what makes the RSPP condition come out.

**(E) Splitting is a local operation on skew shapes.** Removing the "largest" cell from
T^(i) leaves a valid skew shape because the largest cell is forced to be an
INNER CORNER of the ambient skew shape. Merging is legal iff the two adjacent tableaux
concatenate into a semistandard skew tableau — again purely local, decided by row/column
comparison.

## 4. Try to lift to NCSF, immaculate basis

Setup on the NCSF side (Benedetti-Sagan Sec 8, Berg-Bergeron-Saliola-Serrano-Zabrocki
BBS+14):

- NCSF = free assoc algebra Q<H_1, H_2, ...>. Coproduct Delta(H_n) = sum H_i tensor H_{n-i}.
  (Homogeneous, but NOT cocommutative in general at the level of products.)
- Immaculate basis S_alpha (alpha a composition) defined by NCSF-JT-determinant:
  S_alpha = Det(H_{alpha_i + j - i}).
- Under the forgetful map NSym -> Sym, S_alpha maps to s_alpha (Schur/0 depending on alpha
  being a partition).
- **Antipode on H_n**: S(H_n) = (-1)^n R_{1^n} in ribbon basis; in H basis this is
  S(H_n) = sum_{beta |= n} (-1)^{ell(beta)} H_beta (Takeuchi at the generator).
- Since S is an ANTI-algebra map, S(S_alpha) = S(Det(H_{alpha_i+j-i})) blows up into a
  sum with SIGNS coming from expanding the noncommutative determinant, then applying S
  factor-by-factor and REVERSING the order.

Benedetti-Sagan derive
  S(H_alpha) = (-1)^{|alpha|} sum_T S_{sh(T)},                                    (BS 23)
where T runs over dual immaculate tableaux of content (alpha_ell, ..., alpha_1)
(reversed). That formula is CLEAN — it uses the antipode on H's, then applies BBS+14's
multiplication rule S_lambda * S_alpha to normalize back to the immaculate basis. That
rule already has signs.

For **hooks and 2-rows** they get closed forms; for general alpha they conjecture no
clean formula. Zemel arXiv:2607.07870 (Jul 2026) does *not* touch this: he handles
QSym_q, QSym^(q), and only the trivial-permutation slice F^{Id_n}_alpha of
NCQSym-fundamental. Explicitly he says "our theorems cannot be extended to any other
part of the fundamental basis for that algebra" (near end of intro). So the immaculate
antipode is STILL open in general.

## 5. THE OBSTRUCTION — where Phi refuses to lift

Try to run the Cho-Hwang-Lee argument on S(S_alpha):

**Obstruction 1 (fatal, the load-bearing one): the coproduct on S_alpha is NOT a sum of
S_nu/mu tensor S_alpha/nu.** Immaculate has no "skew" version that closes the coproduct
on the same basis. Concretely, from BBS+14,

  Delta(S_alpha) = sum_{0 <= k <= ell} S_{(alpha_1, ..., alpha_k)} tensor
                     (something more complicated in the "right factor"),

where the right factor is NOT S of a composition — it involves creation operators / a
different set of tableaux. Iterating Delta^{k-1} does NOT give a chain of compositions
alpha_0 subset alpha_1 subset ... subset alpha_k = alpha with S_{alpha_i/alpha_{i-1}}
in each tensor slot, because **there is no S_{alpha_i/alpha_{i-1}}**. There is no
established "skew immaculate function" that plays the role of s_{lambda/mu} inside
Takeuchi's expansion.

Fact (A) from Sec 3 is where the whole scheme boots. It fails immediately. There is no
X^alpha_mu = disjoint union over chains of an SSYT-analog to build Phi on.

**Obstruction 2 (also fatal, independent): the H-basis expansion has signs BEFORE the
Takeuchi sign.** Even if you retreat to expressing S_alpha in the H-basis and running
Takeuchi at H's, you get
  Delta^{k-1}(H_alpha) = sum over decompositions of alpha (as a composition, ORDERED),
each summand a MONOMIAL in H_beta's, unsigned — fine so far. Apply Takeuchi:
  S(H_alpha) = sum_k (-1)^k sum_{decomp of alpha into k nonempty pieces} H_{piece_1} ... H_{piece_k}.
This is basically the same as Benedetti-Sagan's polynomial-algebra involution
(their Sec 2, F[x] case): the involution on ordered set partitions collapses to
(-1)^{ell(alpha)} times a single fixed point. That gives S(H_alpha) in the H-basis
easily (it's the reversal formula). But that is NOT S(S_alpha) in the immaculate basis
— to reindex from H-basis back to immaculate you need the CHANGE OF BASIS matrix
between H and S_. That change of basis has signs (dual immaculate tableaux, BS eq (23)).
Cancellations required to reach a clean formula for S(S_alpha) in {S_alpha} basis
live in the CHANGE-OF-BASIS layer, not in the Takeuchi expansion layer.

Cho-Hwang-Lee side-step this problem for Schurs because in Sym the coproduct on Schurs
is already Schur tensor Schur (via skew Schurs) — no change of basis required. That's
fact (A). NCSF has no analog.

**Obstruction 3 (structural, secondary): non-commutativity of the H-basis product means
the "weight" of a tuple depends on ORDER, not just multiset.** In Sym the tuple
(T^(1), ..., T^(k)) has weight = product of x^{T^(i)} = monomial in commuting x's. In
NCSF you have a product H_{gamma^(1)} ... H_{gamma^(k)} which is a WORD in H_1, H_2, ...
— you cannot freely reorder factors within an involution. Cho-Hwang-Lee's Phi swaps
adjacent factors' "boundary" (mergeable operation takes a singleton T^(i) and joins it
to T^(i-1); the reverse splits off the largest cell of T^(i) and re-inserts it as a NEW
factor between T^(i) and T^(i+1)). Both operations preserve the total concatenated
tableau because Sym is commutative — the ORDER of factors is irrelevant to the product.
In NCSF the product IS the ordered word, so an involution that changes the number of
factors changes the underlying word and you cannot claim "weight preserving" for free.

**Obstruction 4 (bookkeeping, not fatal on its own): the antipode is an ANTI-algebra map,
so S(H_alpha) reverses the composition.** Benedetti-Sagan handle this by an explicit
reversal (their eq (23) has content (alpha_ell, ..., alpha_1), reversed). Manageable
if you set up Phi carefully, but it's another sign convention to track.

## 6. Prognosis for phi-conjugation

Rick's Rule 6 (phi-conjugation) helps when you have a nice map phi and the obstruction is
"sign accounting off the commutative locus." That is NOT the primary obstruction here.
The primary obstruction is (1): **no closed skew-object exists on which to define the
chain-tuple set X**. You cannot phi-conjugate your way out of "the coproduct doesn't
close in the basis you want."

Options for using phi-conjugation:

**Option A (Sym-level, useless for the open problem).** phi := forgetful NSym -> Sym.
S(S_alpha) forgets to S(s_alpha) = (-1)^|alpha| s_{alpha^t} (if alpha is a partition).
Cho-Hwang-Lee then applies. But this collapses immaculate structure and loses the
information you want. Won't crack the open problem.

**Option B (H-basis intermediate).** phi := change-of-basis from S_ to H (or back).
S(S_alpha) is straightforward at the H level. The task becomes: find a sign-reversing
involution on the "unrolled" expression sum_{...} +/- H_beta after re-expanding back
via S_. This is essentially what Benedetti-Sagan themselves did in the hook and 2-row
cases (their Thm 8.3): they DO have an involution — the "change the lowest 1 to a 2 /
change the highest two 1s to a 1" operation on dual immaculate tableaux. That IS a
phi-conjugation-style attack, and it works for 2 rows. It stalls at 3+ rows because the
combinatorics of dual immaculate tableaux gets tangled and BBS+14's multiplication rule
S_lambda * S_alpha has more terms than the simple "change lowest one" involution can
absorb. **This is the concrete place to attack.**

**Option C (a genuinely new "skew immaculate" definition).** If someone (Grinberg? or the
Bergeron school) has defined a skew immaculate S_{alpha/beta} such that
Delta(S_alpha) = sum_beta S_beta tensor S_{alpha/beta} with a MONOMIAL expansion (say
over "immaculate skew tableaux"), then Cho-Hwang-Lee lifts almost verbatim, modulo
tracking word-order in the H products (Obstruction 3). I do not know of such a definition
— Bessenrodt-Luoto-van Willigenburg have "skew immaculate" but I recall the coproduct
does not close on them cleanly. FLAG: check Grinberg's Hopf Algebras notes (arXiv:1409.8356
— Cho-Hwang-Lee cite exactly this) for skew immaculate coproduct. If a closed formula
exists, Cho-Hwang-Lee's Phi lifts with edits, and phi-conjugation is used at
Obstruction 3 (word-order sign tracking). This is the LIVE hypothesis.

## 7. Campbell 2023 status

**Not found.** Searched Google Scholar for exact title "Antipodes of Immaculate Functions"
— zero hits. Searched arXiv for "Campbell antipode immaculate" — nothing. Searched
Semantic Scholar with DOI 10.1007/s00026-023-00641-7 (Annals Comb 27(3) candidate DOI) —
returns Rostam, "Identifying Young Diagrams Among Residue Multisets," not Campbell.
Semantic Scholar's rate-limited beyond that.

**Conclusion: either the reference is misremembered (author, title, year, or venue) or
the paper does not exist on arXiv and is not indexed by Google Scholar under that title.**

Guesses for what Rick may be remembering:
- Aliniaeifard-Wang 2022-ish on "Antipode formulas for NSym"?
- Some Hazewinkel-style formula I don't recognize?
- Benedetti-Sagan-Sagan's own follow-up?

I do NOT have Campbell 2023, cannot report on it. If Rick has a copy locally at
~/papers/ or ~/data/, point me at it and I'll re-check.

## 8. Bottom line

The Cho-Hwang-Lee involution is beautiful and totally specific to Sym: it exploits
(A) Delta closes on skew Schurs, (B) each skew Schur is a monomial GF over cell fillings,
(C) commutativity collapses "weight of tuple" to "monomial in multiset." NCSF/immaculate
loses (A) hard — there is no skew immaculate that closes the coproduct in the same basis.
Loses (C) too (word-order matters). phi-conjugation is the RIGHT hammer for (C) but not
for (A). Attack: either (i) develop a skew-immaculate with closed coproduct then lift Phi
via phi-conjugation for order-tracking, or (ii) extend BS's 2-row involution (change
lowest 1 to 2) via phi-conjugation to n rows. Option (ii) is more concrete and closer
to Rick's four successful firings on Psi(e_2^b) — those are also "small-tableau
involution + sign accounting" arguments.
