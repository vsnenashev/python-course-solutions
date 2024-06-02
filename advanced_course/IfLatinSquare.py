# This program checks if a given square matrix is a Latin square.

from copy import *

n = int(input())
mat = []

for i in range(n):
    temp = [int(num) for num in  input().split()]
    mat.append(temp)

matt = deepcopy(mat)  # Create a deep copy of the original matrix

flag = True    

# Check if each row contains all numbers from 1 to n
for i in range(n):
    mat[i].sort()
    if mat[i] != list(range(1, n + 1)):
            flag = False

# Transpose the matrix
for i in range(n):
    for j in range(i, n):
        matt[i][j], matt[j][i] = matt[j][i], matt[i][j]

for i in range(n):
    matt[i].sort()
    if matt[i] != list(range(1, n + 1)):
            flag = False
                        
if flag:
    print("YES")
else:
    print("NO")