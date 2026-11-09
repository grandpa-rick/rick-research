"""Independent replay of every NO kill in log_*.txt: fresh coxeter3 session, recompute from words."""
import sys, json, glob
sys.path.insert(0,'/home/agent/projects/proofs/wake285')
from d8lib import from_word, ldes, length, lmul, Cox, mu_from, word, nbrs
n=8; NB=nbrs(n); cox=Cox('D',8); ok=bad=0
for f in sorted(glob.glob(sys.argv[1] if len(sys.argv)>1 else 'log_*.txt')):
    for line in open(f):
        line=line.strip()
        if not line.startswith('{'): continue
        r=json.loads(line); x=from_word(r['x'],n); z=from_word(r['z'],n); y=from_word(r['y'],n)
        A=ldes(x); B=ldes(z); intA={s for s in A if NB[s]<=A}
        c1 = sorted(A)==r['A'] and sorted(B)==r['B'] and B and B<=intA and x!=z
        c2 = y==lmul(r['r'],x) and not ldes(y)<=A and not A<=ldes(y)       # F2 => y in cell(x), y in W_i(x)
        a,b=sorted([y,z],key=length); la,lb=length(a),length(b)
        if (lb-la)%2==0: m=0; how='even gap'
        else: m=mu_from(cox.pol(word(a),word(b)),la,lb); how='pol'
        good=c1 and c2 and m==0
        ok+=good; bad+=not good
        print(f[4:-4], r['why'][:6], sorted(A), sorted(B), 'l(x),l(z),l(y)=',length(x),length(z),length(y), how, 'mu~(y,z)=',m, 'OK' if good else 'FAIL')
print('replayed',ok,'OK',bad,'FAIL')
