S = 'example'

# if the element is same, return 0
st = set(S) 
if len(st) == 1:
    print(0)

# string is useless, we need something like dict to count the num of appearance
lst = []
for i in st:
    lst.append([S.count(i), i])

# the number cannot add, only minus, so sort and reverse them
lst.sort()
lst.reverse()

# if the latter not less the former, then cut the num of the latter
j = 1
ans = 0
while j < len(lst):
    if lst[j][0] >= lst[j - 1][0]:
        ans += lst[j][0] - lst[j - 1][0] + 1
        lst[j][0] = lst[j - 1][0] - 1

        # if num is 0, del this element
        if lst[j][0] == 0:
            del lst[j]
            continue
    j += 1

print(ans)