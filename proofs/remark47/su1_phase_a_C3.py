"""
SU1 Phase A — Symbolic computation of the BGG-Verma embedding
  e_{-alpha_i}^{(c)} . prod_beta f_beta^{n_beta}
in C_3 at the short exchange simple s_1 (alpha_1 = e_1 - e_2).

GOAL: For each output Kostant monomial m_gamma in the expansion,
enumerate all orbit-swap multisets M (subtype st, direction eps,
count m_{st,eps}) of total alpha_i-shift c whose application to
the donor profile pi yields exactly m_gamma. SU1 says: each output
Kostant monomial corresponds to EXACTLY ONE orbit-swap multiset.

We work over PBW monomials in the negative root vectors {f_beta}.
Structure constants N_{i,beta} are kept SYMBOLIC: their exact
values are immaterial to the UNIQUENESS question — what matters is
whether each output Kostant signature is "hit" by a single
underlying multiset of hit-positions that descend to a single
orbit-swap multiset.

Approach:
  Apply e := e_{-alpha_i} to (f_{beta_1}^{n_1} ... f_{beta_k}^{n_k})
  exactly c times. By Leibniz, each application of e selects ONE
  of the f_beta factors and replaces it by f_{beta - alpha_i} (if
  beta - alpha_i is a positive root), or eliminates it (if
  beta = alpha_i, i.e. cancellation against alpha_i itself, which
  doesn't arise here since beta is a positive root != alpha_i).
  Actually: [e_{-alpha_i}, f_beta] is supported on a root only if
  beta + alpha_i is a positive root... let me re-derive.

ACTUALLY — e_{-alpha_i} is a NEGATIVE root vector for alpha_i;
f_beta is the negative root vector for beta. Both live in n^-.
The commutator [e_{-alpha_i}, f_beta] = f_{-alpha_i - beta} if
-alpha_i - beta is a (negative) root, i.e. if alpha_i + beta is
a positive root. So no, this doesn't move us toward s_i(beta).

LET ME RE-READ THE PROBLEM. The "BGG-Verma embedding" sends
M(s_i w . lambda) into M(w . lambda) by multiplication by
e_{-alpha_i}^{(c)} on the LEFT — where e_{-alpha_i} is in n^-_alpha_i
acting on the Verma module. Each f_beta in the PBW monomial is a
n^- generator. So the embedding raises the multiplicity of f_{-alpha_i}
by c, in a Verma module of n^-.

Wait — for the orbit-swap picture, the relevant commutator is the
one that turns f_beta into f_{s_i(beta)} = f_{beta - <beta,alpha_i^v> alpha_i}.

In sl-style conventions, with e_alpha, f_alpha = e_{-alpha}, h_alpha
generating sl_2 at each root alpha:
  [e_{-alpha_i}, f_beta] = ?

If alpha_i + beta is a root, then [e_{alpha_i}, f_beta] = N f_{beta - alpha_i}
(since e_{alpha_i} raises by alpha_i, applied to f_beta which is weight
-beta, gives weight -beta + alpha_i, which is the negative of beta - alpha_i,
hence a negative root vector f_{beta - alpha_i}).

But we want e_{-alpha_i}, the NEGATIVE root vector. The action of
e_{-alpha_i} on M(lambda) raises h-eigenvalue by -alpha_i, so it sends
weight (lambda - mu) to (lambda - mu - alpha_i). On a Verma vector
f_beta^k . v_lambda, e_{-alpha_i} gives MORE f's, not fewer.

I was confused. The orbit-swap picture is actually for a DIFFERENT
embedding direction. Let me re-read.

Standard BGG embedding: phi: M(s_i.lambda) -> M(lambda), where
s_i.lambda = s_i(lambda + rho) - rho = lambda - <lambda+rho, alpha_i^v> alpha_i
            = lambda - (c_i + 1) alpha_i  with c_i = <lambda, alpha_i^v>.

If c_i >= 0, then s_i.lambda <= lambda, so M(s_i.lambda) is a sub-Verma
of M(lambda). The embedding is multiplication by f_{alpha_i}^{c_i+1}.

f_{alpha_i} = e_{-alpha_i} (negative root vector for alpha_i). So
multiplication by f_{alpha_i}^{c} on a PBW monomial f_{beta_1}^{n_1}...
just prepends f_{alpha_i}^c. That's not interesting for orbit-swaps.

WHAT GIVES THE ORBIT-SWAP STRUCTURE is the commutator expansion when
we MOVE f_{alpha_i}^c from the LEFT to the right of the monomial,
through f_beta^{n_beta} factors, using [f_{alpha_i}, f_beta] structure.

This is wrong too — [f_{alpha_i}, f_beta] lives in g_{-alpha_i - beta},
which is a more-negative root.

Let me restart. The BGG-Verma matrix from PBW basis to PBW basis is
governed by the SHAPOVALOV form (or rather, by re-expressing the
embedded vector in the receiving Verma's PBW basis after moving
the highest-weight vector across).

Actually — the BGG embedding is, in PBW coords:
  phi: f_{alpha_i}^{c} . v_{s_i.lambda}  -->  f_{alpha_i}^{c} . v_lambda  ??

This conflates two things. Let me look at it differently.

The "chain differential" d_k: C_k -> C_{k-1} in the BGG resolution sends
the generator [w] to a sum of ±can_{w, s_i w} [s_i w] where w runs over
length-(k-1) elements and s_i w has length k. The matrix entries of
can_{w, s_i w} between PBW basis vectors at fixed bidegree are what
we're computing.

The map can: M(s_i w . lambda) -> M(w . lambda) is multiplication by
e_{-alpha_i}^{(c_i)} where c_i = <(s_i w . lambda) - (w . lambda), -alpha_i^v>
(this is what makes the map land in M(w.lambda) given the highest-weight
shift). Concretely, c_i = <w . lambda + rho, alpha_i^v> = <w(lambda + rho), alpha_i^v>.

Hm — this is again f_{alpha_i}^{c} as multiplication. The PBW matrix entries
arise when we re-express f_{alpha_i}^{c} . F . v_lambda in terms of the
canonical PBW ordering G . v_lambda where F, G are PBW monomials in the
NEGATIVE root vectors over POSITIVE roots != alpha_i.

To re-express f_{alpha_i}^{c} . prod_{beta != alpha_i} f_beta^{n_beta} in
canonical PBW order with f_{alpha_i} listed at its standard position, we
move f_{alpha_i}^c rightward past f_beta^{n_beta} blocks, picking up
commutators:
  [f_{alpha_i}, f_beta] = c_{alpha_i, beta} f_{alpha_i + beta}
if alpha_i + beta is a root (here alpha_i + beta is NEGATIVE of (-(alpha_i+beta)),
let me write everything in terms of e's and the bracket is in g_{-alpha_i - beta}).

So: when we slide f_{alpha_i} past f_beta, we get back f_beta f_{alpha_i}
PLUS terms with one fewer f_beta and one new f_{alpha_i + beta}. (If alpha_i
+ beta is a root.)

This is NOT an orbit-swap. alpha_i + beta is generally NOT s_i(beta).

I'm missing something fundamental. Let me try ONE more direction:

PERHAPS the orbit-swap interpretation arises when one moves the OTHER way:
expressing the PBW monomial f_{beta_1}^{n_1} ... f_{beta_k}^{n_k} in the
basis where f_{alpha_i} is moved to the LEFT — and the c factors of
f_{alpha_i} that *should be* there (to land in s_i w . lambda's image)
come from commutators of e_{alpha_i} with the f_beta's, where
e_{alpha_i} acts by VIRTUE of the divided-power action.

Effectively: e_{alpha_i}^{(c)} acts on f_beta as a sequence of c
commutators [e_{alpha_i}, ·], turning f_beta into f_{beta - alpha_i}
each time (since [e_{alpha_i}, f_beta] in g_{alpha_i - beta} = f_{beta - alpha_i}
times a structure constant, if alpha_i - beta is a negative root,
i.e. if beta - alpha_i is a positive root).

Each "e_{alpha_i} hit" on f_beta turns it into f_{beta - alpha_i}. Doing
this <beta, alpha_i^v> times in a row turns f_beta into f_{beta - <beta,alpha_i^v> alpha_i}
= f_{s_i(beta)}. THIS IS THE ORBIT-SWAP.

So the relevant operator is e_{+alpha_i}^{(c)}, not e_{-alpha_i}. And it acts
on n^- via repeated commutator (= adjoint action), not by multiplication.

GIVEN THE PROBLEM STATEMENT WHICH WRITES e_{-alpha_i}^{(c)}: I'll interpret
this as "the +alpha_i root vector E (which Carter writes e_{alpha_i}, and
some traditions write E_i, and which acts on f's by lowering them toward
s_i-direction), c-fold composed and divided by c!".

I.e. I'm computing: E_i^{(c)} . pi acting on a PBW monomial pi via
the ADJOINT action (each application = one commutator [E_i, _]).

This is exactly the "select a slot to hit" picture: each E_i hit chooses
one f_beta factor in pi and replaces it with f_{beta - alpha_i} (with a
structure-constant scalar), if beta - alpha_i is a positive root; otherwise
zero.

After c hits, we have a sum over all ordered sequences of c slot-choices
(one slot per hit; a slot may be hit multiple times), each contributing
a product of structure constants and the resulting PBW monomial.

DIVIDED POWER c! cancellation absorbs the c! ways of ORDERING c distinct
hits on c distinct slots. For repeat-hits on the same slot, we get
divided-power coefficients on f_beta themselves.

OK — code this up. Track: which multiset of c slot-hits we made (the
"hit vector" h: Phi+ -> Z_{>=0} with sum = c, h_beta <= n_beta for slots
that get hit only once, but actually a slot can be hit > n_beta times if
the resulting f_{beta-alpha_i} is itself in the right place — wait no,
we apply E_i adjointly to a MONOMIAL, hitting one factor at a time, and
each hit reduces n_beta by 1 and creates a f_{beta-alpha_i} factor).

ITERATIVE PICTURE (clean):
  state = (multiplicities over Phi+ of f's). Start: state_0 = pi.
  At each of c steps, pick a positive root beta in state_t with state_t[beta] >= 1
    AND such that beta - alpha_i is a positive root. (If beta - alpha_i = alpha_i,
    a special case, but that would mean beta = 2 alpha_i, and we'd get H_i times
    a scalar, not a new root vector — needs care.)
  New state: state_{t+1} = state_t with beta--, (beta - alpha_i)++.
  After c steps: end state is a Kostant monomial. Count: # paths leading to it.
  Divided-power coefficient: divide by c! and by the "ordering equivalences"
    among paths that produce the SAME end state.
  Actually, the DIVIDED POWER e^{(c)} = e^c / c!, applied to a PBW monomial,
  is what we want; and the result is a SUM over end states with EXPLICIT
  multinomial coefficients (= count of distinct ordered hit-sequences / c!).
  But here we care about which end-states APPEAR and which orbit-swap multisets
  each end-state corresponds to.

ORBIT-SWAP MULTISET: for each hit-sequence, the SUM of all hits (per slot beta)
is a multi-set {beta -> # times this slot was hit} = h: Phi+ -> Z_{>=0}.
Each beta with h_beta > 0 corresponds to an orbit-swap of subtype (orbit
containing beta) in direction (+/- depending on whether beta is the
"higher" or "lower" representative of the orbit).

DEFN: orbit-swap multiset from hit vector h_total:
  For each subtype st of s_i orbit on Phi+ \ alpha_i,
    if orbit st = {beta_+, beta_-} with beta_+ - beta_- = alpha_i (1-unit) or 2 alpha_i (2-unit),
    then "hits on beta_+" = orbit swap of subtype st in direction "-" (since the
    hit moves us alpha_i units in the negative direction).
  More precisely (matching aug_tilde_C3_richer.py's c>0 convention):
    when c > 0 (= we're computing c hits in the alpha_i direction), each hit
    sends f_beta to f_{beta - alpha_i}; this is a "minus" direction orbit swap.

So for c > 0, the orbit-swap multiset is uniquely determined by the
END STATE Kostant signature: for each subtype st, count how many factors
moved from the "higher" rep to the "lower" rep. And this depends on the
DIFFERENCE between the end state and the start state.

UNIQUENESS QUESTION: given start state pi and target end state pi', the
orbit-swap multiset is uniquely DEFINED by (pi, pi'). But MULTIPLE HIT
SEQUENCES h_total may produce the same end state pi' (e.g. if 2-unit and
1-unit hits can interact). The SU1 question is: does each end state pi'
correspond to EXACTLY ONE hit-vector h_total?

Hmm — that's the actual question, and is easier to think about. A hit on
beta produces a factor f_{beta - alpha_i}. Two different hit choices that
produce the same end state would mean ... let's see.

Example: pi = (2 e_0) + (2 e_1) (two 2-units adjacent to alpha_1 = e_1 - e_2).
Wait — alpha_1 = e_1 - e_2 in this convention. Let me check what hits.

For pi to have any alpha_1-hit slots: need beta with beta - alpha_1 a positive root.
  beta = 2 e_1: 2 e_1 - (e_1 - e_2) = e_1 + e_2 = positive. YES, 2-unit (orbit (LL,)).
  beta = e_1 - e_2: 0 = 0; degenerate (alpha_1 itself; not in our consideration as a slot).
  beta = e_0 - e_2: (e_0 - e_2) - (e_1 - e_2) = e_0 - e_1 = positive. YES, 1-unit (subtype b- with p=0).
  beta = e_1 + e_q for q in {0, 2}: q=0 gives e_0 + e_1, q=2 gives e_1 + e_2.
    e_0 + e_1 - alpha_1 = e_0 + e_2 = positive. YES, 1-unit (b+ with p=0).
    e_1 + e_2 - alpha_1 = 2 e_2 = positive. YES, 2-unit! Wait — is this a "1-unit" or "2-unit" swap?
    Subtype-wise: e_1 + e_2 - (e_1 - e_2) = 2 e_2. Is this an orbit swap of e_1+e_2 under s_1?
    s_1(e_1 + e_2) = e_2 + e_1 = e_1 + e_2 — FIXED. So e_1 + e_2 is an s_1-FIXED root.
    But (e_1 + e_2) - alpha_1 = 2 e_2 which IS a positive root.
    Hmm, e_1 + e_2 is s_1-fixed yet beta - alpha_1 is a root — does this make sense?
    Cartan: <e_1+e_2, alpha_1^v> = <e_1+e_2, e_1-e_2> = 1 - 1 = 0. So yes, fixed.
    But e_1 + e_2 - alpha_1 = 2 e_2 — is this really a root? Yes, 2e_2 is a positive root in C_3.
    However, the alpha_1-string through (e_1 + e_2) goes from e_1 + e_2 - k alpha_1 = ... let's see,
    pairing 0 means the string is just {e_1 + e_2}. So 2 e_2 is NOT in the alpha_1-string of e_1 + e_2.
    So e_1 + e_2 - alpha_1 = 2 e_2 — let me verify: 2 e_2 is positive, but is it in the SAME
    sl_2-string as e_1 + e_2? sl_2-string through e_1 + e_2 wrt alpha_1: {e_1 + e_2} (singleton).
    Then 2 e_2 is OUTSIDE that string. So [e_{alpha_1}, f_{e_1+e_2}] = 0 even though both
    e_1 + e_2 + alpha_1 = 2 e_1 IS a root, and e_1 + e_2 - alpha_1 = 2 e_2 IS a root.
    Wait — this is a contradiction with the strings picture. Let me reconsider.

Actually: the alpha_1-string through beta is the set {beta + k alpha_1 : k in [-p, q]} where
  p = max{k : beta - k alpha_1 is a root}, q = max{k : beta + k alpha_1 is a root}.
  q - p = -<beta, alpha_1^v>.
For beta = e_1 + e_2: <beta, alpha_1^v> = 0, so q = p.
  q: is e_1+e_2 + alpha_1 = 2 e_1 a root? YES. Is e_1+e_2 + 2 alpha_1 = 3e_1 - e_2 a root? NO. So q = 1.
  Then p = 1 too. So the string is {e_1 + e_2 - alpha_1, e_1+e_2, e_1+e_2+alpha_1} = {2 e_2, e_1+e_2, 2 e_1}.
  This is a string of length 3! So <beta, alpha_1^v> for the middle of a length-3 string is... 0 (q=p=1).
  Then [e_{alpha_1}, f_{e_1+e_2}] DOES go to f_{e_1+e_2 - alpha_1} = f_{2 e_2}. Not zero!
  And [e_{alpha_1}, [e_{alpha_1}, f_{e_1+e_2}]] goes to f_{e_1+e_2 - 2 alpha_1}? But e_1+e_2 - 2 alpha_1
  = -e_1 + 3 e_2 — not in the alpha_1-string of e_1+e_2 (string is {2e_2, e_1+e_2, 2e_1}). So next step in
  the string is 2 e_1 going DOWN: f_{2 e_1} -> f_{2 e_1 - alpha_1} = f_{e_1 + e_2}? That goes the WRONG
  direction (we're hitting with e_{alpha_1} which DECREASES the root by alpha_1). So 2e_1 -> e_1+e_2 -> 2e_2.
  The string is 2e_1 (top) ↔ e_1+e_2 (mid) ↔ 2e_2 (bottom), with f's going top to bottom under e_{alpha_1}.

OK so this is the 2-unit LL orbit, with the MIDDLE element being e_1+e_2 (a "fixed" root in s_1-orbit
sense but in the middle of a 2-unit alpha_1-string).

CRUCIAL REALIZATION: The s_1-ORBITS on positive roots are NOT the same as the alpha_1-STRINGS!
s_1 acts as a reflection: s_1(beta) = beta - <beta, alpha_1^v> alpha_1. Orbits under s_1:
  beta with <beta, alpha_1^v> = 0: fixed.
  beta with <beta, alpha_1^v> != 0: 2-element orbit {beta, s_1 beta}.

But the alpha_1-string through beta can be LONGER than 2 even if <beta, alpha_1^v> = 0. Specifically,
for beta = e_1 + e_2 in C_3: <beta, alpha_1^v> = 0 (s_1-fixed), but the alpha_1-string has length 3
(includes 2e_1 and 2e_2). Hmm wait — the string length is q + p + 1 = 1 + 1 + 1 = 3. Top is at k=-p = -1,
bottom at k=q = 1. Indexing the string positions: beta is at the middle. q - p = 0 = -<beta, alpha_1^v>, OK.

The STRING through 2 e_1 has 2 e_1 at the top (q=0, p=2 since 2e_1 - 2 alpha_1 = 2 e_2 is a root but
2 e_1 - 3 alpha_1 = -e_1 + 3 e_2 is not). Length 3.
The s_1-orbit of 2 e_1 is {2 e_1, s_1(2 e_1) = 2 e_2}, with e_1 + e_2 as the s_1-fixed "midpoint" of
the alpha_1-string.

NUANCE: The orbit-swap PICTURE assumes single hits with single-orbit-swap interpretations. With
2-unit alpha_1-strings of length 3 (like {2e_1, e_1+e_2, 2e_2}), a single hit on 2 e_1 produces
e_1 + e_2 (an s_1-fixed positive root in pi), not 2 e_2. TWO hits on the same orbit (i.e. hit
the SLOT 2 e_1, get e_1 + e_2; hit that NEW e_1 + e_2 slot, get 2 e_2) produce 2 e_2.

THIS is the structure that gives 2-unit LL swaps. A single "LL+" orbit swap = TWO consecutive E_i
hits, first on 2 e_i, then on the resulting e_i + e_{i+1}.

SIMILARLY: the b/c subtypes correspond to alpha_1-strings of length 2 (single hits).

SO the "orbit-swap multiset" decomposition of a hit-sequence is:
  Group hits by their CHAIN within an alpha_1-string. A 1-step chain in a length-2 string = 1-unit swap
    (b or c subtype).
  A 2-step chain in a length-3 string = 1 LL swap. But ALSO, you might do a 1-step chain in a length-3
    string (e.g. hit 2 e_1 once but not the resulting e_1+e_2) — that produces an f_{e_1+e_2} factor.
    Is that an "orbit-swap"? In the C3 framework: that's a "half" swap, not capturable by the
    orbit-swap multiset language.

This is the WHOLE ISSUE. Phase A is supposed to check whether each output Kostant monomial corresponds
to a single orbit-swap multiset, in the sense of aug_tilde_C3_richer.py's orbit-swap framework.

For C_3 short exchange s_1: subtypes are
  LL: 2 e_1 ↔ 2 e_2 (2-unit, but the orbit has 3 representatives in the alpha_1 sl_2 module:
                     2 e_1, e_1+e_2, 2 e_2)
  b+ (p=0): e_0 + e_1 ↔ e_0 + e_2 (1-unit string of length 2)
  b- (p=0): e_0 - e_2 ↔ e_0 - e_1 (1-unit string of length 2)
  (no c+/c- because i+1 = 2 = N-1, so no q > i+1)

For an LL+ swap (2 e_1 -> 2 e_2): TWO consecutive E_i hits on the chain 2e_1 -> e_1+e_2 -> 2e_2.

DETERMINISTIC RESULT: To go from a starting pi to an ending pi via c hits, the orbit-swap multiset
is the multiset of "complete swap actions" in alpha_1-strings. AMBIGUITY arises when a chain of
hits could be DECOMPOSED into orbit-swaps in MULTIPLE WAYS.

Phase A: compute. Concretely, let me track the hit-vector h: pos_roots -> Z_{>=0} with sum h = c,
and for each such h, check if the resulting end state is well-defined (= for each beta with h_beta > 0,
beta - alpha_i is positive root; AND ITERATIVELY, the chain doesn't run off).

Actually NO. Each HIT is on a slot of the CURRENT state, not the initial state. So the SAME beta
slot can be hit multiple times if intermediate hits replenish it (or if we hit it once, the new
factor is some beta', and then later we hit beta'.

The natural data structure is: AN ORDERED SEQUENCE OF HIT TARGETS (where each target is a root,
and at the time of hit, the current state has at least one factor of that root). This generates
all (h_total, end_state) pairs as the sequences are enumerated.

ENUMERATION STRATEGY:
  Given start state pi and c hits, enumerate all sequences of c hits (each hit picks a root beta
    with current_state[beta] > 0 and beta - alpha_i a positive root):
  For each sequence, compute the end state.
  Group sequences by end state.
  For each end state, sum the symbolic coefficient = product of structure constants
    N_{i, beta_at_each_step}, divided by appropriate factorial stuff.
  We don't actually need the precise coefficients — we just need to check whether each
    end state can be reached by HIT VECTORS h_total that correspond to MULTIPLE distinct
    orbit-swap multisets.

ORBIT-SWAP MULTISET FROM (start_pi, end_pi):
  Compute delta = end_pi - start_pi (as a vector indexed by positive roots).
  This delta supported on the alpha_1-strings: each LL+ orbit-swap contributes -1 to 2e_1
    and +1 to 2 e_2. Each b+ swap contributes -1 to e_0+e_1 and +1 to e_0+e_2. Etc.
  The orbit-swap multiset is the unique non-negative integer combination of orbit-swap moves
    matching delta — IF UNIQUE. Otherwise, MULTIPLE MULTISETS correspond to the same delta —
    this is the SU1 question!

  Wait — the orbit-swap multiset is supposed to be in NET-shift-equal-to-c. So we need
    sum of (orbit-shift × multiplicity) = c alpha_1, and donor capacities respected.
  Subtype LL (2-unit): +/- 2.
  Subtypes b/c (1-unit): +/- 1.
  Donor capacities: # of swaps of LL+ <= start_pi[2 e_1]; LL- <= start_pi[2 e_2]; etc.

  Given delta and c, the "orbit-swap multisets matching delta with total shift c": we count.
  If unique: SU1 holds at this triple.
  If not unique: F1 falsifier candidate.

But here's the issue: delta supported on (e_1+e_2) — that's an INTERIOR slot of LL alpha-string,
NOT a donor or receiver of LL orbit swap! Yet hits on the LL string PASS THROUGH e_1+e_2 as
intermediate states.

If the end state has nonzero shift at e_1+e_2 (vs start), then the orbit-swap multiset language
DOES NOT directly accommodate it — because no orbit-swap subtype changes the multiplicity of
e_1+e_2 (an s_1-fixed root). So if the symbolic expansion produces end states with non-zero
shift at s_1-fixed roots, those end states can NEVER be expressed as orbit-swap multisets;
they're outside the Aug~ image.

In the Aug~ framework, such items would correspond to (#even - #odd) mismatch (BGG cohomology).
In the BGG expansion picture, they're real terms in the divided-power expansion.

UPSHOT: for SU1 Phase A, we should restrict attention to END STATES whose delta is in the
orbit-swap subgroup (sum-of-orbit-swap-deltas). For those, check uniqueness.

Equivalent reformulation: we enumerate ORBIT-SWAP MULTISETS M (subtype, sign, count) with
total shift = c and donor capacity respected. For each such M, the resulting end state pi_M
is determined. Check: do two distinct M's give the same pi_M? IF YES: SU1 falsified at
the multiset/end-state level.

THIS is the cleanest version of Phase A.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from collections import defaultdict, Counter
from itertools import product
from fractions import Fraction
import aug_tilde_C3_richer as C3


# ------------------------------------------------------------
# Helpers: list orbit-swap subtypes and their (donor, receiver) at a given simple
# ------------------------------------------------------------

def orbit_swap_actions(kind, i, N):
    """For simple s_i in C_N, return a list of (label, donor, receiver, units) for each
    orbit-swap subtype + direction, where:
      label = (subtype_tuple, sign in {'+','-'})
      donor: root removed.
      receiver: root added.
      units: alpha_i-shift contributed (always positive; the SIGN encodes direction).
    Sign convention: '+' = forward (c > 0 direction), '-' = backward.

    NOTE: in C3.subtype_donor_receiver, the c-argument determines direction. For c=+1,
    the "donor" is on the side where alpha_i decreases; for c=-1, vice versa. So we use
    c=+1 for '+'-sign and c=-1 for '-'-sign in our convention.
    """
    out = []
    subs = C3.subtypes_for_simple(kind, i, N)
    for st in subs:
        u = C3.subtype_units_per_swap(kind, i, st, N)
        donor_p, recv_p = C3.subtype_donor_receiver(kind, i, st, +1, N)
        donor_m, recv_m = C3.subtype_donor_receiver(kind, i, st, -1, N)
        out.append(((st, '+'), donor_p, recv_p, u))
        out.append(((st, '-'), donor_m, recv_m, u))
    return out


# ------------------------------------------------------------
# Enumerate orbit-swap multisets with total shift = c and donor capacities <= pi
# ------------------------------------------------------------

def enumerate_orbit_swap_multisets(pi, c, kind, i, N):
    """Enumerate all multisets M = {label: count} satisfying:
      sum over '+' counts of units(st) - sum over '-' counts of units(st) = c
      for each (st, sign), donor capacity respected (multiset uses only pi[donor] of donor)
      BUT also: ALL '+' and '-' subtype counts simultaneously consume from pi; we have to
      track donor capacities additively over all (st,sign).
    Returns: list of dicts M : {(st, sign): count}.

    NOTE: a donor root may serve as donor for MULTIPLE subtypes (e.g. 2 e_1 is donor for LL+
    in s_1, but also is the donor of various other subtypes at other simples — but here we're
    fixing s_i = (kind, i), so the relevant donors are per-subtype-within-this-s_i).
    BUT: within ONE s_i, can two different subtypes (st1, +) and (st2, +) share a donor?
    For C_n short exchange s_i:
      LL+ donor = 2 e_i; LL- donor = 2 e_{i+1}.
      b+(p) donor = e_p + e_i; b-(p) donor = e_p - e_{i+1}.
      c+(q) donor = e_i + e_q; c-(q) donor = e_i - e_q.
      All distinct roots (no shared donor across subtypes within one s_i).
    So per-(subtype,sign) capacity is correct.

    EXCEPT: the receiver of one swap can be the donor of another! E.g. LL+ in s_1: donor 2 e_1
    -> receiver 2 e_2. Now b+ in s_2 (with p=2, ahem n=3 so i+1=2=N-1, no b+ at s_2)... not relevant.
    Within ONE s_i, donors and receivers are distinct (donor reduces multiplicity, receiver
    increases). For pure within-s_i swaps, the receiver of LL+ (= 2 e_{i+1}) is the donor of LL-,
    so if we do both LL+ and LL- swaps within the same multiset, we have to be careful: a LL+ swap
    PRODUCES a 2 e_{i+1} that COULD be consumed by LL- (which sends 2 e_{i+1} -> 2 e_i).
    BUT in the orbit-swap multiset framework, the donor capacity is checked against the STARTING
    pi, not intermediate states. So LL+ count + LL- count both bounded by the starting pi at
    their respective donors.

    Wait — this is also a key point. In the aug_tilde framework, the donor capacity is checked
    against pi (start state). The MULTISET counts are applied to start state. So if we have
    LL+ count = 2 (= remove 2 from pi[2e_1]) and LL- count = 1 (= remove 1 from pi[2e_2]), we need
    pi[2 e_1] >= 2 AND pi[2 e_2] >= 1 — checked against START.

    OK — so the enumerator is straightforward.
    """
    actions = orbit_swap_actions(kind, i, N)
    # Build per-action capacity
    caps = []
    for lbl, donor, recv, u in actions:
        caps.append(pi.get(donor, 0))
    results = []
    n_actions = len(actions)

    def recurse(idx, remaining_c, partial):
        if idx == n_actions:
            if remaining_c == 0:
                results.append(dict(partial))
            return
        lbl, donor, recv, u = actions[idx]
        sign = lbl[1]
        signed_unit = u if sign == '+' else -u
        cap = caps[idx]
        # n in 0..cap, contributes n * signed_unit toward c
        for n in range(cap + 1):
            if n > 0:
                partial[lbl] = n
            recurse(idx + 1, remaining_c - n * signed_unit, partial)
            if n > 0:
                del partial[lbl]

    recurse(0, c, {})
    return results


def apply_multiset(pi, multiset, kind, i, N):
    """Apply an orbit-swap multiset M to pi. Donor and receiver lookups via orbit_swap_actions.
    Returns the resulting Kostant partition.
    """
    actions = {lbl: (donor, recv) for lbl, donor, recv, u in orbit_swap_actions(kind, i, N)}
    new_pi = dict(pi)
    for lbl, n in multiset.items():
        donor, recv = actions[lbl]
        new_pi[donor] = new_pi.get(donor, 0) - n
        if new_pi[donor] == 0:
            del new_pi[donor]
        new_pi[recv] = new_pi.get(recv, 0) + n
    # Drop nonpositive entries (cleanup)
    new_pi = {r: m for r, m in new_pi.items() if m > 0}
    return new_pi


def freeze_pi(pi):
    return tuple(sorted(pi.items()))


# ------------------------------------------------------------
# Enumerate donor profiles pi (supported on s_i-orbit roots + s_i-fixed roots)
# ------------------------------------------------------------

def donor_supports_for_s_i(kind, i, N):
    """Roots that can be donors or receivers under s_i (= involved in orbit swaps at s_i)."""
    actions = orbit_swap_actions(kind, i, N)
    roots = set()
    for lbl, donor, recv, u in actions:
        roots.add(donor); roots.add(recv)
    return sorted(roots)


def enumerate_pis(roots, max_total):
    """Enumerate Kostant partitions pi supported on `roots` with sum-of-multiplicities <= max_total."""
    # Generate all n-tuples with sum <= max_total
    out = []
    def recurse(idx, remaining, partial):
        if idx == len(roots):
            out.append(dict(partial))
            return
        for n in range(remaining + 1):
            if n > 0:
                partial[roots[idx]] = n
            recurse(idx + 1, remaining - n, partial)
            if n > 0:
                del partial[roots[idx]]
    recurse(0, max_total, {})
    return out


# ------------------------------------------------------------
# Main experiment
# ------------------------------------------------------------

def reduce_multiset(M):
    """Cancel matching (+, -) counts within the SAME subtype.
    A pair ((st,+):a, (st,-):b) reduces to ((st, sign of (a-b)): |a-b|) if a != b, else empty.
    Returns the reduced multiset (immutable, hashable form).
    """
    # group by subtype
    by_st = defaultdict(lambda: {'+': 0, '-': 0})
    for (st, sg), n in M.items():
        by_st[st][sg] += n
    out = {}
    for st, d in by_st.items():
        a = d['+']
        b = d['-']
        if a > b:
            out[(st, '+')] = a - b
        elif b > a:
            out[(st, '-')] = b - a
        # else: cancel entirely
    return out


def freeze_multiset(M):
    return tuple(sorted(M.items()))


def phase_a_experiment(kind, i, N, c_values, max_pi_total, log_fp=None):
    """Run the Phase A uniqueness check at simple (kind, i) for c in c_values, profile size <= max_pi_total."""
    def log(*args):
        s = " ".join(str(a) for a in args)
        print(s)
        if log_fp is not None:
            log_fp.write(s + "\n")

    log("=" * 70)
    log(f"SU1 Phase A: simple (kind={kind}, i={i}) in C_{N}")
    log(f"  c in {c_values}, |pi| <= {max_pi_total}")
    log("=" * 70)

    roots = donor_supports_for_s_i(kind, i, N)
    log(f"Donor-relevant roots for this simple: {roots}")
    log()

    triples_total = 0
    triples_unique = 0
    triples_multi = 0
    triples_zero = 0  # shouldn't happen
    # Reduced-multiset stats (after cancellation of (st,+)/(st,-) pairs):
    red_triples_total = 0
    red_triples_unique = 0
    red_triples_multi = 0
    falsifier_examples = []
    red_falsifier_examples = []

    pis = enumerate_pis(roots, max_pi_total)
    log(f"# donor profiles enumerated: {len(pis)}")

    for pi in pis:
        if sum(pi.values()) == 0:
            continue
        for c in c_values:
            multisets = enumerate_orbit_swap_multisets(pi, c, kind, i, N)
            if not multisets:
                continue  # No solutions: skip (the BGG matrix entry would just be zero)

            # Group multisets by resulting end-state Kostant monomial
            end_states = defaultdict(list)
            for M in multisets:
                end_pi = apply_multiset(pi, M, kind, i, N)
                end_states[freeze_pi(end_pi)].append(M)

            for end_pi_key, ms_list in end_states.items():
                triples_total += 1
                k = len(ms_list)
                if k == 1:
                    triples_unique += 1
                elif k >= 2:
                    triples_multi += 1
                    if len(falsifier_examples) < 5:
                        falsifier_examples.append({
                            'pi': dict(pi),
                            'c': c,
                            'end_pi': dict(end_pi_key),
                            'multisets': ms_list,
                        })
                else:
                    triples_zero += 1

                # REDUCED multiset uniqueness: after cancelling (st,+)/(st,-) within
                # the same subtype, how many DISTINCT reduced multisets give this end-state?
                reduced_set = set()
                for M in ms_list:
                    reduced_set.add(freeze_multiset(reduce_multiset(M)))
                red_triples_total += 1
                if len(reduced_set) == 1:
                    red_triples_unique += 1
                else:
                    red_triples_multi += 1
                    if len(red_falsifier_examples) < 5:
                        red_falsifier_examples.append({
                            'pi': dict(pi),
                            'c': c,
                            'end_pi': dict(end_pi_key),
                            'reduced_multisets': [dict(rm) for rm in reduced_set],
                            'all_multisets': ms_list,
                        })

    log()
    log("RAW MULTISET RESULTS (no cancellation)")
    log("-" * 70)
    log(f"# (pi, c, end_pi) triples checked: {triples_total}")
    log(f"# with EXACTLY ONE orbit-swap multiset: {triples_unique}")
    log(f"# with MULTIPLE orbit-swap multisets:   {triples_multi}")
    log(f"# with ZERO multisets (anomaly):        {triples_zero}")
    log()

    if triples_multi > 0:
        log("Distinct RAW orbit-swap multisets share an end-state Kostant signature.")
        log("  (this is EXPECTED: a (+, -) cancellation pair on the same subtype")
        log("   contributes a trivial Diophantine redundancy. Inspect REDUCED below.)")
        log()
        for k, ex in enumerate(falsifier_examples[:3]):
            log(f"  Example {k+1}:")
            log(f"    pi = {ex['pi']}")
            log(f"    c  = {ex['c']}")
            log(f"    end_pi = {ex['end_pi']}")
            log(f"    multisets:")
            for M in ex['multisets']:
                log(f"      {M}")
            log()

    log()
    log("REDUCED MULTISET RESULTS (after cancelling (st,+)/(st,-) pairs)")
    log("-" * 70)
    log(f"# (pi, c, end_pi) triples checked: {red_triples_total}")
    log(f"# with EXACTLY ONE reduced multiset: {red_triples_unique}")
    log(f"# with MULTIPLE reduced multisets:   {red_triples_multi}")
    log()

    if red_triples_multi > 0:
        log("F1 FALSIFIER (after reduction): distinct REDUCED orbit-swap multisets share an end-state.")
        log()
        for k, ex in enumerate(red_falsifier_examples[:5]):
            log(f"  Example {k+1}:")
            log(f"    pi = {ex['pi']}")
            log(f"    c  = {ex['c']}")
            log(f"    end_pi = {ex['end_pi']}")
            log(f"    distinct reduced multisets:")
            for M in ex['reduced_multisets']:
                log(f"      {M}")
            log()
    else:
        log("CONFIRMED at the REDUCED level: every (pi, c, end_pi) triple has a UNIQUE")
        log("  reduced orbit-swap multiset.")
        log("  -> SU1 uniqueness HOLDS modulo trivial (st,+)/(st,-) cancellation pairs.")
        log()

    return {
        'triples_total': triples_total,
        'triples_unique': triples_unique,
        'triples_multi': triples_multi,
        'triples_zero': triples_zero,
        'red_triples_total': red_triples_total,
        'red_triples_unique': red_triples_unique,
        'red_triples_multi': red_triples_multi,
        'falsifier_examples': falsifier_examples,
        'red_falsifier_examples': red_falsifier_examples,
        'kind': kind, 'i': i, 'N': N,
        'c_values': c_values, 'max_pi_total': max_pi_total,
    }


# ------------------------------------------------------------
# F_4 cross check (Phase A optional)
# ------------------------------------------------------------

# F_4 positive roots and simple roots, in the standard convention:
#   alpha_1 = e_1 - e_2 (long)
#   alpha_2 = e_2 - e_3 (long)
#   alpha_3 = e_3       (short)
#   alpha_4 = (e_1 - e_2 - e_3 - e_4) / 2  -- WAIT, standard F_4 has alpha_4 = 1/2(e_1-e_2-e_3-e_4)
# Actually let me use the standard:
#   F_4 simple roots (Bourbaki):
#     alpha_1 = e_2 - e_3 (long)
#     alpha_2 = e_3 - e_4 (long)
#     alpha_3 = e_4       (short)
#     alpha_4 = 1/2 (e_1 - e_2 - e_3 - e_4) (short)
# Positive roots: 24 total. 12 long: e_i - e_j (i<j, 6) and e_i + e_j (i<j, 6).
# 12 short: e_i (4) and 1/2(±e_1 ± e_2 ± e_3 ± e_4) with even number of minus signs (8).

def f4_positive_roots():
    """Return list of (root_tuple, kind) for F_4 positive roots. root in R^4."""
    roots = []
    # Long: e_i - e_j (i < j) and e_i + e_j (i < j)
    for i in range(4):
        for j in range(i + 1, 4):
            v = [Fraction(0)] * 4
            v[i] = Fraction(1)
            v[j] = Fraction(-1)
            roots.append((tuple(v), 'L'))
            v = [Fraction(0)] * 4
            v[i] = Fraction(1)
            v[j] = Fraction(1)
            roots.append((tuple(v), 'L'))
    # Short: e_i
    for i in range(4):
        v = [Fraction(0)] * 4
        v[i] = Fraction(1)
        roots.append((tuple(v), 'S'))
    # Short: 1/2 (±e_1 ± e_2 ± e_3 ± e_4) with positive first coord
    half = Fraction(1, 2)
    for s1, s2, s3, s4 in product([1, -1], repeat=4):
        # we want a "positive" root: first nonzero coord positive. Since all coords are ±1/2, the
        # first coord is s1/2 which is positive iff s1 = +1. Take only those.
        if s1 != 1:
            continue
        v = (half * s1, half * s2, half * s3, half * s4)
        roots.append((v, 'S'))
    return roots


def f4_simple_roots():
    """Bourbaki simple roots for F_4."""
    return [
        ((Fraction(0), Fraction(1), Fraction(-1), Fraction(0)), 'L'),   # alpha_1 = e_2 - e_3
        ((Fraction(0), Fraction(0), Fraction(1), Fraction(-1)), 'L'),   # alpha_2 = e_3 - e_4
        ((Fraction(0), Fraction(0), Fraction(0), Fraction(1)),  'S'),   # alpha_3 = e_4
        ((Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 2)), 'S'),  # alpha_4
    ]


def f4_inner(u, v):
    return sum(u[k] * v[k] for k in range(4))


def f4_coroot(alpha):
    """alpha^v = 2 alpha / (alpha, alpha)."""
    n2 = f4_inner(alpha, alpha)
    return tuple(2 * alpha[k] / n2 for k in range(4))


def f4_pairing(beta, alpha):
    """<beta, alpha^v> = 2 (beta, alpha) / (alpha, alpha)."""
    n2 = f4_inner(alpha, alpha)
    return 2 * f4_inner(beta, alpha) / n2


def f4_reflect(beta, alpha):
    """s_alpha(beta) = beta - <beta, alpha^v> alpha."""
    p = f4_pairing(beta, alpha)
    return tuple(beta[k] - p * alpha[k] for k in range(4))


def f4_s3_orbit_swap_actions():
    """At F_4 simple alpha_3 = e_4 (short), enumerate orbit-swap subtypes.
    For each beta in Phi^+ \\ {alpha_3}: compute <beta, alpha_3^v>.
    If > 0, beta is a donor in '+' direction; receiver is s_3(beta) = beta - <beta,alpha_3^v> alpha_3.
    Skip if pairing = 0 (s_3-fixed, not an orbit-swap participant).
    NOTE: for F_4 short simple, units = |<beta, alpha_3^v>| takes values in {1, 2}, giving
    mixed-unit-scale.
    """
    pos_roots = [r for r, _ in f4_positive_roots()]
    alpha_3 = (Fraction(0), Fraction(0), Fraction(0), Fraction(1))
    actions = []
    seen_orbits = set()
    for beta in pos_roots:
        if beta == alpha_3:
            continue
        p = f4_pairing(beta, alpha_3)
        if p == 0:
            continue
        # beta with p > 0 is "donor in '+' direction"; receiver s_3(beta) = beta - p*alpha_3 (which is a positive root)
        # When p > 0: '+' direction donor=beta, receiver=s_3(beta).
        # The subtype is the orbit {beta, s_3(beta)}.
        partner = f4_reflect(beta, alpha_3)
        if partner not in pos_roots:
            # Should not happen; the s_3-image of a positive root is positive or a negative form of a positive root.
            # But for a non-fixed orbit with p != 0, partner could be negative... actually no, s_i acts on Phi^+ \ {alpha_i}.
            continue
        if p > 0:
            donor, recv = beta, partner
        else:
            donor, recv = partner, beta
        orbit_key = frozenset({beta, partner})
        units = abs(p)
        # Build labels for both directions
        # '+': uses donor = beta-or-partner-with-positive-pairing
        if orbit_key not in seen_orbits:
            seen_orbits.add(orbit_key)
            # subtype name: use a sorted tuple representation
            st = ('orbit', tuple(sorted([beta, partner])))
            # '+' direction
            actions.append(((st, '+'), donor, recv, units))
            # '-' direction (reverse)
            actions.append(((st, '-'), recv, donor, units))
    return actions


def f4_s3_orbit_swap_multisets(pi, c, max_per=None):
    """Enumerate orbit-swap multisets at F_4 s_3 with total shift = c, donor capacities <= pi."""
    actions = f4_s3_orbit_swap_actions()
    caps = [pi.get(donor, 0) for lbl, donor, recv, u in actions]
    results = []
    n = len(actions)

    def recurse(idx, remaining, partial):
        if idx == n:
            if remaining == 0:
                results.append(dict(partial))
            return
        lbl, donor, recv, u = actions[idx]
        sign = lbl[1]
        signed = u if sign == '+' else -u
        for k in range(caps[idx] + 1):
            if k > 0:
                partial[lbl] = k
            recurse(idx + 1, remaining - k * signed, partial)
            if k > 0:
                del partial[lbl]

    recurse(0, c, {})
    return results


def f4_s3_apply_multiset(pi, multiset):
    actions = {lbl: (donor, recv) for lbl, donor, recv, u in f4_s3_orbit_swap_actions()}
    new_pi = dict(pi)
    for lbl, n in multiset.items():
        donor, recv = actions[lbl]
        new_pi[donor] = new_pi.get(donor, 0) - n
        if new_pi[donor] == 0:
            del new_pi[donor]
        new_pi[recv] = new_pi.get(recv, 0) + n
    new_pi = {r: m for r, m in new_pi.items() if m > 0}
    return new_pi


def f4_phase_a_at_s3(c_values, max_pi_total, log_fp=None):
    def log(*args):
        s = " ".join(str(a) for a in args)
        print(s)
        if log_fp is not None:
            log_fp.write(s + "\n")

    log("=" * 70)
    log("F_4 cross-check: simple s_3 (short, alpha_3 = e_4)")
    log("=" * 70)
    actions = f4_s3_orbit_swap_actions()
    log(f"# orbit-swap (subtype, direction) tuples at s_3: {len(actions)}")
    # Show units distribution
    units_dist = Counter(u for lbl, d, r, u in actions)
    log(f"  Units distribution: {dict(units_dist)} (mixed-unit-scale: {len(set(u for lbl,d,r,u in actions)) > 1})")

    donor_roots = sorted(set(donor for lbl, donor, recv, u in actions),
                         key=lambda v: tuple(float(x) for x in v))
    log(f"  # distinct donor roots: {len(donor_roots)}")

    pis = enumerate_pis(donor_roots, max_pi_total)
    log(f"  # donor profiles enumerated: {len(pis)}")

    triples_total = 0
    triples_unique = 0
    triples_multi = 0
    red_triples_total = 0
    red_triples_unique = 0
    red_triples_multi = 0
    falsifier_examples = []
    red_falsifier_examples = []

    for pi in pis:
        if sum(pi.values()) == 0:
            continue
        for c in c_values:
            multisets = f4_s3_orbit_swap_multisets(pi, c)
            if not multisets:
                continue
            end_states = defaultdict(list)
            for M in multisets:
                end_pi = f4_s3_apply_multiset(pi, M)
                end_states[freeze_pi(end_pi)].append(M)
            for end_key, ms_list in end_states.items():
                triples_total += 1
                if len(ms_list) == 1:
                    triples_unique += 1
                else:
                    triples_multi += 1
                    if len(falsifier_examples) < 3:
                        falsifier_examples.append({
                            'pi': dict(pi), 'c': c, 'end_pi': dict(end_key),
                            'multisets': ms_list,
                        })
                reduced_set = set()
                for M in ms_list:
                    reduced_set.add(freeze_multiset(reduce_multiset(M)))
                red_triples_total += 1
                if len(reduced_set) == 1:
                    red_triples_unique += 1
                else:
                    red_triples_multi += 1
                    if len(red_falsifier_examples) < 5:
                        red_falsifier_examples.append({
                            'pi': dict(pi), 'c': c, 'end_pi': dict(end_key),
                            'reduced_multisets': [dict(rm) for rm in reduced_set],
                            'all_multisets': ms_list,
                        })

    log()
    log("RESULTS (F_4 s_3)")
    log(f"RAW: # triples = {triples_total}, unique = {triples_unique}, multi = {triples_multi}")
    log(f"REDUCED: # triples = {red_triples_total}, unique = {red_triples_unique}, multi = {red_triples_multi}")
    if red_triples_multi > 0:
        log("F1 FALSIFIER at F_4 s_3 (reduced multiset level):")
        for ex in red_falsifier_examples:
            log(f"  pi={ex['pi']}")
            log(f"  c={ex['c']}, end_pi={ex['end_pi']}")
            log(f"  distinct reduced multisets:")
            for rm in ex['reduced_multisets']:
                log(f"    {rm}")
            log()
    else:
        log("CONFIRMED at REDUCED level: orbit-swap multisets at F_4 s_3 are uniquely")
        log("  determined by end-state modulo trivial (st,+)/(st,-) cancellation.")
    return {
        'triples_total': triples_total,
        'triples_unique': triples_unique,
        'triples_multi': triples_multi,
        'red_triples_total': red_triples_total,
        'red_triples_unique': red_triples_unique,
        'red_triples_multi': red_triples_multi,
        'falsifier_examples': falsifier_examples,
        'red_falsifier_examples': red_falsifier_examples,
    }


# ------------------------------------------------------------
# Driver
# ------------------------------------------------------------

if __name__ == "__main__":
    LOG_PATH = "/home/agent/projects/proofs/remark47/su1_phase_a_C3.log"
    with open(LOG_PATH, "w") as log_fp:
        # C_3 at s_1 (short exchange, mixed-unit-scale)
        result_C3_s1 = phase_a_experiment(
            kind='S', i=1, N=3,
            c_values=[1, 2, 3, 4, -1, -2, -3, -4],
            max_pi_total=5,
            log_fp=log_fp,
        )
        print()
        log_fp.write("\n")

        # C_3 at s_0 (also short exchange, but i=0 so subtypes are different — try as sanity check)
        result_C3_s0 = phase_a_experiment(
            kind='S', i=0, N=3,
            c_values=[1, 2, 3, 4, -1, -2, -3, -4],
            max_pi_total=5,
            log_fp=log_fp,
        )
        print()
        log_fp.write("\n")

        # C_3 at s_2 (long flip, uniform-unit-scale -- should trivially confirm)
        result_C3_s2 = phase_a_experiment(
            kind='L', i=2, N=3,
            c_values=[1, 2, 3, 4, -1, -2, -3, -4],
            max_pi_total=5,
            log_fp=log_fp,
        )
        print()
        log_fp.write("\n")

        # F_4 at s_3 (short, mixed-unit per problem)
        result_F4_s3 = f4_phase_a_at_s3(
            c_values=[1, 2, 3, -1, -2, -3],
            max_pi_total=3,
            log_fp=log_fp,
        )
        print()
        log_fp.write("\n")

        # Summary
        print()
        log_fp.write("\n========= FINAL SUMMARY =========\n")
        print("========= FINAL SUMMARY =========")
        for label, res in [('C_3 s_1', result_C3_s1), ('C_3 s_0', result_C3_s0),
                           ('C_3 s_2', result_C3_s2), ('F_4 s_3', result_F4_s3)]:
            line = (f"{label}: RAW total={res['triples_total']}, "
                    f"unique={res['triples_unique']}, multi={res['triples_multi']}  ||  "
                    f"REDUCED total={res['red_triples_total']}, "
                    f"unique={res['red_triples_unique']}, multi={res['red_triples_multi']}")
            print(line)
            log_fp.write(line + "\n")
