A = [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]

# if len <= 2 then cannot judge
if len(A) <= 2:
    print(0)

# make a list to contain the len of stable period
time = []
v = A[1] - A[0]
l = 1
for i in range(2, len(A)):
    # newv means the new velocity, then compare it with the former
    newv = A[i] - A[i - 1]
    if newv == v:
        # equal then add len
        l += 1
    else:
        # not equal, then judge if the len is enough
        if l >= 2:
            time.append(l)
        v = newv
        l = 1
if l >= 2:
        time.append(l)

# count the num of different situation
n = 0
for a in time:
    for b in range(3, a + 2):
        n += a + 1 - b + 1

print(n)



# A = [1,1,2,5,7]

# i = 0
# j = 1

# tm = []
# v = A[j] - A[i]
# while j <= len(A) - 1:
#     if A[j] - A[j - 1] != v:
#         if j - 1 - i >= 2:
#             tm.append([i, j - 1])
            
#         i = j - 1
#         v = A[j] - A[j - 1]
#     j += 1
# if j - 1 -i >= 2:
#     tm.append([i, j - 1])

# ans = 0
# for i in tm:
#     for j in range(1, i[1] - i[0]):
#         ans += i[1] - i[0] - j

# if ans > 1000000000:
#     print(-1)

# print(ans)