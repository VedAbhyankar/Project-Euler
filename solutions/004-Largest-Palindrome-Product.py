ans = max(i*j for i in range(100, 1000) for j in range(100, 1000) \
                                        if str(i*j)[::-1] == str(i*j))

print(f"Largest palindrome number made from a prodict of 2 3-digit numers: {ans}")
