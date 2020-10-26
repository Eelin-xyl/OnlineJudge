nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]

def check(n):
    if len(n) < 2:
        return False
    if len(n) == 2:
        return True
    for a in range(1, len(n)):
        if n[a] - n[a - 1] != n[1] - n[0]:
            return False
    return True

find = []
for i in range(len(l)):
    find.append([l[i], r[i]])

ans = []
for j in find:
    num = nums[j[0] : j[1] + 1]
    num.sort()
    ans.append(check(num))
print(ans)