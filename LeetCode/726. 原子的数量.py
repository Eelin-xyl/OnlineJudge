formula = "((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"

lst = []
c = ''

a = ''
n = ''

for i in formula:
    if i.islower() == True:
        a += i
        continue
    if i.isnumeric() == True:
        n += i
        continue
    if i.isupper() == True:
        if a == '':
            a = i
            if n != '':
                lst.append(int(n))
                n = ''
            continue
        else:
            if a == '':
                if n != '':
                    lst.append(int(n))
            else:
                if n == '':
                    n = 1
                lst.append([a, int(n)])
            a = ''
            n = ''
            a += i
    if i == '(' or i == ')':
        if a == '':
            if n != '':
                lst.append(int(n))
        else:
            if n == '':
                n = 1
            lst.append([a, int(n)])
        a = ''
        n = ''
        lst.append(i)

if a != '':
    if n == '':
        n = 1
    lst.append([a, int(n)])
else:
    if n != '':
        lst.append(int(n))

print(lst)

a = 0
b = len(lst) - 1

while a <= b:
    if type(lst[a]) == list:
        a += 1
        continue
    if type(lst[b]) == list:
        b -= 1
        continue
    print(lst[b])
    num = lst[b]
    b -= 1

    for j in range(a + 1, b):
        if type(lst[j]) == list:
            lst[j][1] *= num

    del lst[b + 1]
    del lst[b]
    del lst[a]
    a = 0
    b = len(lst) - 1

lst.sort()
print(lst)

dic = {}
for i in lst:
    if i[0] not in dic:
        dic[i[0]] = i[1]
    else:
        dic[i[0]] += i[1]

print(dic)

ans = ''
for k in dic:
    ans += k
    if dic[k] != 1:
        ans += str(dic[k])

print(ans)
