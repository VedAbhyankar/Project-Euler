from tqdm import tqdm

n = 1000
ans = 1

flag = False

for a in tqdm(range(n)):
    for b in range(a + 1, n):
        for c in range(b + 1, n):
            if a + b + c == n:
                if a**2 + b**2 == c**2:
                    ans = a*b*c
                    print(f"The product of the special pythagorean triplet: {ans}")
                    print(a, b, c)
                    flag = True
                    break
        if flag:
            break
    if flag:
        break

# Find a better solution than brute force