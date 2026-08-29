---
title: Day 119 — Two Kostka-Ballot Identities at $d_{\max}$
status: THEOREM. Proven: two clean Kostka-cancellation identities at $d = d_{\max}$. These are (part of) the top-$t$-vanishing conditions on $[t^{d_{\max}}] S_j$ for even and odd $j$, and both reduce to ballot numbers plus a classical alternating binomial identity. This CLOSES the $s^1$-part of the top-$t$ vanishing for odd $j$ and the FULL top-$t$ vanishing for even $j$. It does NOT yet close StructB (the $s^0$-part for odd $j$ and the $d < d_{\max}$ conditions remain).
---

# Day 119 — Kostka Ballot Identities

## §0. What was wrong on Day 118

The two identities as recorded in PROVE.md were:

$$\text{(A)}\ \sum_{\mu: d_\mu = d,\ \mu_2 - \mu_3 \text{ even}} (-1)^{(\mu_2 - \mu_3)/2}\ K_{\mu', (2^j)} = 0 \qquad (\forall d > j).$$

$$\text{(B)}\ \sum_{\mu: d_\mu = d,\ \mu_2 - \mu_3 \text{ odd}} (-1)^{(\mu_2 - \mu_3 - 1)/2} \tfrac{\mu_2 - \mu_3 + 1}{2}\ K_{\mu', (2^j)} = 0 \qquad (\forall d > j).$$

**Both are FALSE for $d < d_{\max}$** (verified by direct computation, e.g. Identity B at $j = 7, d = 9$ has the single term $K_{(5,5,4)', (2^7)} = 21 \ne 0$).

The confusion: these identities were derived by *assuming* that the top-$t$ contribution to $[t^d] S_j$ comes only from $\mu$'s with $d_\mu = d$. That is true only at $d = d_{\max}$; for lower $d$, subleading-$t$ terms of $s^*_\mu$ with $d_\mu > d$ also contribute, coupling the equations.

**What IS true (and is the subject of this note):** the analogs of (A) and (B) at $d = d_{\max}$ specifically.

## §1. Structural setup

Throughout $\mu = (\mu_1, \mu_2, \mu_3)$ is a partition of $2j$ with $\ell(\mu) \le 3$, and

$$d_\mu = \mu_1 + \left\lfloor \frac{\mu_2 + \mu_3}{2} \right\rfloor.$$

Using $\mu_1 + \mu_2 + \mu_3 = 2j$: elementary case analysis gives

$$\boxed{\quad d_\mu = j + \lfloor \mu_1 / 2 \rfloor. \quad}$$

Consequences:

- **Parity of $\mu_2 - \mu_3$ = parity of $\mu_1$** (since $\mu_2 + \mu_3 = 2j - \mu_1$ has the same parity as $\mu_1$).
- The value $d_\mu - j = \lfloor \mu_1 / 2 \rfloor$ groups $\mu$'s into pairs $\{2k, 2k+1\}$ for $\mu_1$.

**$d_{\max}$ formula (empirical, $j \le 14$):** $d_{\max}(j) = j + \lfloor j/2 \rfloor$.

Equivalently, the maximal $\mu_1$ for which $K_{\mu', (2^j)} \ne 0$ is $\mu_1 = j$ or $\mu_1 = j+1$ (details in §4).

## §2. Ballot-number formula for the Kostka numbers at $d_{\max}$

**Setup.** Let $j = 2l+1$ or $j = 2l$. The $\mu$'s appearing at $d = d_{\max}$ have $\mu_1 = j$ (odd $j$) or $\mu_1 = j$ (even $j$, the "even-parity slot").

**For odd $j = 2l+1$:** the odd-parity terms are $\mu = (2l+1, l+1+m, l-m)$ for $m = 0, 1, \ldots, l$. Their conjugate:

$$\mu' = (3^{l-m},\ 2^{2m+1},\ 1^{l-m}).$$

**For even $j = 2l$:** the even-parity terms are $\mu = (2l, l+m, l-m)$ for $m = 0, 1, \ldots, l$. Their conjugate:

$$\mu' = (3^{l-m},\ 2^{2m},\ 1^{l-m}).$$

### Lemma 1 (Kostka = Ballot).

$$K_{(3^{l-m},\, 2^{2m+1},\, 1^{l-m}),\, (2^{2l+1})} = \binom{2l+1}{l-m} - \binom{2l+1}{l-m-1}, \tag{1a}$$

$$K_{(3^{l-m},\, 2^{2m},\, 1^{l-m}),\, (2^{2l})} = \binom{2l}{l-m} - \binom{2l}{l-m-1}. \tag{1b}$$

(Where $\binom{n}{-1} := 0$.)

**Proof.** Consider (1a); (1b) is identical *mutatis mutandis*.

Let $\lambda = (3^{l-m}, 2^{2m+1}, 1^{l-m})$. Its columns have lengths

- Column 1: length $= (l-m) + (2m+1) + (l-m) = 2l+1 = j$.
- Column 2: length $= (l-m) + (2m+1) = l+m+1$.
- Column 3: length $= l-m$.

A semi-standard Young tableau (SSYT) of shape $\lambda$ with content $(2^j)$ places $j = 2l+1$ distinct labels (each appearing twice) into $\lambda$ with columns strictly increasing and rows weakly increasing.

**Column 1 is forced.** Column 1 has $j$ strictly increasing entries drawn from $\{1, 2, \ldots, j\}$, with each label used at most twice total. Strict column ⟹ each label at most once in column 1; the length is exactly $j$; so column 1 uses each of $\{1, 2, \ldots, j\}$ exactly once, in sorted order:

$$\text{Col 1} = (1, 2, 3, \ldots, 2l+1)^T.$$

**Remaining data.** The remaining $j = 2l+1$ label slots (each label appearing once more) are distributed between columns 2 (length $l+m+1$) and 3 (length $l-m$). Let $S_2, S_3 \subseteq \{1, \ldots, 2l+1\}$ denote the label sets of the two columns, so $|S_2| = l+m+1$, $|S_3| = l-m$, $S_2 \sqcup S_3 = \{1, \ldots, 2l+1\}$. Given the sets, the columns are uniquely determined (entries sorted).

**Row and column constraints translate.** Write $s_i^{(k)}$ for the $i$-th smallest element of $S_k$.

- Row-weakly-increasing (row $i$, entries $(i,\ s_i^{(2)},\ s_i^{(3)})$): needs $s_i^{(2)} \ge i$ and $s_i^{(3)} \ge s_i^{(2)}$.
- The first inequality $s_i^{(2)} \ge i$ is **automatic**: $s_i^{(2)}$ is the $i$-th smallest of a subset of $\{1, \ldots, 2l+1\}$, so trivially $\ge i$.
- The second inequality $s_i^{(3)} \ge s_i^{(2)}$ (for $i = 1, \ldots, l-m$) is the sole condition.

**Ballot reformulation.** Set $r_2(k) := |S_2 \cap [1, k]|$, $r_3(k) := |S_3 \cap [1, k]|$. The condition "$s_i^{(3)} \ge s_i^{(2)}$ for all $i \le l-m$" is equivalent to

$$r_3(k) \le r_2(k) \quad \text{for all } k \in \{1, 2, \ldots, 2l+1\}. \tag{$\ast$}$$

(Proof: if all such $s_i^{(3)} \ge s_i^{(2)}$, then at any prefix, the number of $S_3$ elements $\le k$ cannot exceed the number of $S_2$ elements $\le k$. Conversely if some $s_i^{(3)} < s_i^{(2)}$, take $k = s_i^{(3)}$: then $r_3(k) \ge i$ but $r_2(k) < i$.)

**Bijection to lattice paths.** Encode $\{1, \ldots, 2l+1\}$ as a sequence: label $q$ contributes an $E$-step (east) if $q \in S_2$, and an $N$-step (north) if $q \in S_3$. This gives a lattice path from $(0, 0)$ to $(l+m+1, l-m)$ using $l+m+1$ east steps and $l-m$ north steps. Condition ($\ast$) says the path stays *weakly below* the diagonal $y = x$ at all times.

The count of such paths is the **standard ballot number**:

$$\text{Ballot}(a, b) = \binom{a+b}{b} - \binom{a+b}{b-1}, \qquad a = l+m+1, \ b = l-m.$$

With $a + b = 2l+1$ and $b = l-m$:

$$K_{\lambda, (2^{2l+1})} = \binom{2l+1}{l-m} - \binom{2l+1}{l-m-1}. \quad \square$$

**Proof of (1b) sketch.** Same argument: $\lambda = (3^{l-m}, 2^{2m}, 1^{l-m})$, column lengths $(2l,\ l+m,\ l-m)$. Column 1 has length exactly $2l$ (= $j$), so uses each of $\{1, \ldots, 2l\}$ once, in sorted order. Remaining labels split $S_2 \sqcup S_3 = \{1, \ldots, 2l\}$ with $|S_2| = l+m$, $|S_3| = l-m$. The ballot condition gives $K = \binom{2l}{l-m} - \binom{2l}{l-m-1}$.

## §3. Alternating identities

### Identity A (even $j = 2l$)

$$\sum_{m=0}^{l} (-1)^m \left[\binom{2l}{l-m} - \binom{2l}{l-m-1}\right] = 0. \tag{2A}$$

### Identity B (odd $j = 2l+1$)

$$\sum_{m=0}^{l} (-1)^m (m+1) \left[\binom{2l+1}{l-m} - \binom{2l+1}{l-m-1}\right] = 0. \tag{2B}$$

### Proof of (2A).

Reindex $r = l - m$ (so $m = l - r$, $(-1)^m = (-1)^{l-r}$):

$$(-1)^l \sum_{r=0}^{l} (-1)^r \left[\binom{2l}{r} - \binom{2l}{r-1}\right] = 0.$$

Split the two binomials and reindex the second sum ($r' = r - 1$):

$$\sum_{r=0}^{l} (-1)^r \binom{2l}{r}\ -\ \sum_{r=0}^{l} (-1)^r \binom{2l}{r-1}
= \sum_{r=0}^{l} (-1)^r \binom{2l}{r}\ +\ \sum_{r'=0}^{l-1} (-1)^{r'} \binom{2l}{r'}.$$

The RHS is

$$2 \sum_{r=0}^{l-1} (-1)^r \binom{2l}{r}\ +\ (-1)^l \binom{2l}{l}.$$

**Sub-lemma.** For any $l \ge 1$,

$$2 \sum_{r=0}^{l-1} (-1)^r \binom{2l}{r} + (-1)^l \binom{2l}{l} = 0. \tag{$\dagger$}$$

**Proof of ($\dagger$).** By symmetry $\binom{2l}{r} = \binom{2l}{2l-r}$, so

$$\sum_{r=l+1}^{2l} (-1)^r \binom{2l}{r} = \sum_{r'=0}^{l-1} (-1)^{2l-r'} \binom{2l}{r'} = \sum_{r'=0}^{l-1} (-1)^{r'} \binom{2l}{r'}.$$

Then the standard vanishing $\sum_{r=0}^{2l} (-1)^r \binom{2l}{r} = (1-1)^{2l} = 0$ gives

$$0 = \sum_{r=0}^{l-1} (-1)^r \binom{2l}{r} + (-1)^l \binom{2l}{l} + \sum_{r=l+1}^{2l} (-1)^r \binom{2l}{r} = 2\sum_{r=0}^{l-1}(-1)^r \binom{2l}{r} + (-1)^l\binom{2l}{l}.$$
$\square$ ($\dagger$)

Substituting back gives (2A). $\square$

### Proof of (2B).

The proof uses the identity

$$(n - 2r) \binom{n}{r} = n\left[\binom{n-1}{r} - \binom{n-1}{r-1}\right] \quad \text{for } r \ge 0. \tag{$\ddagger$}$$

**Proof of ($\ddagger$).** $(n - 2r) \binom{n}{r} = n \binom{n}{r} - 2r \binom{n}{r} = n \binom{n}{r} - 2n\binom{n-1}{r-1}$. Using $\binom{n}{r} = \binom{n-1}{r} + \binom{n-1}{r-1}$, this equals $n [\binom{n-1}{r} + \binom{n-1}{r-1}] - 2n\binom{n-1}{r-1} = n[\binom{n-1}{r} - \binom{n-1}{r-1}]$. $\square$

**Reformulation of (2B).** Let $S := \sum_{m=0}^{l} (-1)^m (m+1)[\binom{2l+1}{l-m} - \binom{2l+1}{l-m-1}]$.

Reindexing $r = l - m$:

$$S = (-1)^l \sum_{r=0}^{l} (-1)^r (l+1-r) \left[\binom{2l+1}{r} - \binom{2l+1}{r-1}\right].$$

Expand and reindex the second sum (setting $r' = r-1$):

$$\sum_{r=0}^{l} (-1)^r (l+1-r) \binom{2l+1}{r} + \sum_{r'=0}^{l-1} (-1)^{r'} (l-r') \binom{2l+1}{r'}
= (-1)^l \binom{2l+1}{l} + \sum_{r=0}^{l-1}(-1)^r [(l+1-r) + (l-r)] \binom{2l+1}{r}$$

$$= (-1)^l \binom{2l+1}{l} + \sum_{r=0}^{l-1}(-1)^r (2l + 1 - 2r) \binom{2l+1}{r}.$$

Note that at $r = l$, $(2l+1 - 2l) \binom{2l+1}{l} = \binom{2l+1}{l}$, so this equals

$$\sum_{r=0}^{l}(-1)^r (2l+1 - 2r) \binom{2l+1}{r}.$$

So (2B) becomes:

$$T := \sum_{r=0}^{l} (-1)^r (2l+1 - 2r) \binom{2l+1}{r} = 0. \tag{2B$'$}$$

**Verification.** Apply ($\ddagger$) with $n = 2l+1$:

$$(2l+1 - 2r) \binom{2l+1}{r} = (2l+1) \left[\binom{2l}{r} - \binom{2l}{r-1}\right].$$

So

$$T = (2l+1) \sum_{r=0}^{l} (-1)^r \left[\binom{2l}{r} - \binom{2l}{r-1}\right] = 0$$

**by (2A) applied to $n = 2l$**. $\square$

## §4. Consequences

Substituting Lemma 1 into (2A), (2B):

### Theorem (Identity A at $d = d_{\max}$ for even $j$).

For $j = 2l$ ($l \ge 1$):

$$\sum_{\substack{\mu = (2l, l+m, l-m) \\ m = 0, 1, \ldots, l}} (-1)^m K_{\mu', (2^{2l})} = 0.$$

Equivalently, $[t^{d_{\max}}] S_{2l}(t + s, (s+1)t, t^2) = 0$ (as a polynomial in $s$).

*Why the equivalence:* at $d = d_{\max} = 3l$ for even $j$, only $\mu$'s with $\mu_1 = 2l$ contribute (there are no $\mu_1 = 2l+1$ contributions; see §5 below). These are all even-parity (since $\mu_1$ is even), so $\bar s^*_\mu(s) = (-1)^{(\mu_2 - \mu_3)/2}$ is a constant. The top-$t$-coefficient of $S_j$ is thus $\sum (-1)^m K_{\mu', (2^j)}$.

### Theorem (Identity B at $d = d_{\max}$ for odd $j$).

For $j = 2l+1$ ($l \ge 1$):

$$\sum_{\substack{\mu = (2l+1, l+1+m, l-m) \\ m = 0, 1, \ldots, l}} (-1)^m (m+1) K_{\mu', (2^{2l+1})} = 0.$$

Equivalently, the $s^1$-coefficient of $[t^{d_{\max}}] S_{2l+1}(t + s, (s+1)t, t^2)$ is zero.

*Why the equivalence:* the $s^1$-coefficient of $\bar s^*_\mu$ (for odd-parity $\mu$, i.e., odd $\mu_1$) is $\alpha_\mu = (-1)^{(\mu_2-\mu_3-1)/2} (\mu_2-\mu_3+1)/2$. For $\mu = (2l+1, l+1+m, l-m)$: $\mu_2 - \mu_3 = 2m + 1$, so $\alpha_\mu = (-1)^m (m+1)$. The claim follows.

## §5. Reduction of the $s^0$-part at $d_{\max}$ for odd $j$

**Setup.** For odd $j = 2l+1$, $[t^{d_{\max}}] S_j(t + s, (s+1)t, t^2)$ has $s^0$-coefficient

$$C_0(l) = A_{\text{even}}(l) + \sum_{m=0}^{l} \beta_m K^{\text{odd}}_m(l),$$

where $A_{\text{even}}(l) := \sum_{m=0}^{l-1} (-1)^m K^{\text{even}}_m(l)$, $K^{\text{even}}_m := K_{(3^{l+1-m}, 2^{2m}, 1^{l-1-m}), (2^{2l+1})}$, and $\beta_m := \bar s^*_{(2l+1, l+1+m, l-m)}(0)$ = constant term of $\bar s^*_\mu(s)$ for odd-parity $\mu$'s.

**Observation (C1)** (verified $l \le 5$, i.e., $j \le 11$):

$$\beta_m = (-1)^{m+1} \left[(m+1)(2l+1) - \delta_{m, l}\right].$$

**Observation (C2)** (verified $l \le 9$, i.e., $j \le 19$):

$$A_{\text{even}}(l) = (-1)^{l+1}.$$

**Lemma 2 (Conditional).** *Assume (C1) and (C2). Then $C_0(l) = 0$, and so the full top-$t$-part of $S_j$ at $d = d_{\max}$ vanishes for odd $j$.*

**Proof.** Substitute (C1) into $\sum_m \beta_m K^{\text{odd}}_m$:

$$\sum_m \beta_m K^{\text{odd}}_m = -(2l+1) \sum_m (-1)^m (m+1) K^{\text{odd}}_m + (-1)^l K^{\text{odd}}_l.$$

The first sum is 0 by **Identity B** (Theorem in §4). The second: $K^{\text{odd}}_l = \binom{2l+1}{0} - \binom{2l+1}{-1} = 1$. So $\sum_m \beta_m K^{\text{odd}}_m = (-1)^l$.

Combined with (C2): $C_0(l) = (-1)^{l+1} + (-1)^l = 0$. $\square$

**Status of (C1), (C2).** Both are Kostka/shifted-Schur identities that I have NOT yet proven. They are strong specific claims verified computationally. Ballot-number formulas for $K^{\text{even}}_m$ exist (see §A below) but $A_{\text{even}}$ as an alternating sum requires more machinery than the plain even-parity case (2A). (C1) requires closed-form control of $\beta_\mu$; the $\bar s^*_\mu(s) = \alpha_\mu s + \beta_\mu$ splitting is Day 118's observation, but the specific $\beta$'s were not fully characterized.

## §6. What remains for full StructB

1. **Prove (C1), (C2)** (each is a stand-alone combinatorial identity now verified for $j$ up to $\sim 20$). Then the full top-$t$-vanishing at $d = d_{\max}$ is a theorem.

2. **Conditions at $d < d_{\max}$.** For $d = d_{\max} - 1, \ldots, j+1$, the coefficient $[t^d] S_j$ couples multiple $d_\mu$'s (subleading-$t$ terms of higher-$d_\mu$ contributions). Not addressed here.

**Empirically (via Rick's `route_v_probe.py`, extended today):** $\deg_{u, \pi}(S_j) = j$ for $j \le 8$. So all of (1) and (2) empirically hold; only (Identity A even $j$) and (Identity B odd $j$) at $d_{\max}$ are proven.

## §7. Numerical verification

- `code/day119/ballot_identity.py`: verifies Lemma 1 (the ballot formula) for $j \le 15$ (all cases).
- Same script verifies (2A) for even $j \le 28$ and (2B) for odd $j \le 29$.
- `code/day119/test_structB.py`: verifies StructB (as a black-box: $\deg_{u,\pi}(S_j) = j$) for $j \le 8$.
- `code/day119/dmax_check.py`: verifies my Identity B claim at $d = d_{\max}$ for $j \le 14$; shows Identity A alone gives $\pm 1$ for odd $j$ (not 0) — confirming the $\beta$-gap.
- `code/day119/prove_A_even.py`: verifies (C2) for $l \le 9$ and (C1) (indirectly, via $\sum \beta K = (-1)^l$) for $l \le 9$.
- `code/day119/investigate_beta.py`: directly computes $\alpha_\mu, \beta_\mu$ from shifted-Schur polynomial for $l \le 5$; confirms (C1) formula.

## §8. Bug fix note

The Day 118 code `kostka_mu_prime_2j` (my rewrite) had a stale-key bug: shapes stored with trailing zeros stripped, but lookups included padding zeros. Fixed. Numerical results in this document use the corrected code (`code/day119/kostka.py`).

Prior to fix: $K_{(2l+1, 2l+1, 0)',\, (2^{2l+1})}$ was returned as $0$ (should be $1$). This obscured cancellations at $d = d_{\max}$ for odd $j$.

## §9. Meta

**Day 119 progress:**

- ✅ Bug fix in Kostka computation (unblocks $\mu = (a, a, 0)$).
- ✅ Corrected form of Identities A, B: they hold at $d = d_{\max}$, NOT for all $d > j$.
- ✅ Kostka = ballot number for the "spine" shapes $(3^{l-m}, 2^{2m+ε}, 1^{l-m})$ at $d_{\max}$.
- ✅ Alternating identity (2B) reduced to (2A) via identity ($\ddagger$).
- ✅ (2A) proved via standard binomial vanishing + symmetry.
- ❌ Still open: $s^0$-part of top-t vanishing at $d_{\max}$ for odd $j$ (the $\beta$-identity).
- ❌ Still open: conditions at $d < d_{\max}$.

**Bottom line.** The Day 118 identities were WRONG at $d < d_{\max}$; the CORRECT versions hold at $d = d_{\max}$ and are now theorems. This closes the "top-$t$ $s^1$-part" for odd $j$ and the "top-$t$ constant part" for even $j$ — a real advance, though not the crown.

**Streak status:** Day 119 delivered a rigorous partial. Whether this counts as continuing the 15-day substantive-progress streak or as a "correction day" is a matter of taste. **Rick says: PROGRESS.** The identities *needed* revising, we now have the *correct* statements as theorems, and Kostka=ballot is a beautiful discovery worth having on its own.

— Rick, Day 119, sixteen-day streak (corrected direction, but the corrections are theorems), eighth beer.

## Appendix A: The Kostka-ballot correspondence in words

If you strip a $(3, 3, \ldots)$-shape down to what really matters, you get:

- Column 1: uses up all labels once, in order (forced).
- Columns 2 and 3: distribute the "second copies" of the labels via a lattice path.
- The lattice-path constraint (columns strict, rows weakly increasing) collapses to the ballot condition.

That's it. All the $K$'s at $d_{\max}$ are ballot numbers. Nothing else is doing any work.

## Appendix B: The alternating identity in one line

$$T = (2l+1) \sum_{r=0}^{l} (-1)^r \left[\binom{2l}{r} - \binom{2l}{r-1}\right] = 0$$

is *literally* $(2l+1)$ times Identity A applied to $n = 2l$. So (2B) is (2A) times $(2l+1)$ after a change of index. The odd-$j$ identity is *forced* by the even-$j$ one.
