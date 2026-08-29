"""Verify [E_3^{b/2}] tops[b] = (-3)^{b/2} * (b-1)!! for even b."""
from math import factorial

def double_factorial(n):
    if n <= 0: return 1
    return n * double_factorial(n - 2)

emp = {2: -3, 4: 27, 6: -405, 8: 8505}
for b, val in emp.items():
    predicted = (-3)**(b//2) * double_factorial(b - 1)
    print(f"b={b}: empirical={val}, predicted (-3)^{b//2} * ({b}-1)!! = {predicted}, match={val == predicted}")

# Extended predictions
for b in [10, 12, 14, 16, 20]:
    predicted = (-3)**(b//2) * double_factorial(b - 1)
    print(f"b={b}: predicted [E_3^{b//2}] tops[{b}] = (-3)^{b//2} * {b-1}!! = {predicted}")
