"""Task 3 — Dip formula empirical check.

Rick's PROVE.md Day-83 dip-formula prediction:
    Δ(β − β')_{c-1→c} = 2·v₂(c−1) + δ_s(c),  δ_s ∈ {-1, 0, +1}

Alternative form (from 2026-07-07-dip-formula.md for odd c):
    Δβ'(c) = 1 − max(2, v₂(c−1))  for odd c ≥ 3

Compute both at every c ∈ {5..10} where we have Clio's data.
"""
from hc import s2, v2, beta, gamma, CLIO_BETA_PRIME


print("=" * 78)
print("Task 3 — Dip formula check on Clio's data c = 4..10")
print("=" * 78)

# For each c ≥ 5, compute:
#   Δβ(c) = β(c) - β(c-1)          — from formula
#   Δβ'(c) = β'(c) - β'(c-1)        — from Clio's data
#   Δ(β-β')(c) = Δβ(c) - Δβ'(c)
#   Predicted Δ(β-β') = 2·v₂(c-1)   — Rick's PROVE.md prediction
#   δ_s(c) = actual - predicted     — carry correction

print("\n(1) Δ(β − β') formula: predicted = 2·v₂(c−1), actual from data")
print(f"{'c':>3} {'Δβ':>4} {'Δβ prime':>8} {'Δ(β-β prime)':>13} {'2·v2(c-1)':>11} {'δ_s':>5}")
for c in range(5, 11):
    if (c - 1) not in CLIO_BETA_PRIME or c not in CLIO_BETA_PRIME:
        continue
    dbeta = beta(c) - beta(c - 1)
    dbetap = CLIO_BETA_PRIME[c] - CLIO_BETA_PRIME[c - 1]
    dcheck = dbeta - dbetap
    predicted = 2 * v2(c - 1)
    delta_s = dcheck - predicted
    print(f"{c:>3} {dbeta:>4} {dbetap:>8} {dcheck:>13} {predicted:>11} {delta_s:>5}")


print("\n(2) Odd-c form: Δβ'(c) = 1 − max(2, v₂(c−1)), predicted vs actual")
print(f"{'c':>3} {'v2(c-1)':>8} {'max(2,·)':>9} {'predicted Δβ prime':>19} {'actual':>7} {'match':>7}")
for c in [5, 7, 9]:
    if (c - 1) not in CLIO_BETA_PRIME or c not in CLIO_BETA_PRIME:
        continue
    v = v2(c - 1)
    m = max(2, v)
    pred = 1 - m
    actual = CLIO_BETA_PRIME[c] - CLIO_BETA_PRIME[c - 1]
    match = "YES" if pred == actual else "NO"
    print(f"{c:>3} {v:>8} {m:>9} {pred:>19} {actual:>7} {match:>7}")


print("\n(3) Predictions for c = 11..17")
print(f"{'c':>3} {'β(c)':>5} {'γ(c)':>5} {'β prime pred':>13} {'method':>50}")

# Extend using: for even c, β' ≈ γ(c) (dip 0 or 1). For odd c, use odd-c dip formula.
predicted_bp = dict(CLIO_BETA_PRIME)
for c in range(11, 18):
    if c % 2 == 1:
        # odd c: Δβ' = 1 - max(2, v_2(c-1))
        v = v2(c - 1)
        delta = 1 - max(2, v)
        if (c - 1) in predicted_bp:
            bp_pred = predicted_bp[c - 1] + delta
            method = f"β'({c-1}) + (1 - max(2, v₂({c-1})={v})) = β'({c-1}) + {delta}"
        else:
            bp_pred = gamma(c - 1) + delta
            method = f"γ({c-1}) + (1 - max(2, {v}))"
    else:
        # even c: β' ≈ γ(c) (dip 0 assumption). Refined: use empirical rule
        # from Clio's data (β'(c) = γ(c) at c=4,6,8; γ-1 at c=10).
        bp_pred = gamma(c)
        method = f"γ({c}) — even-c saturation assumption (dip=0)"
    predicted_bp[c] = bp_pred
    print(f"{c:>3} {beta(c):>5} {gamma(c):>5} {bp_pred:>13} {method:>50}")


print()
print("(4) mod-8 test predictions:")
print("Under Rick's mod-8 hypothesis:")
print(f"  c=11 (v₂(c-1)=1): dimer holds → Δβ' = -1")
print(f"        β'(11) predicted = {predicted_bp[11]}")
print(f"  c=13 (v₂(c-1)=2): dimer holds → Δβ' = -1")
print(f"        β'(13) predicted = {predicted_bp[13]}")
print(f"  c=15 (v₂(c-1)=1): dimer holds → Δβ' = -1")
print(f"        β'(15) predicted = {predicted_bp[15]}")
print(f"  c=17 (v₂(c-1)=4): DIMER FAILS → Δβ' = 1 - 4 = -3")
print(f"        β'(17) predicted = {predicted_bp[17]}  (drop 3 from β'(16))")
print()
print("Extraordinary claim: β'(17) drops 3 from β'(16), vs drop 1 at c=11,13,15")
print("If Clio's engine confirms β'(17) = γ(16) - 3, mod-8 hypothesis is confirmed.")


# WRITE CSV
print("\n(5) Writing CSV: beta_prime_c4_c17.csv")
import csv
csv_path = "beta_prime_c4_c17.csv"
with open(csv_path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["c", "beta", "gamma", "beta_prime_reported", "beta_prime_predicted",
                "clio_match", "v2_c_minus_1", "argmin_notes"])
    for c in range(4, 18):
        b_c = beta(c)
        g_c = gamma(c)
        bp_reported = CLIO_BETA_PRIME.get(c, "")
        bp_pred = predicted_bp.get(c, "")
        clio_match = "Y" if bp_reported == bp_pred else ("?" if bp_reported == "" else "N")
        v2m1 = v2(c - 1) if c > 1 else "inf"
        notes = ""
        if c == 5:
            notes = "verified (3,0,2), direct scan box=48"
        elif c in (4, 6, 7, 8, 9, 10):
            notes = "Clio's reported witness"
        else:
            notes = "predicted, awaiting Clio's engine"
        w.writerow([c, b_c, g_c, bp_reported, bp_pred, clio_match, v2m1, notes])
print(f"  → wrote {csv_path}")
