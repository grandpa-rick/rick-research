from util import *
exec(open('s2b.py').read().split('def W_nosign')[0].split('# ---------- Thm 4.4')[0])
def hist_unl(lam, tt):
    out = {}
    def rec(i, blocks, w):
        if i < 0:
            k=srt(blocks); out[k]=(out.get(k,0)+w)%p; return
        k = lam[i]; rec(i-1, blocks+[k], w)
        seen=set()
        for T in subsets(blocks):
            if not T: continue
            J=tuple(sorted(blocks[x] for x in T))
            if J in seen: continue
            seen.add(J)
            rest=list(blocks)
            for j in J: rest.remove(j)
            rec(i-1, rest+[k+sum(J)], w*W_closed(k,J,tt)%p)
    rec(len(lam)-1, [], 1); return out
R=Res("Thm3.7 unlabeled-blocks reading (expected FAIL => labeled reading is the true one)")
for n in range(3,8):
    for lam in partitions(n):
        if cost(lam)>4e4: continue
        H=hist_unl(lam,0)
        for mu in partitions(n):
            if mu==lam or kappa(lam,mu)!=len(mu): continue
            m=len(lam)-len(mu); R.chk(es(lam,0,m+1)[mu][m]==H.get(mu,0), f"{lam}{mu}")
print(R)
