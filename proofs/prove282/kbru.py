"""Bruhat-level control of Prop K mechanism: rho_T(c)<rho_T'(c) => (T,Q) not<= (T',Q) for every Q with n at c; and x(n)=rho_T(c)."""
import sys; sys.path.insert(0,'.')
from count_int import partitions, syt
from reduce import rb, corners
from cfg import rsk_inv, bru
n=int(sys.argv[1]); trig=bad=lastbad=0
for lam in partitions(n):
    S=[[list(r) for r in t] for t in syt(lam)]
    if len(S)>60: S=S[:60]
    for T in S:
        for T2 in S:
            if T==T2: continue
            for c in corners(T):
                a=rb(T,c)[0]; b=rb(T2,c)[0]
                for Q in S:
                    if n not in Q[c]: continue
                    x=rsk_inv(T,Q); z=rsk_inv(T2,Q)
                    if x[-1]!=a: lastbad+=1
                    if a<b:
                        trig+=1
                        if bru(x,z): bad+=1
print('n',n,'triggered (T,T2,c,Q)',trig,'Bruhat violations',bad,'x(n)!=rho mismatches',lastbad)
