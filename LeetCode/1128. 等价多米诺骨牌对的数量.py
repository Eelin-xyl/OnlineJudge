dominoes = [[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2]]
for i, v in enumerate(dominoes):
    v.sort()
    dominoes[i] = str(v[0]) + str(v[1])

s = {}

for i in dominoes:
    if i not in s:
        s[i] = 1
    else:
        s[i] += 1

ans = 0

for i in s:
    if s[i] > 1:
        for j in range(1, s[i]):
            ans += j

print(ans)