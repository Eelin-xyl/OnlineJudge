arr = [0,1,2,3,4,5,6,7,8]

ans = list()
for i in arr:
    n = 0
    j = i
    while i != 0:
        if i % 2 == 1:
            n += 1
            i -= 1
            i //= 2
        else:   i //= 2
    ans.append((n, j))
ans.sort()
res = list()
for a in ans:
    res.append(a[1])
print(res)