# Kirillov–Noumi first-hand read (2026-10-03)

Sources (TeX read in full where relevant, in /home/agent/projects/reading/kn99/):
- KN-R = arXiv **q-alg/9605005**, "q-Difference raising operators for Macdonald polynomials and the integrality of transition coefficients" (CRM Proc. 1999). File: kn_raising.tex. ID verified via arXiv abs title.
- KN-H = arXiv **q-alg/9605004**, "Affine Hecke algebras and raising operators for Macdonald polynomials" (Duke 1998). File: kn_hecke.tex. ID verified.
The arXiv source is AMSTeX, so no page numbers. All locators below are theorem/equation numbers.

## Q1. Do they give a q→∞ or q→0 limit to Hall–Littlewood?
**No (verified from text).** I grepped both files for "Hall", "Littlewood", "q=0", "\to 0", "\to\infty", "limit" and "Whittaker". The only hits for "Hall" are Macdonald's book title in the bibliographies. The only limits they take are:
- KN-R (2.13)–(2.16): "Let $q=t^{\alpha}$ and let $t\to1$" gives Jack raising operators $\mathcal K_m$ (Thm 2.6). The lowering analogue is (5.12)–(5.14).
- KN-H (3.13): "the limit as $q\to 1$ with rescaling $t=q^\beta$" gives Dunkl operators in the Jack case.
- q=0 and t=0 come up only in the integrality proof, as "regular at $t=0$" and "Taylor expansions at $t=q=0$" (KN-R proof of Thm 2.4; KN-H proof of Thm 3.2 and lines near (3.12)). No HL polynomial is ever named.
- The only involution they use is $(\cdot)^\vee$: "$q\to q^{-1}$, $t\to t^{-1}$" (KN-R (2.2)), which relates $K^-_m$ to $K^+_m$. They also use the q↔t duality $J_\lambda(x;q,t)\leftrightarrow J_{\lambda'}(x;t,q)$ (Ma VI.8.6/8.15).

There is no formula to match against Theorem A, so no involutions apply. My inference: one can of course take q→0 in $K^\pm_m$, because the classical fact $P_\lambda(x;0,t)=P_\lambda(x;t)$ (Macdonald VI) would give HL raising operators. KN do not do this. Rick's s=∞ edge is in variables $P_\nu(x;s,1/t)$. Matching it to the classical q→0 HL limit would need (s,1/t)→(1/s,t) via $P_\lambda(q^{-1},t^{-1})=P_\lambda(q,t)$, then q=1/s→0. That is textbook Macdonald VI (4.14(iv)), not KN.

## Q2. Integrality theorem
Verified from text:
- KN-R Thm 2.3 / KN-H Thm 3.2(1): "the Macdonald polynomial $J_\lambda(x)$ is expressed as a linear combination of monomial symmetric functions $m_\mu(x)$ with coefficients in $\mathbb Z[q,t]$". This is stated for any n and hence for infinitely many variables.
- KN-R Thm 2.4 / KN-H Thm 3.2(2): "the double Kostka coefficient $K_{\lambda,\mu}(q,t)$ is a polynomial in $q$ and $t$ with integral coefficients". Here $J_\mu=\sum K_{\lambda\mu}S_\lambda(x;t)$ (big Schur), equivalently $\tilde J_\mu=\sum K_{\lambda\mu}s_\lambda$ (KN-H (8.4)).
- KN-H Thm 8.1: $B_{\lambda\mu}(q,t)$, the $m_\mu$-coefficients of $\tilde J_\lambda=J_\lambda[X/(1-t)]$, lie in $\mathbb Z[q,t]$, with $B_{(n),\mu}=q^{n(\mu')}(q;q)_n/\prod(q;q)_{\mu_i}$ and duality $B_{\lambda',\mu}(q,t)=q^{n(\lambda')}t^{n(\lambda)}B_{\lambda,\mu}(t^{-1},q^{-1})$.

So the ring is $\mathbb Z[q,t]$. The bases are Macdonald J → m, J → S(t), and H̃(=J̃) → s, m. **Unrelated** to DS as stated (my inference). DS concerns the $e_\lambda$-expansion of a *⋆-transported* basis, with exact s-valuation $n(\mu)$ and dominance up-set support. KN say nothing about valuation, support, or the e-basis. Integrality of $\tilde J\to m$ and $\tilde J\to s$ does not give integrality of e-coefficients of some other basis without the transport's own integrality. At most it is a possible ingredient "with work", if Rick's transported basis is a ℤ[s,t]-unitriangular image of H̃. The $q^{n(\mu')}$ prefactor in Thm 8.1(3) has the same flavour as the valuation $n(\mu)$, but that is a resemblance only (classical fact for $\tilde H_{(n)}$).

## Q3. The raising operators
Verified from text:
- KN-H (3.1): $B^x_m=\sum_{k_1<\dots<k_m}x_{k_1}\cdots x_{k_m}(1-t^mY_{k_1})(1-t^{m-1}Y_{k_2})\cdots(1-tY_{k_m})$. Here $Y_i$ are Cherednik Dunkl operators, $Y_i=\bar T_i\cdots\bar T_{n-1}\,\omega\,\bar T_1^{-1}\cdots\bar T_{i-1}^{-1}$ (2.14), with ω the cyclic shift times $T_{q,x_n}$. Thm 3.1: $B^x_mP_\lambda=\prod_{i=1}^m(1-t^{m-i+1}q^{\lambda_i})P_{\lambda+(1^m)}$ for $\ell(\lambda)\le m$, and on J: $B^x_mJ_\lambda=J_{\lambda+(1^m)}$ (3.8).
- KN-R (2.1) gives $K^\pm_m$ as explicit W-invariant q-difference operators: $K^+_m=\sum_{|J|=m}x_J\sum_{I\subset J}(-t^{m-n+1})^{|I|}t^{\binom{|I|}2}\prod_{i\in I,j\notin I}\frac{tx_i-x_j}{x_i-x_j}\prod_{i\in I}T_{q,x_i}$. KN-R Prop 2.5 (2.10)–(2.11): $K^+_m=\Delta^{-1}\sum_w\varepsilon(w)w(x^\delta e_m(X_1,\dots,X_n))$ with $X_i=x_i(1-t^{m-i+1}T_{q,x_i})$.

Resemblance to (N) (my inference): the shape is "$e_m$ of $x_k\cdot(1-t^{\cdot}Y_k)$", i.e. multiplication by $x$'s interlaced with Y-factors. That is an X·Y product, **not** a conjugation $\hat\gamma X_i\hat\gamma^{-1}$. There is no Gaussian, no $\gamma$/theta-function, and no $e_k(Y)$ acting on a conjugated operator. KN-H Lemma 3.3 (the key lemma) is generating-function action on $\Pi(x,y)$ (Mimachi basis), not Gaussian conjugation. The nearest link is the Cherednik/DAHA philosophy that $\gamma X\gamma^{-1}$ relates to Y. KN do not use or state it.

## Q4. Modified product, ∇-like conjugation, Pieri?
**No (verified by grep and read of intro, §2/§3, §5, §8).** No product on Sym other than ordinary multiplication. No ∇ or plethystic eigenoperator conjugation. The word "Pieri" does not occur. Plethysm appears only as the definition $\tilde J=J[X/(1-t)]$ (KN-H (8.1)–(8.2)). The raising operators act by $\lambda\mapsto\lambda+(1^m)$, i.e. adding a full column. I infer this is the "e_m-Pieri at the extreme term": $B_m$ is like multiplication by $e_m$ projected onto one term. KN do not phrase it that way.

## Bottom line
- Theorem A novelty risk from KN: **none** (no HL limit in either paper). The residual risk is classical Macdonald VI (q→0, q↔1/q symmetry), not KN.
- DS-polynomiality risk from KN: **low**. Different basis and different statement, and no valuation or support claims.
- Note: KN-R is the paper that DFK 1505.01657 cites for raising operators. DFK's use (q-Whittaker/t=0 edge, Theorem B) is DFK's own, not something KN state.
