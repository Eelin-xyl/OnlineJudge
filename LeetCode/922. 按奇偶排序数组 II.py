A = [4,2,5,7]

odd = []
even = [] 
for i in A:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
ans = []
while odd or even:
    ans.append(even.pop())
    ans.append(odd.pop())
print(ans)