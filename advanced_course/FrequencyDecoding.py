# This code decrypts a secret word using frequency analysis.

m = [el for el in input()]
n = {el: m.count(el) for el in m}
k = int(input())

str = [tuple(a for a in input().split(": ")) for _ in range(k)]
dict1 = {}

for el in str:
    dict1[int(el[1])] = el[0]
for el in m:
    print(dict1[n[el]], end="")