# a = int(input())
# b = str(input())
# l = set(b.split())
# for i in range(1, a + 1):
#     c = str(i)
#     if c not in l:
#         print(i)
#         break
#     l.remove(c)

a = int(input())
b = str(input()) + ' '
n = set(range(1, a+1))
c = ''
for i in b:
    if i != ' ':
        c += i
    else:
        n.remove(int(c))
        c = ''
print(n.pop())