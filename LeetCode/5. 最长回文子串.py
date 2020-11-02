s = "babad"

def huiwen(st):
    if len(set(s)) == 1:    return st
    a = 0
    b = len(st) - 1
    while a < b:
        if st[a] != st[b]:
            return ''
        a += 1
        b -= 1
    return st

i1 = 0
i2 = 0
if len(s) <= 1:
    print(s)
ans = s[0]
if len(set(s)) == 1: print(s)
while i1 < len(s):
    i2 = len(s) - 1
    while i1 < i2:
        if s[i1] == s[i2]:
            h = huiwen(s[i1 : i2 + 1])
            if len(ans) < len(h):
                ans = h
                break
        i2 -= 1
    i1 += 1

print(ans)