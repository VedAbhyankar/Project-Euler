from tqdm import tqdm

n = 2000000

primes = [True] * (n + 1)
primes[0] = primes[1] = False

ans = 0

for i in tqdm(range(2, n + 1)):
    if primes[i]:
        ans += i
        if 2*i <= n:
            for j in range(2*i, n + 1, i):
                primes[j] = False

# print(primes)
print(ans)
