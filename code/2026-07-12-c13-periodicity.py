"""Day 92 -- c=13 periodicity check at T=16 to certify beta'(13) >= 16.

Adapts the c=11 periodicity strategy (T=12) to c=13 (T=16). Uses the
Q_k catalog for k = 0..6 (with factorized h_k = (a+3)_L * (b+2)_L * Q_k(a,b,c))
and cached fitted polynomials for k = 7..12.

Grid: 2^16 x 2^16 = 2^32 pairs total, shell (a+b odd) = 2^31 = 2.1B residues per k.
Chunked in b to fit memory: chunk size 65536 x 4096 = 2 GB per chunk, 16 chunks.

Combined with Day 91 UB witness H_13(7, 0, 6) with v_2 = 16, PASS => beta'(13) = 16 EXACT.

Writes JSON result to /home/agent/projects/code/2026-07-12-c13-periodicity-result.json.
"""
import gc
import json
import pickle
import resource
import sys
import time
from math import factorial

import numpy as np
from sympy import Poly, expand, symbols, sympify


def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024


def v2(n):
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def load_Q_catalog():
    with open("/home/agent/projects/code/2026-07-11-Qk-catalog.json") as f:
        cat = json.load(f)
    a_s, b_s, c_s = symbols('a b c')
    Q = {}
    for ks, s in cat["Q_k_low_k"].items():
        Q[int(ks)] = sympify(s)
    Q[6] = sympify(cat["Q_k_extended"]["6"]["poly_factored"])
    return Q, a_s, b_s, c_s


def Q_poly_coeff_dict(Q_poly, a_s, b_s, c_s, c_val):
    Q_c = expand(Q_poly.subs(c_s, c_val))
    p = Poly(Q_c, a_s, b_s)
    return p.as_dict()


def chunked_check_hk_via_catalog(coeff_dict, L, T, size, b_chunk):
    """h_k^{(13)}(a, b) = (a+3)_L * (b+2)_L * Q(a, b) mod 2^T.
    Return (min_v2, n_zero, n_total) over shell a+b odd.
    """
    modulus = 1 << T
    mask = np.int64(modulus - 1)
    max_da = max((k[0] for k in coeff_dict.keys()), default=0)
    max_db = max((k[1] for k in coeff_dict.keys()), default=0)

    a_vec = np.arange(size, dtype=np.int64)
    poch_a = np.ones(size, dtype=np.int64) & mask
    for i in range(L):
        poch_a = (poch_a * ((a_vec + 3 + i) & mask)) & mask

    a_powers = np.zeros((max_da + 1, size), dtype=np.int64)
    a_powers[0, :] = 1
    for d in range(1, max_da + 1):
        a_powers[d, :] = (a_powers[d - 1, :] * a_vec) & mask
    C = np.zeros((max_da + 1, max_db + 1), dtype=np.int64)
    for (da, db), coef in coeff_dict.items():
        C[da, db] = int(coef) % modulus
    step1 = np.matmul(a_powers.T, C) & mask  # (size, max_db+1)

    total_n_zero = 0
    total_n_shell = 0
    min_v2_global = float('inf')

    for b_start in range(0, size, b_chunk):
        b_end = min(b_start + b_chunk, size)
        w = b_end - b_start
        b_vec = np.arange(b_start, b_end, dtype=np.int64)
        poch_b = np.ones(w, dtype=np.int64) & mask
        for i in range(L):
            poch_b = (poch_b * ((b_vec + 2 + i) & mask)) & mask
        b_powers = np.zeros((max_db + 1, w), dtype=np.int64)
        b_powers[0, :] = 1
        for d in range(1, max_db + 1):
            b_powers[d, :] = (b_powers[d - 1, :] * b_vec) & mask
        Q_chunk = np.matmul(step1, b_powers) & mask  # (size, w)
        h_chunk = (Q_chunk * poch_a[:, None]) & mask
        h_chunk = (h_chunk * poch_b[None, :]) & mask
        parity_a = (a_vec & 1)
        parity_b = (b_vec & 1)
        parity_mask = ((parity_a[:, None] + parity_b[None, :]) & 1) == 1
        shell_residues = h_chunk[parity_mask]
        n_shell = int(parity_mask.sum())
        n_zero = int((shell_residues == 0).sum())
        total_n_shell += n_shell
        total_n_zero += n_zero
        nz = shell_residues[shell_residues != 0]
        if len(nz) > 0:
            lowbit = nz & (-nz)
            v2s = np.log2(lowbit.astype(np.float64)).astype(np.int32)
            m = int(v2s.min())
            if m < min_v2_global:
                min_v2_global = m
        del h_chunk, Q_chunk, poch_b, b_powers, shell_residues, parity_mask, nz
        gc.collect()
    if total_n_zero == total_n_shell:
        return (T, total_n_zero, total_n_shell, True)  # min v2 >= T
    return (min_v2_global, total_n_zero, total_n_shell, False)


def chunked_check_hk_via_fit(coeff_dict, T, size, b_chunk):
    """Evaluate polynomial P(a, b) mod 2^T chunked in b."""
    modulus = 1 << T
    mask = np.int64(modulus - 1)
    max_da = max(k[0] for k in coeff_dict.keys())
    max_db = max(k[1] for k in coeff_dict.keys())

    a_vec = np.arange(size, dtype=np.int64)
    a_powers = np.zeros((max_da + 1, size), dtype=np.int64)
    a_powers[0, :] = 1
    for d in range(1, max_da + 1):
        a_powers[d, :] = (a_powers[d - 1, :] * a_vec) & mask

    C = np.zeros((max_da + 1, max_db + 1), dtype=np.int64)
    for (da, db), coef in coeff_dict.items():
        C[da, db] = int(coef) % modulus
    step1 = np.matmul(a_powers.T, C) & mask

    total_n_zero = 0
    total_n_shell = 0
    min_v2_global = float('inf')

    for b_start in range(0, size, b_chunk):
        b_end = min(b_start + b_chunk, size)
        w = b_end - b_start
        b_vec = np.arange(b_start, b_end, dtype=np.int64)
        b_powers = np.zeros((max_db + 1, w), dtype=np.int64)
        b_powers[0, :] = 1
        for d in range(1, max_db + 1):
            b_powers[d, :] = (b_powers[d - 1, :] * b_vec) & mask
        h_chunk = np.matmul(step1, b_powers) & mask
        parity_a = (a_vec & 1)
        parity_b = (b_vec & 1)
        parity_mask = ((parity_a[:, None] + parity_b[None, :]) & 1) == 1
        shell_residues = h_chunk[parity_mask]
        n_shell = int(parity_mask.sum())
        n_zero = int((shell_residues == 0).sum())
        total_n_shell += n_shell
        total_n_zero += n_zero
        nz = shell_residues[shell_residues != 0]
        if len(nz) > 0:
            lowbit = nz & (-nz)
            v2s = np.log2(lowbit.astype(np.float64)).astype(np.int32)
            m = int(v2s.min())
            if m < min_v2_global:
                min_v2_global = m
        del h_chunk, b_powers, shell_residues, parity_mask, nz
        gc.collect()
    if total_n_zero == total_n_shell:
        return (T, total_n_zero, total_n_shell, True)
    return (min_v2_global, total_n_zero, total_n_shell, False)


def main():
    print("=" * 80, flush=True)
    print("Day 92 -- c=13 periodicity check at T=16 (chunked)", flush=True)
    print("Goal: prove LB_k >= 16 for all k = 0..12, giving beta'(13) >= 16 tight.", flush=True)
    print("=" * 80, flush=True)

    c_val = 13
    T_check = 16
    jmax = c_val - 1
    size = 1 << T_check  # 65536
    b_chunk = 256  # keep chunk memory small: 65536 * 256 * 8 = 128 MB per int64 array

    print(f"Grid: {size} x {size} = 2^{2*T_check} pairs. Shell: 2^{2*T_check - 1}.", flush=True)
    print(f"Chunk: {size} x {b_chunk} = {size * b_chunk * 8 // (1<<20)} MB per int64 array, "
          f"{size // b_chunk} chunks.", flush=True)
    print(flush=True)

    Q_cat, a_s, b_s, c_s = load_Q_catalog()
    Q_coeffs = {}
    for k, Q_poly in Q_cat.items():
        Q_coeffs[k] = Q_poly_coeff_dict(Q_poly, a_s, b_s, c_s, c_val)

    with open("/home/agent/projects/code/2026-07-12-c13-coeff-high-k.pkl", "rb") as f:
        hk_coeff_high = pickle.load(f)

    print(f"[k=0..6 via Q-cat + Pochhammer factorization]", flush=True)
    print(f"[k=7..12 via fitted polynomial from cache]", flush=True)
    print(flush=True)

    all_pass = True
    fail_details = []
    results = {}
    t_start_total = time.time()
    for k in range(jmax + 1):
        t0 = time.time()
        if k in Q_coeffs:
            L = c_val - 1 - k
            min_v2, n_zero, n_total, all_zero = chunked_check_hk_via_catalog(
                Q_coeffs[k], L, T_check, size, b_chunk)
            src = "Q-cat"
        elif k in hk_coeff_high:
            min_v2, n_zero, n_total, all_zero = chunked_check_hk_via_fit(
                hk_coeff_high[k], T_check, size, b_chunk)
            src = "fit"
        else:
            print(f"  k={k}: SKIPPED (no source)", flush=True)
            all_pass = False
            continue
        dt = time.time() - t0
        if all_zero:
            status = f"PASS (all zero mod 2^{T_check})"
            min_v2_report = f">={T_check}"
        elif min_v2 >= T_check:
            status = f"PASS-partial (min v_2 = {min_v2})"
            min_v2_report = int(min_v2)
        else:
            status = f"FAIL (min v_2 = {min_v2} < {T_check})"
            all_pass = False
            fail_details.append((k, int(min_v2)))
            min_v2_report = int(min_v2)
        print(f"  k={k:>2d} [{src:>5s}]: min v_2 = {min_v2_report}, "
              f"{n_zero}/{n_total} zero, {dt:.1f}s  {status}", flush=True)
        results[k] = dict(source=src, min_v2=min_v2_report,
                          n_zero=n_zero, n_total=n_total,
                          all_zero=bool(all_zero), time_s=dt)

    total_dt = time.time() - t_start_total
    print(flush=True)
    print("=" * 80, flush=True)
    print(f"Total periodicity check: {total_dt:.1f}s", flush=True)
    print("=" * 80, flush=True)
    if all_pass:
        print(f"  All k in {{0..{jmax}}}: h_k^{{({c_val})}} mod 2^{T_check} == 0 or v_2 >= {T_check}.", flush=True)
        print(f"  By 2^{T_check}-periodicity lemma, LB_k^{{({c_val})}} >= {T_check} for all k.", flush=True)
        print(f"  By v_2(sum) >= min(v_2): beta'({c_val}) >= {T_check}.", flush=True)
        print(f"  UB witness: H_13(7, 0, 6) = 933042399799910400000, v_2 = 16, distinct-min.", flush=True)
        print(f"  Hence beta'(13) = 16 EXACT. QED. (computed grade.)", flush=True)
        verdict = "beta_prime_13_equals_16_EXACT"
    else:
        print(f"  FAIL. Some k have min v_2 < {T_check}:", flush=True)
        for k, mv in fail_details:
            print(f"    k={k}: min v_2 = {mv}", flush=True)
        verdict = "FAIL_lower_valuation_found"

    output = {
        "c": c_val,
        "T": T_check,
        "n_residues_per_k": (size * size) // 2,
        "n_k_values": jmax + 1,
        "total_time_s": total_dt,
        "all_pass": bool(all_pass),
        "verdict": verdict,
        "per_k_results": {str(k): v for k, v in results.items()},
        "fail_details": [{"k": k, "min_v2": mv} for k, mv in fail_details],
    }
    out_path = "/home/agent/projects/code/2026-07-12-c13-periodicity-result.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"[json] wrote {out_path}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
