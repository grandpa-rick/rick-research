# Strict #AXIS partition into prefix-strict + long-strict (n = 5..9)

**Date.** 2026-07-05. Runner: `partition.py` (this directory).

## Result

For every $n \in \{5,6,7,8,9\}$ the strict-#AXIS coordinate count
partitions cleanly into $(n-1)$ prefix-strict + $(n-1)$ long-strict:

| $n$ | prefix-strict | long-strict | both | neither | total | $2(n{-}1)$ | match |
|---:|---:|---:|---:|---:|---:|---:|:--:|
| 5 | 4 | 4 | 0 | 0 |  8 |  8 | YES |
| 6 | 5 | 5 | 0 | 0 | 10 | 10 | YES |
| 7 | 6 | 6 | 0 | 0 | 12 | 12 | YES |
| 8 | 7 | 7 | 0 | 0 | 14 | 14 | YES |
| 9 | 8 | 8 | 0 | 0 | 16 | 16 | YES |

**Conjecture confirmed** at $n = 5..9$: strict $\#\mathrm{AXIS} =
2(n-1) = (n-1)_{\rm prefix\text{-}strict} + (n-1)_{\rm long\text{-}strict}$.

## Per-$i$ structure

- **prefix-strict** coords are exactly $\{\mathrm{prefix}[1],\ldots,
  \mathrm{prefix}[n-2], \mathrm{prefix}[n]\}$ — the interior prefix
  slots plus the free top $\mathrm{prefix}[n]$. Interior prefixes are
  AXIS via the Day-71 simple-divert family; $\mathrm{prefix}[n]$ is
  AXIS via the Day-69 free-top family.
- **long-strict** coords are exactly $\{\mathrm{long}[1],\ldots,
  \mathrm{long}[n-1]\}$. $\mathrm{long}[1]$ is AXIS via the R-double /
  free-bottom family; $\mathrm{long}[2..n-1]$ are AXIS via the Day-72
  $\ell_j$-divert family.
- The three families of non-AXIS AII coords are:
  $\mathrm{prefix}[n-1]$, $\mathrm{long}[n]$, and every
  $\mathrm{short}[i]$ / $\mathrm{linkLHS}$ — all max group size $\le 2$
  in the current augmented registry. No surprises.

## Surprises / red flags

None. `n_both = 0` structurally (AII coords have a unique family label:
prefix XOR long XOR short XOR linkLHS). `n_neither = 0` empirically at
$n \le 9$ — no AXIS coord slipped into the short/linkLHS families.

## Caveat on the "strict-AXIS ray" phrasing

The task prompt describes strict-AXIS in terms of AII **extreme rays**
whose image "escapes Im($\pi_{\rm base}$)". This does not match the
established codebase notion: Day 80 Theorem 9.2 proves that **every**
AII extreme ray supports a single-column witness with image inside
Im($\pi_{\rm base}$), so by the "counterpositive" hint no rays would
qualify — contradicting the expected $2(n-1)$ counts. The expected
counts, in contrast, exactly match the Day-72 strict-AXIS **coordinate**
enumeration (3-clique on the wall $\{c = 0\}$; see
`code/2026-06-17-strict-axis/README.md`). I therefore treated the task
as a partition of the strict-AXIS coordinates. Rick may want to
clarify the intended definition if he really meant a ray-level object.
