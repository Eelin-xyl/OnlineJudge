num = "1173"
k = 2
# if k == len(num) or len(num) == 1:
#     print("0")

# while k > 0:
#     i = 0
#     while i < len(num) - 1:
#         if num[i] > num[i + 1]:
#             new = ''
#             for a in range(len(num)):
#                 if a != i:
#                     new += num[a]
#             num = new
#             k -= 1
#             break
#         elif i + 1 == len(num) - 1:
#             num = num[:-1]
#             k -= 1
#             break
#         i += 1
# print(str(int(num)))

if k == 0:
    print(num)
if len(num) == k:
    print('0')
if len(num) == 1:
    print(num)

i = 1
while k > 0:
    if num[i - 1] > num[i]:
        new = ''
        for a in range(len(num)):
            if a != i - 1:
                new += num[a]
        num = str(int(new))
        k -= 1
        if i == len(num):
            i -= 1
        continue
    i += 1
    if i == len(num):
        break

if k > 0:
    print(str(int(num[0 : len(num) - k])))
else:
    print(num)