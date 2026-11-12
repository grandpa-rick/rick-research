import itertools
from collections import defaultdict
from eng import A_rw,R_in_S,D,S_to_R,word2comp,comp2word,valid
def Dm_rw(m,s):
    P='r'+s+'u'; out=defaultdict(int)
    for i in range(len(P)-m):
        w=P[i:i+m+1]
        if w[0]=='r' and w[-1]=='u':
            sg=(-1)**w[1:-1].count('u')
            for y in 'ru':
                Q=P[:i]+y+P[i+m+1:]
                if valid(Q): out[Q[1:-1]]+=sg
    return {k:v for k,v in out.items() if v}
bad=0;n=0
for m in (1,2,3,4):
  for L in range(m+1,10):
    for s in map(''.join,itertools.product('ru',repeat=L)):
        T={comp2word(k):v for k,v in S_to_R(D(m,R_in_S(word2comp(s)))).items()}
        n+=1; bad+= T!=Dm_rw(m,s)
print('D_m cut rule m<=4, L<=9:',n,'bad',bad)
# A=0 iff even alternating, for all s L<=14
badA=0
for L in range(3,15):
    for s in map(''.join,itertools.product('ru',repeat=L)):
        alt=all(s[i]!=s[i+1] for i in range(L-1))
        badA+= (not A_rw(s)) != (alt and L%2==0)
print('A=0 iff even alt, L<=14: bad',badA)
