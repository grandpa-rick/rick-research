import sys,re,random
sys.path.insert(0,'/home/agent/projects/proofs/wake285')
from wg_twins import parse
from d8lib import from_word, ldes, length, word, Cox, mu_from
n=6
cells=parse('/home/agent/projects/proofs/wake285/wgraphs/D6_wg.txt')
lc=[]
for line in open('lc/D6_lc.txt'):
    m=re.match(r'\s*(\d+)\s*:\s*\{(.*)\}',line)
    if m: lc.append([from_word(w.strip(),n) for w in m.group(2).split(',')])
print(len(cells),len(lc))
bad=sum(1 for c,l in zip(cells,lc) if len(c)!=len(l) or any(D!=ldes(w) for (D,E),w in zip(c,l)))
print('descent/order mismatches',bad)
# mu check on random edges and non-edges
cox=Cox('D',n); random.seed(0); mm=0; tot=0
for _ in range(400):
    ci=random.randrange(len(cells)); c=cells[ci]; l=lc[ci]
    if len(c)<2: continue
    i,j=random.sample(range(len(c)),2)
    if c[j][0]<=c[i][0]: continue   # edge i->j listed when L(j) not subset L(i)
    a,b=l[i],l[j]; la,lb=length(a),length(b)
    if la==lb or (la-lb)%2==0: m=0
    else:
        if la>lb: a,b,la,lb=b,a,lb,la
        m=mu_from(cox.pol(word(a) ,word(b)) if la else cox.pol('',word(b)),la,lb)
    tot+=1; mm+= (m!=c[i][1].get(j,0))
print('mu checks',tot,'mismatch',mm)
random.seed(0); k=0
for _ in range(400):
    ci=random.randrange(len(cells)); c=cells[ci]; l=lc[ci]
    if len(c)<2: continue
    i,j=random.sample(range(len(c)),2)
    if c[j][0]<=c[i][0]: continue
    a,b=l[i],l[j]; la,lb=length(a),length(b)
    if la==lb or (la-lb)%2==0: m=0;P=None
    else:
        if la>lb: a,b,la,lb=b,a,lb,la
        P=cox.pol(word(a),word(b)) if la else cox.pol('',word(b)); m=mu_from(P,la,lb)
    if m!=c[i][1].get(j,0) and k<8:
        k+=1; print(ci,i,j,sorted(c[i][0]),sorted(c[j][0]),word(l[i]),word(l[j]),length(l[i]),length(l[j]),'mine',m,P,'native ij',c[i][1].get(j),'ji',c[j][1].get(i))
