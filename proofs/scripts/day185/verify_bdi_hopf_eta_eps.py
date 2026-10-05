"""
Verify: (eta*eps - t*e_1) star (eta*eps - s*e_1) as endomorphism of Sym.

We work in Sym over Q(s,t). Basis: power sums p_lambda.
Coproduct: Delta(p_n) = p_n ⊗ 1 + 1 ⊗ p_n. (p_n primitive.)
Product: Sym is polynomial in p_1, p_2, p_3, ...
Eulerian idempotent e_1 = projection onto Prim = span{p_n}:
  e_1(p_lambda) = p_lambda if ell(lambda) = 1, else 0.
  e_1(1) = 0.
eta o eps: (eta o eps)(x) = x if deg(x) = 0, else 0.
  So (eta o eps)(1) = 1, (eta o eps)(p_lambda) = 0 for lambda != empty.

Convolution: (f * g)(x) = sum f(x_(1)) g(x_(2)).

Test on all p_lambda with |lambda| <= 4.
"""
from sympy import symbols, expand, Poly, Rational, sympify
from sympy.combinatorics.partitions import IntegerPartition

s, t = symbols('s t')

# Represent power sums p_n as sympy symbols
MAX_N = 5
p = {n: symbols(f'p_{n}') for n in range(1, MAX_N+1)}

# All partitions with |lambda| <= MAX_N, encoded as tuples in decreasing order
def all_partitions(n):
    """All partitions of integers 0, 1, ..., n."""
    parts = [tuple()]
    def gen(remaining, max_part, current):
        if remaining == 0:
            parts.append(tuple(current))
            return
        for k in range(min(remaining, max_part), 0, -1):
            gen(remaining - k, k, current + [k])
    for m in range(1, n+1):
        gen(m, m, [])
    return parts

def p_lambda(lam):
    """Symbolic p_lambda = prod p_lambda_i."""
    if not lam:
        return sympify(1)
    r = sympify(1)
    for pi in lam:
        r *= p[pi]
    return r

def length(lam):
    return len(lam)

def coproduct(lam):
    """
    Delta(p_lambda) as list of (left_lam, right_lam) with multiplicity.
    Delta(p_n) = p_n ⊗ 1 + 1 ⊗ p_n.
    For lam = (lam_1, ..., lam_r): Delta(p_lam) = prod (p_{lam_i} ⊗ 1 + 1 ⊗ p_{lam_i}).
    Choose for each i whether p_{lam_i} goes left or right.
    """
    r = len(lam)
    result = []  # list of (left_lam, right_lam) — no multiplicity, since choices are distinct
    for mask in range(2**r):
        left = []
        right = []
        for i in range(r):
            if (mask >> i) & 1:
                left.append(lam[i])
            else:
                right.append(lam[i])
        left.sort(reverse=True)
        right.sort(reverse=True)
        result.append((tuple(left), tuple(right)))
    return result

def apply_eps_eta(lam, scalar):
    """(eta o eps)(scalar * p_lam) = scalar if lam = (), else 0."""
    if len(lam) == 0:
        return scalar
    return 0

def apply_e1(lam, scalar):
    """e_1(scalar * p_lam) = scalar if len(lam) == 1, else 0. Result stays as scalar * p_lam if len == 1."""
    if len(lam) == 1:
        return scalar
    return 0

def apply_op(op_name, lam, scalar):
    """
    op_name: '(eta*eps - t*e_1)' or '(eta*eps - s*e_1)'.
    Returns (new_lam, new_scalar) with new_lam either (), or lam if len(lam)==1, or None (zero).
    Actually op preserves lam when nonzero: returns list of (lam, scalar) contributions.
    """
    contribs = []
    ee = apply_eps_eta(lam, scalar)
    if ee != 0:
        contribs.append((lam, ee))  # lam = ()
    if op_name == 't':
        e1 = apply_e1(lam, scalar)
        if e1 != 0:
            contribs.append((lam, -t * e1))
    else:  # 's'
        e1 = apply_e1(lam, scalar)
        if e1 != 0:
            contribs.append((lam, -s * e1))
    return contribs

def multiply_lambdas(lam1, lam2):
    """Product p_lam1 * p_lam2 = p_(lam1 concat lam2), sorted decreasing."""
    combined = list(lam1) + list(lam2)
    combined.sort(reverse=True)
    return tuple(combined)

def convolution_apply(lam):
    """Apply (eta*eps - t e_1) star (eta*eps - s e_1) to p_lam."""
    cp = coproduct(lam)
    result = {}  # map partition tuple -> scalar
    for (left, right) in cp:
        left_contribs = apply_op('t', left, sympify(1))
        for (l_lam, l_sc) in left_contribs:
            right_contribs = apply_op('s', right, sympify(1))
            for (r_lam, r_sc) in right_contribs:
                prod_lam = multiply_lambdas(l_lam, r_lam)
                sc = l_sc * r_sc
                if prod_lam in result:
                    result[prod_lam] += sc
                else:
                    result[prod_lam] = sc
    # Simplify
    result = {k: expand(v) for k, v in result.items() if expand(v) != 0}
    return result

# Test predicted formula: eigenvalue on p_lam depends only on ell(lam):
# ell = 0: 1
# ell = 1: -(s+t)
# ell = 2: 2*s*t
# ell >= 3: 0
def predicted(lam):
    l = length(lam)
    if l == 0: return sympify(1)
    if l == 1: return -(s + t)
    if l == 2: return 2*s*t
    return sympify(0)

partitions = all_partitions(MAX_N)
print(f"Testing {len(partitions)} partitions with |lam| <= {MAX_N}.\n")
all_pass = True
for lam in partitions:
    result = convolution_apply(lam)
    pred_scalar = predicted(lam)
    # Expected: result = {lam: pred_scalar} if pred_scalar != 0, else {}
    if pred_scalar == 0:
        expected = {}
    else:
        expected = {lam: pred_scalar}
    if result != expected:
        # More lenient check: eigenvalue on lam
        if len(result) == 1 and lam in result:
            got = expand(result[lam])
            if expand(got - pred_scalar) == 0:
                print(f"  lam={lam} ell={length(lam)}: OK  eigenvalue = {got}")
                continue
        print(f"  lam={lam} ell={length(lam)}: FAIL")
        print(f"    predicted: {pred_scalar} * p_{lam}")
        print(f"    got: {result}")
        all_pass = False
    else:
        eig = pred_scalar
        print(f"  lam={lam} ell={length(lam)}: OK  eigenvalue = {eig}")

print()
print("ALL PASS" if all_pass else "SOME FAILURES")
