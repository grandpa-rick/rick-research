"""
Wider, more diagnostic version of the test:
- Functional coordinates up to ±6.
- For each decomposition, dump the set of distinct level-count signatures
  observed; check whether any of the three Bucket-2 signatures appears.
"""

from __future__ import annotations

from collections import Counter
from itertools import product

from test_bucket2_match import (
    BASE_IRREPS, T_I2, T_I236, T_I23456, TARGETS,
    decompositions_of_22, enumerate_functionals,
    irrep_weight_multiset, level_signature, union_weight_multiset,
)


def histogram_for_decomp(decomp, max_coord):
    W = union_weight_multiset(decomp)
    fs = enumerate_functionals(max_coord)
    sig_counter: Counter = Counter()
    sig_to_examples: dict = {}
    for f in fs:
        sig = level_signature(W, f)
        sig_counter[sig] += 1
        sig_to_examples.setdefault(sig, []).append(f)
    return W, sig_counter, sig_to_examples


def closest_signatures(sigs: list[tuple[int, ...]], target: tuple[int, ...], n: int = 5):
    """Among observed signatures, rank by L1 distance after padding to same length."""
    L = max(len(target), max(len(s) for s in sigs))
    def pad(s):
        return tuple([0] * (L - len(s)) + list(s))
    t = pad(target)
    ranked = sorted(set(sigs), key=lambda s: sum(abs(a - b) for a, b in zip(pad(s), t)))
    return ranked[:n]


def main():
    decomps = decompositions_of_22()
    print(f"{len(decomps)} decompositions; functionals with |coord| <= 6.")
    print()

    any_full_match = False
    overall_observed_sigs: set = set()
    for decomp in decomps:
        labels = Counter(lab for (lab, hw, dd) in decomp)
        W, sig_counter, sig_to_examples = histogram_for_decomp(decomp, max_coord=6)
        observed = set(sig_counter.keys())
        overall_observed_sigs |= observed

        hits = {t: t in observed for t in TARGETS}
        if any(hits.values()):
            print(f"Decomp {dict(labels)}: hits {hits}")
            for t, label in TARGETS.items():
                if hits[t]:
                    print(f"  {label} = {t}: example functionals = {sig_to_examples[t][:5]}")
            if all(hits.values()):
                # Try independent triple
                from test_bucket2_match import linearly_independent_triple
                triple = linearly_independent_triple(
                    sig_to_examples[T_I2], sig_to_examples[T_I236], sig_to_examples[T_I23456]
                )
                if triple:
                    print(f"  *** FULL MATCH (lin-indep): {triple}")
                    any_full_match = True

    print()
    print(f"Total distinct level-signatures observed across all decomps: {len(overall_observed_sigs)}")

    # For the most flexible decomp (e.g., 2 vec + 10 trivials, etc.) print closest signatures
    # to each Bucket-2 target.
    print()
    print("Closest signatures observed (across all decomps) to each Bucket-2 target:")
    all_sigs = list(overall_observed_sigs)
    for t, label in TARGETS.items():
        close = closest_signatures(all_sigs, t, n=10)
        print(f"  {label} = {t}:")
        for s in close:
            print(f"    {s}")
        print()

    if not any_full_match:
        print(">>> NO FULL MATCHES. OQ-NAITOSAGAKI-BDI REFUTED at the marginal-pattern level.")


if __name__ == "__main__":
    main()
