def isMatch(s, p):
    p += '+'
    p = p.split('*')
    p = p[:-1]
    ct = 0
    a = 0
    num = 0
    k = 0
    while a < len(s):
        for i in range(a, len(s)):
            if s[i] == s[a]:
                ct += 1
                continue
            else:
                break
        while k < len(p):
            for j in range(k, len(s)):
                if s[j] == '*':
                    break
                if s[j] == s[k]:
                    num += 0
                    continue
                # elif s[j] =
        ct = 0
        a = i


print(isMatch(s="aaba", p="ab*a*c*a"))
