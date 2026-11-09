import json, numpy as np, sympy as sp
from scipy.optimize import linprog
cells=json.load(open('cells5.json'))
A=[np.array(a,float) for a in cells[3]['A']]
def pointed(G):
    G=np.array(G,float); r=linprog(np.zeros(5),A_ub=-G,b_ub=-np.ones(len(G)),bounds=[(None,None)]*5,method='highs'); return r.status==0
def incone(G,x):
    G=np.array(G,float).T; r=linprog(np.zeros(G.shape[1]),A_eq=G,b_eq=x,bounds=[(0,None)]*G.shape[1],method='highs'); return r.status==0
def closure(v,maxn=200):
    G=list(np.eye(5))+[v]; fr=[v]
    while fr:
        new=[]
        for u in fr:
            for a in A:
                w=a@u
                if incone(G,w): continue
                w=w/np.abs(w).max(); G.append(w); new.append(w)
                if len(G)>maxn: return G,False
                if not pointed(G): return G,'notpointed'
        fr=new
    return G,True
for t in [0.5,0.6,0.61,0.617,0.6185,0.62,0.65,0.7,0.8,0.9,1.0,1.2]:
    v=np.zeros(5); v[4]=1; v[2]=-t
    G,st=closure(v); print(t,st,len(G)-5)
lo,hi=0.617,0.6185
for _ in range(40):
    m=(lo+hi)/2; v=np.zeros(5); v[4]=1; v[2]=-m
    G,st=closure(v,maxn=400)
    if st is True: lo=m
    else: hi=m
print('threshold',lo,hi,'1/phi',(5**.5-1)/2)
