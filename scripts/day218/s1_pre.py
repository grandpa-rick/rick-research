import sys,pickle,sympy as sp
sys.path.insert(0,'/home/agent/projects/scripts/day214')
from ek_subset_engine import transpose, parts, dominates
s,t,v=sp.symbols('s t v')
mats=pickle.load(open('/home/agent/projects/scripts/day216/mats_N5.pkl','rb'))
def nn(m): return sum(i*x for i,x in enumerate(m))
print(sorted(set(k for k in mats))[:20])
# E_k(e_lam) at s=1, compare to e_k*e_lam = e_{sort(lam+k)}
for (k,m),D in sorted(mats.items()):
    for lam,img in D.items():
        out={}
        for nu,dd in img.items():
            c=sp.factor(sp.cancel((dd*s**(-nn(lam))*s**nn(nu)).subs(s,1)))
            if c!=0: out[nu]=c
        print(f'e_{k} * e{lam} |s=1 =',out)
