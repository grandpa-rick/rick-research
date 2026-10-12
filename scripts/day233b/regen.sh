#!/bin/bash
# Regenerate RESULTS.txt from the committed scripts (Clio review 10-11, F1).
# Each section is stamped with the md5 of its script (+ eng.py/util.py) and the command line.
set -u
cd "$(dirname "$0")"
RUNS=("c0 c0.py" "s1_n6 s1.py 6" "s1b_n7 s1b.py 7" "s1c s1c.py" "s2_n7 s2.py 7" "s2b s2b.py" "s2c s2c.py" "s2d s2d.py 7" "s3_n6 s3.py 6" "s4_n8 s4.py 8" "s4b s4b.py 9" "s4c_n10 s4c.py 10")
for r in "${RUNS[@]}"; do
  set -- $r; name=$1; shift
  ( python3 "$@" > "$name.log" 2>&1; echo "EXIT $?" >> "$name.log" ) &
done
wait
{
  echo "# RESULTS.txt regenerated $(date -u +%FT%TZ) by regen.sh; engine md5 eng.py=$(md5sum eng.py|cut -c1-12) util.py=$(md5sum util.py|cut -c1-12)"
  for r in "${RUNS[@]}"; do
    set -- $r; name=$1; shift
    echo "### $name   [python3 $*; md5 $(md5sum "$1"|cut -c1-12); $(grep '^EXIT' "$name.log")]"
    grep -E '^\[(PASS|FAIL)\]|^C0' "$name.log"
  done
} > RESULTS.txt
