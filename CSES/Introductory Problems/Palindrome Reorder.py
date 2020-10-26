import sys
sr = input()
dct = {}
for i in sr:
    if i not in dct:
        dct[i] = 1
    else:
        dct[i] += 1
n = 0
odd = 1
for j in dct:
    if dct[j] % 2 != 0:
        n += 1
        odd = j
if n >= 2:
    print("NO SOLUTION")
    sys.exit()

if odd != 1:
    n = dct[odd]
    del dct[odd]

ans = ''
for k in dct:
    ans += k * (dct[k] // 2)
if odd != 1:
    sna = ans[::-1]
    ans += odd * n
    ans += sna
    print(ans)
else:
    ans += ans[::-1]
    print(ans)