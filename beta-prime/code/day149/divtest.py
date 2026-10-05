import sympy as sp, pickle, random
from math import factorial
N=8
PsiE=[sp.sympify(s) for s in pickle.load(open('/home/agent/projects/beta-prime/code/day149/PsiE%d.pkl'%N,'rb'))]
E1,E2,E3=sp.symbols('E1 E2 E3')
f=[sp.lambdify((E1,E2,E3),p,'math') for p in PsiE]
def disc(e1,e2,e3): return e1**2*e2**2-4*e2**3-4*e1**3*e3+18*e1*e2*e3-27*e3**2
def vl(x,l):
    if x==0: return 99
    v=0
    while x%l==0: x//=l; v+=1
    return v
Pe=[sp.Poly(p,E1,E2,E3) for p in PsiE]
def ev(n,e):
    return int(Pe[n].eval({E1:e[0],E2:e[1],E3:e[2]}))
random.seed(1)
bad=0; tested=0
for trial in range(4000):
    e=(random.randint(-30,30),random.randint(-30,30),random.randint(-30,30))
    D=disc(*e)
    if D==0: continue
    for l in [2,3,5,7,11]:
        if D%l==0: continue
        tested+=1
        for n in range(N+1):
            val=ev(n,e)
            if val!=0 and vl(val,l)<vl(factorial(n),l):
                bad+=1
                if bad<12: print("VIOLATION l=%d n=%d E=%s v=%d need %d"%(l,n,e,vl(val,l),vl(factorial(n),l)))
print("tested (E,l) pairs:",tested,"violations:",bad)
