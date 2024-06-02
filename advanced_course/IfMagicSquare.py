# The program checks if a given square matrix is a magic square.

n = int(input())
mat = []

for i in range(n):
    temp = [int(num) for num in  input().split()]
    mat.append(temp)
    
# Calculate the magic sum for comparison
s = int(sum(range(1, n ** 2 + 1)) / n)

res = "YES"

matx = []
matxx = []
ran = [i for i in range(1, n ** 2 + 1)]

for i in mat:
    matx.extend(i)

# Check if all elements are unique and within the range [1, n^2]    
for el in matx:
    if el in ran:
        matxx.append(el)
        ran.remove(el)
        
if matx != matxx:
    res = "NO"

sum1 = 0
sum2 = 0

for i in range(n):
    sum1 += mat[i][i]
    if sum(mat[i]) != s:
        res = "NO"
    sum2 += mat[i][0]

# Compare sums of main diagonal and first column to the magic sum
if sum1 != s:
    res = "NO"
if sum2 != s:
    res = "NO"

