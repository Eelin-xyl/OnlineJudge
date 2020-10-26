s = "5525"
a = 9
b = 2
s = list(s)
def leijia(s, a):
    for num in range(len(s)):
        s[num] = int(s[num])
    for i in range(1, len(s), 2):
        s[i] += a
        s[i] %= 10
    for num in range(len(s)):
        s[num] = str(s[num])
def lunzhuan(s, b):
    for num in range(len(s)):
        s[num] = int(s[num])
    t = s[0]
    del s[0]
    s.append(t)
    for num in range(len(s)):
        s[num] = str(s[num])
print('初态' + ''.join(s))
leijia(s, a)
print('累加' + ''.join(s))
lunzhuan(s, b)
print('轮转' + ''.join(s))