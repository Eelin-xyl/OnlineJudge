n = 19
s = str(n)
seen = set()
nxt = 0
while nxt != 1:
    nxt = 0
    for i in range(len(s)):
        nxt += (int(s[-i - 1])) ** 2
    print(nxt)
    print(seen)
    if nxt in seen:
        break
    else:
        seen.add(nxt)
    s = str(nxt)