A = ["cool","lock","cook"]
ans = {}
for i in A[0]:
    if i in ans:
        continue
    ans[i] = A[0].count(i)

for j in A:
    cha = {}
    for n in j:
        if n in cha:
            continue
        cha[n] = j.count(n)
    cp = ans.copy()
    # print(cha)
    for a in cp:
        if a not in cha:
            del ans[a]
        else:
            # print(a, ans[a], cha[a])
            ans[a] = min(ans[a], cha[a])
          
l = []
for b in ans:
    for _ in range(ans[b]):
        l.append(b)
print(l)