import sys,pickle,sympy as sp
sys.path.insert(0,'/home/agent/projects/scripts/day214')
from ek_subset_engine import transpose
s,t=sp.symbols('s t')
RES=pickle.load(open('psi_e.pkl','rb'))
def nn(m): return sum(i*x for i,x in enumerate(m))
for n,(P,M) in sorted(RES.items()):
    m=len(P); bad=[];off=[];diag=[]
    for i in range(m):
        for j in range(m):
            x=sp.cancel(M[i,j]); num,den=sp.fraction(x)
            if sp.cancel(den.subs(s,1))==0: bad.append((P[i],P[j]))
            val=sp.factor(sp.cancel(x.subs(s,1))) if (P[i],P[j]) not in bad else None
            if i==j: diag.append((P[i],val, sp.simplify(val - t**(-nn(transpose(P[i]))))==0))
            elif val not in (0,None): off.append((P[i],P[j],val))
    print('n',n,'poles at s=1:',bad,'| offdiag nonzero at s=1:',off)
    print('   diag == t^{-n(mu\')}:',all(d[2] for d in diag), diag if not all(d[2] for d in diag) else '')
