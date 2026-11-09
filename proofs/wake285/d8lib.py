"""D_n toolkit in coxeter3 labelling + persistent coxeter3 session.

coxeter3 D_n labels: nodes 1,2 both joined to 3, chain 3-4-...-n.
Model: signed permutations w (window tuple w[0..n-1] = w(1..n)), even # of negatives.
  node 1 = t'  : right mult swaps positions 1,2 with sign change; left mult swaps VALUES 1<->-2, 2<->-1
  node 2 = t_1 : swaps 1,2
  node k>=3 = t_{k-1} : swaps k-1,k
Left multiplication acts on values.
"""
import os, re, subprocess, select, time

def length(w):
    n = len(w); l = 0
    for i in range(n):
        for j in range(i+1, n):
            if w[i] > w[j]: l += 1
            if w[i] + w[j] < 0: l += 1
    return l

def inverse(w):
    n = len(w); inv = [0]*n
    for i, v in enumerate(w):
        inv[abs(v)-1] = (i+1) if v > 0 else -(i+1)
    return tuple(inv)

def rmul(w, s):
    """w*s (acts on positions)."""
    w = list(w)
    if s == 1: w[0], w[1] = -w[1], -w[0]
    else:
        i = s - 1  # t_{s-1} swaps positions s-1,s (1-based)
        w[i-1], w[i] = w[i], w[i-1]
    return tuple(w)

def lmul(s, w):
    return inverse(rmul(inverse(w), s))

def rdes(w):
    D = set()
    if w[0] + w[1] < 0: D.add(1)
    for k in range(2, len(w)+1):
        if w[k-2] > w[k-1]: D.add(k)
    return frozenset(D)

def ldes(w):
    return rdes(inverse(w))

def word(w):
    """reduced word (coxeter3 labels) with w = s_{a1} ... s_{ak}."""
    out = []
    w = tuple(w)
    while True:
        R = rdes(w)
        if not R: break
        s = min(R); out.append(s); w = rmul(w, s)
    return ''.join(map(str, reversed(out)))

def from_word(wd, n):
    w = tuple(range(1, n+1))
    for c in wd: w = rmul(w, int(c))
    return w

def edges(n):
    E = [(1, 3), (2, 3)] + [(k, k+1) for k in range(3, n)]
    return E

def nbrs(n):
    N = {i: set() for i in range(1, n+1)}
    for a, b in edges(n): N[a].add(b); N[b].add(a)
    return N

def lstar(w, s, t):
    L = ldes(w)
    if (s in L) == (t in L): return None
    for u in (lmul(s, w), lmul(t, w)):
        Lu = ldes(u)
        if (s in Lu) != (t in Lu): return u
    raise RuntimeError

def star_orbit(w, n, cap=20000):
    E = edges(n)
    seen = {w}; st = [w]
    while st:
        u = st.pop()
        for s, t in E:
            v = lstar(u, s, t)
            if v is not None and v not in seen:
                seen.add(v); st.append(v)
                if len(seen) > cap: return None
    return seen

def bruhat_leq(x, y):
    """Bruhat order via subword property on reduced word of y (exponential-safe greedy):
    x <= y iff x can be obtained; use standard: x<=y iff for s in R(y): (xs<=ys if s in R(x)) else (x<=ys)."""
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def le(a, b):
        la, lb = length(a), length(b)
        if la > lb: return False
        if la == lb: return a == b
        if la == 0: return True
        s = min(rdes(b)); bs = rmul(b, s)
        if s in rdes(a): return le(rmul(a, s), bs)
        return le(a, bs)
    return le(tuple(x), tuple(y))


class Cox:
    """Persistent coxeter3 session; pol(x,y) returns coefficient list of P_{x,y} (x<=y) or None."""
    BIN = "/home/agent/projects/proofs/wake285/coxeter/coxeter"
    def __init__(self, typ, rank):
        self.p = subprocess.Popen(["stdbuf", "-o0", "-e0", self.BIN], stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0)
        self.buf = b""
        self._send(f"type\n{typ}\n{rank}\n")
        self._wait(rb"rank : ")
        self.ncalls = 0
    def _send(self, s): self.p.stdin.write(s.encode()); self.p.stdin.flush()
    def _wait(self, pat, timeout=3600):
        t = time.time()
        while True:
            m = re.search(pat, self.buf, re.S)
            if m:
                self.buf = self.buf[m.end():]; return m
            r, _, _ = select.select([self.p.stdout], [], [], 5)
            if r:
                c = os.read(self.p.stdout.fileno(), 65536)
                if not c: raise RuntimeError("coxeter died: " + self.buf[-500:].decode(errors='replace'))
                self.buf += c
            if time.time() - t > timeout: raise TimeoutError
    def pol_raw(self, xw, yw):
        assert xw and yw
        self._send(f"pol\n{xw}\n{yw}\n")
        m = self._wait(rb"second : ([^\n]*)\n")
        self.ncalls += 1
        return m.group(1).decode().strip()
    def pol(self, xw, yw):
        r = self.pol_raw(xw, yw)
        return parse_poly(r)
    def close(self):
        try: self._send("qq\n")
        except Exception: pass
        self.p.kill(); self.p.wait()

def parse_poly(r):
    if not re.fullmatch(r"[0-9q^+]+", r): return None  # error message / not comparable
    c = {}
    for term in r.split('+'):
        m = re.fullmatch(r"(\d*)(q(\^(\d+))?)?", term)
        coef = int(m.group(1)) if m.group(1) else 1
        deg = (int(m.group(4)) if m.group(4) else 1) if m.group(2) else 0
        c[deg] = c.get(deg, 0) + coef
    return [c.get(i, 0) for i in range(max(c)+1)]

def mu_from(P, lx, ly):
    """P = P_{x,y}, x<y, lengths lx<ly."""
    g = ly - lx
    if P is None or g % 2 == 0: return 0
    d = (g - 1)//2
    return P[d] if d < len(P) else 0

def f2_closure(w, n, cap=20000):
    """Closure of {w} under u -> r u whenever L(u), L(ru) are incomparable.
    By (F1) every mu-edge between elements with incomparable L is of this form, and by (F2) it is
    a two-way left-preorder link, so the closure lies inside the left cell of w (KL-free)."""
    seen = {w}; st = [w]
    while st:
        u = st.pop(); Lu = ldes(u)
        for r in range(1, n+1):
            v = lmul(r, u); Lv = ldes(v)
            if not (Lu <= Lv) and not (Lv <= Lu) and v not in seen:
                seen.add(v); st.append(v)
                if len(seen) > cap: return None
    return seen
