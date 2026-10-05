"""Alternative reading: (id - t e_1) star (id - s e_1)."""
from sympy import symbols, expand, sympify

s, t = symbols('s t')
MAX_N = 5
p = {n: symbols(f'p_{n}') for n in range(1, MAX_N+1)}

def all_partitions(n):
    parts = [tuple()]
    def gen(remaining, max_part, current):
        if remaining == 0:
            parts.append(tuple(current)); return
        for k in range(min(remaining, max_part), 0, -1):
            gen(remaining - k, k, current + [k])
    for m in range(1, n+1):
        gen(m, m, [])
    return parts

def coproduct(lam):
    r = len(lam); result = []
    for mask in range(2**r):
        left, right = [], []
        for i in range(r):
            if (mask >> i) & 1: left.append(lam[i])
            else: right.append(lam[i])
        left.sort(reverse=True); right.sort(reverse=True)
        result.append((tuple(left), tuple(right)))
    return result

def apply_op_id(op_scalar, lam):
    """(id - c*e_1)(p_lam) = p_lam if len(lam) != 1, else (1 - c) p_lam.
       (id - c*e_1)(1) = 1."""
    if len(lam) == 1:
        return [(lam, 1 - op_scalar)]
    else:
        return [(lam, sympify(1))]

def multiply_lambdas(lam1, lam2):
    return tuple(sorted(list(lam1) + list(lam2), reverse=True))

def convolution_apply(lam):
    cp = coproduct(lam)
    result = {}
    for (left, right) in cp:
        for (l_lam, l_sc) in apply_op_id(t, left):
            for (r_lam, r_sc) in apply_op_id(s, right):
                prod_lam = multiply_lambdas(l_lam, r_lam)
                sc = l_sc * r_sc
                result[prod_lam] = result.get(prod_lam, 0) + sc
    return {k: expand(v) for k, v in result.items() if expand(v) != 0}

# Predicted formula: eigenvalue c_ell on p_lam:
# c_0 = 1
# c_1 = 2 - (s+t)
# c_2 = 4 - 2(s+t) + 2*s*t
# c_ell = 2^ell - ell*(s+t) for ell >= 3
def predicted(ell):
    if ell == 0: return sympify(1)
    if ell == 1: return 2 - (s+t)
    if ell == 2: return 4 - 2*(s+t) + 2*s*t
    return 2**ell - ell*(s+t)

partitions = all_partitions(MAX_N)
print("Reading: 1 = id_Lambda.\n")
for lam in partitions:
    result = convolution_apply(lam)
    ell = len(lam)
    pred = predicted(ell)
    if pred == 0:
        expected = {}
    else:
        expected = {lam: pred}
    if len(result) == 1 and lam in result and expand(result[lam] - pred) == 0:
        print(f"  lam={lam} ell={ell}: OK  eig = {expand(pred)}")
    elif not result and pred == 0:
        print(f"  lam={lam} ell={ell}: OK  eig = 0")
    else:
        print(f"  lam={lam} ell={ell}: FAIL  pred={pred}  got={result}")
