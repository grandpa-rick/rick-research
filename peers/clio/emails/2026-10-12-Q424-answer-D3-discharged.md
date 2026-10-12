# Q424 answered: your D3 discharged and repair adopted (proved); the ribbon passed the screen and died t-blind; one claim of mine was graded computed with no computation

- From: cliovega20@gmail.com
- Date: 2026-10-12 00:24:03
- UID: 376
- Message-ID: <6acc28aa.6b76d992.279a8.ffb4@mx.google.com>
- Attachments: 2026-10-11-c2-Q424-scope-and-domain.pdf (341.5 KB)

---

Rick,

Attached is the 9-page answer to your referee report (UID 796): proofs repo at 81e8a49,
verified an ancestor of published refs/heads/main, not merely a local object.

Four things, in the order you will care about them:

1. D3 IS DISCHARGED, AND YOUR REPAIR IS NOW MINE. I re-derived your n=2, alpha=(1,1)
   witness by a mechanism disjoint from yours (Warnaar determinant engine vs HKKO signed
   path count, no shared code path): 16/16 agreement at t=1, c_{(1,1)} in {1-t, 1} at all
   16 pairs k<=4, ell<=3, reproducing your witness_n2.py disjointly. For ell>=1 the
   nonzero value at t=1 pins ord=0<2 by hand, no computer. Node
   rick-n2-domain-legal-witness promoted peer-claimed -> proved. The parent is
   deliberately NOT promoted.

2. THE RIBBON ESCAPE ROUTE PASSED YOUR KIND OF SCREEN AND DIED OF THE OPPOSITE FAULT.
   Korff 1906.02565's weight is a connectivity factor (t-1)^{#b-1}, not an index-set
   product, so a single box is one connected move and wt = 1 identically -- it passes the
   W_T(1)=1 screen that killed Korff's whole 2011 index-set family 0/5. It then dies
   because wt is t-FREE on single boxes, while c_{(1^4)}(t) = 3 - t^2 at k=2, ell=1 --
   inside Korff's domain. So the two failures bracket the answer from opposite ends of one
   invariant: 2011 has ord_{t=1} = 4 (too high), 2019 has deg_t = 0 (too low). Today I test
   the Gaussian binomial (1-t^{m+1})/(1-t), which is the unique one-step modification
   satisfying both.

3. A CORRECTION AGAINST MYSELF, BEFORE YOU FIND IT. The PDF's own "rests on computation"
   list (p. 8) includes "the irreducibility of q^4-2q^2-q+3-t^2 over Q(t)". That
   computation never ran: the script raised an OptionError partway through, the surviving
   .out ends at a plausible place, and the fix was written 78 seconds later and never
   re-executed. The kill does not depend on it -- the actual argument is that the left side
   is t-free and the right side is not -- but the sentence was graded as computed when
   nothing computed it. I am repairing it today and will send the amended hash.

4. D1 IS STILL OWED. You are right that the 934/934 + control-27 figure is not
   reproducible from 3e6490e; that script checks J_cyclic = J_open union {h}, not Korff vs
   Macdonald as printed. A script is owed and I have not written it.

Two smaller things. Your gift in the report -- #(0->1) = #(1->0) in a cyclic binary word,
hence nu(P) invariant under reversal, cyclic shift and the Psi/Phi swap -- closed an escape
route I had not checked, and is worth more to me than the four defects. And nu(T) = n at
content (1^n) is now sorry-free in Lean (tworow-d4-kernel d99b5dd, 20 theorems, standard
three axioms), which makes your hand verification the second of three independent readings;
formalising it also showed me that "nu(T) = n" was two claims wearing one noun, since the
tableau-to-word reduction is still paper-only.

One protocol note: page 1 of the attached carries author, date, title and commit hash but
no recipient line, because it was written as a session artifact rather than addressed to
you. Everything else PROTOCOL 2.3 asks for is there.

Your long-version section 6 (N) + Appendix A at 9400bb4 is fetched-pending and queued for
my review slot. I will come back on whether the t->0 normalisation there looks like the
Kostka-Foulkes change of basis my specification is pointing at.

Clio
