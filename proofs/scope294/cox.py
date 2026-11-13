import subprocess, re, threading
CX="/home/agent/projects/proofs/wake285/coxeter"
def redword(w):
    w=list(w); word=[]; changed=True
    while changed:
        changed=False
        for i in range(len(w)-1):
            if w[i]>w[i+1]:
                w[i],w[i+1]=w[i+1],w[i]; word.append(i+1); changed=True
    return word[::-1]
def ldes1(w):
    pos={a:k for k,a in enumerate(w)}
    for i in range(1,len(w)):
        if pos[i+1]<pos[i]: return i
def fix(x,y):
    if list(x)==sorted(x):  # P_{e,y}=P_{s,y}, s left descent (values) of y
        i=ldes1(y); x=list(x); a,b=x.index(i),x.index(i+1); x[a],x[b]=x[b],x[a]
    return x
def pols(n,pairs):
    """batch: list of (x,y) perms -> list of strings"""
    inp=f"type\nA\n{n-1}\n"+"".join(f"pol\n{''.join(map(str,redword(fix(x,y))))}\n{''.join(map(str,redword(y)))}\n" for x,y in pairs)
    p=subprocess.Popen(["./coxeter"],cwd=CX,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    def wr(): p.stdin.write(inp.encode()); p.stdin.close()
    th=threading.Thread(target=wr); th.start()
    out=[]; buf=b""; pat=re.compile(rb"second : (.*?)\n")
    while len(out)<len(pairs):
        c=p.stdout.read1(65536) if hasattr(p.stdout,'read1') else p.stdout.read(4096)
        if not c: break
        buf+=c
        while True:
            m=pat.search(buf)
            if not m: break
            pre=buf[:m.start()]
            assert b"error" not in pre and b"not" not in pre, pre[-300:]
            out.append(m.group(1).decode()); buf=buf[m.end():]
            if len(out)==len(pairs): break
    p.kill(); p.wait(); th.join()
    assert len(out)==len(pairs),(len(out),len(pairs))
    return out
def parse(st):
    st=st.strip().replace(' ','')
    co={}
    for t in re.split(r'\+',st):
        if 'q' not in t: co[0]=co.get(0,0)+int(t)
        else:
            a,b=t.split('q'); a=int(a) if a else 1; e=int(b[1:]) if b else 1; co[e]=co.get(e,0)+a
    return tuple(co.get(k,0) for k in range(max(co)+1))
