import sys
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import *
B=14
P=build_P(B)
def ev(A,e1,e2,e3): return sum(c*e1**m[0]*e2**m[1]*e3**m[2] for m,c in A.items())
print("P_b(0,0,0) :",[ev(P[b],0,0,0) for b in range(B+1)])
print("P_b(1,1,1) :",[ev(P[b],1,1,1) for b in range(B+1)])
print("P_b(1,0,0) :",[ev(P[b],1,0,0) for b in range(B+1)])
print("P_b(0,1,0) :",[ev(P[b],0,1,0) for b in range(B+1)])
print("P_b(0,0,1) :",[ev(P[b],0,0,1) for b in range(B+1)])
print("[E1^b]P_b  :",[P[b].get((b,0,0),0) for b in range(B+1)])
print("[E2^b]P_b  :",[P[b].get((0,b,0),0) for b in range(B+1)])
print()
print("P_1 =",P[1]); print("P_2 =",P[2]); print("P_3 =",P[3])
