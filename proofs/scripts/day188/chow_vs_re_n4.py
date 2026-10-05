"""Day 188 — Route A cheap test.

Compute X_{P_4}(q) e-coefficients via Hikita's φ_c Markov chain (equivalently
Chow's watershed reformulation) and check against Rick's (Re) recursion.

Hikita SS-proof (arXiv:2410.12758):
- Conjugate Hessenberg function e = (e(1), ..., e(n)) with e(i) = min j (edge j-i) - 1.
- For P_n: e(i) = i-2 for i ≥ 2, e(1) = 0. So e_{P_4} = (0, 0, 1, 2).
- Markov chain on standard Young tableaux SYT_i.
- At step i, from T ∈ SYT_{i-1}, with r = e(i), form Maya diagram δ = δ^{(r)}(T):
  - View T from above; box i in column i has "top entry" topT(i) (∞ if column empty).
  - δ_i = 1 if column i has top entry > r or column i empty above the "red" cutoff.

Actually let me re-read: δ^{(r)}(T) is defined for r ∈ Z and T ∈ SYT_m as follows
(Def 1.1 in Hikita SS):
  - δ_i for i ∈ Z: consider column i (French convention). If topT(i) > r, δ_i = 1;
    if topT(i) ≤ r, δ_i = 0. And adding infinite red (=1) boxes to the left,
    infinite white (=0) boxes to the right.

  Wait — from the figure and text: "coloring the box i with i > r red, and then
  adding infinitely many red boxes to the left and infinitely many white boxes
  to the right."

  So actually the coloring rule is:
    - Look at T from above, get top-entry of each column.
    - Color topT(i) RED (δ=1) if topT(i) > r, WHITE (δ=0) otherwise.
    - To the LEFT (columns not present yet, i.e., negative i), all RED.
    - To the RIGHT (empty columns), all WHITE.

  W(δ) = {i : δ_i = 0, δ_{i-1} = 1} = white boxes just after a red run
       = left endpoints of white runs
  R(δ) = {i : δ_i = 1, δ_{i-1} = 0} = red boxes just after a white run
       = left endpoints of red runs

Transition: at step n, r = e(n). Pick c ∈ W(δ^{(r)}(T)) with probability φ_c.
Result: add new box (containing entry n) on top of column c-1 (there's an
indexing subtlety — see Def 1.4: "add n on top of c-th column"). Actually
Def 1.4: If c ∈ W(δ^{(r)}(T)), add n on top of c-th column of T. This gives T'.

φ_c(δ; q) = Π_{b ∈ R(δ)} [c - b]_q / Π_{a ∈ W(δ) \ {c}} [c - a]_q.

For X_Γ(x; q), the e-coefficient of e_λ where λ = shape(T_n) is
  [e_λ] X_Γ = Σ over trajectories ending at T_n of shape λ, of Π φ_c along trajectory.

Actually re-reading Thm 1.6 more carefully needed. Let me code it and check.
"""

from sympy import symbols, simplify, Rational, factor, expand, poly, Poly, collect, Symbol
from sympy.abc import q
from fractions import Fraction
from collections import defaultdict


def q_bracket(k):
    """[k]_q = (1 - q^k)/(1 - q) = 1 + q + ... + q^{k-1} for k > 0.
    For k < 0: [k]_q = -q^k [-k]_q^{-1} · q^k? Actually the standard extension is
    [-n]_q = -q^{-n} [n]_q, using [k]_q := (1 - q^k)/(1 - q).
    For k=0: [0]_q = 0.
    """
    if k == 0:
        return 0
    if k > 0:
        return sum(q**i for i in range(k))
    # k < 0: [k]_q = (1 - q^k)/(1 - q) = -q^k (1 - q^{-k})/(1 - q) · q^{-k}? Simpler:
    # [k]_q = -q^k · [(-k)]_q where [-k]_q above is positive-k formula, but with q → 1/q.
    # Actually cleanest: use symbolic (1 - q^k)/(1 - q).
    from sympy import Rational, simplify
    return simplify((1 - q**k)/(1 - q))


# ---------------------------------------------------------------------------
# Rick's (Re): X_{P_n}(q) recursion in e-basis
# ---------------------------------------------------------------------------

def rick_X_Pn(n, cache=None):
    """Return dict {partition (as sorted tuple, largest-first): coeff in q}
    representing X_{P_n}(q) via Rick's (Re) recursion.

    X_{P_n} = e_n + q Σ_{k=2}^n [k-1]_q · e_k · X_{P_{n-k}}
    """
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n == 0:
        result = {(): 1}
        cache[n] = result
        return result

    result = defaultdict(int)
    # e_n term
    result[(n,)] += 1
    # sum
    for k in range(2, n + 1):
        coef = q * q_bracket(k - 1)
        sub = rick_X_Pn(n - k, cache)
        for lam, c in sub.items():
            # e_k · e_lam → append k to the partition, sort largest-first
            new_lam = tuple(sorted((k,) + lam, reverse=True))
            result[new_lam] = expand(result[new_lam] + coef * c)
    result = {k: expand(v) for k, v in result.items()}
    cache[n] = result
    return result


# ---------------------------------------------------------------------------
# Hikita's Markov chain
# ---------------------------------------------------------------------------

def build_maya(T, r, max_col):
    """T is a list of columns (each column is a list, entries top->bottom
    or bottom->top?). French convention: columns grow up.

    We store T as tuple of column heights (since only shape matters for shape,
    but Markov chain tracks tableau, need to track top-of-column entries for
    δ^{(r)}(T)).

    Actually for computing φ_c only the "top entries" matter. But then the
    chain moves from T to T' by adding a box on top of column c. The top
    entry of column c after step n is n. So track top entries.

    Represent T as tuple (top_1, top_2, ..., top_L) where top_i is the top
    entry in column i (French: rightmost/highest box). If column i is empty,
    top_i = None (or 0).

    Height of column i is a separate accounting for shape.

    Returns list of δ values indexed by column c ∈ {0, 1, ..., max_col+1}:
    δ_c = 1 (RED) if topT(c) > r or c ≤ 0, else 0 (WHITE) with c > current_last_col
    being WHITE.

    Actually: Maya diagram runs over all Z. To the left (c ≤ 0 or c ≤ some
    boundary), all RED. To the right (beyond current tableau's used columns),
    all WHITE. In between, coloring based on topT(c) vs r.
    """
    pass  # will inline below


def next_maya_transitions(T_cols, r):
    """Given tableau state T (list of top entries per column, index 1..L;
    T_cols[0] is unused or dummy), and cutoff r, return dict {c: (new_T, φ_c)}
    where c ∈ W(δ^{(r)}(T)) and adding n = (current_step) on top of column c
    yields the new state.

    Actually since T is state (not tableau), just track top-entries per column.
    We need to know the current shape too — track column HEIGHTS separately.

    Simplify: represent state as (heights, top_entries). heights[i] = height of
    column i (1..L). top_entries[i] = value of top box of column i.

    For adding box in column c, new heights[c] += 1, new top_entries[c] = n.

    Empty columns: heights = 0, top_entry = None. For Maya:
      - if column c is empty (heights[c]=0), it's "white" in the sense that we
        might add here.
      - "topT(i) > r" means column i's top entry > r ⟹ δ_i = 1 (RED).
      - "topT(i) ≤ r" means δ_i = 0 (WHITE).
      - Empty column: topT(i) = 0 (or "-∞"), so 0 ≤ r ⟹ WHITE.
      - Actually convention: infinite white boxes to the right, so empty
        columns to the right are WHITE.

    Let L_use = index of last nonempty column. Columns 1..L_use may be any
    color; columns > L_use are all WHITE (0).

    For c > L_use, the maya has consecutive WHITE forever. So W(δ) contains
    L_use + 1 only if δ_{L_use} = 1 (RED). Otherwise the "run" of WHITE started
    earlier. Then all further c > L_use+1 are WHITE but not preceded by RED,
    so not in W.

    So c ∈ W(δ) iff δ_c = 0 and δ_{c-1} = 1.

    Convention: δ_0 = 1 (part of infinite RED to left)? Or does "left" start
    at some fixed integer? The paper says "infinitely many red boxes to the
    left" — so for column index c → -∞, δ_c = 1.

    We only care about c ≥ 1 in practice (columns exist for i ≥ 1). But c
    can also be = 1 if column 0 is RED (which it is by convention: all c ≤ 0
    are RED).

    So c = 1 is in W(δ) iff column 1 is WHITE (topT(1) ≤ r or column empty).

    Let's just enumerate columns c from 1 to L_use + 1 and check δ_{c-1} and δ_c.
    """
    heights, top = T_cols  # heights[i], top[i] for i=1..
    L_use = max((i for i in range(1, len(heights)) if heights[i] > 0), default=0)

    # Build δ_c for c = 0, 1, ..., L_use + 1
    # δ_0 = 1 (RED by convention, boundary)
    # For c in 1..L_use: δ_c = 1 if top[c] > r else 0. (If column empty in this
    #   range, top[c] = 0, so δ_c = 0 = WHITE.)
    # For c = L_use + 1: WHITE (0), start of infinite WHITE tail.
    delta = {}
    delta[0] = 1
    for c in range(1, L_use + 2):
        if c <= L_use and heights[c] > 0:
            delta[c] = 1 if top[c] > r else 0
        else:
            delta[c] = 0  # empty or beyond

    # W(δ) = {c : δ_c = 0, δ_{c-1} = 1}
    W = [c for c in range(1, L_use + 2) if delta[c] == 0 and delta[c - 1] == 1]
    # R(δ) = {c : δ_c = 1, δ_{c-1} = 0}
    R = [c for c in range(1, L_use + 2) if delta[c] == 1 and delta[c - 1] == 0]

    # φ_c(δ; q) = Π_{b ∈ R} [c - b]_q / Π_{a ∈ W \ {c}} [c - a]_q
    transitions = {}
    for c in W:
        num = 1
        for b in R:
            num = num * q_bracket(c - b)
        den = 1
        for a in W:
            if a != c:
                den = den * q_bracket(c - a)
        if den == 0:
            continue
        phi = num / den
        # Adding box on column c: heights[c] += 1, top[c] = (step number, will
        # be set by caller). But we need to keep track of step number.
        # Return c and phi; caller updates state.
        transitions[c] = phi
    return transitions


def hikita_X_Pn(n):
    """Compute the e-coefficients of X_{P_n}(x; q) via Hikita's Markov chain.

    e_{P_n}(i) = 0 for i=1,2; = i-2 for i ≥ 3.

    Start with empty tableau. At step i, use r = e(i). Enumerate all
    trajectories, weighting by Π φ_c. The e-coefficient of e_λ is the total
    weight of trajectories ending at shape λ.
    """
    # Compute e_{P_n}
    e_hess = [0]  # e[0] unused
    for i in range(1, n + 1):
        if i <= 2:
            e_hess.append(0)
        else:
            e_hess.append(i - 2)

    # State: (heights_tuple, top_tuple, weight_so_far). Use tuples for
    # hashability. heights[0], top[0] unused.
    # Initial: empty tableau.
    max_cols = n + 1  # can never have more than n columns
    init_heights = tuple(0 for _ in range(max_cols + 2))
    init_top = tuple(0 for _ in range(max_cols + 2))
    init_state = (init_heights, init_top)

    # BFS over steps
    states = {init_state: 1}  # state → weight

    for step in range(1, n + 1):
        r = e_hess[step]
        new_states = defaultdict(int)
        for (heights, top), w in states.items():
            # Enumerate transitions
            trans = next_maya_transitions((list(heights), list(top)), r)
            for c, phi in trans.items():
                # Add box in column c: heights[c] += 1, top[c] = step
                new_h = list(heights)
                new_t = list(top)
                new_h[c] += 1
                new_t[c] = step
                new_state = (tuple(new_h), tuple(new_t))
                new_states[new_state] = expand(new_states[new_state] + w * phi)
        states = new_states

    # Collect by shape (partition = row-lengths, from column heights)
    # column heights list H → shape λ where λ_j = #{cols with height ≥ j}
    result = defaultdict(int)
    for (heights, top), w in states.items():
        col_heights = [h for h in heights if h > 0]
        # Now convert to shape (row lengths)
        if not col_heights:
            shape = ()
        else:
            max_h = max(col_heights)
            shape = tuple(sum(1 for h in col_heights if h >= j)
                          for j in range(1, max_h + 1))
        result[shape] = expand(result[shape] + w)

    return dict(result)


def _q_factorial(k):
    """[k]_q! = [1]_q [2]_q ... [k]_q."""
    result = 1
    for i in range(1, k + 1):
        result = result * q_bracket(i)
    return result


def hikita_e_coeffs(n):
    """Compute e-coefficients via Hikita Thm 1.6:
    [e_λ] X_Γ = Pr[X_n = λ] · Π [λ_i]_q!
    """
    shape_probs = hikita_X_Pn(n)
    result = {}
    for lam, prob in shape_probs.items():
        qfact = 1
        for li in lam:
            qfact = qfact * _q_factorial(li)
        result[lam] = expand(prob * qfact)
    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def compare(n):
    from sympy import simplify, cancel, together
    print(f"\n=== n = {n} ===")
    rick = rick_X_Pn(n)
    hik = hikita_e_coeffs(n)

    all_shapes = set(rick.keys()) | set(hik.keys())
    all_ok = True
    for lam in sorted(all_shapes, key=lambda p: (-sum(p), p)):
        r_c = expand(rick.get(lam, 0))
        h_c = cancel(hik.get(lam, 0))
        diff = simplify(r_c - h_c)
        ok = (diff == 0)
        if not ok:
            all_ok = False
        print(f"  e_{lam}:   Rick = {r_c}   Hikita = {h_c}   {'OK' if ok else 'MISMATCH'}")
    print(f"  → {'ALL MATCH' if all_ok else 'MISMATCH DETECTED'}")


if __name__ == "__main__":
    import sys
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    for n in range(1, N + 1):
        compare(n)
