N = 600851475143
n = N

ans, p = 1, 2           # set ans to be 1 and p to be the smallest prime

while n % p == 0:       # divide out 2 so we can iterate p by 2 instead of 1
    n = n // p
    ans = p

p += 1
while n > 1:

    while n % p == 0:   # only enter loop of p is a prime by dividing out p
        n = n // p      # divide out the prime factor p, 
        ans = p         # set ans to be the current largest prime found
    
    p += 2

print(f"Largest prime factor of {N}: {ans}")