"""Task 3: is D = f(v)^3/f(v^3) in 1+3v Z_3[[v]] AUTOMATIC for any integer f with f_0=1?
Answer: YES.  Freshman's dream: f(v)^3 = f(v^3) mod 3 whenever f has Z_3 coefficients.
Demonstrated here on random integer sequences, plus a controlled failure when one
coefficient is made non-3-integral."""
import random
from fractions import Fraction as Q
def v3(x):
    if x==0: return None
    n,d=Q(x).numerator,Q(x).denominator; v=0
    while n%3==0: n//=3;v+=1
    while d%3==0: d//=3;v-=1
    return v
def mul(A,B,N):
    R=[Q(0)]*(N+1)
    for i,a in enumerate(A):
        if a==0: continue
        for j,b in enumerate(B):
            if i+j>N: break
            R[i+j]+=a*b
    return R
def inv(A,N):
    B=[Q(0)]*(N+1); B[0]=Q(1)/A[0]
    for n in range(1,N+1):
        s=Q(0)
        for j in range(1,n+1): s+=A[j]*B[n-j]
        B[n]=-s/A[0]
    return B
def D(f,N):
    f=[Q(x) for x in f]
    g=[Q(0)]*(N+1)
    for j in range(N+1):
        if 3*j<=N: g[3*j]=f[j]
    return mul(mul(mul(f,f,N),f,N),inv(g,N),N)
N=14
print("=== A: 200 RANDOM integer sequences, f_0 = 1 ===")
worst=99; bad=0
for t in range(200):
    f=[1]+[random.randint(-10**6,10**6) for _ in range(N)]
    d=D(f,N)
    vs=[v3(d[n]) for n in range(1,N+1) if d[n]!=0]
    if any(v<1 for v in vs): bad+=1
    worst=min(worst,min(vs) if vs else 99)
print(f"  sequences violating v3>=1 in degrees>=1: {bad}/200   (min v3 seen over all: {worst})")
print("  => the test PASSES for every integer sequence.  It is a theorem, not evidence.")
print()
print("=== B: f_0 = 1 but ONE coefficient not 3-integral (h_5 -> h_5/3) ===")
h=[1,8,119,2200,45500,1007904,23387442,561163152,13809781700,346645093984,
   8840919351575,228449188011224,5968029850876084]
f=[Q(x) for x in h]; f[5]=f[5]/3
d=D(f,12)
print("  v3 of D_n, n=0..12:", [v3(d[n]) for n in range(13)])
print("  first degree with v3<1:", next((n for n in range(1,13) if d[n]!=0 and v3(d[n])<1),None))
print()
print("=== C: what the test detects, degree by degree ===")
print("  coeff of v^n in D depends only on h_0..h_n.")
print("  h_0..h_n in Z_3  =>  v3([v^n](D-1)) >= 1.   (proved: Frobenius mod 3)")
print("  So the test at degree n carries EXACTLY the information 'h_0..h_n in Z_3',")
print("  which is checked directly and more cheaply by printing v3(h_j).")
