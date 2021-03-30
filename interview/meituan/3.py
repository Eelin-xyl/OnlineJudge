# 题目描述：
# 小美的记忆力超级棒，小团决定来考一考小美。小团给了小美 n 个数，从左到右排成一行，给了1 分钟让小美记住。然后小团会询问 m 次，每次都问数 x 第一次出现的位置和最后一次出现的位置，若数 x 没出现过，那么回答 0 即可。小美的记忆力好，但是 1 分钟记住这么多数实在是太难了，请你帮帮小美，完成这次不可能的挑战。


# 输入描述
# 第一行两个数 n, m。(1 ≤ n, m ≤ 50000)。

# 第二行 n 个数，第 i 个数是 ai。(1 ≤ ai ≤ 1000000000)。

# 接下来 m 行，每行一个数 x (1 ≤ x ≤ 1000000000)，代表一次询问。

# 输出描述
# 输出 m 行，若数 x 出现过，输出数 x 第一次出现的位置和最后一次出现的位置。若数 x 没出现过，输出 0。


# 样例输入
# 6 4
# 2 3 1 2 3 3
# 1
# 2
# 3
# 4
# 样例输出
# 3 3
# 1 4
# 2 6
# 0

# 提示
# 1 出现的位置有 3，所以答案为 3 3。
# 2 出现的位置有 1, 4，所以答案为 1 4。
# 3 出现的位置有 2, 5, 6，所以答案为 2 6。
# 4 没有出现过，所以答案为 0。


# 6 4
# 2 3 1 2 3 3
# 1
# 2
# 3
# 4

# one = input().split()
# m = int(one[1])
# lst = input().split()
# test = []
# for _ in range(m):
#     test.append(input())

lst = ['2', '3', '1', '2', '3', '3']
test = ['1', '2', '3', '4']
ans = []

for i in test:
    if lst.count(i) == 0:
        ans.append(str(0))
        continue
    if lst.count(i) == 1:
        k = lst.index(i)
        ans.append(str(k + 1) + ' ' + str(k + 1))
        continue
    a = lst.index(i)
    # for b in range(len(lst) - 1, -1, -1):
    for b in range(len(lst) - 1, 0, -1):
        if lst[b] == i:
            break
    ans.append(str(a + 1) + ' ' + str(b + 1))

for p in ans:
    print(p)
