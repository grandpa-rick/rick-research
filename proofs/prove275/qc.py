# Q62: quasi-Kashiwara operators on words, factor-locality, characters.
# Definition (Cain-Malheiro hypoplactic, reconstructed from memory -- OWNER CHECK OWED):
#   w has an i-inversion iff subword (i+1, i) occurs.  ëi(w)=ẽi(w), f̈i(w)=f̃i(w) if no i-inversion, else undefined.
#   With no inversion the {i,i+1}-subword is i^a (i+1)^b; ẽ: leftmost i+1 -> i, f̃: rightmost i -> i+1. ε̈=b, φ̈=a; inversion => ∞.
import itertools, sys
from collections import Counter, defaultdict
INF=10**9
def inv(w,i):
    seen=False
    for c in w:
        if c==i+1: seen=True
        elif c==i and seen: return True
    return False
def kash(w,i,op):
    # Kashiwara: bracket (i+1 ... i) pairs  [i+1 = '(' , i = ')' ]
    st=[];unb=[]
    for p,c in enumerate(w):
        if c==i+1: st.append(p)
        elif c==i:
            if st: st.pop()
            else: unb.append(p)   # unbracketed i
    unbi=unb; unbj=st              # reduced word i^a (i+1)^b
    w=list(w)
    if op=='e':
        if not unbj: return None
        w[unbj[0]]=i; return tuple(w)
    else:
        if not unbi: return None
        w[unbi[-1]]=i+1; return tuple(w)
def kstr(w,i):
    st=[];a=0
    for c in w:
        if c==i+1: st.append(1)
        elif c==i:
            if st: st.pop()
            else: a+=1
    return len(st),a   # eps, phi
def quasi(w,i,op):
    if inv(w,i): return None
    return kash(w,i,op)
def qstr(w,i):
    if inv(w,i): return INF,INF
    return w.count(i+1), w.count(i)
