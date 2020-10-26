nums = [8,1,2,2,3]

n = nums.copy()
n.sort()
s = set()
s.add((n[0], 0))
a = n.count(n[0])
for i in range(1, len(n)):
    if n[i] == n[i - 1]:
        continue
    s.add((n[i], a))
    c = n.count(n[i])
    a += c

ans = []
for x in nums:
    for y in s:
        if y[0] == x:
            ans.append(y[1])
            break
print(ans)