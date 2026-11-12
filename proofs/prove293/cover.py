import itertools,re
from eng import A_rw,B_rw
def blocks(P):
    a=[];b=[]
    for m in re.finditer(r'(r+)(u+)',P): a.append(len(m.group(1))); b.append(len(m.group(2)))
    assert 'r'+''.join('r'*x+'u'*y for x,y in zip(a,b))[1:]==P
    return a,b
def top_ok(a,b):
    m=len(a)
    IA=[i for i in range(m) if a[i]>=2 and not(i==0 and a[0]==2)]
    IB=[i for i in range(m) if not(i==0 and a[0]==1)]
    return len(IA)>0 and len(IB)>=2
def bot_ok(a,b):
    m=len(a)
    IA=[i for i in range(m) if b[i]>=2 and not(i==m-1 and b[m-1]==2)]
    IB=[i for i in range(m) if not(i==m-1 and b[m-1]==1)]
    return len(IA)>0 and len(IB)>=2
def family(P):
    if re.fullmatch(r'r+u+',P): return 'i'
    if re.fullmatch(r'ru+r+u',P): return 'ii'
    if re.fullmatch(r'rur+uu',P): return 'iii'
    if re.fullmatch(r'rru+ru',P): return 'iv'
    if re.fullmatch(r'r{1,2}u(ru)*ru{1,2}',P) : return 'v'
    return None
def proj(X,f,val): return {k:v for k,v in X.items() if f(k)==val}
bad=0
for L in range(3,15):
    left={}
    for s in map(''.join,itertools.product('ru',repeat=L)):
        P='r'+s+'u'; a,b=blocks(P)
        # verify the graded-component claims
        A,B=A_rw(s),B_rw(s); U=P.count('u'); V=P.count('r')
        cu=lambda k:('r'+k+'u').count('u'); cr=lambda k:('r'+k+'u').count('r')
        assert max([cu(k) for k in list(A)+list(B)],default=0)<=U
        if top_ok(a,b):
            AU,BU=proj(A,cu,U),proj(B,cu,U)
            assert AU and BU and not set(AU)&set(BU), s
        if bot_ok(a,b):
            AV,BV=proj(A,cr,V),proj(B,cr,V)
            C={k:BV.get(k,0)+AV.get(k,0) for k in set(AV)|set(BV)}; C={k:v for k,v in C.items() if v}
            assert AV and C and not set(AV)&set(C), s
        if not(top_ok(a,b) or bot_ok(a,b)):
            f=family(P); left[f]=left.get(f,0)+1
            if f is None: bad+=1; print('UNCOVERED',s)
    print(L,left)
print('bad',bad)
