import json, sympy as sp
cells=json.load(open('cells5.json'))
t=sp.symbols('t',positive=True)
fams={'52a':(3,[[-t,0,0,0,1],[-2*t,-t,0,1,2],[-t,-2*t,1-t,2,1]]),
 '52b':(3,[[0,0,-t,0,1],[0,-t,-2*t,1-t,2],[-t,-2*t,1-2*t,2-2*t,1-t],[-2*t,-t,0,1-t,2-2*t]]),
 '52c':(3,[[0,-t,0,1,0],[-t,-2*t,1-t,2,1],[-2*t,-t,0,1,2]]),
 '51tw':(0,[[-t,0,1,0,0],[-2*t,1-t,2,1,0]])}
for f,(ci,gs) in fams.items():
    A=[sp.Matrix(a) for a in cells[ci]['A']]
    print('==',f)
    for k,g in enumerate(gs):
        for s in range(3):
            print('  (1+s%d)g%d ='%(s+1,k+1), list(sp.expand(A[s]*sp.Matrix(g))))
