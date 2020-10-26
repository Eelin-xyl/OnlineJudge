import math

sr = 'aabac'
n = len(sr)
dct = {}
for i in sr:
    if i not in dct:
        dct[i] = 1
    else:
        dct[i] += 1
ans1 = math.factorial(n)
for j in dct:
    if dct[j] > 1:
        ans1 //= math.factorial(dct[j])
print(ans1)