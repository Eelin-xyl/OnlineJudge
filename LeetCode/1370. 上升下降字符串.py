s = "rat"

st = s
st = set(st)
st = sorted(st)
dic = {}

for i in st:
    dic[i] = s.count(i)

ans = ''

l = []
for i in st:
    l.append(i)
l.reverse()

while len(ans) != len(s):
    for i in dic:
        if dic[i] == 0:
            continue
        ans += i
        dic[i] -= 1
    for j in l:
        if dic[j] == 0:
            continue
        ans += j
        dic[j] -= 1

print(ans)