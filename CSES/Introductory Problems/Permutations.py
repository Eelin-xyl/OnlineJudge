import sys

n = int(input())
if n == 1:
    print(1)
    sys.exit()
if n == 2 or n == 3:
    print("NO SOLUTION")
    sys.exit()

# ans =''
# for i in range(2, n + 1, 2):
#     ans += str(i) + ' '
# for j in range(1, n + 1, 2):
#     ans += str(j) + ' '
# print(ans)

# ans = list()
# ans.extend(list(range(2, n + 1, 2)))
# ans.extend(list(range(1, n + 1, 2)))
# print(' '.join([str(x) for x in ans]))
# for i in ans:
#     print(i, end=' ')


print(' '.join([str(x) for x in range(2, n + 1, 2)]), end=' ')
print(' '.join([str(x) for x in range(1, n + 1, 2)]))
