from helper import sieve_of_eratosthenes

n = 2000000

sieve = sieve_of_eratosthenes(n)
ans = sum(p for p in range(n + 1) if sieve[p])

print(f"\nSum of prime numbers till {n}: {ans}")
