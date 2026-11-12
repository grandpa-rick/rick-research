# replay: DP coeff vs brute-force shuffle coeff (cap_rank.coeff), all s with L<=6, all u,v subwords; and ranks vs out files
import itertools
from fastcap import coeff_dp, basis, ranks
from cap_rank_import import coeff
n=mm=0
for L in range(0,7):
    for s in (''.join(t) for t in itertools.product('01',repeat=L)):
        d=L+1
        for i in range(d+1):
            for u in basis(s,i):
                for v in basis(s,d-i):
                    n+=1; mm+= coeff_dp(u,v,s)!=coeff(u,v,s)
        # also non-subword u (should be zero)
print('entries',n,'mismatch',mm)
for L in range(0,12):
    s=('01'*10)[:L]; print(L,ranks(s))
