import ast, random, sympy as sp
from fractions import Fraction as Fr
ok=True
for line in open('../wake291/gs/PREDICTIONS_all.txt'):
    if not line[0].isdigit(): continue
    L=int(line.split()[0]); r=ast.literal_eval(line[line.index('['):line.index(']')+1]); d=L+1
    f=[min(i//2,(d-i)//2)+1 for i in range(d+1)] if L%2 else [1 if i in (0,d) else min((i+1)//2,(d-i+1)//2) for i in range(d+1)]
    ok&= f==r
print("closed formulas match table L<=22:",ok, flush=True)
u=sp.symbols('u')
def taylor(expr,N): s=sp.series(expr,u,0,N+1).removeO(); return [Fr(str(s.coeff(u,n))) for n in range(N+1)]
def mul(a,b,N): return [sum(a[i]*b[n-i] for i in range(n+1)) for n in range(N+1)]
def compose(c,A,N):  # sum c_n A^n, A has A[0]=0
    out=[Fr(0)]*(N+1); P=[Fr(1)]+[Fr(0)]*N
    for n in range(N+1):
        out=[o+c[n]*p for o,p in zip(out,P)]; P=mul(P,A,N)
    return out
def run(d,npts=None):
    N=d; sech=taylor(sp.sech(u),N); tanh=taylor(sp.tanh(u),N)
    tp=[ [Fr(1)]+[Fr(0)]*N ]
    for o in range(1,N+2): tp.append(mul(tp[-1],tanh,N))
    rs=[]; npts=npts or 4*d+8
    pts=[]
    for _ in range(npts):
        p={n:Fr(random.randint(-9,9),random.randint(1,5)) for n in range(1,d+1,2)}; yv=Fr(random.randint(-9,9),random.randint(1,5))
        A=[Fr(0)]*(N+1)
        for n in p:
            A[n]=p[n]/n
        E=[Fr(0)]*(N+1)
        for b in range(0,N//2+1): E[2*b]=(-yv/2)**b/sp.factorial(b)
        pts.append((A,[Fr(str(e)) for e in E]))
    for i in range(d+1):
        j=d-i; rows=[]
        if d%2==0: os=list(range(i%2,i+1,2)); fn=lambda o: mul(sech,tp[o],N)
        else:
            if i in (0,d): rs.append(1); continue
            os=list(range(2-i%2,i+1,2)); fn=lambda o: [a-b for a,b in zip(tp[o+1],tp[o-1])]
        for o in os:
            c=fn(o); row=[]
            for A,E in pts:
                v=compose(c,A,N)
                if d%2==0: v=mul(E,v,N)
                row.append(v[j])
            rows.append(row)
        rs.append(sp.Matrix(rows).rank())
    return rs
for d in range(2,15):
    f=[min(i//2,(d-i)//2)+1 for i in range(d+1)] if d%2==0 else [1 if i in (0,d) else min((i+1)//2,(d-i+1)//2) for i in range(d+1)]
    r=run(d); print(d,r,r==f,flush=True)
