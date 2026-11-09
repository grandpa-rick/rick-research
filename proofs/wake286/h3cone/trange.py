import json, numpy as np
from scipy.optimize import linprog
cells=json.load(open('cells5.json'))
def gens(fam,t):
    if fam=='52a': return [[-t,0,0,0,1],[-2*t,-t,0,1,2],[-t,-2*t,1-t,2,1]]
    if fam=='52b': return [[0,0,-t,0,1],[0,-t,-2*t,1-t,2],[-t,-2*t,1-2*t,2-2*t,1-t],[-2*t,-t,0,1-t,2-2*t]]
    if fam=='52c': return [[0,-t,0,1,0],[-t,-2*t,1-t,2,1],[-2*t,-t,0,1,2]]
    if fam=='51tw': return [[-t,0,1,0,0],[-2*t,1-t,2,1,0]]
def pointed(G):
    G=np.array(G,float); r=linprog(np.zeros(5),A_ub=-G,b_ub=-np.ones(len(G)),bounds=[(None,None)]*5,method='highs'); return r.status==0
def incone(G,x):
    G=np.array(G,float).T; r=linprog(np.zeros(G.shape[1]),A_eq=G,b_eq=x,bounds=[(0,None)]*G.shape[1],method='highs'); return r.status==0
for fam,ci in [('52a',3),('52b',3),('52c',3),('51tw',0)]:
    A=[np.array(a,float) for a in cells[ci]['A']]
    lo,hi=0.0,50.0
    def ok(t):
        G=list(np.eye(5))+[np.array(g,float) for g in gens(fam,t)]
        inv=all(incone(G,a@g) for g in G for a in A)
        return pointed(G) and inv, pointed(G), inv
    for t in [0.05,0.2,0.3,0.381,0.382,0.4,0.5,0.618,0.62,0.7,0.9,1,1.5,2]:
        print(fam,t,ok(t))
