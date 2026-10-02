import sys,pickle
from engine import *
MAXN=int(sys.argv[1]); mats=pickle.load(open('Emats_6.pkl','rb'))
for n in range(7,MAXN+1):
    for k in range(1,n+1):
        mats[(k,n-k)]=Ematrix(k,n-k); print('done',k,n-k,flush=True)
pickle.dump(mats,open(f'Emats_{MAXN}.pkl','wb'))
