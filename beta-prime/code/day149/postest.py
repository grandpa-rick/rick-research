import sys
sys.path.insert(0,'/home/agent/projects/beta-prime/code/day146_prove')
from core import *
B=20
P=build_P(B)
print("P_b positivity:")
for b in range(B+1):
    negs=[(m,c) for m,c in P[b].items() if c<0]
    print("  b=%2d  #mon=%3d  min=%-14s  #neg=%d"%(b,len(P[b]),min(P[b].values()),len(negs)))
    if negs and b<6: print("     ",negs[:6])
