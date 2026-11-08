import sys,json,time
from kl import P_interval
from interval import length
B=json.load(open('qbest.json')); k=int(sys.argv[1]); r=B[k]; x,z=r['x'],r['z']
t=time.time(); res,N,E=P_interval(x,z,'lex')
p=res[tuple(x)]; d=length(z)-length(x)
print('inst',k,r['lam'],'N',N,'E',E,'lx',length(x),'lz',length(z),'P_{x,z}',p,'mu',p[(d-1)//2] if len(p)>(d-1)//2 else 0,'time %.1f'%(time.time()-t))
json.dump({'inst':k,'x':x,'z':z,'N':N,'E':E,'P':p,'mu':(p[(d-1)//2] if len(p)>(d-1)//2 else 0),
  'P_all_nontriv':sum(1 for u,q in res.items() if any(q[1:]))},open(f'mu_inst{k}.json','w'))
