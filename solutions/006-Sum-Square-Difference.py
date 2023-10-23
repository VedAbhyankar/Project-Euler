# Sum of first n natural numbers = n(n+1)/2 = SN
# Sum of squares of first n natural numbers = n(n+1)(2n+1)/6 = SSqN

from helper import sum_first_n_powers

n = 100
ans = (sum_first_n_powers(n, 1) ** 2) - sum_first_n_powers(n, 2)

print(f"Difference between the sum of the squares and the square of the sum\
        of the first {n} numbers: {ans}")