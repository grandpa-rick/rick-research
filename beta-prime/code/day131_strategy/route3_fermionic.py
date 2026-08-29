"""Route 3: Fermionic / residue interpretation of M(T) and F(T).

Key data:
  A'/A = (E2 - E1)/(1 + E1*T)         -- simple pole at T = -1/E1
  E3 * M'(T) = -E3 * T (3 + E1 T) / (1 + E1 T)^3   -- triple pole at T = -1/E1
  M(T) = T/(E1*(1+E1 T)^2) - log(1+E1 T)/E1^2
  A(T) = (1 + E1 T)^{(E2-E1)/E1}

Everything factors through the SINGLE point T = -1/E1 in some sense.
This is REMARKABLE and looks like a "single-particle" propagator structure.

The factor form F = A * exp(E3 M) is exactly a "coherent state" / "vertex operator"
expression when we think of E3 M(T) as a fermion bilinear expectation.

Concrete guess about fermionic backbone:
- (1+E1 T)^{(E2-E1)/E1} arises in the theta-function / boson-fermion correspondence as
  the expectation <psi(z) psi*(z')> of a single fermion pair.
- exp(E3 * M(T)) is exp of a "corrected" propagator — with the (n^2-1)/n twist
  characteristic of higher-spin / factorial-Schur / factorial-gq function.

Let's compute a few things to see structure:
"""

from sympy import (symbols, simplify, factor, series, Rational, Symbol, log,
                    exp, expand, apart, together, sqrt, I)

T = Symbol('T')
E1s, E2s, E3s = symbols('E1 E2 E3')

# Verify: -T(3+E1 T)/(1+E1 T)^3 = derivative of  T/(E1 (1+E1 T)^2) - log(1+E1 T)/E1^2
M = T / (E1s * (1 + E1s*T)**2) - log(1 + E1s*T)/E1s**2
Mprime = M.diff(T)
print("M'(T) =", simplify(Mprime))
print("simplified:", simplify(Mprime + T*(3+E1s*T)/(1+E1s*T)**3))

# Partial fraction of M':
print("\nApart of M':", apart(Mprime, T))

# Compute A'/A
A = (1 + E1s*T)**((E2s - E1s)/E1s)
Aprime = A.diff(T)
AoverA = simplify(Aprime/A)
print(f"\nA'/A = {AoverA}")

# Full log(F) = log(A) + E3 M:
# log(F) = ((E2-E1)/E1) * log(1 + E1 T) + E3 * [T/(E1 (1+E1 T)^2) - log(1+E1 T)/E1^2]
# Coefficient of log(1+E1 T): (E2-E1)/E1 - E3/E1^2 = (E1(E2-E1) - E3)/E1^2 = (E1 E2 - E1^2 - E3)/E1^2
# The FACTOR (E1 E2 - E1^2 - E3) has a nice interpretation:
# In terms of roots of u^3 - E1 u^2 + E2 u - E3 = 0 (i.e., u_1, u_2, u_3),
# u_i * (E2 - u_i^2)? Nope. Let me try. At u = E1 (which is the "average" root sum),
# E1 * (E1 E2 - E1^2 - E3)... hmm.
# Actually consider substituting u = 0: -E3. u = "generic": depends.
# Alternatively, is (E1 E2 - E1^2 - E3) related to a discriminant or resultant?
# For a cubic u^3 - E1 u^2 + E2 u - E3, discriminant is
# Delta = 18 E1 E2 E3 - 4 E1^3 E3 + E1^2 E2^2 - 4 E2^3 - 27 E3^2.
# So E1 E2 - E1^2 - E3 is not the discriminant.
# But it might be a partial discriminant or "reduced" value.

# Signature (n^2-1)/n = (n-1)(n+1)/n. Hmm this is characteristic of "3-string" or
# "spin-1" propagators. Note (n^2-1) = (n-1)(n+1), which shows up in:
#  - Bosonic string oscillator sums (contributions to zero-point energy)
#  - Character formulas for sl(2) modules of highest weight n
#  - The Virasoro shift term c(n^3 - n)/12 in central extension
# The presence of "/n" is standard in log gen functions.

# So M(T) could be:
#   E1^{-2} sum_{n>=2} (-1)^{n-1} (n^2-1)/n * (E1 T)^n
# Let y = E1 T. Then E1^2 M = sum_{n>=2} (-1)^{n-1} (n^2-1)/n * y^n.

# Split:
# sum_{n>=2} (-1)^{n-1} n y^n = y d/dy sum_{n>=1} (-1)^{n-1} y^n = y d/dy [y/(1+y)] = y (1/(1+y)^2)
#                             = y / (1+y)^2
# sum_{n>=2} (-1)^{n-1} y^n / n = -sum_{n>=2} (-y)^n / n = -[-log(1+y) - (-y)] = log(1+y) - y
# So sum_{n>=2} (-1)^{n-1} y^n / n = -log(1-(-y)) + (-y) subtracted... let me redo:
#   sum_{n>=1} (-1)^{n-1} y^n / n = log(1+y).  So sum_{n>=2} = log(1+y) - y.
# Therefore:
#   sum_{n>=2} (-1)^{n-1} (n^2-1)/n y^n = y/(1+y)^2 - [log(1+y) - y]
#                                        = y/(1+y)^2 + y - log(1+y).
# Hmm doesn't match "T/(E1(1+E1T)^2) - log(1+E1 T)/E1^2".
# Let me recompute Rick's stated formula.

# Actually  E1^2 * M(T) = sum_{n>=2} (-1)^{n-1}(n^2-1)/n * (E1 T)^n
# Set y = E1 T. E1^2 M = sum_{n>=2} (-1)^{n-1} (n^2-1)/n y^n
# = y/(1+y)^2 + y - log(1+y).
# Then M = (1/E1^2)*[E1 T/(1+E1 T)^2 + E1 T - log(1+E1 T)]
#        = T/(E1 (1+E1 T)^2) + T/E1 - log(1+E1 T)/E1^2.
# But Rick's formula was M = T/(E1 (1+E1 T)^2) - log(1+E1 T)/E1^2.  Missing T/E1.
# Discrepancy: T/E1 term.
# Hmm. Let me recompute using the Taylor of M directly:
Msym = T/(E1s*(1+E1s*T)**2) - log(1+E1s*T)/E1s**2
ser = series(Msym, T, 0, 8).removeO()
print("\nTaylor of Rick's M(T):", expand(ser))
# Also my derivation:
M_alt = T/(E1s*(1+E1s*T)**2) + T/E1s - log(1+E1s*T)/E1s**2
ser2 = series(M_alt, T, 0, 8).removeO()
print("Taylor of M_alt (with T/E1):", expand(ser2))

# Check the signature match:
# M(T) coefficients should be (-1)^{n-1}(n^2-1)/n * E1^{n-2} for n>=2 per Rick.
# So [T^n] M = (-1)^{n-1}(n^2-1)/n E1^{n-2}, [T^0] = 0, [T^1] = 0.
# Look at n=1 case: (n^2-1)/n = 0, so no T^1 term.  Good.
# So T/E1 SHOULDN'T be there if Rick's formula is correct.
# Let me re-derive M cleanly.
# E1^2 M = sum_{n>=2} (-1)^{n-1}(n^2-1)/n y^n.
# (n^2-1)/n = n - 1/n.
# sum_{n>=2} (-1)^{n-1} n y^n = y d/dy [ sum_{n>=1} (-1)^{n-1} y^n ] - the n=1 term (with n=1)
#                            = y d/dy [y/(1+y)] - 1*y^1*(-1)^0 * 1  (subtract n=1 term)
#                            Wait, more carefully:
# sum_{n>=1} (-1)^{n-1} y^n = y/(1+y).
# d/dy(y/(1+y)) = 1/(1+y)^2.
# sum_{n>=1} (-1)^{n-1} n y^{n-1} = 1/(1+y)^2.
# so sum_{n>=1} (-1)^{n-1} n y^n = y/(1+y)^2.
# subtracting n=1 term: n=1 contributes (-1)^0 * 1 * y = y.
# So sum_{n>=2} (-1)^{n-1} n y^n = y/(1+y)^2 - y.

# sum_{n>=1} (-1)^{n-1} y^n / n = log(1+y).
# subtracting n=1: 1*y = y. So sum_{n>=2} = log(1+y) - y.

# E1^2 M = [y/(1+y)^2 - y] - [log(1+y) - y] = y/(1+y)^2 - log(1+y).
# So M = y/(E1^2 (1+y)^2) - log(1+y)/E1^2 = T*E1/(E1^2 (1+E1 T)^2) - log(1+E1 T)/E1^2
#       = T/(E1 (1+E1 T)^2) - log(1+E1 T)/E1^2.
# Good — matches Rick. I had an arithmetic error before. Rick's formula is correct.

# So partial fraction analysis of M(T):
# M = T / (E1 (1+E1 T)^2) - log(1+E1 T)/E1^2.
# Let y = E1 T:  E1^2 M = y/(1+y)^2 - log(1+y).
# Expand y/(1+y)^2: let u = 1+y, so y = u-1, y/u^2 = (u-1)/u^2 = 1/u - 1/u^2.
# So y/(1+y)^2 = 1/(1+y) - 1/(1+y)^2.
# So E1^2 M = 1/(1+y) - 1/(1+y)^2 - log(1+y).
# Nice: three "terms" 1/(1+y), 1/(1+y)^2, log(1+y).
# All have poles only at y = -1 (i.e., T = -1/E1).

# Similarly A(T) = (1+y)^{(E2-E1)/E1}, singular only at y = -1.

# So EVERYTHING happens at T = -1/E1.  This is the "single-particle" pole
# characteristic of a fermion at that momentum/energy.

# Fermionic interpretation:
# In boson-fermion correspondence, generating functions of the form
#   exp(sum_k p_k h_k) * <charge-vac> ...
# have coherent-state interpretations.
# Here F(T) = A(T) * exp(E3 M(T)).
# If E3 were a fermionic bilinear like <psi(z) psi*(z')> = 1/(z-z'), then
# exp(E3 M(T)) with M(T) rational in (1+E1 T) is exactly the structure of
# a shifted fermion propagator.
# The factor A(T) = (1 + E1 T)^{alpha} is the "vertex operator" for a
# free boson with weight alpha.

# Bottom line for Route 3: The structure IS suggestive of a bilinear/vertex form.
# But without a specific fermionic model of Psi itself, this is an OBSERVATION, not a proof.
# To make this a proof: we'd need to reinterpret Psi's DEFINITION (T of f V / V)
# in a Fock-space language. Then A * exp(E3 M) would fall out from Wick contractions.

# The known fermionic-side identity most similar is the Boson-Fermion correspondence's
# tau function:  tau(x) = <vac| exp(sum p_k Jk) |lambda>
# which factorizes as product of "one-particle" contributions at fermion momenta.
# For symmetric functions in 3 variables, we have a rank-3 fermion Fock module,
# where u_1, u_2, u_3 are the fermion "momenta".
# The Vandermonde V = prod (u_i - u_j) is exactly the STATE of a 3-fermion vacuum
# (fully occupied lowest 3 levels).  Then f*V represents f acting on this ground state
# as a multiplication operator on symmetric functions.  T is a specific "spectral" operator.

# This suggests: T is possibly a shift on the fermionic lattice, and Psi = T . / V is
# a "kernel" of a correlator.  But making this precise is a research project, not a
# short proof.
print("\n\nRoute 3 assessment: Structurally suggestive but requires nontrivial")
print("identification of Psi with a fermionic operation.")
print("The (n^2-1)/n signature and pole-at-y=-1 structure is consistent with")
print("a vertex-operator/free-fermion representation.")
