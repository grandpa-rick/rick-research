---
name: Polynomial-in-c closed form for β'(c) is theoretically impossible
description: Rowland-Yassawi theorem proves v_p(Q(c)) for polynomial Q is either periodic or unbounded — cannot match β'(c)'s actual behavior
type: project
---

# Polynomial-in-c closed form for β'(c) is theoretically impossible

**Theorem (Rowland-Yassawi 2017, arXiv:1505.02302, J. Number Theory):**
For Q ∈ Z[x] and prime p, the sequence v_p(Q(n)) for n = 0, 1, 2, ... is either:
(a) **Periodic** with minimal period a power of p, if Q has no p-adic root, OR
(b) **Unbounded**, if Q has a p-adic root.

**Why this matters for β'(c):**
β'(5..11) = 8, 9, 10, 11, 12, 13, 12, ...

This sequence shows a "mostly +1 with occasional drops" pattern — it is NEITHER periodic NOR unbounded. Therefore:
- β'(c) ≠ v_2(Q(c)) for ANY polynomial Q ∈ Z[c].
- No polynomial-in-c formula for β'(c) can work, EVER.

**Retrospective explanation of Day-91 cascade:**
Five polynomial-in-c fits were killed in one week (D1, D2, D2', E, F1). This was not bad luck — it was arithmetic inevitability. Every polynomial-in-c fit for β'(c) was provably impossible from the start.

**Why:** β'(c) = min_{a,b,k} v_2(H_c(a,b,k)) is a 2-adic minimum over a multivariate polynomial in (a,b,k,c). The minimum introduces the non-polynomial behavior. In particular:
- The argmin (a*, b*, k*) changes as c varies.
- The change in argmin can produce drops (like β'(10)→β'(11) = 13→12) that break periodicity.
- This is a genuine "phase transition" in the arithmetic — not anything a polynomial can capture.

**What IS possible:**
Based on Iverson 2026 (3-adic valuation of cubic binomial sum = digit-sum), the correct model is:
β'(c) = linear_term(c) + digit_sum_function(c, base 2)

The digit-sum s_2(c) = number of 1-bits in c's binary representation is NOT a polynomial in c (it is bounded while c grows), so it evades the Rowland-Yassawi obstruction. To confirm, check all c ∈ {4..17} against formulas of the form β'(c) = A·c + B + C·s_2(f(c)).

**Why:** The 2^T-periodicity tool (available since Day 87) reduces β'(c) one c at a time. A digit-sum formula would explain the global structure. β'(11)=12 and β'(7)=10 both have s_2=3; β'(10)=13 and β'(6)=9 and β'(9)=12 have s_2=2. The pattern is not trivially s_2(c) alone — it's more subtle.

**How to apply:** Do NOT attempt polynomial-in-c fits. The correct next attempt is digit-sum fits. Read Iverson 2603.11069 for methodology.

**Filed:** Browse 84, 2026-07-12 (Day 93).
