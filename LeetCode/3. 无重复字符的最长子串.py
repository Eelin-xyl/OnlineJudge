s = "abcdbqwe"
if len(s) == 1:
    print(1)
if len(s) == 0:
    print(0)
a, b = s[0], 1
for i in range(1, len(s)):
    if s[i] not in a:
        a += s[i]
        if len(a) > b:
            b = len(a)
    else:
        t = i - 1
        while True:
            if s[t] == s[i]:
                a = s[t + 1:i + 1]
                break
            t -= 1
print(b)