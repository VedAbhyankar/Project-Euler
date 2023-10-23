# Sum of first n natural numbers = n(n+1)/2 = SN
# Sum of squares of first n natural numbers = n(n+1)(2n+1)/6 = SSqN
# Thus, after factorisation SN^2 - SSqN = (n-1)n(n+1)(3n+1)/12

n = 100
ans = (((n * (n + 1)) / 2) ** 2) - ((n * (n + 1) * ((2 * n) + 1)) / 6)

print(f"Difference between the sum of the squares and the square of the sum\
        of the first {n} numbers: {ans}")