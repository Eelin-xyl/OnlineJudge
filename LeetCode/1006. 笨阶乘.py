def clumsy(N):
    i = N
    lst1 = []
    lst2 = []
    while i > 0:
        l = i
        if i - 1 > 0:
            l *= i - 1
        if i - 2 > 0:
            l //= i - 2
        if i - 3 > 0:
            lst2.append(i - 3)
        lst1.append(l)
        i -= 4

    ans = lst1[0] * 2
    for a in lst1:
        ans -= a
    for b in lst2:
        ans += b
    return ans


print(clumsy(1))
