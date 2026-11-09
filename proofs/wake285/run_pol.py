import subprocess, sys, time, re
def pol(typ, rank, x, y, timeout=600):
    inp = f"type\n{typ}\n{rank}\npol\n{x}\n{y}\nq\n"
    t=time.time()
    p = subprocess.Popen(["./coxeter"], cwd="/home/agent/projects/proofs/wake285/coxeter",
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.stdin.write(inp.encode()); p.stdin.close()
    buf=b""
    while True:
        c=p.stdout.read(256)
        if not c: break
        buf+=c
        m=re.search(rb"second : (.*?)\n", buf)
        if m or len(buf)>20000 or time.time()-t>timeout: break
    p.kill(); p.wait()
    m=re.search(rb"second : (.*?)\n", buf)
    return (m.group(1).decode() if m else buf[-400:].decode(errors='replace')), time.time()-t
if __name__=="__main__":
    typ,rank,x,y=sys.argv[1:5]
    r,dt=pol(typ,rank,x,y); print(repr(r), f"{dt:.2f}s")
