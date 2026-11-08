import time
from kl import *
def dmax(y,I,J):
    y=tuple(y); ch=True
    while ch:
        ch=False
        for i in I:
            s=lswap(y,i)
            if length(s)>length(y): y=s; ch=True
        for j in J:
            s=rswap(y,j)
            if length(s)>length(y): y=s; ch=True
    return y
if __name__=="__main__":
    x=(5,4,3,1,9,8,7,2,15,14,11,6,13,10,12,16)
    z=(14,8,4,1,15,9,5,2,16,10,6,3,11,7,12,13)
    print(length(x),length(z),leq(x,z))
    I=ldes(z); J=rdes(z); print('L(z)',[i+1 for i in I],'R(z)',[j+1 for j in J])
    xs=dmax(x,I,J); print('x*',xs,length(xs),leq(xs,z))
    t=time.time(); S=interval(xs,z); print('|[x*,z]|',len(S),time.time()-t)
