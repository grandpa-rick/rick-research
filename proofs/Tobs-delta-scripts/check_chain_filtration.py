# Quick sanity check: verify the comult inclusion T_{r+s} \subseteq T_r T_s
# holds for the chain filtration on {0,1}^n.
#
# Setup: X = {0,1}^n. ~_r = fibers of projection onto first (n-r) coords.
# Strategy sigma : X -> Y. sigma is ~_r-measurable iff constant on ~_r-classes.

from itertools import product

n = 4
X = list(product([0,1], repeat=n))
Y = [0, 1]

def proj(x, r):
    # project to first (n-r) coords (drop last r)
    if r >= n: return ()
    return x[:n-r]

def equiv_classes(r):
    cls = {}
    for x in X:
        key = proj(x, r)
        cls.setdefault(key, []).append(x)
    return list(cls.values())

def is_measurable(sigma, r):
    # sigma : X -> Y as dict; check sigma constant on ~_r classes
    for cls in equiv_classes(r):
        vals = set(sigma[x] for x in cls)
        if len(vals) > 1:
            return False
    return True

# Try all 2^16 strategies. For each, check ~_r-measurability for r=0..n.
all_strategies = []
for vals in product(Y, repeat=len(X)):
    sigma = {x: v for x, v in zip(X, vals)}
    all_strategies.append(sigma)

print(f"Total strategies: {len(all_strategies)}")

# For each r, count ~_r-measurable strategies
for r in range(n+1):
    count = sum(1 for s in all_strategies if is_measurable(s, r))
    print(f"  r={r}: {count} ~_r-measurable strategies")

# Verify: r=0 gives all, r=n gives 2 (constants).
# Verify chain: r <= s implies ~_r-measurable strategies INCLUDE ~_s-measurable strategies
print("\nChain check (anti-monotone in r):")
for r in range(n):
    M_r = {tuple(sorted(s.items())) for s in all_strategies if is_measurable(s, r)}
    M_rp1 = {tuple(sorted(s.items())) for s in all_strategies if is_measurable(s, r+1)}
    print(f"  M_{r} >= M_{r+1}: {M_rp1 <= M_r} (sizes {len(M_r)} vs {len(M_rp1)})")

# Verify comult: T_{r+s} \subseteq T_r T_s
# (sigma is ~_{r+s}-measurable) implies (sigma is ~_r AND ~_s -measurable)
print("\nComult check: ~_{r+s} measurable => ~_r AND ~_s measurable")
for r in range(n+1):
    for s in range(n+1):
        rs = min(r+s, n)
        M_rs = {tuple(sorted(sig.items())) for sig in all_strategies if is_measurable(sig, rs)}
        M_r_and_s = {tuple(sorted(sig.items())) for sig in all_strategies if is_measurable(sig, r) and is_measurable(sig, s)}
        ok = M_rs <= M_r_and_s
        eq = M_rs == M_r_and_s
        flag = "=" if eq else ("⊊" if ok else "FAIL")
        print(f"  r={r}, s={s} (r+s={rs}): |T_{{r+s}}|={len(M_rs)}, |T_r∩T_s|={len(M_r_and_s)}, {flag}")
