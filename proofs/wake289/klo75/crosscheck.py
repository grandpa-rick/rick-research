import sys; from indmodel import *
p=32003; CS={m:connected_shapes(m) for m in range(1,7)}
tot=ok=0
for n in range(2,int(sys.argv[1])+1):
  for comps in all_shapes(n,CS):
    if len(comps)<2: continue
    cells=star(comps); B,act,s=build_module(cells); d=len(B); check_relations(act,n)
    G1=dense(act,d); G2,n2,d2=ind_product(comps); assert n2==n
    tot+=1
    c1=character(B,n); c2=char_dense(G2,n,d2)
    good = d==d2 and c1==c2
    if d<=40:
        iso=is_iso(G1,G2,d,p); isorev=is_iso(G1,ind_product(comps[::-1])[0],d,p)
    else: iso=isorev=None
    if good and iso is not False: ok+=1
    print(n,lam_mu(cells),'d',d,d2,'char',c1==c2,'iso(order 1..k)',iso,'iso(reversed)',isorev,flush=True)
print('total',tot,'ok',ok)
