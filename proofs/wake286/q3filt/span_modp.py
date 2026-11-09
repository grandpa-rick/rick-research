import numpy as np
P = 2147483629
class Echelon:
    def __init__(self, ncols):
        self.rows = []; self.piv = []; self.n = ncols
    def reduce(self, v):
        v = np.array(v, dtype=np.int64) % P
        for r, p in zip(self.rows, self.piv):
            c = v[p]
            if c: v = (v - c * r) % P
        return v
    def add(self, v):
        v = self.reduce(v); nz = np.nonzero(v)[0]
        if len(nz) == 0: return False
        p = nz[0]; inv = pow(int(v[p]), P-2, P); v = (v * inv) % P
        # keep fully reduced: eliminate p from existing rows
        for k in range(len(self.rows)):
            c = self.rows[k][p]
            if c: self.rows[k] = (self.rows[k] - c * v) % P
        self.rows.append(v); self.piv.append(p); return True

def algebra_span_modp(gens, d):
    """gens: numpy int arrays d x d. Returns list of numpy matrices spanning unital algebra (mod p closure)."""
    E = Echelon(d*d); I = np.eye(d, dtype=np.int64); E.add(I.ravel())
    basis = [I]; frontier = [I]
    while frontier:
        new = []
        for X in frontier:
            for g in gens:
                Y = g @ X
                if E.add(Y.ravel()): basis.append(Y); new.append(Y)
        frontier = new
    return basis
