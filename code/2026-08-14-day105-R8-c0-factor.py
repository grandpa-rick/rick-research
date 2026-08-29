"""Day 105 (2026-08-13) — Factor c_0 = Q_{16}(6, 8, R=8) via Vandermonde solve on
37 samples of Q_{16}(6, 8, c) at c ≡ 8 mod 16, then test H4 hunch.

H4 predicts c_0 = 2^29 * O_8 with O_8 = 3^8 * 5^4 * 7^2 * 11 * 13.
"""

import json
import time
import sys
import sympy as sp
from sympy import Matrix, factorint


def v_p(n, p):
    if n == 0:
        return None
    n = abs(int(n))
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def main():
    data_path = '/home/agent/projects/code/2026-08-14-day105-R8-samples.json'
    with open(data_path) as f:
        data = json.load(f)
    data = [(int(t), int(c), int(Q)) for (t, c, Q) in data]
    n = len(data)
    print(f"Loaded {n} samples", flush=True)
    print(f"t range: {data[0][0]} .. {data[-1][0]}", flush=True)

    # Vandermonde solve: A[i][k] = t_i^k, y[i] = Q_i.
    print(f"Building {n}x{n} Vandermonde system...", flush=True)
    A_rows = []
    y_vec = []
    for (t, c, Q) in data:
        A_rows.append([t**k for k in range(n)])
        y_vec.append(Q)
    A = Matrix(A_rows)
    y = Matrix(y_vec)

    print(f"Solving {n}x{n} system...", flush=True)
    t0 = time.time()
    sol = A.solve(y)
    print(f"Solve took {time.time()-t0:.1f}s", flush=True)

    # c_0 is the constant term in t: this corresponds to t=0, i.e. c = 8 = R.
    c_0 = int(sol[0])
    print(f"\nc_0 = Q_16(6, 8, 8) = {c_0}", flush=True)
    print(f"digits: {len(str(abs(c_0)))}", flush=True)
    print(f"sign: {'+' if c_0 > 0 else ('-' if c_0 < 0 else '0')}", flush=True)

    # Factor
    n_abs = abs(c_0)
    print("\nAttempting full factorization with sympy.factorint...", flush=True)
    t1 = time.time()
    try:
        fac = factorint(n_abs)
        print(f"factorint took {time.time()-t1:.1f}s", flush=True)
        print(f"Factorization: {fac}", flush=True)
    except Exception as e:
        print(f"factorint raised: {e}", flush=True)
        fac = None

    # Print valuations for small primes.
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19]
    print("\nValuations at small primes:")
    for p in small_primes:
        vp = v_p(c_0, p)
        print(f"  v_{p}(c_0) = {vp}")

    # H4 predicted factorization
    H4_predicted = {2: 29, 3: 8, 5: 4, 7: 2, 11: 1, 13: 1}
    predicted_val = 1
    for p, e in H4_predicted.items():
        predicted_val *= p**e
    print(f"\nH4 predicted magnitude: 2^29 * 3^8 * 5^4 * 7^2 * 11 * 13 = {predicted_val}")
    if fac is not None:
        print(f"Actual |c_0|                                          = {n_abs}")
        print(f"Ratio |c_0| / predicted = {sp.Rational(n_abs, predicted_val)}")

    # Match check
    if fac is not None:
        matches = (fac == H4_predicted)
        print(f"\nH4 exact match? {'YES' if matches else 'NO'}")
        if not matches:
            print("Diffs:")
            all_primes = sorted(set(H4_predicted) | set(fac))
            for p in all_primes:
                pred = H4_predicted.get(p, 0)
                act = fac.get(p, 0)
                mark = "OK" if pred == act else "MISMATCH"
                print(f"  p={p}: predicted={pred}, actual={act} [{mark}]")

    # Also save c_0 for downstream use.
    out = {
        'c_0': str(c_0),
        'factorization': {str(p): e for p, e in (fac.items() if fac else [])},
        'H4_predicted': {str(p): e for p, e in H4_predicted.items()},
    }
    with open('/home/agent/projects/code/2026-08-14-day105-R8-c0-result.json', 'w') as f:
        json.dump(out, f, indent=2)
    print("\nSaved result JSON.")


if __name__ == '__main__':
    main()
