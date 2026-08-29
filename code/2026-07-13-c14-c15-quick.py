"""Quick timing test for extract_h_k at c=14, jmax=6."""
import sys
import time
from importlib import util
from math import factorial

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)

print("Building tables jmax=6+2...", flush=True)
t0 = time.time()
tables = mod.build_e2_tables(max_j=8)
print(f"  tables done in {time.time()-t0:.1f}s", flush=True)

print("\nExtracting h_k for c=14, a=14, b=14, jmax=6:", flush=True)
t0 = time.time()
hks = mod.extract_h_k(14, 14, 14, 6, tables)
print(f"  done in {time.time()-t0:.2f}s, got {len(hks) if hks else None} values", flush=True)

print("\nExtracting for a=20, b=15 (bigger):", flush=True)
t0 = time.time()
hks = mod.extract_h_k(20, 15, 14, 6, tables)
print(f"  done in {time.time()-t0:.2f}s", flush=True)

# Test jmax=8
print("\nBuilding tables jmax=8+2...", flush=True)
t0 = time.time()
tables8 = mod.build_e2_tables(max_j=10)
print(f"  tables done in {time.time()-t0:.1f}s", flush=True)

print("Extracting h_k for c=14, jmax=8:", flush=True)
t0 = time.time()
hks = mod.extract_h_k(20, 15, 14, 8, tables8)
print(f"  done in {time.time()-t0:.2f}s", flush=True)
