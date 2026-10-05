#!/bin/sh
# Day 205: run every reduction check; each writes a .log next to it.
cd /home/agent/projects/proofs/scripts/day205
for s in 0_conventions A_sigma_pi B_pi_split C_pieces D_assembly; do
  python3 reduction_$s.py > reduction_$s.log 2>&1
  grep OVERALL reduction_$s.log
done
