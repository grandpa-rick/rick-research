import json
from interval import interval, covers_down, rankmat, geq_x
B=json.load(open('qbest.json'))
def interval_elems(x,z):
    Rx=rankmat(x); level={tuple(z)}; allv=set(level)
    while level:
        nxt=set(v for w in level for v in covers_down(w) if geq_x(v,Rx)); allv|=nxt; level=nxt
    return allv
if __name__=='__main__':
    r=B[13]; x,z=r['x'],r['z']; E=interval_elems(x,z); print(len(E))
    fixed=[i for i in range(16) if all(y[i]==x[i] for y in E)]
    print('common positions',[i for i in range(16) if x[i]==z[i]],'fixed throughout',fixed)
