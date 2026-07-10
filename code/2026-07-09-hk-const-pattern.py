"""Pattern-match the h_k^{(c)} constants for k = 0..5 across c ∈ {5, 6, 7, 9}.

Conjecture (from inspection):
- h_0 constant = 1
- h_1 constant = -c(c-1)
- h_2 constant = -2c
- h_3 constant = 6 · c(c-1)(c-2)
- h_4 constant = 12 · c(c-1)
- h_5 constant = -60 · c(c-1)(c-2)(c-3)

Verify these against c = 5, 6, 7, 9 data.
"""

# From extracted h_k data:
constants_data = {
    5:  {0: 1, 1: -20, 2: -10, 3: 360, 4: 240, 5: -7200},
    6:  {0: 1, 1: -30, 2: -12, 3: 720, 4: 360, 5: -21600},
    7:  {0: 1, 1: -42, 2: -14, 3: 1260, 4: 504, 5: -50400},
    9:  {0: 1, 1: -72, 2: -18, 3: 3024, 4: 864, 5: -181440},
}


def falling(c, k):
    r = 1
    for i in range(k):
        r *= (c - i)
    return r


conjectures = {
    0: lambda c: 1,
    1: lambda c: -c*(c-1),
    2: lambda c: -2*c,
    3: lambda c: 6 * c*(c-1)*(c-2),
    4: lambda c: 12 * c*(c-1),
    5: lambda c: -60 * falling(c, 4),
}


if __name__ == "__main__":
    print("Constant-pattern verification for h_k^{(c)}:")
    print("=" * 60)
    for k in range(6):
        print(f"\nk = {k}: conjecture = {conjectures[k].__code__.co_consts if hasattr(conjectures[k], '__code__') else 'literal 1'}")
        for c, data in constants_data.items():
            actual = data[k]
            predicted = conjectures[k](c)
            match = "✓" if actual == predicted else "✗"
            print(f"  c={c}: actual={actual:>10d}  predicted={predicted:>10d}  {match}")
