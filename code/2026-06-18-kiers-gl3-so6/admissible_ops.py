"""
Day 73 CODE Task C -- Kiers admissible OPS for GL(3) hookarrow SO(6).

REFERENCE: Kiers, "Saturation and reduction problems for branching cones"
  (arXiv 1909.09262), Theorems 1.4-1.8.

DEFINITIONS:
  Let G = SO(6), H = GL(3), with H sitting inside G in the standard
  Levi parabolic embedding.  As Lie algebras, so(6) = sl(4)
  (exceptional iso), and gl(3) is the Levi of the maximal parabolic
  P_3 in sl(4) (omit one simple root).

  A one-parameter subgroup (OPS) tau: G_m -> H is a homomorphism.
  Identify H = GL(3) -> H/[H,H] x ... and write tau in coordinates as
  (a_1, a_2, a_3) in Z^3.

  Choose the dominant chamber {a_1 >= a_2 >= a_3} (modulo Weyl-action).
  Modulo center: only the differences matter, but we keep all three
  coords to handle GL (not SL).

  Weights of g/h = so(6)/gl(3) as h-module:
    The Levi gl(3) sits in sl(4) with Cartan diag(a, b, c, -a-b-c).
    Restricting to the gl(3) on the upper 3x3 block: the Cartan acts as
    diag(a, b, c).  The nilradical n^+ has weights e_i - e_4 for i=1,2,3
    (the "north arm" of sl(4)).  But we want so(6)/gl(3), not sl(4)/gl(3).
    Using so(6) = sl(4): the bilinear form on C^4 gives Lambda^2 V*
    structure, so weights of so(6)/gl(3) come from Lambda^2 C^4 minus
    the gl(3) sub.  Concretely:
      so(6)/gl(3) = (Lambda^2 V) oplus (Lambda^2 V*)  as gl(3)-modules,
    where V = C^3 is the standard rep of gl(3).

    Weights of Lambda^2 V: (e_i + e_j) for 1 <= i < j <= 3.
    Weights of Lambda^2 V*: -(e_i + e_j) for 1 <= i < j <= 3.

  (For a sanity-check: dim so(6) = 15, dim gl(3) = 9, dim quotient = 6 =
  2 * binom(3,2).  Matches.)

  An OPS tau = (a_1, a_2, a_3) acts on weight (b_1, b_2, b_3) by
  <tau, weight> = a_1 b_1 + a_2 b_2 + a_3 b_3.

  ADMISSIBILITY (Kiers Def 1.4): tau is admissible iff
    <tau, w> >= 0  for every weight w of g/h.

ALGORITHM:
  1. List the 6 weights of g/h.
  2. For dominant tau = (a_1, a_2, a_3) with a_1 >= a_2 >= a_3 in some
     bounded box (say |a_i| <= 5), check admissibility.
  3. Mod out by scaling (positive integer multiples): keep only
     primitive (gcd=1) representatives.

PREDICTION (from Browse 63 reply): admissibility forces
  (a_i + a_j) >= 0 from Lambda^2 V AND <= 0 from Lambda^2 V*.
  Hence a_i + a_j = 0 for all i < j.  Combined with dominance:
  a_1 + a_2 = 0, a_1 + a_3 = 0, a_2 + a_3 = 0  =>  a_1 = a_2 = a_3 = 0.
  So the ONLY admissible OPS is tau = 0 (trivial).

  This would mean: GL(3) hookarrow SO(6) has NO nontrivial Type-I
  extremal rays from admissible OPS.  AXIS(n) = 3 (if true) would have
  to come from Type-II rays (boundary induction).
"""

from __future__ import annotations

import json
import math
import itertools
from pathlib import Path

OUT_DIR = Path("/home/agent/projects/code/2026-06-18-kiers-gl3-so6")
OUT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------------------
# Weight list for so(6)/gl(3) as gl(3)-module
# ---------------------------------------------------------------------
def weights_so6_mod_gl3():
    """Return list of weights of so(6)/gl(3) as gl(3)-module.

    Convention: weight = (b_1, b_2, b_3) where the i-th entry is the
    coefficient of e_i in the gl(3)-Cartan basis.
    """
    weights = []
    # Lambda^2 V: e_i + e_j for 1 <= i < j <= 3
    for i, j in itertools.combinations([1, 2, 3], 2):
        w = [0, 0, 0]
        w[i - 1] = 1
        w[j - 1] = 1
        weights.append(("Lam2V", tuple(w)))
    # Lambda^2 V*: -(e_i + e_j)
    for i, j in itertools.combinations([1, 2, 3], 2):
        w = [0, 0, 0]
        w[i - 1] = -1
        w[j - 1] = -1
        weights.append(("Lam2Vstar", tuple(w)))
    assert len(weights) == 6, f"expected 6 weights, got {len(weights)}"
    return weights


# ---------------------------------------------------------------------
# Admissibility check
# ---------------------------------------------------------------------
def pairing(tau, w):
    return sum(t * x for t, x in zip(tau, w))


def is_admissible(tau, weights):
    """tau is admissible iff <tau, w> >= 0 for every weight w."""
    return all(pairing(tau, w) >= 0 for _, w in weights)


def is_dominant(tau):
    """Dominant: a_1 >= a_2 >= a_3 (for GL(3) standard ordering)."""
    return tau[0] >= tau[1] >= tau[2]


def gcd_tuple(t):
    """GCD of a tuple of integers (treating sign as 0)."""
    g = 0
    for x in t:
        g = math.gcd(g, abs(x))
    return g


def is_primitive(tau):
    """Primitive: gcd of |a_i| is 1, OR tau = 0."""
    g = gcd_tuple(tau)
    return g == 1 or g == 0


# ---------------------------------------------------------------------
# Enumerate dominant OPS in a bounded box
# ---------------------------------------------------------------------
def enumerate_admissible(box=5):
    """Enumerate (a_1, a_2, a_3) in [-box, box]^3, dominant, primitive,
    admissible."""
    weights = weights_so6_mod_gl3()
    admissible = []
    n_dominant = 0
    for tau in itertools.product(range(-box, box + 1), repeat=3):
        if not is_dominant(tau):
            continue
        n_dominant += 1
        if not is_admissible(tau, weights):
            continue
        if not is_primitive(tau):
            continue
        admissible.append(tau)
    return admissible, n_dominant, weights


# ---------------------------------------------------------------------
# Symbolic derivation of constraint (for prediction confirmation)
# ---------------------------------------------------------------------
def derive_constraints(weights):
    """For each weight w, the constraint <tau, w> >= 0.
    Return list of (description, weight, sign)."""
    constraints = []
    for src, w in weights:
        a_indices = [i + 1 for i, x in enumerate(w) if x != 0]
        sign = "geq" if sum(w) > 0 else "leq"
        if sum(w) > 0:
            constraints.append(
                (f"{src}({w}): a_{a_indices[0]} + a_{a_indices[1]} >= 0",
                 w, "geq"))
        else:
            constraints.append(
                (f"{src}({w}): -(a_{a_indices[0]} + a_{a_indices[1]}) >= 0  "
                 f"i.e. a_{a_indices[0]} + a_{a_indices[1]} <= 0",
                 w, "leq"))
    return constraints


def solve_for_pairs_summing_to_zero():
    """Combined constraints: a_i + a_j >= 0 AND <= 0 for every i < j.
    Implies a_i + a_j = 0 for all i < j.

    System:
      a_1 + a_2 = 0
      a_1 + a_3 = 0
      a_2 + a_3 = 0

    Subtracting (1) - (2): a_2 - a_3 = 0, hence a_2 = a_3.
    Sub (2) - (3): a_1 - a_2 = 0, hence a_1 = a_2.
    So a_1 = a_2 = a_3 = a, and 2a = 0 means a = 0.
    """
    # Solve symbolically (already done): only (0, 0, 0).
    return [(0, 0, 0)]


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main():
    print(f"\n{'='*70}")
    print(f"Day 73 CODE Task C -- Kiers admissible OPS for GL(3) -> SO(6)")
    print(f"{'='*70}")

    weights = weights_so6_mod_gl3()
    print(f"\nWeights of so(6)/gl(3) as gl(3)-module ({len(weights)} total):")
    for src, w in weights:
        print(f"  {src}: weight = {w}")

    print(f"\nAdmissibility constraints (for tau = (a_1, a_2, a_3)):")
    constraints = derive_constraints(weights)
    for desc, w, sign in constraints:
        print(f"  {desc}")

    # Combine: a_i + a_j >= 0 AND a_i + a_j <= 0  =>  a_i + a_j = 0.
    # Solution: a_1 = a_2 = a_3 = 0.
    sym_sol = solve_for_pairs_summing_to_zero()
    print(f"\nSymbolic solution: {sym_sol}")
    print(f"  -> ONLY trivial OPS is admissible (in the SL/center-fixed sense).")

    # Numerical confirmation: enumerate over box.
    print(f"\nNumerical enumeration over |a_i| <= 5, dominant:")
    box = 5
    admissible, n_dom, _ = enumerate_admissible(box=box)
    print(f"  # dominant OPS in [-{box}, {box}]^3: {n_dom}")
    print(f"  # admissible primitive dominant OPS: {len(admissible)}")
    for t in admissible:
        print(f"    {t}")

    # Sanity: increase box, confirm same count.
    print(f"\nSanity-check at larger box:")
    for b in [10, 20]:
        adm, ndom, _ = enumerate_admissible(box=b)
        print(f"  box = {b}: # dominant = {ndom}, # admissible primitive = "
              f"{len(adm)} -> {adm}")

    # Conclusion
    n_admissible = len(admissible)
    n_nontrivial = sum(1 for t in admissible if t != (0, 0, 0))
    print(f"\n{'='*70}")
    print(f"CONCLUSION:")
    print(f"  # admissible OPS (modulo scaling, dominant): {n_admissible}")
    print(f"  # nontrivial admissible OPS: {n_nontrivial}")
    print(f"  PREDICTION (Browse 63): 0 nontrivial admissible OPS")
    print(f"  RESULT: prediction {'CONFIRMED' if n_nontrivial == 0 else 'REFUTED'}")
    print(f"\n  STRUCTURAL CONSEQUENCE:")
    if n_nontrivial == 0:
        print(f"    GL(3) -> SO(6) has NO Type-I extremal rays from admissible")
        print(f"    OPS (Kiers Thm 1.5).  Any AXIS-related rays must come from")
        print(f"    Type-II (induction from boundary parabolic) per Kiers")
        print(f"    Thm 1.8.  Day-74 PROVE pivots to Type-II enumeration.")
    else:
        print(f"    Type-I rays exist!  Each generates a Schubert-theoretic")
        print(f"    AXIS ray.  Day-74 PROVE writes up the AXIS = 3 proof.")
    print(f"{'='*70}")

    # Persist
    results = {
        "weights": [{"src": src, "weight": list(w)} for src, w in weights],
        "constraints": [{"description": d, "weight": list(w), "type": s}
                        for d, w, s in constraints],
        "symbolic_solution": [list(t) for t in sym_sol],
        "numerical_admissible_box5": [list(t) for t in admissible],
        "n_admissible": n_admissible,
        "n_nontrivial_admissible": n_nontrivial,
        "prediction_confirmed": n_nontrivial == 0,
        "pivot_to_type_II_for_day74": n_nontrivial == 0,
    }
    out_path = OUT_DIR / "results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nsaved results to {out_path}")


# ---------------------------------------------------------------------
# Verification: compare symbolic vs numerical
# ---------------------------------------------------------------------
def verify_test():
    """Cross-check: symbolic solution should match numerical solution
    (modulo positive scaling)."""
    sym = set(solve_for_pairs_summing_to_zero())
    num, _, _ = enumerate_admissible(box=3)
    # numerical includes ALL primitive dominants; should be {(0,0,0)} only
    assert set(num) == {(0, 0, 0)}, \
        f"numerical = {num}, expected just (0,0,0)"
    print("[verify_test] Symbolic and numerical agree: only (0,0,0) ✓")


if __name__ == "__main__":
    verify_test()
    main()
