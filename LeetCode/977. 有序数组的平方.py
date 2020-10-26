A = [-3,-3,-2,1]
if len(A) == 1:
    print([A[0]**2])
A.append(float("inf"))
ans = []
for i in range(len(A)):
    if abs(A[i]) < abs(A[i + 1]):
        z = i
        break
del A[len(A)-1]
pre = z
post = z + 1
while pre >= 0 or post < len(A):
    if pre >= 0 and post < len(A):
        if A[pre]**2 <= A[post]**2:
            ans.append(A[pre]**2)
            pre -= 1
            continue
        else:
            ans.append(A[post]**2)
            post += 1
            continue    
    if pre >= 0 and post == len(A):
        ans.append(A[pre]**2)
        pre -= 1
        continue
    if pre < 0 and post < len(A):
        ans.append(A[post]**2)
        post += 1
        continue

print(ans)