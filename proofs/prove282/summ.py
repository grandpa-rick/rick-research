import json
from collections import Counter
for n in (15,16):
    c=Counter(); pl=Counter()
    for l in open('out_muxz%d.txt'%n):
        try: d=json.loads(l)
        except: continue
        c[(d['muxz'],d['verdict'])]+=1
        if d['path'] is not None: pl[len(d['path'])]+=1
    print(n,dict(c),'pathlens',dict(pl))
