from lv_engine import *
import itertools
def HLP(lam,x,u):
    m=len(x); lamp=list(lam)+[0]*(m-len(lam))
    tot=Fr(0)
    for w in itertools.permutations(range(m)):
        y=[x[w[i]] for i in range(m)]
        term=prod(y[i]**lamp[i] for i in range(m))*prod((y[i]-u*y[j])/(y[i]-y[j]) for i in range(m) for j in range(i+1,m))
        tot+=term
    # v_lambda(u)
    from collections import Counter
    v=Fr(1)
    for part,mm in Counter(lamp).items():
        v*=prod((1-u**(i+1))/(1-u) for i in range(mm))
    return tot/v
