"""
Refined dip formula test (2026-07-07).
- beta(c) closed form: beta(c) = 2(c-1) - s2(c-1)  (proved).
- beta'(c) empirical from Clio for c=4..10: [4, 3, 7, 6, 11, 9, 14].
- Refined conjecture: Delta beta'(c) = 1 - max(2, v2(c-1))  for odd c >= 3.
"""
import os
from importlib import util

_here = os.path.dirname(os.path.abspath(__file__))
_spec = util.spec_from_file_location(
    "c5spot", os.path.join(_here, "2026-07-05-clio-c5-spotcheck.py"))
_c5 = util.module_from_spec(_spec)
_spec.loader.exec_module(_c5)
H5 = _c5.H5


def s2(n): return bin(n).count("1")


def v2(n):
    if n == 0:
        return float("inf")
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def beta(c):
    return 2 * (c - 1) - s2(c - 1)


# Clio's empirical beta'(c) for c = 4..10
BETA_PRIME = {4: 4, 5: 3, 6: 7, 7: 6, 8: 11, 9: 9, 10: 14}


def predicted_dbp(c):
    """Refined conjecture: Delta beta'(c) = 1 - max(2, v2(c-1)), odd c >= 3."""
    return 1 - max(2, v2(c - 1))


# ---------- Table 1: beta and Delta beta vs Kummer ----------
print("=" * 78)
print("Table 1: beta(c) and Delta_beta(c) vs 1 + v2(c-1) (Kummer identity)")
print("=" * 78)
hdr = "  c  v2(c-1)  s2(c-1)   beta(c)  Dbeta   1+v2   match"
print(hdr)
kummer_ok = True
for c in range(3, 16):
    b = beta(c)
    bp = beta(c - 1)
    db = b - bp
    v = v2(c - 1)
    pred = 1 + v
    ok = (db == pred)
    if not ok:
        kummer_ok = False
    print(f" {c:>2}    {v:>3}      {s2(c-1):>3}      {b:>3}   {db:>3}    "
          f"{pred:>3}   {str(ok):>5}")
print(f"Kummer identity Delta_beta(c) = 1 + v2(c-1) holds for c=3..15: {kummer_ok}")

# ---------- Table 2: refined conjecture, odd c in [5,7,9] ----------
print()
print("=" * 78)
print("Table 2: Refined conjecture  Delta_beta'(c) = 1 - max(2, v2(c-1)), odd c")
print("=" * 78)
print("  c  v2(c-1)  bp(c-1)  bp(c)  Dbp   pred   match")
conj_results = {}
for c in [5, 7, 9]:
    v = v2(c - 1)
    bp_prev = BETA_PRIME[c - 1]
    bp_now = BETA_PRIME[c]
    d = bp_now - bp_prev
    pred = predicted_dbp(c)
    ok = (d == pred)
    conj_results[c] = ok
    print(f" {c:>2}    {v:>3}     {bp_prev:>3}    {bp_now:>3}   {d:>+3}   "
          f"{pred:>+3}   {str(ok):>5}")

# ---------- Table 3: Predictions for c = 11..17 ----------
print()
print("=" * 78)
print("Table 3: Predictions for c = 11..17 (assuming refined conjecture on odd c)")
print("=" * 78)
print("Note: refined conjecture only covers odd c. For even c we extrapolate")
print("empirical Clio deltas Dbp(6)=4, Dbp(8)=5, Dbp(10)=5 --> assume Dbp(even)=5.")
print()
print("  c  v2(c-1)   Dbp   source           pred bp(c)")
predictions = {}
running = BETA_PRIME[10]  # 14
for c in range(11, 18):
    v = v2(c - 1)
    if c % 2 == 1:
        d = predicted_dbp(c)
        tag = "odd (conj)"
    else:
        d = 5  # empirical extrapolation
        tag = "even (emp)"
    running += d
    predictions[c] = running
    print(f" {c:>2}    {v:>3}    {d:>+3}   {tag:<15}   {running:>5}")

# ---------- Task 7: independent beta'(5) via H5 brute force ----------
print()
print("=" * 78)
print("Task 7: independent beta'(5) from H_5 brute force (a,b<32, j<12)")
print("=" * 78)
best = None
best_tup = None
for a in range(32):
    for b in range(32):
        for j in range(12):
            H = H5(a, b, j)
            if H == 0:
                continue
            v = v2(H)
            if best is None or v < best:
                best = v
                best_tup = (a, b, j)
print(f"min v2(H_5(a,b,j)) = {best} at (a,b,j) = {best_tup}")
print(f"Matches Clio's beta'(5) = 3? {best == 3}")

# ---------- Task 8: parity/carry structure for odd c ----------
print()
print("=" * 78)
print("Task 8: parity/carry structure  Dbp + v2  and  v2>=3 --> Dbp = 1 - v2")
print("=" * 78)
print("  c  v2(c-1)  Dbp   Dbp+v2   low(v2<=2, in {-1,0,1})   high(v2>=3, 1-v2)")
for c in [5, 7, 9]:
    v = v2(c - 1)
    d = BETA_PRIME[c] - BETA_PRIME[c - 1]
    s = d + v
    if v <= 2:
        low = "yes" if s in (-1, 0, 1) else "no"
        high = "n/a"
    else:
        low = "n/a"
        high = "yes" if d == 1 - v else "no"
    print(f" {c:>2}    {v:>3}    {d:>+3}   {s:>+4}      {low:>18}         {high:>10}")

# ---------- Task 9: pure-power phenomenon at c-1 = 2^k ----------
print()
print("=" * 78)
print("Task 9: pure-power c-1 = 2^k (k>=3):  refined dip Dbp = 1 - k")
print("=" * 78)
print("  k   c-1   c   v2   Dbp   baseline(1-max(2,2)=-1)   delta_s = Dbp - baseline")
for k in range(3, 7):
    cm1 = 2 ** k
    c = cm1 + 1
    v = k
    d = 1 - max(2, v)
    baseline = -1
    delta_s = d - baseline
    print(f" {k:>2}  {cm1:>4}  {c:>3}   {v:>2}   {d:>+3}     {baseline:>+3}"
          f"                       {delta_s:>+4}")
print("So delta_s = -(k-2) for pure powers: the dip DEEPENS linearly in k,")
print("it is NOT zero at pure powers (contra a 'pure-power zero-correction' guess).")

# ---------- Summary ----------
print()
print("=" * 78)
print("Summary")
print("=" * 78)
print(f"Kummer Delta_beta(c) = 1 + v2(c-1) confirmed for c=3..15: {kummer_ok}")
print("Refined conjecture Delta_beta'(c) = 1 - max(2, v2(c-1)) matches Clio:")
for c, ok in conj_results.items():
    print(f"  c={c}: {ok}")
print(f"Independent beta'(5) from H_5 brute force: {best}")
print(f"Predicted beta'(11) = {predictions[11]}")
print(f"Predicted beta'(13) = {predictions[13]}")
print(f"Predicted beta'(15) = {predictions[15]}")
print(f"Predicted beta'(17) = {predictions[17]}")
