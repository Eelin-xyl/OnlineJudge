A = [-1, -1]
B = [-1, 1]
C = [-1, 1]
D = [1, -1]

if not A or not B or not C or not D:
    print(0)

ans = 0

da = {}
for i in A:
    if i not in da:
        da[i] = 1
    else:
        da[i] += 1
sa = {}
for i in sorted(da):
    sa[i] = da[i]
db = {}
for i in B:
    if i not in db:
        db[i] = 1
    else:
        db[i] += 1
sb = {}
for i in sorted(db):
    sb[i] = db[i]
dc = {}
for i in C:
    if i not in dc:
        dc[i] = 1
    else:
        dc[i] += 1
sc = {}
for i in sorted(dc):
    sc[i] = dc[i]
dd = {}
for i in D:
    if i not in dd:
        dd[i] = 1
    else:
        dd[i] += 1
sd = {}
for i in sorted(dd):
    sd[i] = dd[i]

A = [i for i in sa.keys()]
B = [i for i in sb.keys()]
C = [i for i in sc.keys()]
D = [i for i in sd.keys()]

for a in A:
    if a + B[0] + C[0] + D[0] > 0:
        break
    for b in B:
        if a + b + C[0] + D[0] > 0:
            break
        for c in C:
            if a + b + c + D[0] > 0:
                break
            for d in D:
                if a + b + c + d > 0:
                    break
                if a + b + c + d == 0:
                    ans += sa[a] * sb[b] * sc[c] * sd[d]
print(ans)