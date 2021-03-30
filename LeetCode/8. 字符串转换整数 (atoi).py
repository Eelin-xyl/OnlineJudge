def myAtoi(s: str) -> int:
    if s == '':
        return 0
    ans = ''
    for k, i in enumerate(s):
        if i == ' ':
            continue
        if i == '-':
            break
        if i == '+':
            break
        if i.isnumeric() == False:
            return 0
        else:
            break
    ans += i
    if k != len(s) - 1:
        for a in range(k + 1, len(s)):
            if s[a].isnumeric() == True:
                ans += s[a]
            else:
                break

    try:
        ans = int(ans)
    except:
        ans = 0

    ans = max(-2**31, ans)
    ans = min(ans, 2**31 - 1)

    return ans


print(myAtoi(""))
