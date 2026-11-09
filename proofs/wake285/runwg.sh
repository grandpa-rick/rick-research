#!/bin/bash
# usage: runwg.sh n timeout_s
n=$1; T=$2
start=$(date +%s)
printf "type\nD\n$n\nlcwgraphs\nD${n}_wg.txt\nqq\n" | timeout $T /home/agent/projects/proofs/wake285/coxeter/coxeter > log$n.txt 2>&1 &
pid=$!
peak=0
while kill -0 $pid 2>/dev/null; do
  p=$(pgrep -P $pid coxeter || echo $pid)
  r=$(awk '/VmRSS/{print $2}' /proc/$p/status 2>/dev/null); r=${r:-0}
  [ "$r" -gt "$peak" ] && peak=$r
  sleep 2
done
wait $pid; echo "exit $? elapsed $(( $(date +%s)-start ))s peakRSS ${peak}kB"
