import sys, pickle
sys.argv = ['x']; from rl import *
mods = pickle.load(open('mods5.pkl', 'rb'))
for j, x in enumerate(mods[5]):
    if x[4] > 12: continue
    G, n, d = dense(x[2]); print(5, x[0], x[1], 'd', d, 'proj', x[3], 'R', R(G, n, d), 'L', L(G, n, d), flush=True)
