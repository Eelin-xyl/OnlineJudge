def reverseBits(n):
    t = ''
    n = str(n)
    if n[0] == '-':
        t += n[0]
        n = n[1:]
    n = bin(int(n, 10))
    n = n[2:]
    n = (32 - len(n)) * '0' + n
    ans = ''
    for i in range(len(n) - 1, -1, -1):
        ans += n[i]
    ans = str(int(t + ans, 2))
    ans = (32 - len(ans)) * '0' + ans
    return int(t + ans)


print(reverseBits(43261596))
# 00000010100101000001111010011100
