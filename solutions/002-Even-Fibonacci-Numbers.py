# Fibonacci numbers are defined as f(n+1) = f(n) + f(n-1), f(0) = 0, f(1) = 1

f_curr, f_next = 0, 1
threshold = 4000000

ans = 0

while f_next < threshold:

    if f_next % 2 == 0:
        ans += f_next

    f_curr, f_next = f_next, f_curr + f_next

print(f"\nSum of even fibonacci numbers less than {threshold}: {ans}")    
