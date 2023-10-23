m = 1000

ans = sum(i for i in range(m) if i % 3 == 0 or i % 5 == 0)

print(f"\nans of multiples of 3 or 5 under {m}: {ans}")