"""Careful asymptotics of h_j and b_k: fit r_j = h_{j+1}/h_j = L*(1 + a/j + b/j^2 + ...)."""
import json,sys,math
fn=sys.argv[1] if len(sys.argv)>1 else "data_120.json"
d=json.load(open(fn)); H=[int(x) for x in d["h"]]; B=[int(x) for x in d["b"]]
def analyse(a,name):
    print(f"### {name}: {len(a)} terms")
    r=[a[j+1]/a[j] for j in range(len(a)-1)]
    print("  last 6 ratios:", [round(x,5) for x in r[-6:]])
    # Richardson extrapolation of order m assuming r_j = L + c1/j + ... + cm/j^m
    for m in range(1,6):
        seq=r[:]
        idx=list(range(len(r)))  # r[i] corresponds to j=i+ (offset)
        off = 1 if name.startswith("b") else 1
        # j value for r[i]: for h, r[i]=h_{i+1}/h_i -> use j=i+1
        js=[i+1 for i in range(len(r))]
        cur=seq[:]; cj=js[:]
        for k in range(1,m+1):
            new=[]; nj=[]
            for i in range(1,len(cur)):
                j1,j2=cj[i-1],cj[i]
                # eliminate 1/j^k term: L ~ (j2^k*cur[i] - j1^k*cur[i-1])/(j2^k-j1^k)
                new.append((j2**k*cur[i]-j1**k*cur[i-1])/(j2**k-j1**k)); nj.append(j2)
            cur=new; cj=nj
        print(f"  Richardson order {m}: last 4 = {[round(x,4) for x in cur[-4:]]}")
    # subexponential exponent: assume a_j ~ C L^j j^alpha ; then j*(r_j/L - 1) -> alpha
    print("  --- assume a_j ~ C L^j j^alpha; solve L,alpha,C from last 3 terms ---")
    n=len(a)-1
    import itertools
    def solve3(i1,i2,i3):
        # log a_j = c + j logL + alpha log j
        import numpy as np
        M=np.array([[1.0,i,math.log(i)] for i in (i1,i2,i3)])
        y=np.array([math.log(a[i]) for i in (i1,i2,i3)])
        return np.linalg.solve(M,y)
    try:
        for tri in [(n-2,n-1,n),(n-6,n-3,n),(n-12,n-6,n)]:
            c,lL,al=solve3(*tri)
            print(f"    from j={tri}: L={math.exp(lL):.4f}  alpha={al:.4f}  C={math.exp(c):.5g}")
    except Exception as e: print("   ",e)
    print()
analyse(H,"h_j"); analyse(B,"b_k (k>=1)")
print("### ratio b_k / h_{k}? and b_{k}/b_{k-1} vs h_j ratios")
n=min(len(H)-1,len(B))
print("  b_k/h_k for k=1..:", [round(B[k-1]/H[k],6) for k in range(1,n+1)][-8:])
