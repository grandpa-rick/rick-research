"""Check b_1..b_9 (once computed) against OEIS."""
import json, urllib.request, sys

b_seq = [3, 27, 417, 7851, 164124, 3661389, 85384566]
try:
    with open('/home/agent/projects/beta-prime/code/day144_bk_extension/a8_b8.txt') as f:
        for line in f:
            if line.startswith('b_8'):
                b_seq.append(int(line.split('=')[1].strip()))
except FileNotFoundError:
    pass
try:
    with open('/home/agent/projects/beta-prime/code/day144_bk_extension/a9_b9.txt') as f:
        for line in f:
            if line.startswith('b_9'):
                b_seq.append(int(line.split('=')[1].strip()))
except FileNotFoundError:
    pass

print(f"b sequence ({len(b_seq)} terms): {b_seq}")


def query_oeis(seq, label):
    print("=" * 70)
    print(f"OEIS query [{label}]: {seq}")
    q = ",".join(str(x) for x in seq)
    url = f"https://oeis.org/search?q={q}&fmt=json"
    print(f"  URL: {url}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        if data.get('results'):
            for r in data['results'][:5]:
                print(f"  A{r['number']:06d}: {r.get('name', '')}")
                if 'formula' in r:
                    print(f"    Formula: {r['formula'][:200]}")
        else:
            print(f"  No OEIS matches.")
    except Exception as e:
        print(f"  OEIS query failed: {e}")


# Various tests
query_oeis(b_seq, "raw b_k")
# Try divided by 3
if all(x % 3 == 0 for x in b_seq):
    query_oeis([x // 3 for x in b_seq], "b_k / 3")
