"""Q52 set-wise check: |D_{w,z}| for z in W^P, w notin W^P (LS12 (3.2)), plus the
stronger lemma: D_R(w) cap S_P subset D_R(dn(w,tau)) for every coset tau <= wW_P."""
import sys; sys.path.insert(0,'../wake265')
import check
from fractions import Fraction as Fr
def run(m):
    S=check.setup(m); W,act,mul,L,leq=S['W'],S['act'],S['mul'],S['L'],S['leq']
    om=tuple([1]*m)
    coset={}
    for w in W: coset.setdefault(act(w,om),[]).append(w)
    minrep={mu:min(ws,key=lambda w:L[w]) for mu,ws in coset.items()}
    # simple reflections: s_i = swap e_i,e_{i+1}; s_m: e_m -> -e_m. W_P = stab(om) = S_m: s_1..s_{m-1}
    def swap(i): return tuple(((i+1,1) if t==i else (i,1) if t==i+1 else (t,1)) for t in range(m))
    SP=[swap(i) for i in range(m-1)]
    inWP={w for ws in coset.values() for w in ws if w==minrep[act(w,om)]}
    def dn(w,tau):
        c=[v for v in coset[tau] if leq(v,w)]; mx=[v for v in c if all(leq(u,v) for u in c)]
        assert len(mx)==1; return mx[0]
    cleq=lambda a,b: leq(minrep[a],minrep[b])
    # lemma check
    bad=0; tests=0
    for w in W:
        DR=[s for s in SP if L[mul(w,s)]<L[w]]
        for tau in coset:
            if cleq(tau,act(w,om)):
                v=dn(w,tau); tests+=1
                if any(L[mul(v,s)]>L[v] for s in DR): bad+=1
    # set-wise D_{w,z} via paths: reuse check's path enumeration by recomputing (copy)
    import itertools
    mus=list(coset)
    covers={}
    for a in mus:
        for b in mus:
            if a!=b and cleq(b,a) and L[minrep[a]]==L[minrep[b]]+1:
                for be in S['pos']:
                    if act(S['refl'](be),b)==a: covers[(a,b)]=abs(S['cp'](b,be)); break
    def achain(s,t):
        if s==t: return True
        return any(x==s and (Fr(1,2)*bd).denominator==1 and cleq(t,y) and achain(y,t) for (x,y),bd in covers.items())
    paths=[(t,) for t in mus]+[(a,b) for a in mus for b in mus if a!=b and cleq(b,a) and achain(a,b)]
    cnt_off=0; cnt_ctrl=0
    for w in W:
        for p in paths:
            if not cleq(p[0],act(w,om)): continue
            z=w
            for d in p: z=dn(z,d)
            if w not in inWP and z in inWP: cnt_off+=1
            if w not in inWP and z not in inWP: cnt_ctrl+=1
    print(dict(m=m,paths=len(paths),lemma_tests=tests,lemma_bad=bad,D_offWP_into_WP=cnt_off,control_offWP_into_offWP=cnt_ctrl))
for m in map(int,sys.argv[1:]): run(m)
