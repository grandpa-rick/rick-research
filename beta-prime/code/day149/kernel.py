import pickle, sympy as sp
H=pickle.load(open('H16.pkl','rb'))
N=16
E1,E2,E3,T,Y=sp.symbols('E1 E2 E3 T Y')
W=[]
for n in range(N+1):
    A={m:c for m,c in H[n].items() if m[0]+2*m[1]+3*m[2]==n}
    assert all(c%(n+1)==0 for c in A.values())
    W.append(sp.expand(sum(sp.Integer(c//(n+1))*E1**m[0]*E2**m[1]*E3**m[2] for m,c in A.items())))
# Y = T * calW  ; find psi with calW = psi(Y)
# series reversion: Y(T)= sum_{n>=0} W_n T^{n+1}
Ycoef=[sp.Integer(0)]+W[:]           # Y = sum_{k>=1} W_{k-1} T^k
# invert: T = sum_{k>=1} c_k Y^k
M=N+1
c=[sp.Integer(0)]*(M+1)
c[1]=sp.Integer(1)
# use Lagrange: T(Y) determined by composing.  do it iteratively
def compose(f,g,M):   # f(g(T)) with f,g lists indexed by power, g[0]=0
    res=[sp.Integer(0)]*(M+1)
    gp=[sp.Integer(0)]*(M+1); gp[0]=sp.Integer(1)
    for k in range(0,M+1):
        if k>0:
            new=[sp.Integer(0)]*(M+1)
            for i in range(M+1):
                if gp[i]==0: continue
                for j in range(1,M+1-i):
                    if g[j]==0: continue
                    new[i+j]=sp.expand(new[i+j]+gp[i]*g[j])
            gp=new
        if f[k]!=0:
            for i in range(M+1): 
                if gp[i]!=0: res[i]=sp.expand(res[i]+f[k]*gp[i])
    return res
# Newton iteration for reversion
Tc=[sp.Integer(0)]*(M+1); Tc[1]=sp.Integer(1)
for it in range(M+1):
    comp=compose(Ycoef,Tc,M)   # Y(T(Y)) should equal Y
    err=[sp.expand(comp[k]-(1 if k==1 else 0)) for k in range(M+1)]
    k0=None
    for k in range(2,M+1):
        if err[k]!=0: k0=k; break
    if k0 is None: break
    Tc[k0]=sp.expand(Tc[k0]-err[k0])
psi=compose([sp.Integer(0)]+W,Tc,M)   # calW(T(Y)) as series in Y ... calW = sum W_n T^n
# careful: calW = sum_{n>=0} W_n T^n ; compose needs f with f[0] term
f=[W[n] for n in range(N+1)]
psi=[sp.Integer(0)]*(M+1)
gp=[sp.Integer(0)]*(M+1); gp[0]=sp.Integer(1)
for k in range(M+1):
    if k>0:
        new=[sp.Integer(0)]*(M+1)
        for i in range(M+1):
            if gp[i]==0: continue
            for j in range(1,M+1-i):
                if Tc[j]==0: continue
                new[i+j]=sp.expand(new[i+j]+gp[i]*Tc[j])
        gp=new
    if f[k]!=0:
        for i in range(M+1):
            if gp[i]!=0: psi[i]=sp.expand(psi[i]+f[k]*gp[i])
print("psi(Y) coefficients:")
for k in range(0,min(9,M+1)):
    print("  Y^%d : %s"%(k,sp.factor(psi[k])))
