"""Day 100 — Merge Q_7 and Q_8 into the master Q_k catalog."""

import json

# Load existing catalog
with open('/home/agent/projects/code/2026-07-11-Qk-catalog.json') as f:
    catalog = json.load(f)

# Load new fits
with open('/home/agent/projects/code/2026-07-16-day100-Qk-catalog-extend.json') as f:
    new = json.load(f)

for k in ['7', '8']:
    if new['per_k'].get(k) is None:
        print(f"k={k}: no new fit available")
        continue
    r = new['per_k'][k]
    catalog['Q_k_extended'][k] = {
        'poly_expanded': r['poly_expanded'],
        'poly_factored': r['poly_factored'],
        'total_degree': r['total_degree'],
        'num_samples': None,
        'fit_time_sec': None,
        'cv_c8_pass': None,  # different CV protocol used; see below
        'cv_holdout_pass': f"{r['cv_ok']}/{r['cv_ok'] + r['cv_fail']} at c ∈ [c_max+1, c_max+3]",
        'day': '100 (2026-07-16)',
    }
    print(f"k={k}: merged (total degree {r['total_degree']})")

# Update note
catalog['note'] = (
    "Q_k(a, b, c) — normalized h_k^{(c)}(a, b) polynomials. "
    "h_k^{(c)}(a, b) = (a+3)_{c-1-k} * (b+2)_{c-1-k} * Q_k(a, b, c). "
    "k = 0..5 from Day 88 fit; k = 6 from Day 89; k = 7, 8 from Day 100."
)
catalog['Day_100_source'] = "2026-07-16-day100-Qk-catalog-extend.py (coefficient-wise interpolation)"

out = '/home/agent/projects/code/qk-catalog.json'
with open(out, 'w') as f:
    json.dump(catalog, f, indent=2, default=str)
print(f"\nSaved {out}")

# Also update the original catalog file
with open('/home/agent/projects/code/2026-07-11-Qk-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2, default=str)
print(f"Updated 2026-07-11-Qk-catalog.json in place")
