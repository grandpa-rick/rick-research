import sys, math
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import build_Psi, subs_E12
from fractions import Fraction as Q

def ff(u,n):
    r=Q(1)
    for i in range(n): r*= (u-i)
    return r

def Phi_coeff(v,b):
    """[T^b] Phi(v;T) = sum_{a+bb+c=b} 1/(a!bb!c!) (v1)_{a+bb}(v2)_{a+c}(v3)_{bb+c}"""
    tot=Q(0)
    for a in range(b+1):
        for bb in range(b+1-a):
            c=b-a-bb
            tot += Q(1,math.factorial(a)*math.factorial(bb)*math.factorial(c))*ff(v[0],a+bb)*ff(v[1],a+c)*ff(v[2],bb+c)
    return tot

def Vand(u): return (u[0]-u[1])*(u[0]-u[2])*(u[1]-u[2])

def Psi_formula(u,b):
    from itertools import permutations
    V=Vand(u); tot=Q(0)
    # V(y)=sum_w sgn(w) y_{w1}^2 y_{w2}^1 y_{w3}^0
    perms=list(permutations([0,1,2]))
    def sgn(p):
        s=1
        for i in range(3):
            for j in range(i+1,3):
                if p[i]>p[j]: s=-s
        return s
    for p in perms:
        v=list(u)
        coef = ff(u[p[0]],2)*ff(u[p[1]],1)
        v[p[0]] = u[p[0]]-2
        v[p[1]] = u[p[1]]-1
        tot += sgn(p)*coef*Phi_coeff(v,b)
    return tot*math.factorial(b)/V

BM=8
Psi=build_Psi(BM)
u=(Q(1,2),Q(1,3),Q(1,5))
E1=u[0]+u[1]+u[2]; E2=u[0]*u[1]+u[0]*u[2]+u[1]*u[2]; E3=u[0]*u[1]*u[2]
def ev(P):
    return sum(Q(c)*E1**m[0]*E2**m[1]*E3**m[2] for m,c in P.items())
for b in range(BM+1):
    a=ev(Psi[b]); c=Psi_formula(u,b)
    print(b, a==c, a if b<3 else '', c if b<3 else '')
