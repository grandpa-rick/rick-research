def qint(n,step=1):
    c=[0]*((n-1)*step+1)
    for j in range(n): c[j*step]=1
    return c
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c
def pred(L):
    d=L+1
    if L%2==1:
        k=(L+1)//2; return mul(qint(k//2+1,2),qint(2*((k+1)//2)+1))
    k=L//2; m=(k+1)//2
    P={0:1}
    for j in range(1,m): P[2*j+1]=1
    if k<=2: P={0:1}
    num=[0]*(d+2)
    for e,c in P.items(): num[e]+=c; num[d+1-e]-=c
    out=[];acc=0
    for j in range(d+1): acc+=num[j]; out.append(acc)
    return out
if __name__=='__main__':
    for L in range(0,23): print(L,pred(L),sum(pred(L)))
