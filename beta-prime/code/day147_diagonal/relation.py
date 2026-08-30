"""Cross-check: the MAIN IDENTITY F^2-F = vartheta*Hcal*(2F-3) determines F from Hcal.
Verify that the resulting F is exactly sum_k b_k vartheta^k."""
import json,sys
from fractions import Fraction as Q
d=json.load(open(sys.argv[1] if len(sys.argv)>1 else "data_36.json"))
h=[Q(int(x)) for x in d["h"]]; b=[int(x) for x in d["b"]]
N=len(h)-1
f=[Q(0)]*(N+1)          # F, f[0]=0
for n in range(1,N+1):
    # [v^n]: sum_{i+j=n} f_i f_j - f_n = [v^{n-1}] Hcal*(2F-3)
    lhs_known=sum(f[i]*f[n-i] for i in range(1,n))       # excludes 2*f_0*f_n = 0
    rhs=Q(0)
    m=n-1
    for j in range(0,m+1):
        # Hcal_j * (2F-3)_{m-j}
        co = (2*f[m-j] - (3 if m-j==0 else 0))
        rhs += h[j]*co
    # lhs_known - f_n = rhs
    f[n]=lhs_known-rhs
print("F coefficients f_1..f_N :", [str(x) for x in f[1:]])
print("b_k                     :", [str(x) for x in b])
print("MATCH:", [int(f[k]) for k in range(1,min(N,len(b))+1)]==b[:min(N,len(b))])
