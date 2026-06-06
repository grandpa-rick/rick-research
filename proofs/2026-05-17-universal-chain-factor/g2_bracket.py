"""
G_2 bracket / crystal verifier for the universal chain factor conjecture at m=3.

Setup:
  G_2 positive roots (Bourbaki, alpha_1 short, alpha_2 long, a_{12}=-1, a_{21}=-3):
    alpha_1                short, pairing  <., alpha_1^v> = +2  (singleton)
    alpha_2                long,  pairing -3   (bot of chain)
    alpha_2 + alpha_1      short, pairing -1   (low-mid)
    alpha_2 + 2 alpha_1    short, pairing +1   (hi-mid)
    alpha_2 + 3 alpha_1    long,  pairing +3   (top of chain)
    3 alpha_1 + 2 alpha_2  long,  pairing  0   (fixed singleton, no contribution)

Chain through alpha_2 has length 4 (m=3).

We test two proposed bracket layouts for the chain block:

LAYOUT_NESTED (my proposal, length-(m+1) generalization of B_n mid-framing):
    interior closers (chain order: low-mid then hi-mid):  )^{c_1} )^{2 c_2}
    bot openers:                                          (^{3 c_0}
    top closers:                                          )^{3 c_3}
    interior openers (REVERSE chain order):               (^{c_2} (^{2 c_1}
    singleton alpha_1:                                    )^S

LAYOUT_NAIVE (simple chain order, per-copy signature concatenation):
    chain: prod_{k=0..3} (per-copy signature of beta_k)^{c_k}
           = (^{3 c_0} [each copy of beta_1 = )(( ] [each copy of beta_2 = ))( ] )^{3 c_3}

We then check crystal axioms:
  (A1) eps(e_i x) = eps(x) - 1 when eps(x) >= 1
  (A2) phi(f_i x) = phi(x) - 1 when phi(x) >= 1
  (A3) e_i f_i x = x always
  (A4) f_i e_i x = x when e_i x != 0
"""

from typing import Dict, Tuple, Optional, List

# G_2 positive root labels
S0 = 'a1'         # alpha_1 = short simple, singleton at alpha_1-action, pairing +2
B0 = 'a2'         # alpha_2, bot of chain, pairing -3
B1 = 'a2_a1'      # alpha_2 + alpha_1, low-mid, pairing -1
B2 = 'a2_2a1'     # alpha_2 + 2 alpha_1, hi-mid, pairing +1
B3 = 'a2_3a1'     # alpha_2 + 3 alpha_1, top, pairing +3
FX = '3a1_2a2'    # 3 alpha_1 + 2 alpha_2, fixed singleton, pairing 0

ROOTS = [S0, B0, B1, B2, B3, FX]
CHAIN = [B0, B1, B2, B3]
# Coefficients of (alpha_1, alpha_2) for each root
ROOT_AB = {
    S0: (1, 0),
    B0: (0, 1),
    B1: (1, 1),
    B2: (2, 1),
    B3: (3, 1),
    FX: (3, 2),
}
# Pairing with alpha_1^v (alpha_1 is short, alpha_1^v = alpha_1)
# <a alpha_1 + b alpha_2, alpha_1^v> = 2a - 3b
PAIRING_A1 = {r: 2 * ab[0] - 3 * ab[1] for r, ab in ROOT_AB.items()}

assert PAIRING_A1[S0] == 2
assert PAIRING_A1[B0] == -3
assert PAIRING_A1[B1] == -1
assert PAIRING_A1[B2] == 1
assert PAIRING_A1[B3] == 3
assert PAIRING_A1[FX] == 0

KP = Dict[str, int]


def kp_clean(pi: KP) -> KP:
    return {r: c for r, c in pi.items() if c}


def kp_add(pi: KP, root: str, delta: int) -> KP:
    out = dict(pi)
    out[root] = out.get(root, 0) + delta
    if out[root] == 0:
        del out[root]
    return out


def kp_repr(pi: KP) -> str:
    pi = kp_clean(pi)
    if not pi:
        return '<vacuum>'
    return ' + '.join(f'{c}*{r}' for r, c in sorted(pi.items()))


def root_minus_alpha1(beta):
    """beta - alpha_1.  Returns root name or None if not in Phi^+ (incl. 0)."""
    return {S0: None,  # alpha_1 - alpha_1 = 0 -> remove copy (return None)
            B0: None,  # alpha_2 - alpha_1 not in Phi^+
            B1: B0,    # (alpha_2 + alpha_1) - alpha_1 = alpha_2
            B2: B1,
            B3: B2,
            FX: None,  # 3 alpha_1 + 2 alpha_2 - alpha_1 = 2 alpha_1 + 2 alpha_2 not in Phi^+
            }[beta]


def root_plus_alpha1(beta):
    """beta + alpha_1.  Returns root name or None if not in Phi^+."""
    return {S0: None,  # 2 alpha_1 not a root
            B0: B1,    # alpha_2 + alpha_1
            B1: B2,
            B2: B3,
            B3: None,  # alpha_2 + 4 alpha_1 not a root
            FX: None,  # 4 alpha_1 + 2 alpha_2 not a root
            }[beta]


# ============================================================
# Layout: NESTED (my conjectured universal chain factor)
# ============================================================

def S_1_nested(pi: KP) -> List[Tuple[str, str]]:
    """Bracket sequence for G_2 at alpha_1-action, NESTED layout."""
    c0, c1, c2, c3 = pi.get(B0, 0), pi.get(B1, 0), pi.get(B2, 0), pi.get(B3, 0)
    cS = pi.get(S0, 0)
    s = []
    # Interior closers: chain order (low-mid then hi-mid)
    for _ in range(1 * c1):
        s.append((')', B1))
    for _ in range(2 * c2):
        s.append((')', B2))
    # Bot openers
    for _ in range(3 * c0):
        s.append(('(', B0))
    # Top closers
    for _ in range(3 * c3):
        s.append((')', B3))
    # Interior openers: REVERSE chain order (hi-mid then low-mid)
    for _ in range(1 * c2):
        s.append(('(', B2))
    for _ in range(2 * c1):
        s.append(('(', B1))
    # Singleton alpha_1 closer
    for _ in range(cS):
        s.append((')', S0))
    return s


# ============================================================
# Layout: NAIVE chain-order per-copy signature concatenation
# ============================================================

def S_1_naive(pi: KP) -> List[Tuple[str, str]]:
    """Per-copy signature concatenation, chain order bot -> top."""
    c0, c1, c2, c3 = pi.get(B0, 0), pi.get(B1, 0), pi.get(B2, 0), pi.get(B3, 0)
    cS = pi.get(S0, 0)
    s = []
    # bot: 3 openers per copy
    for _ in range(c0):
        for _ in range(3):
            s.append(('(', B0))
    # low-mid: per copy )((
    for _ in range(c1):
        s.append((')', B1))
        for _ in range(2):
            s.append(('(', B1))
    # hi-mid: per copy ))(
    for _ in range(c2):
        for _ in range(2):
            s.append((')', B2))
        s.append(('(', B2))
    # top: 3 closers per copy
    for _ in range(c3):
        for _ in range(3):
            s.append((')', B3))
    # singleton
    for _ in range(cS):
        s.append((')', S0))
    return s


# ============================================================
# Cancellation and crystal operators
# ============================================================

def cancel(s: list) -> list:
    s = list(s)
    while True:
        for k in range(len(s) - 1):
            if s[k][0] == '(' and s[k + 1][0] == ')':
                del s[k:k + 2]
                break
        else:
            return s


def eps(pi, layout):
    sc = cancel(layout(pi))
    return sum(1 for c, _ in sc if c == ')')


def phi(pi, layout):
    sc = cancel(layout(pi))
    return sum(1 for c, _ in sc if c == '(')


def e_op(pi, layout):
    """e_1 via rightmost ')' in cancelled bracket."""
    pi = kp_clean(pi)
    sc = cancel(layout(pi))
    rightmost_close = None
    for k in range(len(sc) - 1, -1, -1):
        if sc[k][0] == ')':
            rightmost_close = sc[k]
            break
    if rightmost_close is None:
        return None
    beta = rightmost_close[1]
    new_root = root_minus_alpha1(beta)
    out = kp_add(pi, beta, -1)
    if new_root is not None:
        out = kp_add(out, new_root, +1)
    return kp_clean(out)


def f_op(pi, layout):
    """f_1 via leftmost '(' in cancelled bracket. If no '(', append simple root alpha_1."""
    pi = kp_clean(pi)
    sc = cancel(layout(pi))
    leftmost_open = None
    for tok in sc:
        if tok[0] == '(':
            leftmost_open = tok
            break
    if leftmost_open is None:
        return kp_clean(kp_add(pi, S0, +1))
    beta = leftmost_open[1]
    new_root = root_plus_alpha1(beta)
    out = kp_add(pi, beta, -1)
    if new_root is not None:
        out = kp_add(out, new_root, +1)
    return kp_clean(out)


def weight_alpha1(pi):
    """<pi, alpha_1^v> = sum c_beta * pairing(beta)."""
    return sum(c * PAIRING_A1[r] for r, c in pi.items())


# ============================================================
# Enumeration
# ============================================================

def enumerate_partitions(max_total):
    """Enumerate Kostant partitions with total height bounded by max_total.
    Don't include FX (no contribution to alpha_1-action; just adds free param)."""
    out = []
    # Encode multiplicities (cS, c0, c1, c2, c3)
    for cS in range(max_total + 1):
        for c0 in range(max_total + 1 - cS):
            for c1 in range(max_total + 1 - cS - c0):
                for c2 in range(max_total + 1 - cS - c0 - c1):
                    for c3 in range(max_total + 1 - cS - c0 - c1 - c2):
                        pi = {}
                        if cS: pi[S0] = cS
                        if c0: pi[B0] = c0
                        if c1: pi[B1] = c1
                        if c2: pi[B2] = c2
                        if c3: pi[B3] = c3
                        out.append(pi)
    return out


# ============================================================
# Tests
# ============================================================

def test_layout(layout_name, layout, max_total=4):
    print(f"\n=== {layout_name} ===\n")

    n_total = 0
    fails_weight = []
    fails_ef = []      # e_i f_i = id
    fails_fe = []      # f_i e_i = id on slice
    fails_eps_drop = []  # eps(e_i x) = eps(x) - 1

    for pi in enumerate_partitions(max_total):
        n_total += 1
        e = eps(pi, layout)
        p = phi(pi, layout)
        w = weight_alpha1(pi)
        # Check phi - eps = -<pi, alpha_1^v>
        if p - e != -w:
            fails_weight.append((pi, e, p, w))

        # e_i f_i = id
        f_pi = f_op(pi, layout)
        e_f_pi = e_op(f_pi, layout)
        if e_f_pi != kp_clean(pi):
            fails_ef.append((pi, f_pi, e_f_pi))

        # f_i e_i = id when e_i pi != None
        e_pi = e_op(pi, layout)
        if e_pi is not None:
            f_e_pi = f_op(e_pi, layout)
            if f_e_pi != kp_clean(pi):
                fails_fe.append((pi, e_pi, f_e_pi))
            # eps(e_i pi) = eps(pi) - 1
            new_eps = eps(e_pi, layout)
            if new_eps != e - 1:
                fails_eps_drop.append((pi, e, e_pi, new_eps))

    print(f"  Tested {n_total} partitions.")
    print(f"  weight axiom phi-eps=-<pi,alpha^v>: {n_total - len(fails_weight)}/{n_total} OK")
    if fails_weight:
        print(f"    FAILURES (first 5):")
        for pi, e, p, w in fails_weight[:5]:
            print(f"      pi = {kp_repr(pi)}: eps={e}, phi={p}, weight={w}")

    print(f"  e_i f_i = id: {n_total - len(fails_ef)}/{n_total} OK")
    if fails_ef:
        print(f"    FAILURES (first 5):")
        for pi, fp, efp in fails_ef[:5]:
            print(f"      pi = {kp_repr(pi)}: f_i pi = {kp_repr(fp)}, e_i f_i pi = {kp_repr(efp)}")

    print(f"  f_i e_i = id on slice: {len([1 for pi in enumerate_partitions(max_total) if e_op(pi, layout) is not None]) - len(fails_fe)} of {len([1 for pi in enumerate_partitions(max_total) if e_op(pi, layout) is not None])} OK")
    if fails_fe:
        print(f"    FAILURES (first 5):")
        for pi, ep, fep in fails_fe[:5]:
            print(f"      pi = {kp_repr(pi)}: e_i pi = {kp_repr(ep)}, f_i e_i pi = {kp_repr(fep)}")

    n_eps_slice = len([1 for pi in enumerate_partitions(max_total) if eps(pi, layout) >= 1])
    print(f"  eps(e_i pi) = eps(pi) - 1: {n_eps_slice - len(fails_eps_drop)}/{n_eps_slice} OK")
    if fails_eps_drop:
        print(f"    FAILURES (first 5):")
        for pi, e0, ep, e1 in fails_eps_drop[:5]:
            print(f"      pi = {kp_repr(pi)}: eps={e0}, e_i pi = {kp_repr(ep)}, eps(e_i pi) = {e1}")


# ============================================================
# Layout: TOP-CLOSERS-LAST (Watanabe-style: closers first all together, then openers)
# ============================================================

def S_1_closers_first(pi: KP) -> List[Tuple[str, str]]:
    """All closers in chain order, then all openers in chain order."""
    c0, c1, c2, c3 = pi.get(B0, 0), pi.get(B1, 0), pi.get(B2, 0), pi.get(B3, 0)
    cS = pi.get(S0, 0)
    s = []
    # All closers in chain order
    for _ in range(1 * c1):
        s.append((')', B1))
    for _ in range(2 * c2):
        s.append((')', B2))
    for _ in range(3 * c3):
        s.append((')', B3))
    # All openers in chain order
    for _ in range(3 * c0):
        s.append(('(', B0))
    for _ in range(2 * c1):
        s.append(('(', B1))
    for _ in range(1 * c2):
        s.append(('(', B2))
    # Singleton alpha_1
    for _ in range(cS):
        s.append((')', S0))
    return s


# ============================================================
# Layout: PER-COPY, chain order (each copy of beta_k contributes )^k (^{m-k} individually)
# ============================================================

def S_1_per_copy(pi: KP) -> List[Tuple[str, str]]:
    c0, c1, c2, c3 = pi.get(B0, 0), pi.get(B1, 0), pi.get(B2, 0), pi.get(B3, 0)
    cS = pi.get(S0, 0)
    s = []
    for _ in range(c0):
        for _ in range(3): s.append(('(', B0))
    for _ in range(c1):
        s.append((')', B1))
        for _ in range(2): s.append(('(', B1))
    for _ in range(c2):
        for _ in range(2): s.append((')', B2))
        s.append(('(', B2))
    for _ in range(c3):
        for _ in range(3): s.append((')', B3))
    for _ in range(cS):
        s.append((')', S0))
    return s


# ============================================================
# Layout: NESTED with bot-openers swapped with interior-closers (?)
# Put interior openers ADJACENT to top closers, to allow cancellation
# ============================================================

def S_1_nested_v2(pi: KP) -> List[Tuple[str, str]]:
    """Variation: interior openers come BEFORE top closers, not after."""
    c0, c1, c2, c3 = pi.get(B0, 0), pi.get(B1, 0), pi.get(B2, 0), pi.get(B3, 0)
    cS = pi.get(S0, 0)
    s = []
    # Interior closers (chain order)
    for _ in range(1 * c1):
        s.append((')', B1))
    for _ in range(2 * c2):
        s.append((')', B2))
    # Bot openers
    for _ in range(3 * c0):
        s.append(('(', B0))
    # Interior openers (reverse chain order)
    for _ in range(1 * c2):
        s.append(('(', B2))
    for _ in range(2 * c1):
        s.append(('(', B1))
    # Top closers
    for _ in range(3 * c3):
        s.append((')', B3))
    # Singleton
    for _ in range(cS):
        s.append((')', S0))
    return s


# ============================================================
# Layout: REVERSE chain order, each block = closers-then-openers
# This mimics Kashiwara signature for tensor products: rightmost factor first
# ============================================================

def S_1_nested_v3(pi: KP) -> List[Tuple[str, str]]:
    """Interior closers AFTER top closers; mirror-nested in interior openers.
    closers in chain order pre-top: low-mid. closers post-top: hi-mid then top?
    Actually: try ALL interior closers AFTER top."""
    c0, c1, c2, c3 = pi.get(B0, 0), pi.get(B1, 0), pi.get(B2, 0), pi.get(B3, 0)
    cS = pi.get(S0, 0)
    s = []
    # Bot openers leading
    for _ in range(3 * c0):
        s.append(('(', B0))
    # Top closers
    for _ in range(3 * c3):
        s.append((')', B3))
    # Hi-mid closers
    for _ in range(2 * c2):
        s.append((')', B2))
    # Low-mid closer
    for _ in range(1 * c1):
        s.append((')', B1))
    # Low-mid openers
    for _ in range(2 * c1):
        s.append(('(', B1))
    # Hi-mid opener
    for _ in range(1 * c2):
        s.append(('(', B2))
    # Singleton closer
    for _ in range(cS):
        s.append((')', S0))
    return s


def S_1_per_root_grouped(pi: KP) -> List[Tuple[str, str]]:
    """Each chain root contributes its closer-then-opener block IN PLACE in chain order.
    This is the layout that allows beta_1's brackets to potentially cancel.
    Order: beta_1's closers+openers as one block, then beta_2's, then beta_3 closers, then beta_0 openers, singleton."""
    c0, c1, c2, c3 = pi.get(B0, 0), pi.get(B1, 0), pi.get(B2, 0), pi.get(B3, 0)
    cS = pi.get(S0, 0)
    s = []
    # beta_1 block: closer then openers
    for _ in range(1 * c1):
        s.append((')', B1))
    for _ in range(2 * c1):
        s.append(('(', B1))
    # beta_2 block: closers then opener
    for _ in range(2 * c2):
        s.append((')', B2))
    for _ in range(1 * c2):
        s.append(('(', B2))
    # beta_3 closers
    for _ in range(3 * c3):
        s.append((')', B3))
    # beta_0 openers
    for _ in range(3 * c0):
        s.append(('(', B0))
    # singleton
    for _ in range(cS):
        s.append((')', S0))
    return s


def S_1_split_v1(pi: KP) -> List[Tuple[str, str]]:
    """For each chain root, place ALL its brackets together (closer block then opener block).
    Order chain roots from extreme to interior to match B_n's mid-framing intuition:
    bot -> top -> hi-mid -> low-mid (innermost last).
    """
    c0, c1, c2, c3 = pi.get(B0, 0), pi.get(B1, 0), pi.get(B2, 0), pi.get(B3, 0)
    cS = pi.get(S0, 0)
    s = []
    # bot block: only openers
    for _ in range(3 * c0):
        s.append(('(', B0))
    # top block: only closers
    for _ in range(3 * c3):
        s.append((')', B3))
    # hi-mid block: closers then openers
    for _ in range(2 * c2):
        s.append((')', B2))
    for _ in range(1 * c2):
        s.append(('(', B2))
    # low-mid block: closer then openers
    for _ in range(1 * c1):
        s.append((')', B1))
    for _ in range(2 * c1):
        s.append(('(', B1))
    for _ in range(cS):
        s.append((')', S0))
    return s


def S_1_top_leading(pi: KP) -> List[Tuple[str, str]]:
    """Top closers FIRST, then interior closers (chain order), then openers."""
    c0, c1, c2, c3 = pi.get(B0, 0), pi.get(B1, 0), pi.get(B2, 0), pi.get(B3, 0)
    cS = pi.get(S0, 0)
    s = []
    # Top closers first
    for _ in range(3 * c3):
        s.append((')', B3))
    # Hi-mid closers
    for _ in range(2 * c2):
        s.append((')', B2))
    # Low-mid closer
    for _ in range(1 * c1):
        s.append((')', B1))
    # Bot openers
    for _ in range(3 * c0):
        s.append(('(', B0))
    # Hi-mid opener
    for _ in range(1 * c2):
        s.append(('(', B2))
    # Low-mid openers
    for _ in range(2 * c1):
        s.append(('(', B1))
    # Singleton
    for _ in range(cS):
        s.append((')', S0))
    return s


def S_1_reverse(pi: KP) -> List[Tuple[str, str]]:
    c0, c1, c2, c3 = pi.get(B0, 0), pi.get(B1, 0), pi.get(B2, 0), pi.get(B3, 0)
    cS = pi.get(S0, 0)
    s = []
    # beta_3 block: just closers (top of chain)
    for _ in range(3 * c3):
        s.append((')', B3))
    # beta_2 block: closers then openers
    for _ in range(2 * c2):
        s.append((')', B2))
    for _ in range(1 * c2):
        s.append(('(', B2))
    # beta_1 block: closer then openers
    for _ in range(1 * c1):
        s.append((')', B1))
    for _ in range(2 * c1):
        s.append(('(', B1))
    # beta_0 block: just openers (bot of chain)
    for _ in range(3 * c0):
        s.append(('(', B0))
    # singleton
    for _ in range(cS):
        s.append((')', S0))
    return s


# ============================================================
# Tester wrapper to handle None efp
# ============================================================

def test_layout_safe(layout_name, layout, max_total=3):
    print(f"\n=== {layout_name} ===\n")
    n_total = 0
    fails_ef = []
    fails_fe = []
    fails_eps_drop = []
    parts = enumerate_partitions(max_total)
    for pi in parts:
        n_total += 1
        e = eps(pi, layout)
        # e_i f_i = id
        f_pi = f_op(pi, layout)
        e_f_pi = e_op(f_pi, layout)
        if e_f_pi is None or e_f_pi != kp_clean(pi):
            fails_ef.append((pi, f_pi, e_f_pi))
        # f_i e_i = id when e_i pi != None
        e_pi = e_op(pi, layout)
        if e_pi is not None:
            f_e_pi = f_op(e_pi, layout)
            if f_e_pi != kp_clean(pi):
                fails_fe.append((pi, e_pi, f_e_pi))
            new_eps = eps(e_pi, layout)
            if new_eps != e - 1:
                fails_eps_drop.append((pi, e, e_pi, new_eps))

    n_eslice = len([1 for pi in parts if e_op(pi, layout) is not None])
    print(f"  Tested {n_total} partitions; e_i-slice {n_eslice}.")
    print(f"  e_i f_i = id:           {n_total - len(fails_ef)}/{n_total}")
    print(f"  f_i e_i = id on slice:  {n_eslice - len(fails_fe)}/{n_eslice}")
    print(f"  eps(e_i x) = eps(x)-1:  {n_eslice - len(fails_eps_drop)}/{n_eslice}")
    if fails_ef:
        print(f"  e_i f_i failures (first 5):")
        for pi, fp, efp in fails_ef[:5]:
            efp_repr = kp_repr(efp) if efp is not None else 'None'
            print(f"      pi={kp_repr(pi)}, f_i pi={kp_repr(fp)}, e_i f_i pi={efp_repr}")
    if fails_fe:
        print(f"  f_i e_i failures (first 5):")
        for pi, ep, fep in fails_fe[:5]:
            print(f"      pi={kp_repr(pi)}, e_i pi={kp_repr(ep)}, f_i e_i pi={kp_repr(fep)}")


if __name__ == '__main__':
    print("=" * 75)
    print("G_2 bracket layout verification, alpha_1-action")
    print("=" * 75)
    test_layout_safe("LAYOUT_NESTED", S_1_nested, max_total=4)
    test_layout_safe("LAYOUT_CLOSERS_FIRST", S_1_closers_first, max_total=4)
    test_layout_safe("LAYOUT_PER_COPY", S_1_per_copy, max_total=4)
    test_layout_safe("LAYOUT_NESTED_V2", S_1_nested_v2, max_total=4)
    test_layout_safe("LAYOUT_REVERSE (chain top-to-bot, closers-then-openers per block)", S_1_reverse, max_total=4)
    test_layout_safe("LAYOUT_TOP_LEADING (top closers first, then interior closers, then openers)", S_1_top_leading, max_total=4)
    test_layout_safe("LAYOUT_NESTED_V3 (interior closers AFTER top)", S_1_nested_v3, max_total=4)
    test_layout_safe("LAYOUT_SPLIT_V1 (bot, top, hi-mid block, low-mid block)", S_1_split_v1, max_total=4)
    test_layout_safe("LAYOUT_PER_ROOT_GROUPED (each root: closer then opener, in chain order)", S_1_per_root_grouped, max_total=4)
