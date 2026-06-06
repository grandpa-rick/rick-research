"""
B_2 consistency check: Rick's tilde-B_1 tilde-B_2 tilde-B_1 vs. Azenhas-Torres
orthogonal evacuation xi_B on B(omega_1 + omega_2).

This script runs two interpretations of Rick's tilde-B_i operator:

  (R1) "On-B(lambda)" interpretation: tilde-B_i acts directly on the finite
       KN-tableau crystal B(omega_1+omega_2) via the Watanabe parity rule.
       Falls off the edge in 10/16 vertices (where the required e_i is None).

  (R2) "K_p(infty)" interpretation: embed B(omega_1+omega_2) into K_p(infty)
       and apply tilde-B_i = (e_i if phi_i even else f_i) there. The naive
       transport-via-f_i embedding is NOT INJECTIVE (16 -> 14), so this
       interpretation is ALSO ill-defined as stated.

Both interpretations fail to reproduce AT's xi_B. We document the failures
precisely so Rick can refine the operator/embedding.
"""

import sys
sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')
from b_i_b2 import (
    e_i as kp_e, f_i as kp_f, eps_i as kp_eps, phi_i as kp_phi,
    kp_clean, kp_repr, B11, B12, G12, B22
)
from collections import defaultdict
from typing import Optional, Tuple, Dict, List

# ----------------------------------------------------------------------
# Build B(omega_1+omega_2) at B_2 via Kashiwara tensor product
# ----------------------------------------------------------------------

V_ELEMS = ['1', '2', '0', 'b2', 'b1']
V_WT = {'1':(1,0),'2':(0,1),'0':(0,0),'b2':(0,-1),'b1':(-1,0)}
V_F1 = {'1': '2', 'b2': 'b1'}
V_F2 = {'2': '0', '0': 'b2'}
V_E1 = {b: a for a, b in V_F1.items()}
V_E2 = {b: a for a, b in V_F2.items()}

def v_f(x, i): return (V_F1 if i == 1 else V_F2).get(x)
def v_e(x, i): return (V_E1 if i == 1 else V_E2).get(x)
def v_eps(x, i):
    c = 0; cur = x
    while v_e(cur, i) is not None: cur = v_e(cur, i); c += 1
    return c
def v_phi(x, i):
    c = 0; cur = x
    while v_f(cur, i) is not None: cur = v_f(cur, i); c += 1
    return c

S_ELEMS = ['12', '1b2', '2b1', 'b2b1']
S_WT = {'12':(0.5,0.5),'1b2':(0.5,-0.5),'2b1':(-0.5,0.5),'b2b1':(-0.5,-0.5)}
S_F2 = {'12': '1b2', '2b1': 'b2b1'}
S_F1 = {'1b2': '2b1'}
S_E2 = {b: a for a, b in S_F2.items()}
S_E1 = {b: a for a, b in S_F1.items()}

def s_f(x, i): return (S_F1 if i == 1 else S_F2).get(x)
def s_e(x, i): return (S_E1 if i == 1 else S_E2).get(x)
def s_eps(x, i):
    c = 0; cur = x
    while s_e(cur, i) is not None: cur = s_e(cur, i); c += 1
    return c
def s_phi(x, i):
    c = 0; cur = x
    while s_f(cur, i) is not None: cur = s_f(cur, i); c += 1
    return c

def t_wt(t):
    a = V_WT[t[0]]; b = S_WT[t[1]]
    return (a[0] + b[0], a[1] + b[1])

def pair_alpha(wt, i):
    return wt[0] - wt[1] if i == 1 else 2 * wt[1]

def t_eps(t, i):
    x, y = t
    return max(v_eps(x, i), s_eps(y, i) - pair_alpha(V_WT[x], i))

def t_phi(t, i):
    x, y = t
    return max(s_phi(y, i), v_phi(x, i) + pair_alpha(S_WT[y], i))

def t_f(t, i):
    x, y = t
    if v_phi(x, i) > s_eps(y, i):
        nx = v_f(x, i)
        if nx is None: return None
        return (nx, y)
    ny = s_f(y, i)
    if ny is None: return None
    return (x, ny)

def t_e(t, i):
    x, y = t
    if v_phi(x, i) >= s_eps(y, i):
        nx = v_e(x, i)
        if nx is None: return None
        return (nx, y)
    ny = s_e(y, i)
    if ny is None: return None
    return (x, ny)

def connected_component(start):
    seen = {start}; stack = [start]
    while stack:
        b = stack.pop()
        for i in (1, 2):
            for op in (t_e, t_f):
                nb = op(b, i)
                if nb is not None and nb not in seen:
                    seen.add(nb); stack.append(nb)
    return seen

AT_NS = {'1':'1','2':'2','0':'0','b2':'bar2','b1':'bar1'}
AT_SP = {'12':'12','1b2':'1bar2','2b1':'2bar1','b2b1':'bar2bar1'}
def at_fmt(t):
    if t is None: return 'None'
    return f"({AT_NS[t[0]]} | {AT_SP[t[1]]})"


AT_TABLE = {
    ('1', '12'): ('b1', 'b2b1'),
    ('2', '12'): ('b2', 'b2b1'),
    ('1', '1b2'): ('b1', '2b1'),
    ('2', '1b2'): ('b1', '1b2'),
    ('0', '12'): ('b2', '2b1'),
    ('2', '2b1'): ('b2', '1b2'),
    ('b2', '12'): ('0', '2b1'),
    ('0', '1b2'): ('b1', '12'),
    ('b1', '12'): ('0', '1b2'),
    ('0', '2b1'): ('b2', '12'),
    ('b2', '1b2'): ('2', '2b1'),
    ('b2', '2b1'): ('0', '12'),
    ('b1', '1b2'): ('2', '1b2'),
    ('b1', '2b1'): ('1', '1b2'),
    ('b2', 'b2b1'): ('2', '12'),
    ('b1', 'b2b1'): ('1', '12'),
}


# ======================================================================
# INTERPRETATION R1: tilde-B_i directly on B(omega_1+omega_2)
# ======================================================================

def tilde_B_finite(b, i):
    """Watanabe rule on a finite crystal element."""
    if b is None: return None
    p = t_phi(b, i)
    if p % 2 == 0:
        return t_e(b, i)
    else:
        return t_f(b, i)

def braid_finite(b):
    a = tilde_B_finite(b, 1)
    if a is None: return None
    a = tilde_B_finite(a, 2)
    if a is None: return None
    return tilde_B_finite(a, 1)

def braid_finite_other(b):
    a = tilde_B_finite(b, 2)
    if a is None: return None
    a = tilde_B_finite(a, 1)
    if a is None: return None
    return tilde_B_finite(a, 2)


# ======================================================================
# INTERPRETATION R2: tilde-B_i on K_p(infty) via embedding
# ======================================================================

def kp_clean_dict(pi):
    return {k: v for k, v in pi.items() if v}

def kp_freeze(pi):
    return tuple(sorted(kp_clean_dict(pi).items()))

def kp_eq(a, b):
    return kp_clean_dict(a) == kp_clean_dict(b)

def build_embedding_naive():
    """BFS from HW (1,12), transport f_i in K_p(infty). NOT INJECTIVE in general."""
    hw = ('1', '12')
    embed = {hw: {}}
    queue = [hw]
    conflicts = []
    while queue:
        b = queue.pop(0)
        pi = embed[b]
        for i in (1, 2):
            nb = t_f(b, i)
            if nb is None: continue
            new_pi = kp_f(pi, i)
            if nb in embed:
                if not kp_eq(embed[nb], new_pi):
                    conflicts.append((b, i, nb, embed[nb], new_pi))
            else:
                embed[nb] = new_pi
                queue.append(nb)
    return embed, conflicts

def tilde_B_kp(pi, i):
    p = kp_phi(pi, i)
    return kp_e(pi, i) if p % 2 == 0 else kp_f(pi, i)

def braid_kp(pi):
    a = tilde_B_kp(pi, 1)
    if a is None: return None
    a = tilde_B_kp(a, 2)
    if a is None: return None
    return tilde_B_kp(a, 1)

def braid_kp_other(pi):
    a = tilde_B_kp(pi, 2)
    if a is None: return None
    a = tilde_B_kp(a, 1)
    if a is None: return None
    return tilde_B_kp(a, 2)


# ======================================================================
# MAIN
# ======================================================================

def header(s):
    print("\n" + "=" * 78)
    print("  " + s)
    print("=" * 78)

def main():
    hw = ('1', '12')
    B = connected_component(hw)
    assert len(B) == 16
    sorted_B = sorted(B, key=lambda t: (-t_wt(t)[0], -t_wt(t)[1]))

    header("Phase A: B(omega_1+omega_2) at B_2 [16 vertices, AT predictions cached]")
    print(f"  |B(omega_1+omega_2)| = {len(B)}")
    print(f"  AT table is involution + weight-negating: ", end="")
    for k, v in AT_TABLE.items():
        assert AT_TABLE[v] == k
        wk, wv = t_wt(k), t_wt(v)
        assert (wk[0] + wv[0], wk[1] + wv[1]) == (0, 0)
    print("OK")

    # ---- R1: tilde-B on B(lambda) directly ----
    header("Interpretation R1: tilde-B_i acts on B(omega_1+omega_2) directly")
    print("  (Watanabe rule: tilde-B_i b = e_i b if phi_i(b) even else f_i b)\n")
    r1_results = {}
    fmt_hdr = f"  {'b':28s}  {'tilde-B_1 B_2 B_1 (b)':22s}  {'AT predicts':18s}  match"
    print(fmt_hdr)
    print("  " + "-" * 80)
    n_match_r1 = 0
    n_none_r1 = 0
    for b in sorted_B:
        rb = braid_finite(b)
        r1_results[b] = rb
        at = AT_TABLE.get(b)
        m = "MATCH" if rb == at else ("None " if rb is None else "DIFF ")
        if rb is None: n_none_r1 += 1
        if rb == at: n_match_r1 += 1
        print(f"  {at_fmt(b):28s}  {at_fmt(rb):22s}  {at_fmt(at):18s}  [{m}]")
    print(f"\n  R1 summary: {n_match_r1}/16 match AT, {n_none_r1}/16 fall off edge (None)")

    # Braid check R1
    print(f"\n  R1 braid relation B_1 B_2 B_1 = B_2 B_1 B_2 on B(lambda)?")
    fail = 0
    for b in sorted_B:
        a = braid_finite(b); c = braid_finite_other(b)
        if a != c:
            fail += 1
            if fail <= 3:
                print(f"    {at_fmt(b)}: B121 = {at_fmt(a)}, B212 = {at_fmt(c)}")
    print(f"    {fail}/16 vertices fail the braid relation. {'BRAID HOLDS' if fail == 0 else 'BRAID FAILS'}")

    # ---- R2: embedding into K_p(infty)
    header("Interpretation R2: embed B(omega_1+omega_2) -> K_p(infty), apply Watanabe rule there")
    embed, conflicts = build_embedding_naive()
    print(f"  Naive embedding (transport f_i): {len(embed)} elements")
    print(f"  Conflicts (multiple paths to same b give different pi): {len(conflicts)}")
    for b, i, nb, pi_old, pi_new in conflicts:
        print(f"    {at_fmt(nb)}: stored pi = {kp_repr(pi_old)}, via f_{i} from {at_fmt(b)} pi = {kp_repr(pi_new)}")
    inv_embed = {kp_freeze(pi): b for b, pi in embed.items()}
    print(f"  Injective: {len(inv_embed) == len(embed)} (got {len(inv_embed)} distinct image partitions)")
    print()
    print(f"  {'b':28s} {'pi(b) in K_p(infty)':40s}")
    print("  " + "-" * 70)
    for b in sorted_B:
        print(f"  {at_fmt(b):28s} {kp_repr(embed[b]):40s}")

    print(f"\n  R2 apply tilde-B_1 B_2 B_1 to each pi(b), project back:")
    print(f"  {'b':28s} {'pi':32s} {'B_1B_2B_1(pi)':32s} {'project':16s} {'AT pred':16s} match")
    print("  " + "-" * 130)
    n_match_r2 = 0; n_in_image = 0
    for b in sorted_B:
        pi = embed[b]; rpi = braid_kp(pi)
        proj = inv_embed.get(kp_freeze(rpi)) if rpi is not None else None
        at = AT_TABLE.get(b)
        m = "MATCH" if proj == at else ("OFF" if proj is None else "DIFF")
        if proj is not None: n_in_image += 1
        if proj == at: n_match_r2 += 1
        rpi_str = kp_repr(rpi) if rpi is not None else "None"
        print(f"  {at_fmt(b):28s} {kp_repr(pi):32s} {rpi_str:32s} {at_fmt(proj):16s} {at_fmt(at):16s} [{m}]")
    print(f"\n  R2 summary: {n_match_r2}/16 match AT; {n_in_image}/16 results land in embedding image")

    print(f"\n  R2 braid relation on the 16 pi's: ", end="")
    fail = 0
    for b in sorted_B:
        pi = embed[b]; a = braid_kp(pi); c = braid_kp_other(pi)
        if kp_freeze(a or {}) != kp_freeze(c or {}):
            fail += 1
    print(f"{fail}/16 fail. {'BRAID HOLDS' if fail == 0 else 'BRAID FAILS'}")

    # ---- The explicit datum ----
    header("AT explicit datum: xi_B(0|2bar1) = (bar2|12)")
    b_test = ('0', '2b1'); expected = ('b2', '12')
    print(f"  R1 result: tilde-B_1 B_2 B_1 ({at_fmt(b_test)}) = {at_fmt(r1_results[b_test])}")
    pi_test = embed[b_test]
    r_pi = braid_kp(pi_test)
    proj = inv_embed.get(kp_freeze(r_pi)) if r_pi else None
    print(f"  R2 result: braid_kp(pi) = {kp_repr(r_pi) if r_pi else 'None'}, project = {at_fmt(proj)}")
    print(f"  AT predicts                                       = {at_fmt(expected)}")
    print(f"  R1 verdict: {'AGREE' if r1_results[b_test] == expected else 'DISAGREE'}")
    print(f"  R2 verdict: {'AGREE' if proj == expected else 'DISAGREE'}")


if __name__ == '__main__':
    main()
