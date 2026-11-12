from cap_rank import analyse
for L in range(0,10):
    s=('01'*10)[:L]
    b,r,_=analyse(s); print(L, s, 'b=',b,'rank=',r,'sum',sum(r))
