s = "tree"

dic = {}
for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

s = sorted(dic.items(), key=lambda i: i[1], reverse=True)

ans = ''
for j in s:
    ans += j[0] * j[1]

print(ans)
