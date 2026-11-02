# wrong criterion: "adj" := T u {a_j} co-closed (always true for a_j simple) -> predicts every pair local
import re
lines=[l for l in open('a3_h6.out') if ' j=' in l]
wrong=sum(1 for l in lines if (' far' in l) )  # pairs this wrong criterion mislabels
nonloc=sum(1 for l in lines if re.search(r'local (\d+)/(\d+)',l) and re.search(r'local (\d+)/(\d+)',l).group(1)!=re.search(r'local (\d+)/(\d+)',l).group(2))
print("wrong criterion predicts 72/72 local; actually non-local:",nonloc,"-> mismatches",nonloc)
