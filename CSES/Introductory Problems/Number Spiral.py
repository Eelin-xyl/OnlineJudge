n = int(input())
ls = []
for i in range(n):
    l = input().split()
    l[0] = int(l[0])
    l[1] = int(l[1])
    ls.append(l)

ans = []
for j in ls:
    if j[0] >= j[1]:
        if j[0] % 2 != 0:
            a = (j[0] - 1) ** 2 + j[1]
            ans.append(a)
        else:
            a = j[0] * j[0] - j[1] + 1
            ans.append(a)
    else:
        if j[1] % 2 != 0:
            a = j[1] * j[1] - j[0] + 1
            ans.append(a)
        else:
            a = (j[1] - 1) ** 2 + j[0]
            ans.append(a)
for m in ans:
    print(m)