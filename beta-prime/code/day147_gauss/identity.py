"""Check main identity F^2-F = theta*Hcal*(2F-3) with independently computed b_k, h_j.
Then check the claimed EQUIVALENCE both ways on the data."""
import json
from fractions import Fraction as Q
D=json.load(open('/home/agent/projects/beta-prime/code/day147_gauss/data.json'))
h=[Q(x) for x in D["h"]]; b=[Q(0)]+[Q(x) for x in D["b"]]
N=min(len(h)-1, len(b)-1)
F=[b[k] if k<len(b) else Q(0) for k in range(N+2)]
def mul(A,B,n):
    return [sum(A[i]*B[k-i] for i in range(k+1)) for k in range(n+1)]
n=N
F2=mul(F,F,n+1)
LHS=[F2[k]-F[k] for k in range(n+2)]
G=[2*F[k] for k in range(n+2)]; G[0]-=3          # 2F-3
HG=mul(h+[Q(0)]*5, G, n+1)
RHS=[Q(0)]+HG[:n+1]                               # theta * Hcal * (2F-3)
print("k   LHS=[F^2-F]_k        RHS=[th*H*(2F-3)]_k   match")
allok=True
for k in range(n+1):
    ok=LHS[k]==RHS[k]; allok&=ok
    print(f"{k:<3} {str(LHS[k]):<22} {str(RHS[k]):<22} {ok}")
print("MAIN IDENTITY (6.1) holds on independently computed data up to theta^%d: %s"%(n,allok))
print()
# reconstruct h from b via h = (F^2-F)/(theta(2F-3))  -> confirm invertibility & 3-adic content
inv=[None]*(n+2)   # 1/(2F-3)
inv[0]=Q(-1,3)
for k in range(1,n+2):
    inv[k]=-inv[0]*sum(G[i]*inv[k-i] for i in range(1,k+1))
num=[LHS[k+1] for k in range(n+1)]
hrec=mul(num,inv,n)
print("h reconstructed from b_k alone:", [str(x) for x in hrec[:n+1]])
print("matches computed h:", hrec[:n+1]==h[:n+1])
