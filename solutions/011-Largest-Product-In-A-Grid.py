from tqdm import tqdm
import math

with open("011-Largest-Product-In-A-Grid-Input.txt", "r") as file:
    lines = file.readlines()

matrix =[]
for line in lines:
    matrix.append([int(s) for s in line[:-1].split()])

ans = 1
products = []
for i in (range(len(matrix))):
    for j in range(len(matrix[0])):
        row_flag, col_flag = False, False
        if j + 4 <= len(matrix[0]):
            products.append(math.prod(matrix[i][j+k] for k in range(0, 4)))
            col_flag = True
        if i + 4 <= len(matrix):
            products.append(math.prod(matrix[i+k][j] for k in range(0, 4)))
            row_flag = True
        if row_flag and col_flag:
            products.append(matrix[i][j]*matrix[i+1][j+1]*matrix[i+2][j+2]*matrix[i+3][j+3])
            products.append(matrix[i+3][j]*matrix[i+2][j+1]*matrix[i+1][j+2]*matrix[i][j+3])

ans = max(products)
print(ans)