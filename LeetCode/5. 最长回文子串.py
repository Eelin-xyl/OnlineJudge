s = "babad"

if len(sorted(s)) == 1:
    print(s)


def huiwen(str):
    if len(str) == 1:
        return True

    for i in range(len(str) // 2):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


for a in range(len(s), 0, -1):
    for b in range(a, len(s) + 1):
        if huiwen(s[b - a: b]) == True:
            print(s[b - a: b])
