# nth triangular number is n(n+1)/2

from helper import factors, triangular_number

threshold = 500

ans = 1
i = 1

from tqdm import tqdm
while len(factors(ans)) <= threshold:
    ans = triangular_number(i)
    i += 1

print(f"\nFirst triangular number with more than {threshold} factors: {ans}")