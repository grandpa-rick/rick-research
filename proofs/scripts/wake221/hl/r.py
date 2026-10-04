import sympy as sp, sys
sys.path.insert(0,'/tmp/hl')
t=sp.symbols('t')
from sympy.utilities.iterables import partitions
def parts(n):
    return [tuple(sorted([k for k,v in p.items() for _ in range(v)],reverse=True)) for p in partitions(n)]
def raise_coeffs(lam,n):
    l=len(lam)
    # states: alpha tuple -> list of (sign, support size, t-power) as polynomial dict; store sympy poly
    states={tuple(lam):sp.Integer(1)}
    for j in range(l-1,0,-1):
        for i in range(j-1,-1,-1):
            new={}
            for a,c in states.items():
                for k in range(0,a[j]+1):
                    b=list(a); b[i]+=k; b[j]-=k; b=tuple(b)
                    f= 1 if k==0 else -(1-t)*t**(k-1)
                    new[b]=new.get(b,0)+c*f
            states=new
    out={}
    for a,c in states.items():
        mu=tuple(sorted([x for x in a if x>0],reverse=True))
        out[mu]=sp.expand(out.get(mu,0)+c)
    return out
def val(e):
    e=sp.Poly(sp.expand(e),t)
    if e.is_zero: return None
    k=0
    while e.eval(1)==0:
        e=sp.Poly(sp.quo(e.as_expr(),1-t),t); k+=1
    return k
if __name__=="__main__":
    NMAX=int(sys.argv[1])
    import importlib.util
    from w import kappa, dom
    for n in range(2,NMAX+1):
        tot=ok=0
        for lam in parts(n):
            for mu,c in raise_coeffs(lam,n).items():
                if mu==lam or sp.expand(c)==0: continue
                tot+=1; v=val(c)
                ok+= v==len(lam)-kappa(lam,mu)
                if (lam,mu)==((2,2,2),(5,1)): print('ex',lam,mu,sp.factor(c),v)
        print(n,tot,ok,flush=True)
