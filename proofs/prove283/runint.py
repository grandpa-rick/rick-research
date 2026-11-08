import sys,json
from interval import interval
B=json.load(open('qbest.json')); k=int(sys.argv[1]); cap=int(sys.argv[2])
r=B[k]; print('inst',k,r['lam'],'lx',r['lx'],'lz',r['lz'],'x',r['x'],'z',r['z'],flush=True)
t,s,done=interval(r['x'],r['z'],cap=cap)
print('RESULT inst',k,'size',t,'complete',done,'levels',s)
