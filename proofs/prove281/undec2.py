import sys,json; sys.path.insert(0,'.')
from common import *
from orbit2 import search2
Q=[[1,2,3,4,5],[6,7,8,9],[10,11,12],[13,14,15]]
Pz=[[1, 2, 3, 7, 15], [4, 5, 6, 11], [8, 9, 10], [12, 13, 14]]; U=[[1, 2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12], [5, 9, 13]]
y=rsk_inv(U,Q); z=rsk_inv(Pz,Q)
st,p,end,sz=search2(y,z); print(st,'path',p,'len',len(p),'orbit',sz)
json.dump(dict(Q=Q,y=y,z=z,verdict=st,path=p),open('cert_undec.json','w'))
