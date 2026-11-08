# Method A (crownU_sep.py, right-mult) vs Method B (prove283 kl.brute, left-mult): all P_{u,w} in S_6
import sys,os
sys.argv=['x','6','0']; exec(open('crownU_sep.py').read().split('# ---- Knuth')[0]); PA=P
sys.path.insert(0,'/home/agent/projects/proofs/prove283'); os.chdir('/home/agent/projects/proofs/prove283')
from kl import brute
W2,PB,muB=brute(6)
bad=sum(1 for k in PA if tuple(PB[k])!=PA[k]); print('S6 pairs A',len(PA),'B',len(PB),'mismatches',bad)
