def findingUsersActiveMinutes(logs, k):
    ans = [0 for _ in range(k)]
    if len(logs) == 1:
        ans[logs[0][1] - 1] += 1
        return ans
    l = []
    for i in logs:
        l.append((i[0], i[1]))
    l = set(l)
    l = sorted(l)
    pre = l[0][0]
    mi = 1
    for j in range(1, len(l)):
        if l[j][0] == pre:
            mi += 1
        else:
            ans[mi - 1] += 1
            mi = 1
            pre = l[j][0]
    ans[mi - 1] += 1

    return ans


print(findingUsersActiveMinutes(
    [[205740660, 1]], 17016))
