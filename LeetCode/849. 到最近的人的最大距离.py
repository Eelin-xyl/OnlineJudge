seats = [0, 0, 0, 1, 0, 1]

mx = 0
j = 0
if seats[0] == 0:
    ct = 0
    for j in seats:
        if j == 0:
            ct += 1
        else:
            break
    mx = max(mx, ct * 2 - 1)

ct = 0
seats = seats[j:]
for i in seats:
    if i == 0:
        ct += 1
    else:
        mx = max(mx, ct)
        ct = 0

if ct != 0:
    mx = max(mx, ct * 2 - 1)

print((mx + 1) // 2)
