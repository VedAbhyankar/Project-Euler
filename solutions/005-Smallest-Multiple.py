from helper import gcd

ans = 1
n = 20

for i in range(2, n + 1):
    ans = (ans * i) // gcd(ans, i)

print(f"Smallest number divisible by all numbers from 1 to {n}: {ans}")