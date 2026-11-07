# S_14 control: re-certify all 4 S_14 shapes with prove281's certifyn pipeline (output certs14_*.json here)
import sys,os,subprocess
for sh in ['5333','4442','4433','44411']:
    subprocess.run([sys.executable,'-c',
      "import sys;sys.path.insert(0,'../prove281');sys.argv=['certifyn.py','14','%s'];exec(open('../prove281/certifyn.py').read())"%sh],check=True)
