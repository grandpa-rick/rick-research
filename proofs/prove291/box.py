# test Theorem (iv): dec(X [x] Y) <=> dec(X [x] C1) and dec(C1 [x] Y), all indecomposable intervals, a+b<=Nmax, dim cap
import sys, pickle
from math import comb
sys.argv, args = ['x'], sys.argv[1:]
exec(open('q74.py').read().split("mmax = int")[0])   # imports + analyse
mods = pickle.load(open('mods5.pkl', 'rb')); Nmax = int(args[0]); dcap = int(args[1])
box = frozenset({(1,)})
Rb, Lb = {}, {}
for m in mods:
    for j, x in enumerate(mods[m]):
        Rb[(m, j)] = not analyse(product_set(x[2], box))['ind']
        Lb[(m, j)] = not analyse(product_set(box, x[2]))['ind']
    print('m', m, 'R1', sum(Rb[(m, j)] for j in range(len(mods[m]))), 'L1', sum(Lb[(m, j)] for j in range(len(mods[m]))), 'proj', sum(x[3] for x in mods[m]), flush=True)
pickle.dump((Rb, Lb), open('box5.pkl', 'wb'))
cnt = bad = ndec = 0
for a in mods:
    for b in mods:
        if a + b > Nmax: continue
        for ja, X in enumerate(mods[a]):
            for jb, Y in enumerate(mods[b]):
                if comb(a + b, a) * X[4] * Y[4] > dcap: continue
                dec = not analyse(product_set(X[2], Y[2]))['ind']; cnt += 1; ndec += dec
                if dec != (Rb[(a, ja)] and Lb[(b, jb)]):
                    bad += 1; print('MISMATCH', X[:2], Y[:2], dec, flush=True)
    print('a', a, cnt, 'dec', ndec, 'bad', bad, flush=True)
print('TOTAL', cnt, 'dec', ndec, 'bad', bad)
