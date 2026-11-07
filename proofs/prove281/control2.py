"""Control: orbit-search verdicts vs full KL in S_n (n=5,6), all pairs within left cells (Q fixed).
Also tests shape-invariance: mu((P1,Q),(P2,Q)) independent of Q."""
import sys
from klperm import full_kl, MU
import orbit
from orbit import rsk, rsk_inv
from orbit2 import search2
n=int(sys.argv[1]); W,P,mu=full_kl(n)
cells={}
for w in W:
    p,q=rsk(list(w)); cells.setdefault(str(q),[]).append(w)
agree={'mu=1':0,'kill':0}; wrong=0; undecided=0; mu1=0; mu0=0
shape={}; shape_bad=0
for q,C in cells.items():
    for a in C:
        for b in C:
            if a>=b: continue
            m=MU(mu,a,b); mu1+=m==1; mu0+=m==0
            key=(str(rsk(list(a))[0]),str(rsk(list(b))[0]))
            if key in shape and shape[key]!=m: shape_bad+=1
            shape[key]=m
            st=search2(list(a),list(b))[0]
            if st=='mu=1':
                if m==1: agree['mu=1']+=1
                else: wrong+=1
            elif st.startswith('kill'):
                if m==0: agree['kill']+=1
                else: wrong+=1
            else: undecided+=1
print('n',n,'cells',len(cells),'pairs mu=1',mu1,'mu=0',mu0,'agree',agree,'WRONG',wrong,'undecided',undecided,'shape-invariance violations',shape_bad)
