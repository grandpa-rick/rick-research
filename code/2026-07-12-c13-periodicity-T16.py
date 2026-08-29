"""Day 91 -- c=13 periodicity check at T = 16.

Grid: 2^32 pairs -- infeasible to hold in memory. Solution: chunk b dimension.

Goal: prove LB_k^{(13)} >= 16 for all k = 0..12, giving beta'(13) >= 16 and,
combined with UB = 16, beta'(13) = 16 EXACT.

Method: for each k, iterate over b-chunks. For each chunk, compute
h_k(a, b) mod 2^16 for a in [0, 2^16), b in chunk. Check that all shell
residues are 0 mod 2^16 (equivalent to v_2 >= 16).

Uses Q_k catalog for k = 0..6 and fitted polynomials for k = 7..12
(cache: 2026-07-12-c13-coeff-high-k.pkl).
"""
import json
import pickle
import sys
import time
from importlib import util
from math import factorial

import numpy as np
from sympy import Poly, expand, symbols, sympify


def v2(n):
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


# ---------------------------------------------------------------------------
# Q-cat and poly coefficient extraction.
# ---------------------------------------------------------------------------

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
    return p.as_dict()  # {(da, db): coef}


# ---------------------------------------------------------------------------
# Chunked evaluation.
# ---------------------------------------------------------------------------

def chunked_check_hk_via_catalog(coeff_dict, L, T, size, b_chunk):
    """h_k^{(13)}(a, b) = (a+3)_L * (b+2)_L * poly(a, b, coeff_dict) mod 2^T.
    Compute over full grid [0, size)^2 chunked in b. Return (min_v2, n_zero, n_total).

    L is the Pochhammer length. coeff_dict is Q polynomial as {(da, db): coef}.
    """
    modulus = 1 << T
    mask = np.int64(modulus - 1)
    max_da = max((k[0] for k in coeff_dict.keys()), default=0)
    max_db = max((k[1] for k in coeff_dict.keys()), default=0)

    a_vec = np.arange(size, dtype=np.int64)
    # Precompute (a+3)_L
    poch_a = np.ones(size, dtype=np.int64) & mask
    for i in range(L):
        poch_a = (poch_a * ((a_vec + 3 + i) & mask)) & mask

    # Precompute a_powers for Q evaluation
    a_powers = np.zeros((max_da + 1, size), dtype=np.int64)
    a_powers[0, :] = 1
    for d in range(1, max_da + 1):
        a_powers[d, :] = (a_powers[d - 1, :] * a_vec) & mask
    # Build C matrix
    C = np.zeros((max_da + 1, max_db + 1), dtype=np.int64)
    for (da, db), coef in coeff_dict.items():
        C[da, db] = int(coef) % modulus
    # Precompute step1 = a_powers.T @ C, shape (size, max_db+1)
    step1 = np.matmul(a_powers.T, C) & mask

    total_n_zero = 0
    total_n_shell = 0
    min_v2_global = float('inf')

    for b_start in range(0, size, b_chunk):
        b_end = min(b_start + b_chunk, size)
        w = b_end - b_start
        b_vec = np.arange(b_start, b_end, dtype=np.int64)
        # (b+2)_L for chunk
        poch_b = np.ones(w, dtype=np.int64) & mask
        for i in range(L):
            poch_b = (poch_b * ((b_vec + 2 + i) & mask)) & mask
        # b_powers for chunk
        b_powers = np.zeros((max_db + 1, w), dtype=np.int64)
        b_powers[0, :] = 1
        for d in range(1, max_db + 1):
            b_powers[d, :] = (b_powers[d - 1, :] * b_vec) & mask
        # Q_mod for chunk: step1 (size, max_db+1) @ b_powers (max_db+1, w) -> (size, w)
        Q_chunk = np.matmul(step1, b_powers) & mask
        # h_k mod 2^T = poch_a[:, None] * Q_chunk * poch_b[None, :] mod 2^T
        h_chunk = (Q_chunk * poch_a[:, None]) & mask
        h_chunk = (h_chunk * poch_b[None, :]) & mask
        # Parity mask on this chunk: a + b odd
        parity_a = (a_vec & 1)
        parity_b = (b_vec & 1)
        parity_mask = ((parity_a[:, None] + parity_b[None, :]) & 1) == 1
        shell_residues = h_chunk[parity_mask]
        n_shell = int(parity_mask.sum())
        n_zero = int((shell_residues == 0).sum())
        total_n_shell += n_shell
        total_n_zero += n_zero
        # Find min v_2 of nonzero shell residues
        nz = shell_residues[shell_residues != 0]
        if len(nz) > 0:
            lowbit = nz & (-nz)
            v2s = np.log2(lowbit.astype(np.float64)).astype(np.int32)
            m = int(v2s.min())
            if m < min_v2_global:
                min_v2_global = m
        del h_chunk, Q_chunk, poch_b, b_powers
    if total_n_zero == total_n_shell:
        return f">={T}", total_n_zero, total_n_shell
    return min_v2_global, total_n_zero, total_n_shell


def chunked_check_hk_via_fit(coeff_dict, T, size, b_chunk):
    """Evaluate P(a, b) mod 2^T (with P as coeff_dict) chunked in b."""
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
    step1 = np.matmul(a_powers.T, C) & mask  # shape (size, max_db+1)

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
        del h_chunk, b_powers
    if total_n_zero == total_n_shell:
        return f">={T}", total_n_zero, total_n_shell
    return min_v2_global, total_n_zero, total_n_shell


def main():
    print("=" * 80, flush=True)
    print("Day 91 -- c=13 periodicity check at T = 16 (chunked)", flush=True)
    print("Goal: prove LB_k >= 16 for all k, giving beta'(13) >= 16 tight.", flush=True)
    print("=" * 80, flush=True)

    c_val = 13
    T_check = 16
    jmax = c_val - 1
    size = 1 << T_check  # 65536

    # b_chunk: 65536 / 16 = 4096. h_chunk memory: 65536 * 4096 * 8 bytes = 2 GB.
    b_chunk = 4096

    print(f"Grid: {size} x {size} = 2^{2*T_check} pairs. Shell: 2^{2*T_check - 1}.", flush=True)
    print(f"Chunk: 65536 x {b_chunk} = {size * b_chunk * 8 // (1<<30)} GB per chunk", flush=True)
    print(flush=True)

    # Load Q catalog
    Q_cat, a_s, b_s, c_s = load_Q_catalog()
    # Precompute Q coeff dicts for c=13
    Q_coeffs = {}
    for k, Q_poly in Q_cat.items():
        Q_coeffs[k] = Q_poly_coeff_dict(Q_poly, a_s, b_s, c_s, c_val)

    # Load fitted high-k coeffs
    with open("/home/agent/projects/code/2026-07-12-c13-coeff-high-k.pkl", "rb") as f:
        hk_coeff_high = pickle.load(f)

    print("[k=0..6 via Q-cat + Pochhammer factorization]", flush=True)
    print("[k=7..12 via fitted polynomial]", flush=True)
    print(flush=True)

    all_pass = True
    fail_details = []
    t_start_total = time.time()
    for k in range(jmax + 1):
        t0 = time.time()
        if k in Q_coeffs:
            L = c_val - 1 - k
            min_v2, n_zero, n_total = chunked_check_hk_via_catalog(
                Q_coeffs[k], L, T_check, size, b_chunk)
            src = "Q-cat"
        elif k in hk_coeff_high:
            min_v2, n_zero, n_total = chunked_check_hk_via_fit(
                hk_coeff_high[k], T_check, size, b_chunk)
            src = "fit"
        else:
            print(f"  k={k}: SKIPPED (no source)", flush=True)
            all_pass = False
            continue
        dt = time.time() - t0
        if isinstance(min_v2, str):
            status = f"PASS (all zero mod 2^{T_check})"
        elif min_v2 >= T_check:
            status = f"PASS-partial (min v_2 = {min_v2})"
        else:
            status = f"FAIL (min v_2 = {min_v2} < {T_check})"
            all_pass = False
            fail_details.append((k, min_v2))
        print(f"  k={k:>2d} [{src:>5s}]: min v_2 = {min_v2}, {n_zero}/{n_total} zero, {dt:.1f}s  {status}", flush=True)

    total_dt = time.time() - t_start_total
    print(flush=True)
    print("=" * 80, flush=True)
    print(f"Total periodicity check: {total_dt:.1f}s", flush=True)
    print("=" * 80, flush=True)
    if all_pass:
        print(f"  All k = 0..{jmax}: h_k^{{(13)}}(a, b) mod 2^{T_check} == 0 on shell a+b odd.", flush=True)
        print(f"  By 2^{T_check}-periodicity lemma, LB_k^{{(13)}} >= {T_check} for all k.", flush=True)
        print(f"  By v_2(sum) >= min(v_2): beta'(13) >= {T_check}.", flush=True)
        print(f"  UB witness: H_13(7, 0, 6) = 933042399799910400000, v_2 = 16, distinct-min.", flush=True)
        print(f"  Hence beta'(13) = 16 EXACT. QED.", flush=True)
    else:
        print(f"  FAIL. Some k have min v_2 < {T_check}:", flush=True)
        for k, mv in fail_details:
            print(f"    k={k}: min v_2 = {mv}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
