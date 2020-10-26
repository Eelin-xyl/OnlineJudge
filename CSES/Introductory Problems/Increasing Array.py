leth = int(input())
ls = input().split()
cnt = 0
for i in range(1, leth):
    a = int(ls[i - 1])
    b = int(ls[i])
    if a > b:
        ls[i] = ls[i - 1]
        cnt += a - b
print(cnt)