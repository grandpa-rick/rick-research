"""Type A (*) via Kostka positivity: exists SYT pair iff beta <= alpha' (dominance), where
alpha = sort(comp cut at int A), beta = sort(comp cut at A^c). Search A subset [n-1] violating."""
import sys
def comp(n,cuts):
    c=sorted(cuts); prev=0; out=[]
    for i in c: out.append(i-prev); prev=i
    out.append(n-prev); return sorted(out,reverse=True)
def conj(a):
    return [sum(1 for x in a if x>=k) for k in range(1,(a[0] if a else 0)+1)]
def dom(b,a):  # b <= a
    sb=sa=0
    for k in range(max(len(a),len(b))):
        sb+= b[k] if k<len(b) else 0; sa+= a[k] if k<len(a) else 0
        if sb>sa: return False
    return True
for n in range(3,int(sys.argv[1])+1):
    bad=0;ex=None
    for m in range(1,2**(n-1)-1):
        A={i for i in range(1,n) if m>>(i-1)&1}
        I={i for i in A if all(j in A for j in (i-1,i+1) if 1<=j<=n-1)}
        al=comp(n,I); be=comp(n,set(range(1,n))-A)
        if dom(be,conj(al)): bad+=1; ex=ex or (sorted(A),be,conj(al))
    print(n,'violating A:',bad,ex)
