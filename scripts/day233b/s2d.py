# Day 237 (d): Clio review 10-11 flag -- are the s2b Thm 4.4 'dedupe' and Thm 4.5 'position-assignment'
# controls vacuous on some cases?  Measure: stratify each control by whether it CAN differ structurally
#   Thm 4.4 dedupe : differs only if two labelled set partitions give the same multiset of lam-blocks
#                    (needs a repeated part of lam);
#   Thm 4.5 overcount: differs only if some assignment multiplicity mult > 1 (needs a repeated part of mu).
# On the structurally-blind stratum the control has rank 0 and is reported as blind, not as evidence.
# Replacement control that can fail everywhere: the claim pins the s-order of each factor
# ([(s-1)^{|B|-1}] for a block B); use the next order [(s-1)^{|B|}] instead (fibre-varying).
from util import *
import sys
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7
t0 = int(rng.integers(2, p))
def cost(lam): return math.prod(math.comb(sum(lam), k) for k in sorted(lam)[:-1])
cache = {}
def es(lam, tt, K):
    key = (lam, tt, K)
    if key not in cache: cache[key] = estar(Ctx(1, tt, K, maxe=len(lam) + 2), lam)
    return cache[key]
def coef(lam, mu, order): return es(lam, t0, order + 1)[mu][order]
R44 = Res("Thm4.4 (s2d rerun) Lead = sum_pi prod connected leads")
N44 = {b: Res(f"Thm4.4 NEG dedupe [{'can differ' if b else 'structurally blind: no two set partitions share a block multiset'}]") for b in (True, False)}
W44 = Res("Thm4.4 NEG wrong order: block factor [(s-1)^{|B|}] instead of [(s-1)^{|B|-1}]")
blind44 = []
for n in range(2, NMAX + 1):
    for lam in partitions(n):
        if cost(lam) > 4e4: continue
        l = len(lam)
        for mu in partitions(n):
            if mu == lam or kappa(lam, mu) != len(mu): continue
            tot = 0; tot_w = 0; seen = {}; npi = 0
            for pi in setparts(list(range(l))):
                if srt(tuple(sum(lam[i] for i in B) for B in pi)) != mu: continue
                npi += 1; v = 1; vw = 1
                for B in pi:
                    lb = srt(tuple(lam[i] for i in B))
                    if len(B) > 1: v = v * coef(lb, (sum(lb),), len(B) - 1) % p
                    vw = vw * coef(lb, (sum(lb),), len(B)) % p
                tot = (tot + v) % p; tot_w = (tot_w + vw) % p
                seen[tuple(sorted(tuple(sorted((lam[i] for i in B), reverse=True)) for B in pi))] = v
            lead = coef(lam, mu, l - len(mu))
            R44.chk(lead == tot, f"{lam}{mu}")
            can = len(seen) < npi
            N44[can].chk(lead == sum(seen.values()) % p, f"{lam}{mu}")
            if not can: blind44.append((lam, mu, len(set(lam)) == len(lam)))
            W44.chk(lead == tot_w, f"{lam}{mu}")
print(R44); print(N44[True], "(expected FAIL)"); print(N44[False], "(blind: PASS forced)"); print(W44, "(expected FAIL)")
print("C0 Thm4.4 blind stratum: %d cases, of which lam has distinct parts: %d; lam with a repeated part: %d"
      % (len(blind44), sum(1 for b in blind44 if b[2]), sum(1 for b in blind44 if not b[2])))

R45 = Res("Thm4.5 (s2d rerun) block multiplicativity")
N45 = {b: Res(f"Thm4.5 NEG overcount [{'can differ' if b else 'structurally blind: every multiplicity is 1'}]") for b in (True, False)}
W45 = Res("Thm4.5 NEG wrong order: factor [(s-1)^{|C|}] instead of [(s-1)^{|C|-1}]")
def subparts(mu, sizes):
    res = Counter()
    def rec(i, rem, acc):
        if i == len(sizes):
            if not rem: res[tuple(acc)] += 1
            return
        for T in subsets(rem):
            if not T: continue
            nu = srt(tuple(rem[x] for x in T))
            if sum(nu) != sizes[i]: continue
            rec(i + 1, tuple(rem[x] for x in range(len(rem)) if x not in T), acc + [nu])
    rec(0, tuple(mu), []); return res
blind45 = []; W45ok = []; taut45 = 0
for n in range(2, NMAX + 1):
    for lam in partitions(n):
        if cost(lam) > 4e4: continue
        l = len(lam)
        for mu in partitions(n):
            kp = kappa(lam, mu)
            if kp < 1: continue
            taut45 += (kp == 1)
            m = l - kp; lhs = coef(lam, mu, m); tot = tot2 = totw = 0; can = False
            for pi in setparts(list(range(l))):
                if len(pi) != kp: continue
                lC = [srt(tuple(lam[i] for i in B)) for B in pi]
                for tup, mult in subparts(mu, [sum(x) for x in lC]).items():
                    if not all(dom(nu, lc) for nu, lc in zip(tup, lC)): continue
                    v = 1; vw = 1
                    for nu, lc, B in zip(tup, lC, pi):
                        v = v * coef(lc, nu, len(B) - 1) % p
                        vw = vw * coef(lc, nu, len(B)) % p
                    if mult > 1: can = True
                    tot = (tot + v) % p; tot2 = (tot2 + mult * v) % p; totw = (totw + vw) % p
            R45.chk(lhs == tot, f"{lam}{mu}"); N45[can].chk(lhs == tot2, f"{lam}{mu}")
            if not can: blind45.append((lam, mu, len(set(mu)) == len(mu), len(set(lam)) == len(lam)))
            W45.chk(lhs == totw, f"{lam}{mu}")
            if lhs == totw: W45ok.append((lam, mu, lhs))
print("C0 Thm4.5 cases with kappa=1 (single block: identity is a tautology, factor = lhs): %d of %d" % (taut45, R45.ok + R45.bad))
print("C0 Thm4.5 wrong-order coincidences (control passes):", W45ok)
print(R45); print(N45[True], "(expected FAIL)"); print(N45[False], "(blind: PASS forced)"); print(W45, "(expected FAIL)")
print("C0 Thm4.5 blind stratum: %d cases; mu distinct parts: %d; lam distinct parts: %d"
      % (len(blind45), sum(1 for b in blind45 if b[2]), sum(1 for b in blind45 if b[3])))
