from helper import is_prime
from tqdm import tqdm
import time

while True:
    
    inp = input("\nEnter number/'q' to quit/'d' for PE solution: ")
    if inp == 'q':
        break
    elif inp == 'd':
        n = 600851475143
    else:
        n = int(inp)

    s = time.perf_counter()

    ans = 1
    if n % 2 == 0:
        ans = 2

    i = 1
    p_low = p_high = 1

    while i ** 2 <= n:

        if n % i == 0:
            temp = n // i
            if is_prime(i):
                p_low = i
            if is_prime(temp):
                ans = i
                break
        i += 2

    ans = max(p_low, ans)

    l = time.perf_counter() - s
    print(f"Largest prime factor of {n}: {ans}, time: {l}")

    if str(inp) == 'd':
        break