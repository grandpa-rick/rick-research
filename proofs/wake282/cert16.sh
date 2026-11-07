#!/bin/bash
# certify one S_16 shape with prove281 certifyn pipeline
cd /home/agent/projects/proofs/wake282
timeout 1500 python3 -c "import sys;sys.path.insert(0,'../prove281');sys.argv=['certifyn.py','16','$1'];exec(open('../prove281/certifyn.py').read())" > out_cert16_$1.txt 2>&1
echo "$1 exit $? $(grep -c TWIN out_cert16_$1.txt) twin lines"
