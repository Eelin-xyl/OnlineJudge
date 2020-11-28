A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

if not A or not B or not C or not D:
    print(0)

if A[-1] + B[-1] + C[-1] + D[-1] < 0:
    print(0)
if A[0] + B[0] + C[0] + D[0] > 0:
    print(0)

ans = 0

da = {}
for i in A:
    if i not in da:
        da[i] = 1
    else:
        da[i] += 1
sorted(da.keys())
db = {}
for i in B:
    if i not in db:
        db[i] = 1
    else:
        db[i] += 1
sorted(db.keys())
dc = {}
for i in C:
    if i not in dc:
        dc[i] = 1
    else:
        dc[i] += 1
sorted(dc.keys())
dd = {}
for i in D:
    if i not in dd:
        dd[i] = 1
    else:
        dd[i] += 1
sorted(dd.keys())

for a in da:
    if a + db[0] + dc[0] + dd[0] > 0:
        break
    for b in db:
        if a + b + dc[0] + dd[0] > 0:
            break
        for c in dc:
            if a + b + c + dd[0] > 0:
                break
            for d in dd:
                if a + b + c + d > 0:
                    break
                if a + b + c + d == 0:
                    ans += 1
print(ans)