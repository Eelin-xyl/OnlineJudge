# n = int(input())
# t = []
# for i in range(n):
#     s = input().split()
#     t.append([int(s[0]), int(s[1])])

# dic = {}
# key = set()
# mx = 0
# for a in t:
#     for b in range(a[0], a[1] + 1):
#         if b not in key:
#             dic[b] = 1
#             key.add(b)
#         else:
#             dic[b] += 1
#         mx = max(mx, dic[b])

# print(mx)

n = int(input())
customers = list()
for i in range(n):
    a, b = input().split()
    customers.append((int(a), int(b)))

ans = 0
count = 0
hold = dict()

times = set()
for a, b in customers:
    times.add(a)
    times.add(b)
    if a not in hold:
        hold[a] = 1
    else:
        hold[a] += 1
    
    if b not in hold:
        hold[b] = -1
    else:
        hold[b] -= 1
times = sorted(list(times))

for t in times:
    if t in hold:
        count += hold[t]
    ans = max(ans, count)
print(ans)