# Which pairing does Phi_a(g;x,y)=<T_a g, p_x p_y> in FPSAC Thm 6.3 mean? Compare printed formula to Hall and HL pairings.
import sys; sys.path.insert(0,'/home/agent/projects/scripts/day231')
from check_v2_printed import *
gs=[((lambda z: psum(z,1)),1),((lambda z: psum(z,2)),2),((lambda z: psum(z,1)**2),2),((lambda z: psum(z,2)*psum(z,1)),3),((lambda z: Fr(1)),0),((lambda z: psum(z,1)*psum(z,1)),2)]
hall=hl=cnt=0
for a in range(1,4):
  for g,d in gs:
    n=a+d
    if n>6 or n<2: continue
    t=rnd()
    pe=p_expand(lambda xx: Ta(a,g,xx,t),n,n)
    for x in range(1,n):
      y=n-x
      if x<y: continue
      key=(x,y); cnt+=1
      F=Phi_formula(a,g,d,x,y,t)
      H=zee(key)*pe.get(key,Fr(0))
      T=H/((1-t**x)*(1-t**y))
      hall+= (F==H); hl+= (F==T and F!=0)
print('cases',cnt,'printed Thm6.3 == Hall <,>:',hall,' == HL <,>_t:',hl)
