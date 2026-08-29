"""Quick T=16 smoke test for k=0 only."""
import sys
import time
from importlib import util

spec = util.spec_from_file_location(
    "m", "/home/agent/projects/code/2026-07-12-c13-periodicity-T16.py"
)
m = util.module_from_spec(spec)
spec.loader.exec_module(m)


def main():
    print("Loading Q catalog...", flush=True)
    Q_cat, a_s, b_s, c_s = m.load_Q_catalog()
    Q_coeffs = {k: m.Q_poly_coeff_dict(Q_cat[k], a_s, b_s, c_s, 13) for k in Q_cat}
    print(f"Q catalog loaded for k = {sorted(Q_coeffs.keys())}", flush=True)

    T = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    size = 1 << T
    b_chunk = min(4096, size)
    print(f"T={T}, size={size}, b_chunk={b_chunk}", flush=True)
    for k_test in [0, 6, 3]:
        L = 12 - k_test
        print(f"\nRunning k={k_test}, L={L}...", flush=True)
        t0 = time.time()
        min_v2, nz, nt = m.chunked_check_hk_via_catalog(
            Q_coeffs[k_test], L, T, size, b_chunk)
        dt = time.time() - t0
        print(f"  min_v2 = {min_v2}, {nz}/{nt} zero, {dt:.1f}s", flush=True)


if __name__ == "__main__":
    sys.exit(main())
