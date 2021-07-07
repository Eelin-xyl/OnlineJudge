costs = [1, 6, 3, 1, 2, 5]
coins = 20

ans = 0

dic = {}
for i in costs:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
dic = sorted(dic)


for j in dic:
    while dic[j] != 0:
        coins -= j
        if coins < 0:
            break
        else:
            ans += 1
            dic[j] -= 1
    else:
        break

# costs = sorted(costs)
# for i in costs:
#     coins -= i
#     if coins >= 0:
#         ans += 1
#     else:
#         break
print(ans)
