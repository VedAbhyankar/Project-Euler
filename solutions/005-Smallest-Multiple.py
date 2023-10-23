n = 20

ans = 1
n = 20

def gcd(a, b):
    
    if a < b:
        a, b = b, a
    
    if b == 0:
        return a
    
    return gcd(b, a % b)

for i in range(2, n + 1):
    ans = (ans * i) // gcd(ans, i)

print(f"Smallest number divisible by all numbers from 1 to {n}: {ans}")