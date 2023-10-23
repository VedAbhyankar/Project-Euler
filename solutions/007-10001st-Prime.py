p = [2]
n = 10001

i = 3

while len(p) != n:

    count = 0
    for prime in p:
        if i % prime == 0:
            break
        count += 1
    
    if count == len(p):
        p.append(i)
    
    i += 1

ans = p[-1]

print(f"The {n}st prime number is: {ans}")
