sr = input()
cur = sr[0]
mx = 1
cnt = 0
for i in sr:
    if i == cur:
        cnt += 1
    else:
        if cnt > mx:
            mx = cnt
        cnt = 1
        cur = i
if cnt> mx:
    mx = cnt
print(mx)