# Checks of longversion.tex §3 printed statements against the printed subset formula (Thm 2.x).
from lv_engine import *
import sympy as sp
def qp(a,t,n): return prod(1-a*t**i for i in range(n))
def alpha(j,s,t):
    if j<0: return Fr(0)
    return prod((s-t**i)/(1-t**i) for i in range(1,j+1))
def c(n,j,s,t):
    if j<0 or j>n: return Fr(0)
    return qp(s,t,n-j)/qp(t,t,n-j)*(alpha(j,s,t)-s*t**(n-j)*alpha(j-1,s,t))
def Fpoly(n,w,s,t): return sum((c(n,j,s,t)*w**j for j in range(n+1)),Fr(0))
