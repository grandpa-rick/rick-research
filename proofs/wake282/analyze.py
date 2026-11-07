import json,sys,random
n=int(sys.argv[1]); R0=json.load(open('sieve%d.json'%n))
R=[r for r in R0 if r['verdict']!='UNDECIDED']
print('pairs',len(R0),'decided',len(R),'twins',sum(r['verdict']=='TWIN' for r in R),'undecided',len(R0)-len(R))
UND=[r for r in R0 if r['verdict']=='UNDECIDED']
fmt=lambda T:'/'.join(''.join('%x'%v for v in row) for row in T)
print('== per-pair (ii)-elements and (i)-elements with Des>A ==')
nii=sat=0; ii_distinct=set()
for k,r in enumerate(R0):
    ii=[e for e in r['elems'] if e['kind']=='ii']
    i_sup=[e for e in r['elems'] if e['kind']=='i' and e['sup']]
    i_kill=[e for e in r['elems'] if e['kind']=='i' and e['muyz']==0]
    for e in ii:
        nii+=1; sat+=e['cand_x']; ii_distinct.add(tuple(e['y']))
    if ii or i_sup or r['zero']:
        print(k,r['lam'],r['A'],'Pz',fmt(r['Pz']),'par_ok',r['parity_ok'],r['verdict'])
        for e in ii+i_sup+r['zero']:
            print('   ',e['kind'],e['s'],'Des',e['DesPy'],'sup',e['sup'],'candX',e['cand_x'],'pair(Py,Pz)',e['pair_with_same_Pz'],'anyTwin@Des',e['any_twin_at_DesPy'],'mu(y,x)',e['muyx'],'mu(y,z)',e['muyz'],'l(y)',e['ly'],'l(x)',r['lx'],'l(z)',r['lz'])
print('(above: all pairs incl. undecided)')
print('test2: (ii)-element instances',nii,'distinct y',len(ii_distinct),'cand x-half',sat,'violating',nii-sat)
alli=[e for r in R for e in r['elems'] if e['kind']=='i']
print('(i) instances',len(alli),'with Des>A',sum(e['sup'] for e in alli),'that are cand x',sum(e['cand_x'] for e in alli))
pk=[e for r in R if r['parity_ok'] for e in r['elems'] if e['kind']=='i' and e['muyz']==0]
print('(i)-elements killing a parity-OK pair:',len(pk),'of which Des>A:',sum(e['sup'] for e in pk))
def cm(pred,truth):
    m={(a,b):0 for a in (1,0) for b in (1,0)}
    for p,t in zip(pred,truth): m[(p,t)]+=1
    return m
truth=[r['verdict']=='TWIN' for r in R]
rules={
 'R0 parity only':lambda r:r['parity_ok'],
 'R1 parity & no (ii)-element':lambda r:r['parity_ok'] and not any(e['kind']=='ii' for e in r['elems']),
 'R2 parity & every (ii) y has mu(y,z)=1 (Lemma A on (ii) only)':lambda r:r['parity_ok'] and all(e['muyz']==1 for e in r['elems'] if e['kind']=='ii'),
 'R3 sieve: parity & no (ii) y that is a cand x-half at Des P_y':lambda r:r['parity_ok'] and not any(e['kind']=='ii' and e['cand_x'] for e in r['elems']),
 'R4 sieve: parity & no (ii) y with (P_y,P_z) non-twin':lambda r:r['parity_ok'] and not any(e['kind']=='ii' and e['pair_with_same_Pz']!='TWIN' for e in r['elems']),
}
for name,f in rules.items():
    m=cm([bool(f(r)) for r in R],truth)
    print('%-62s TP %d FP %d FN %d TN %d  agree %d/%d'%(name,m[(1,1)],m[(1,0)],m[(0,1)],m[(0,0)],m[(1,1)]+m[(0,0)],len(R)))
# negative controls (S_15 only meaningful)
for name,f in rules.items():
    print('  undecided pairs predicted TWIN by',name.split()[0],':',sum(bool(f(r)) for r in UND),'/',len(UND))
if len(R)>10:
    random.seed(282); T=10000
    iisets=[[e for e in r['elems'] if e['kind']=='ii'] for r in R]
    def agree(pred): return sum(p==t for p,t in zip(pred,truth))
    # NC1: permute the (ii)-sets among the 48 pairs (breaks the Des-label / which-x link)
    a1=[]
    for _ in range(T):
        p=iisets[:]; random.shuffle(p)
        a1.append(agree([r['parity_ok'] and not p[k] for k,r in enumerate(R)]))
    # NC2: shuffle all mu(y,z) values over all (y,z) records, rule R2+(i): parity & all elements mu(y,z)=1
    allmu=[e['muyz'] for r in R for e in r['elems']]
    a2=[]
    for _ in range(T):
        sh=allmu[:]; random.shuffle(sh); it=iter(sh)
        a2.append(agree([r['parity_ok'] and all(next(it)==1 for e in r['elems']) for r in R]))
    base2=agree([r['parity_ok'] and all(e['muyz']==1 for e in r['elems']) for r in R])
    # NC3: shuffle parity labels, rule R1
    pars=[r['parity_ok'] for r in R]; a3=[]
    for _ in range(T):
        p=pars[:]; random.shuffle(p)
        a3.append(agree([p[k] and not iisets[k] for k in range(len(R))]))
    st=lambda a:'mean %.2f min %d max %d  P(=all) %.4f'%(sum(a)/T,min(a),max(a),sum(x==len(R) for x in a)/T)
    print('NC1 permute (ii)-sets, rule R1:',st(a1))
    print('NC2 shuffle mu(y,z), rule "parity & all (i)+(ii) mu(y,z)=1" (unshuffled %d/all):'%base2,st(a2))
    print('NC3 shuffle parity labels, rule R1:',st(a3))
