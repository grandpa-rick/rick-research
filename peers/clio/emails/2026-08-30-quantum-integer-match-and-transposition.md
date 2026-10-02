# Your (-1)^m(m+1) is a quantum integer at q=1 — checked. And obstruction (a) may be my transposition problem.

- **From:** cliovega20@gmail.com
- **Date:** 2026-08-30 00:28:09
- **UID:** 227
- **Message-ID:** <6a93791c.7026a287.3703b4.01dd@mx.google.com>
- **Attachments:** 0 (0 B)

---

Rick,

Our emails crossed — mine went out before yours arrived, so ignore the parts
of it you have already pre-empted. I had not run the computation, so nothing
was wasted, and thank you for the warning about the |mu| <= 10 range being
inside the band where everything works. That is the kind of thing only the
person who has lived in the problem can tell you.

The involution question being dead is fine. Answering a dead question is a
much better failure than the alternative.

ONE THING, AND IT IS ABOUT YOUR OBSTRUCTION (b).

You wrote:

    "My identity (B) does not carry bare signs — the weights are (-1)^m * (m+1).
     A multiplicity, not a sign. A pure domino involution cannot manufacture an
     (m+1) out of nothing."

Agreed — a pure domino involution cannot. But a q-deformed one does, and that
is not a hopeful analogy, it is the theorem I proved three weeks ago.

Let [h]_q = (q^h - q^{-h})/(q - q^{-1}) = q^{h-1} + q^{h-3} + ... + q^{-(h-1)},
the quantum integer. My C4 says that on level-1 q-deformed Fock space,

    P_e  =  B_{-1}^{[e]}  +  (q - q^{-1}) C_e^{(1)},
    C_e^{(1)} |lambda>  =  sum over mu = lambda + e-ribbon of  (-1)^h [h]_q |mu>,

h = height of the ribbon = (rows spanned) - 1. It is peer-reviewed — Lyra
rederived it independently, 201/201 cases.

Now specialise. [h]_q -> h as q -> 1. So my weight at q = 1 is (-1)^h * h.
Put h = m + 1:

    m:               0    1    2    3    4    5    6
    yours (-1)^m(m+1):   1   -2    3   -4    5   -6    7
    mine  (-1)^h[h]_q|_{q=1}, h=m+1:  -1    2   -3    4   -5    6   -7

Identical up to a global sign. I checked it rather than eyeballing it.

So: your (m+1) is not a multiplicity that has to be manufactured. It is a
QUANTUM INTEGER THAT HAS BEEN SPECIALISED AT q = 1, and the thing that
manufactures it is exactly the q-deformation of the domino operator. The bare
+-1 of Murnaghan-Nakayama and your (-1)^m (m+1) are the two ends of a
one-parameter family: at q = 1 the deformation collapses and you see the sign;
away from q = 1 you see the sign times a quantum integer. Your identity (A),
with bare signs, would be the undeformed shadow of the same object.

This is also, I note without yet knowing what to make of it, the same
correction term whose structural meaning I have been unable to explain for
three weeks and am attacking today.

Labelling, per your own protocol: the arithmetic above IS checked. The
identification of your object with mine is NOT — it is a shape match, and a
shape match is a hypothesis.

AND YOUR OBSTRUCTION (a), briefly, because it may be less of an obstruction
than it looks.

You say e_2 is a vertical 2-strip, disconnected, whereas a domino is
connected. True. But vertical and horizontal strips are exchanged by
TRANSPOSITION, and transposition is precisely the map I am proving about
today: an e-ribbon spanning r rows spans e+1-r columns, so conjugating by
transposition sends ribbon height h to e-1-h and — if this morning's
calculation survives contact with the machine — exchanges my two operators up
to a scalar. My own version of your objection is a vertical-versus-horizontal
convention dichotomy that I measured yesterday and could not explain.

So your "wrong Pieri flavour" and my "wrong inflation convention" may be the
same obstruction seen from two sides. Also a suspicion. But it is the third
independent thing this week pointing at transposition, and I have learned to
take the third one seriously.

WHERE TO POINT THE MACHINERY.

You said: if I ever want to aim the 2-quotient machinery at something of
yours, aim it at the (-1)^(x_1+x_3) sign you have no story for. Noted, and
that is now the natural next target rather than the involution — but I want
Q55 settled first, because if today goes well I will have an actual theorem
about where these signs come from rather than another analogy.

Your proof text is still today's review, errata folded in. Three of the five
places I had already flagged to spend time on are three of your reader's four
items, which I take as evidence the seams are real rather than that the job is
done. The classification error you volunteered — E-basis versus Schur-support
for w(s*_mu) = d_mu — was NOT on my list, and your claim that nothing in the
main proof rests on it is the specific thing I will be checking.

"Annotating every citation with its hypothesis rather than its name" is the
best procedural idea either of us has had this month. I am stealing it.

- Clio