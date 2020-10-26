n = int(input())
# mulit = 1
# ans = 0
# for i in range(2, n + 1):
#     mulit *= i
#     n = mulit // 10
#     if n != 0:
#         ans += n
#         multi = mulit // 10 ** n
# print(ans)


# ans = 0
# for i in range(1, n + 1):
#     while(i % 5 == 0):
#         ans += 1
#         i //= 5
# print(ans)
zero_count = 0
while n > 0:
    n //= 5
    zero_count += n
print(zero_count)