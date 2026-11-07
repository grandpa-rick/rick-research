import os
_d=os.path.dirname(os.path.abspath(__file__))+'/../wake279/'
_cwd=os.getcwd(); os.chdir(_d)
exec(open('a13_caseB.py').read().split('\nn=14')[0])
os.chdir(_cwd)
PX=[[1,2,6,10],[3,7,11,14],[4,8,12],[5,9,13]]; PZ=[[1,2,3,7],[4,5,6,11],[8,9,10],[12,13,14]]
PX2=[[1,2,6,10,14],[3,7,11],[4,8,12],[5,9,13]]; PZ2=[[1,2,3,7,11],[4,5,6],[8,9,10],[12,13,14]]
def star_images(x):
    Lx=L(x); n=len(x); out=[]
    for s in range(1,n):
        y=lmul(s,x)
        if (L(y)-Lx) and rsk(y)[1]==rsk(x)[1]: out.append((s,y))
    return out
