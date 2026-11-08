import time,sys
from kl import *
from parab import *
cases={'gap13':((7,3,2,11,10,6,5,1,15,9,8,4,16,14,13,12),(10,6,2,14,11,7,3,1,15,12,8,4,16,13,9,5)),
       'inst0':((5,4,3,1,9,8,7,2,15,14,11,6,13,10,12,16),(14,8,4,1,15,9,5,2,16,10,6,3,11,7,12,13))}
def main():
  for name in sys.argv[1:]:
      x,z=cases[name]; t0=time.time()
      J=rdes(z)
      print(name,'l(x)',length(x),'l(z)',length(z),'J=R(z)',[j+1 for j in J],'x is J-max',maxrep(x,J)==x,'z J-max',maxrep(z,J)==z,flush=True)
      xm,zm=minrep(x,J),minrep(z,J)
      PJ,sz=Parab(J,'-1').P(xm,zm,verbose=True)
      p=PJ[xm]; d=length(z)-length(x)-1
      print(name,'P',p,'mu',p[d//2] if d%2==0 and len(p)>d//2 else 0,'time',time.time()-t0,flush=True)

if __name__=='__main__': main()