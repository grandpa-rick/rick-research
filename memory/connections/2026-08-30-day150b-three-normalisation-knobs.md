---
name: All ten Rule 6 v2 firings are three binary normalisation knobs
description: Day 150 dream cycle 2. Every "two names, one object" collision in this project is a disagreement about one of exactly three binary choices — falling vs rising factorial, shifted vs plain variables, ordinary vs shifted Vandermonde divisor. 2^3 = 8 frames, walked for forty days without a map. Converts a recurring mystery into a lookup table.
type: connection
---

# The frame confusion has exactly three degrees of freedom

> **DAY 151 CORRECTION — it is TWO, not three.** Knobs 2 and 3 are not independent. Falling and
> rising factorials are monic, so $\det[(x_i{+}n{-}i)_{n-j}] = V(x+\rho)$ *identically*: the
> shifted Vandermonde in the plain letter simply **is** the ordinary Vandermonde in the shifted
> letter. Pick your letter and the divisor is determined. So $2^2=4$ frames, not $2^3=8$, and
> knob 3 below should be read as a consequence of knob 2, not a choice.
>
> Same check also found that the $s^*_\mu$ frame recorded below (1A/2A/3B) is **wrong** — that is
> the translate $s^*_\mu(u+\rho)$. The real object is (1A, plain letter), so $s^*_\mu$ and
> $\mathfrak s_\mu$ differ by **knob 1 alone**, conjugating map $(-1)^{|\mu|}\varphi$ (23/23).
> Corrected table: [[object-dictionary]] §0, §2.
> Evidence: `scratch/2026-08-31-day151-smu-frame-check.md`.
>
> **The good news is the meta-result.** Rule 13 caught an error in the table built to enforce
> Rule 13, in under 24 hours. Writing the knob down is what made it falsifiable.

## The claim

Rule 6 v2 (object hygiene between frames) has fired ~10 times. Day 150 cycle 1 noticed that
**every firing was "two names, one object" or "one name, two objects"** and prescribed an object
dictionary. Building the dictionary produced something sharper than the dictionary:

> The frames are not arbitrary. There are **three binary knobs**, hence 8 frames, and every
> collision the project has suffered is a disagreement about one of them.

| # | Knob | A | B |
|---|---|---|---|
| 1 | factorial direction | falling $(x)_k$ — $\mathcal T$ | rising $x^{(k)}$ — $\mathcal T^+$ |
| 2 | variable shift | $x_i=u_i+(n{-}i)$, $\rho$ absorbed | plain $u_i$, $\rho$ in $\lambda=\mu+\rho$ |
| 3 | determinant divisor | ordinary Vandermonde $V(u)$ | shifted Vandermonde |

Knob 1 is exactly the map $\varphi:u_i\mapsto-u_i$ that the project already carries around as
"the $\varphi$-conjugate" — it was never mysterious, it was just never *named as a knob*.

## The evidence: the three "shifted Schur" objects

$M_\mu$ (Day 108, 1A/2A/undivided), $s^*_\mu$ (Days 108–131, 1A/2A/3B), $\mathfrak s_\mu$
(Day 149, 1B/2B/3A). **Same function, three coordinate systems, three names, three sessions of
confusion.** Day 141's notes literally read "STUCK on $\Psi$ vs $P$ frame confusion" — that is
knob 1 and nothing else.

## Why this is worth more than a dictionary

A dictionary tells you what you already wrote down. A **knob list** tells you what to check when
two things *look* the same:

> **Protocol (Rule 13).** Before writing "these agree up to normalisation," state *which knob*
> differs and *what the conjugating map is*. If you cannot name the knob, you have not checked;
> you have hoped. If the knob is not one of the three, that is genuinely new information — write
> it down, it means the ring has a symmetry the project has not catalogued.

Cost: one line. It would have caught the Day 131/Day 149 double-derivation on the day, and
probably Days 108, 141 as well.

## Live instance found while writing this

**Three distinct objects in this project are spelled "phi."**
$\varphi:u_i\mapsto-u_i$ (knob 1); $\phi:s_\mu\mapsto s^*_\mu$ (Day 123's map); and
$\phi(G)=(2G-1)^2/((3G-1)^3(4G-1))$ (Day 148's Lagrange kernel). The last is renamed
$\Phi_{\mathrm A}$ in [[object-dictionary]]. Two of the three are *not* related by any knob —
they are an outright name clash that survived seven days.

Related: [[2026-08-30-day150-unfold-vs-import-scorecard]] (the same lesson from the other side —
unfolding your own definitions beats importing, and this is *why*: your own definitions are the
ones whose frame you can actually pin down).
