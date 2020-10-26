S = "a#c"
T = "b"

# s = []
# t = []
# for i in S:
#     if i != '#':
#         s.append(i)
#     elif s:
#         s.pop()
# print(s)
# for j in T:
#     if j != '#':
#         t.append(j)
#     elif t:
#         t.pop()
# print(t)




S = "##ab#c"
T = "ad#c"
# s = list(S)
# t = list(T)
# for i in range(len(s)):
#     if s[i] == '#':
#         s[i] = '\b'
# S = ''.join(s)
# print(S)
# for j in range(len(t)):
#     if t[j] == '#':
#         t[j] = '\b'
# T = ''.join(t)
# print(T)
# for a in S:
#     print(a)
# for a in T:
#     print(a)
# print(S == T)



s = list(S)
s.append(0)
t = list(T)
t.append(0)
i = j = 0
while s[i] != 0:
    if s[i] == '#':
        if not s[i - 1]:
            s.pop(i)
        else:
            i -= 1
            s.pop(i)
            s.pop(i)
        continue
    i += 1
s.pop()
while t[j] != 0:
    if t[j] == '#':
        if not t[j - 1]:
            t.pop(j)
        else:
            j -= 1
            t.pop(j)
            t.pop(j)
        continue
    j += 1
t.pop()
print(t == s)