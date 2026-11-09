import sys,re,random
sys.path.insert(0,'/home/agent/projects/proofs/wake285')
from wg_twins import parse
from d8lib import from_word, ldes, length, word, Cox, mu_from
n=int(sys.argv[1])
cells=parse(f'/home/agent/projects/proofs/wake285/wgraphs/D{n}_wg.txt')
lc=[]
for line in open(f'lc/D{n}_lc.txt'):
    m=re.match(r'\s*(\d+)\s*:\s*\{(.*)\}',line)
    if m: lc.append([from_word(w.strip(),n) for w in m.group(2).split(',')])
bad=sum(1 for c,l in zip(cells,lc) if len(c)!=len(l) or any(D!=ldes(w) for (D,E),w in zip(c,l)))
print(len(cells),len(lc),'descent/order mismatches',bad)
# convention: line i lists j iff L(i) not subset L(j) and mu != 0
conv=sum(1 for c in cells for i,(D,E) in enumerate(c) for j in E if D<=c[j][0])
print('entries violating convention L(i) not<= L(j):',conv)
cox=Cox('D',n); random.seed(0); mm=0; tot=0; nz=0
for _ in range(int(sys.argv[2])):
    ci=random.randrange(len(cells)); c=cells[ci]; l=lc[ci]
    if len(c)<2: continue
    i,j=random.sample(range(len(c)),2)
    if c[i][0]<=c[j][0]: continue
    a,b=l[i],l[j]; la,lb=length(a),length(b)
    if la==lb or (la-lb)%2==0: m=0
    else:
        if la>lb: a,b,la,lb=b,a,lb,la
        m=mu_from(cox.pol(word(a),word(b)) if la else cox.pol('',word(b)),la,lb)
    tot+=1; mm+=(m!=c[i][1].get(j,0)); nz+=m!=0
print('mu checks',tot,'nonzero',nz,'mismatch',mm)
