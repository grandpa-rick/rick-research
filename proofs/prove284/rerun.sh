#!/bin/bash
# prove284: replay every census certificate with verifyn_ext.py (superset of verifyn_u.py); then the 5533 layer certs.
cd /home/agent/projects/proofs
for f in wake282/certs14_*.json prove281/certs15_*.json wake282/certs16_*.json prove283/certs16_6433_ext.json; do
  echo "== $f"; python3 prove283/verifyn_ext.py $f 2>&1 | awk '{print $NF, $(NF-1)}' | sort | uniq -c
done
echo "== 5533 layer certs"; cd prove282 && python3 verify_red.py rest16.json 2>&1 | tail -8
