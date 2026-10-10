# Check printed U_a(b,c;x,y)=((-1)^n Phi_a(p_bp_c;x,y)-Xi_a(b,c))/m_xy equals [e_xe_y] T_a(p_b p_c) (FPSAC Thm 6.6 proof idea, Clio Finding 3)
import sys; sys.path.insert(0,'/home/agent/projects/scripts/day231')
from check_v2_printed import *
from lv_engine import e_expand
def Xi(a,r,q,t): return (-1)**(r+q)*br(a+r+q,t)/br(a,t)*br(a,t**r)*br(a,t**q)
ok=tot=0
for a in range(1,4):
  for b in range(1,4):
    for c in range(1,4):
      n=a+b+c
      if n>7: continue
      t=rnd(); g=lambda z: psum(z,b)*psum(z,c)
      ee=e_expand(lambda xx: Ta(a,g,xx,t),n,n)
      for x in range(1,n):
        y=n-x
        if x<y: continue
        m=2 if x==y else 1
        U=((-1)**n*Phi_formula(a,g,b+c,x,y,t)-Xi(a,b,c,t))/m
        tot+=1; ok+= U==ee.get((x,y),Fr(0))
print('U_a = [e_xe_y]T_a(p_bp_c):',ok,'/',tot)
