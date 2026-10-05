from fractions import Fraction as Fr
from math import factorial
import itertools, sys

def phi_coeffs(u,N):
    """[T^n] Phi(u) for n<=N, u integer triple, exact rationals."""
    def V(v): return (v[0]-v[1])*(v[0]-v[2])*(v[1]-v[2])
    def fall(x,n):
        r=1
        for j in range(n): r*=(x-j)
        return r
    Vu=V(u); out=[]
    for n in range(N+1):
        tot=Fr(0)
        for a in range(n+1):
            for b in range(n+1-a):
                c=n-a-b; m=(a+b,a+c,b+c)
                t=Fr(1,factorial(a)*factorial(b)*factorial(c))
                for i in range(3): t*= fall(u[i],m[i])
                t*= V([u[i]-m[i] for i in range(3)])
                tot+=t
        out.append(Fr(tot,Vu))
    return out

def vl(x,l):
    if x==0: return 99
    from fractions import Fraction
    n,d=x.numerator,x.denominator
    v=0
    while n%l==0: n//=l; v+=1
    while d%l==0: d//=l; v-=1
    return v

N=14
tests=[(0,1,2),(0,1,3),(1,2,4),(0,2,5),(3,1,-2),(0,1,5),(2,7,11)]
for u in tests:
    ph=phi_coeffs(list(u),N)
    Vu=(u[0]-u[1])*(u[0]-u[2])*(u[1]-u[2])
    print("u=%s V=%d"%(u,Vu))
    for l in [2,3,5,7]:
        vs=[vl(ph[n],l) for n in range(N+1)]
        print("   l=%d  vV=%d  min v_l([T^n]Phi)=%d  profile=%s"%(l,vl(Fr(Vu),l),min(vs),vs))
