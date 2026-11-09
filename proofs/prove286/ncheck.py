import pickle, sys, itertools
sys.path.insert(0,'/home/agent/projects/proofs/wake285')
from d8lib import rdes
from collections import Counter
import sympy as sp
C=pickle.load(open('cons8.pkl','rb')); n=8
glob=Counter()
for p in itertools.permutations(range(1,n+1)):
    for sg in itertools.product((1,-1),repeat=n-1):
        s0=1 if sg.count(-1)%2==0 else -1
        u=(p[0]*s0,)+tuple(a*b for a,b in zip(p[1:],sg))
        glob[rdes(u)]+=1      # L-distribution of W = R-distribution (inversion)
keys=sorted(C); subs=sorted(set(glob)|{A for k in keys for A in C[k]['dist']},key=lambda A:(len(A),sorted(A)))
M=sp.Matrix([[C[k]['dist'].get(A,0) for k in keys] for A in subs]); b=sp.Matrix([glob.get(A,0) for A in subs])
print('rank',M.rank(),'of',len(keys))
sol,params=M.gauss_jordan_solve(b)
N=dict(zip(keys,sol)); print('free params',params.shape)
T=pickle.load(open('/home/agent/projects/proofs/wake285/targets8.pkl','rb'))
for k in T: print(k,N[k])
print('total cells',sum(sol))
