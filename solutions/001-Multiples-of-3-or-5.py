m = 1000
from tqdm import tqdm
ans = sum(i for i in tqdm(range(m)) if i % 3 == 0 or i % 5 == 0)

print(f"\nSum of multiples of 3 or 5 under {m}: {ans}")