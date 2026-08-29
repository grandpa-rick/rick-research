"""Day 118 — Prove d_mu = mu_1 + floor((mu_2 + mu_3)/2) for ell(mu) <= 3.

Recall:
  d_mu := (u, pi)-wdeg(s*_mu(u, y, c))
        = deg_t s*_mu(t+s, (s+1)t, t^2)  [by Char. Lemma]

But actually the Char. Lemma is stated in the e-basis: for f in Q[e_1, e_2, e_3],
  (u, pi)-wdeg(f) = deg_t f(t+s, (s+1)t, t^2).

Applied to s*_mu (which IS in Q[e_1, e_2, e_3] since it's symmetric),
we want deg_t of s*_mu evaluated at (u,y,c) satisfying:
  u + y + c = t + s
  uy + uc + yc = (s+1) t
  u y c = t^2

These are the elementary symmetric polys. Equivalently, u, y, c are roots of
  z^3 - (t+s) z^2 + (s+1)t z - t^2 = 0.

Factor: z^3 - (t+s)z^2 + (s+1)tz - t^2 = (z-t)(z^2 - sz + t).
  - Root z = t.
  - Other two roots: y, c satisfying y + c = s, yc = t.

So under this substitution:
  {u, y, c} = {t, roots of z^2 - sz + t}
Set u = t (one of the roots).

Then s*_mu(t, y, c) = s*_mu(u=t, y, c) where y + c = s, yc = t.

To compute d_mu = deg_t of this:

Approach 1: Use LEADING TERM ARGUMENT. Ordinary Schur s_mu(u, y, c) is the top
(polynomial degree) part of s*_mu. Since d_mu equals the ordinary d_{s_mu} =
d_{s_μ} (empirically, and can be verified from s*_mu = s_mu + lower degree
symmetric polys), we can compute d_mu using s_mu.

Approach 2: Use branching. s_mu(u, y, c) as polynomial in u with coefficients
in y, c:
  s_mu(u, y, c) = Σ_{lambda ⊆ mu, |mu/lambda| horizontal strip} s_lambda(y, c) u^{|mu/lambda|}
No wait: s_mu(x_1, x_2, x_3) = Σ_lambda K_{mu/lambda} m_{...}... hmm.

The classical branching rule:
  s_mu(x_1, x_2, x_3) = Σ_{mu ⊇ mu' horizontal strip} s_{mu'}(x_2, x_3) x_1^{|mu|-|mu'|}
where mu' has ell(mu') <= 2 and mu/mu' is a horizontal strip.

Actually more precisely (SSYT of shape mu with entries 1,2,3 with rows weakly
increasing, cols strictly increasing):
  s_mu(x_1, x_2, x_3) = Σ_T x^T = Σ_{mu' ⊆ mu, mu/mu' horiz strip} x_1^{|mu/mu'|} s_{mu'}(x_2, x_3).

So s_mu(t, y, c) = Σ_{mu' ⊆ mu horiz strip} t^{|mu/mu'|} s_{mu'}(y, c).

Now for mu' with ell(mu') <= 2, s_{mu'}(y, c) with y+c = s, yc = t:
  s_{(p, q)}(y, c) = h_{p-q}(y, c) · (yc)^q · [complete-vs-Schur relation]
  Actually: s_{(p,q)}(y, c) = (h_{p-q}(y,c)) times (something) — Weyl formula:
    s_{(p,q)}(y, c) = det [[y^{p+1}, y^{q}], [c^{p+1}, c^{q}]] / (y - c)
                   = (y^{p+1} c^q - y^q c^{p+1}) / (y - c)
                   = y^q c^q (y^{p-q+1} - c^{p-q+1}) / (y - c)
                   = (yc)^q h_{p-q}(y, c)
  where h_k(y, c) = Σ y^i c^{k-i} = (y^{k+1} - c^{k+1})/(y - c).

So s_{(p, q)}(y, c) = (yc)^q · h_{p-q}(y, c) = t^q · h_{p-q}(y, c).

And h_k(y, c) for y+c=s, yc=t:
  h_k(y, c) = symmetric poly of degree k in y, c
           = poly in (y+c) and yc = poly in (s, t) of "total weighted degree" k
             where s has weight 1, t has weight 2 (since yc has 2 vars each of weight 1,
             so yc "has value" of degree 2 in y, c but 1 in the t-parameter).

  Actually, let's compute h_k(y, c) using generating series:
    Σ_k h_k(y, c) z^k = 1/((1 - yz)(1 - cz))
    Expanding: = 1/(1 - (y+c) z + yc z^2) = 1/(1 - sz + t z^2).
    So h_k(y, c) = coefficient of z^k in 1/(1 - sz + t z^2).
    Recurrence: h_0 = 1, h_1 = s, h_k = s h_{k-1} - t h_{k-2}.

  Solving: h_k(s, t) = polynomial with terms s^a t^b, a + 2b = k. Each term
  contributes t-degree b <= k/2. Top t-degree term is (-t)^{k/2} for k even,
  else... let's check:
    h_0 = 1: deg_t = 0.
    h_1 = s: deg_t = 0.
    h_2 = s^2 - t: deg_t = 1.
    h_3 = s(s^2 - t) - t s = s^3 - 2 s t: deg_t = 1.
    h_4 = s h_3 - t h_2 = s^4 - 2 s^2 t - t(s^2 - t) = s^4 - 3 s^2 t + t^2: deg_t = 2.
    h_5 = s h_4 - t h_3 = s^5 - 3 s^3 t + s t^2 - t (s^3 - 2 s t) = s^5 - 4 s^3 t + 3 s t^2: deg_t = 2.
    So deg_t h_k(y, c) = floor(k / 2).

So under the substitution:
  s_{(p, q)}(y, c) = t^q · h_{p-q}(y, c)
  deg_t = q + floor((p - q) / 2).

Interesting. For p >= q >= 0, this equals q + floor((p-q)/2).
  Check: (p, q) = (1, 0): 0 + floor(1/2) = 0.
  (p, q) = (1, 1): 1 + 0 = 1.
  (p, q) = (2, 0): 0 + 1 = 1.
  (p, q) = (2, 1): 1 + 0 = 1.
  (p, q) = (2, 2): 2 + 0 = 2.
  (p, q) = (3, 0): 0 + 1 = 1.
  (p, q) = (3, 1): 1 + 1 = 2.

Now for full s_mu(t, y, c) = Σ_{mu' ⊆ mu horiz strip} t^{|mu|-|mu'|} s_{mu'}(y, c)
= Σ_{mu' ⊆ mu horiz strip} t^{|mu|-|mu'|} · t^{mu'_2} · h_{mu'_1 - mu'_2}(y, c).

Total t-degree of each summand: |mu| - |mu'| + mu'_2 + floor((mu'_1 - mu'_2)/2).

We want to MAXIMIZE over horizontal strips mu' ⊆ mu with ell(mu') <= 2:
  D(mu') := |mu| - mu'_1 - mu'_2 + mu'_2 + floor((mu'_1 - mu'_2)/2)
         = |mu| - mu'_1 + floor((mu'_1 - mu'_2)/2)

We're maximizing over horiz strips (mu' ⊆ mu, mu/mu' has at most 1 cell in each column).

Let mu = (a, b, c). Horizontal strip mu' = (p, q) with 0 <= q <= p, ell(mu')<=2:
  (a) mu/mu' is a horiz strip: this means each column has at most 1 removed cell.
    Column j is in mu iff mu has a cell there. Row 1 has cells 1..a, row 2 has 1..b, row 3 has 1..c.
    mu' has row 1: 1..p, row 2: 1..q.
    For horiz strip mu/mu' with rows 1..3 → 1..2: need mu' subset of mu (partitionwise:
    p <= a, q <= b), AND the "extras" mu/mu' = (mu\mu') should be a horizontal strip.
    The removed cells: row 1: cells p+1..a; row 2: cells q+1..b; row 3: cells 1..c.
    For a HORIZONTAL strip (each column has at most 1 cell removed):
      Column j: cells in mu are in rows where mu_i >= j.
      In mu, column j appears in row 1 iff a>=j, row 2 iff b>=j, row 3 iff c>=j.
      In mu', column j appears in row 1 iff p>=j, row 2 iff q>=j (row 3 empty).
      Cells removed in column j: [a>=j but p<j] + [b>=j but q<j] + [c>=j] (row 3 always).
      For this to be at most 1 for all j:
        - Column j=1..c: row 3 contributes 1. So we need row 1, 2 to NOT contribute.
          → For j=1..c: p >= j (i.e., p >= c) AND q >= j (i.e., q >= c).
        - Column j=c+1..b: row 3 contributes 0. Row 2 contributes iff q<j, row 1 iff p<j.
          Need at most 1 to contribute. So NOT (p<j AND q<j). Since q<=p, this reduces to
          "not both", equivalent to p>=j OR q>=j, i.e., p>=j (since p>=q).
          → For j=c+1..b: p >= j, i.e., p >= b.
        - Column j=b+1..a: row 2 contributes 0. Row 1 contributes iff p<j. Only 1 possible,
          always <=1. No constraint from horiz.
      So constraints: p >= c, q >= c, p >= b. Combined with p <= a, q <= b: b <= p <= a,
      c <= q <= b. Also q <= p is automatic given q <= b <= p.

So valid mu' = (p, q) satisfy: b <= p <= a, c <= q <= b, and p >= q.
The last is q <= b <= p so automatic.

D(p, q) = |mu| - p + floor((p - q)/2) = a + b + c - p + floor((p-q)/2).

Maximize over b <= p <= a, c <= q <= b:
  For fixed p: floor((p-q)/2) is maximized by MINIMIZING q. So q = c.
  D(p, c) = a + b + c - p + floor((p - c)/2).
  Let r = p - c (>=0). Then D = a + b - r + floor(r/2) = a + b - ceil(r/2).
  To maximize D, minimize ceil(r/2), i.e., minimize r >= 0 subject to p = r+c >= b, so r >= b-c.
  So minimum r = max(0, b-c) = b-c (since b >= c).
  Thus min r = b - c, and D_max = a + b - ceil((b-c)/2) = a + b - ceil((b-c)/2).

Hmm wait, but we also need p <= a. With r = b - c, p = b. Since b <= a, this is fine.

So d_{s_mu} = a + b - ceil((b - c)/2).

Let's compare to conjecture d_mu = a + floor((b+c)/2):
  a + floor((b+c)/2)  vs  a + b - ceil((b-c)/2)
Difference (drop a):
  floor((b+c)/2)  vs  b - ceil((b-c)/2)
Case b + c even (b, c same parity):
  floor((b+c)/2) = (b+c)/2
  ceil((b-c)/2) = (b-c)/2 (since b-c is even)
  b - ceil((b-c)/2) = b - (b-c)/2 = (b+c)/2 ✓
Case b + c odd (b, c different parity):
  floor((b+c)/2) = (b+c-1)/2
  b - c is odd, so ceil((b-c)/2) = (b-c+1)/2
  b - (b-c+1)/2 = (2b - b + c - 1)/2 = (b + c - 1)/2 ✓

So YES: a + floor((b+c)/2) = a + b - ceil((b-c)/2). Formula verified.

Great — we've DERIVED d_mu = mu_1 + floor((mu_2+mu_3)/2) from the Char. Lemma
and the branching rule for s_mu(u, y, c).

We also used: d_{s*_mu} = d_{s_mu}. This is because s*_mu = s_mu + Σ (lower
polynomial-degree symmetric polys), and the lower ones can't beat the (u,pi)-wdeg
of s_mu itself. Actually more carefully: s*_mu is s_mu + Σ c^mu_lambda s_lambda
where |lambda| < |mu| and d_lambda <= d_mu (empirically). We NEED this last
fact to complete the argument — this is the §4 observation.

Let's programatically verify.
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day117')

from ordinary_schur_deg import ord_schur, factorial_schur, all_partitions_len_le_3
from route_v_probe import substitute_sigma_pi, joint_u_pi_deg
from sympy import symbols, expand

u, y, c = symbols('u y c')


def d_from_formula(mu):
    mu = tuple(list(mu) + [0] * (3 - len(mu)))
    return mu[0] + (mu[1] + mu[2]) // 2


if __name__ == "__main__":
    xs = (u, y, c)
    all_ok = True
    for N in range(11):
        for mu in all_partitions_len_le_3(N):
            s_ord = ord_schur(mu, xs)
            d_ord = joint_u_pi_deg(substitute_sigma_pi(s_ord))
            s_star = factorial_schur(mu, xs)
            d_star = joint_u_pi_deg(substitute_sigma_pi(s_star))
            d_pred = d_from_formula(mu)
            if not (d_ord == d_pred == d_star):
                print(f"MISMATCH: mu = {mu}, d_ord = {d_ord}, d_star = {d_star}, predicted = {d_pred}")
                all_ok = False
    print(f"For |mu| <= 10, d_{{s_mu}} = d_{{s*_mu}} = mu_1 + floor((mu_2+mu_3)/2): {all_ok}")
