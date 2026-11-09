import numpy as np
from flint import fmpz_mat, fmpq_mat, fmpq
def _int_rows_from_fmpq(R):
    """rows of fmpq_mat -> integer rows (clear denominators)."""
    from math import lcm
    out = []
    for r in range(R.nrows()):
        row = [R[r, c] for c in range(R.ncols())]
        if all(x == 0 for x in row): continue
        L = 1
        for x in row: L = lcm(L, int(x.q))
        out.append([int(x.p) * (L // int(x.q)) for x in row])
    return out
def basis_of(vecs, d):
    """vecs: list of int vectors (len d). return integer basis (list of vectors) of span (rref)."""
    vecs = [list(map(int, v)) for v in vecs if any(v)]
    if not vecs: return []
    R, rk = fmpq_mat(vecs).rref()
    return _int_rows_from_fmpq(R)[:rk]
def dim_span(vecs):
    vecs = [list(map(int, v)) for v in vecs if any(v)]
    return fmpz_mat(vecs).rank() if vecs else 0
def nullspace(rows, ncols):
    rows = [list(map(int, r)) for r in rows if any(r)]
    if not rows: return [[int(i == j) for j in range(ncols)] for i in range(ncols)]
    X, k = fmpz_mat(rows).nullspace()
    return [[int(X[r, c]) for r in range(ncols)] for c in range(k)]
def apply(M, vecs):  # M numpy int, vecs list -> list
    return [list(M @ np.array(v, dtype=object)) for v in vecs]
def preimage_in(ops, target, d):
    """{v : op v in span(target) for all ops} -- exact."""
    # v in kernel of (Q op) where Q : V -> V/target. Build complement projector via equations:
    # op v in span(T)  <=>  N^T op v = 0 where N spans annihilator of T.
    ann = nullspace(target, d) if target else [[int(i == j) for j in range(d)] for i in range(d)]
    rows = []
    for op in ops:
        for a in ann:
            rows.append(list(np.array(a, dtype=object) @ op))
    return nullspace(rows, d)
def quotient_dim(U, Up):
    return dim_span(U) - dim_span(Up)
