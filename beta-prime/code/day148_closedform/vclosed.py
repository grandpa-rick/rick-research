import sys, math
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import build_Psi, build_P
from fractions import Fraction as Q

def rf(u,n):
    r=Q(1)
    for i in range(n): r*=(u+i)
    return r

def FP_coeff(u,b):
    """[T^b] F_P  ; F_P = sum_b P_b T^b/b!  so this = P_b/b!"""
    d12=u[0]-u[1]; d13=u[0]-u[2]; d23=u[1]-u[2]
    tot=Q(0)
    for a in range(b+1):
        for bb in range(b+1-a):
            c=b-a-bb
            t=Q(1,math.factorial(a)*math.factorial(bb)*math.factorial(c))
            t*= rf(u[0],a+bb)*rf(u[1],a+c)*rf(u[2],bb+c)
            t*= (d12+bb-c)*(d13+a-c)*(d23+a-bb)
            tot+=t
    return tot/(d12*d13*d23)

BM=9
P=build_P(BM)
u=(Q(1,2),Q(1,3),Q(1,5))
E1=u[0]+u[1]+u[2]; E2=u[0]*u[1]+u[0]*u[2]+u[1]*u[2]; E3=u[0]*u[1]*u[2]
def ev(Pl): return sum(Q(c)*E1**m[0]*E2**m[1]*E3**m[2] for m,c in Pl.items())
ok=True
for b in range(BM+1):
    lhs=ev(P[b])/math.factorial(b); rhs=FP_coeff(u,b)
    if lhs!=rhs: ok=False; print("MISMATCH b=",b,lhs,rhs)
print("F_P closed form matches to b=%d:"%BM, ok)
