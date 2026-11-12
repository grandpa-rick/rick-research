from klo import *
CS={m:connected_shapes(m) for m in range(1,9)}
print([len(CS[m]) for m in CS])
cells=star([((0,1),(0,1)),((0,0),)])
print(lam_mu(cells))
B,act,s=build_module(cells); check_relations(act,5)
print(len(B), ''.join(map(str,B[s])), sorted(''.join(map(str,g)) for g in B))
E,F_of,_,_=end_algebra(B,act,s); print('dimEnd',len(E), local_test(E,F_of,32003))
for v in E: print({''.join(map(str,B[k])):int(v[k]) for k in np.nonzero(v)[0]})
print(top(B,act))
