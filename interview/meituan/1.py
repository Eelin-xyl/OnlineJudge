# 题目描述：
# 小美想要为小团摆一行积木，每个积木上都有一个0-9的数字。现在已经摆好了 n 块积木，小美可以把其中一块积木替换成任意一块积木（也可以不替换），使得积木看起来更符合小美的审美。请你帮小美看看，替换后最好看的积木是什么样的。

# 摆好后的积木上面的数字，从左到右会形成一个数字串（由数字组成的字符串）。小美会根据这个数字串来评判积木的好看程度，小美有两条审美标准：

# ①回文数字串相比于非回文数字串更符合小美的审美。例如：12321、2332是回文数字串，而12212、2121不是回文数字串。

# ②数字串形成的数字更小更好看。例如：1312比1313更好看，0102比1102更好看。

# 小美会按照她的审美标准来判断两个数字串哪个更好看，即先按照审美标准①判断，若无法判断再按审美标准②判断。


# 输入描述
# 第一行一个数 T，表示一共有 T 组测试数据。(1 ≤ T ≤ 100)。

# 接下来 T 组数据，每组数据两行，

# 第一行一个数 n，表示有 n 块积木。(1 ≤ n ≤ 20000)。

# 第二行 n 个数字，第 i 块积木上的数字是 si。(si是0-9的数字)。

# 输出描述
# 每组数据输出一行，表示最终摆好的积木形成的数字串。


# 样例输入
# 2
# 5
# 00011
# 5
# 11210
# 样例输出
# 00001
# 01210

# 提示
# 第一组数据：
# 替换一块积木，无法使数字串变成回文数字串，因此只能数字串形成的数字最小。
# 第二组数据：
# 可以把第一块积木1换成0，也可以把第五块积木0换成1，从而使得积木是回文积木。又想要积木字典序最小，所以把第一块积木1替换成0。


# 2
# 5
# 00011
# 5
# 11210

# 00001
# 01210
# n = int(input())
# lst = []
# for _ in range(n):
#     l = int(input())
#     s = input()
#     lst.append(s)


lst = ['00011', '11210']

for k, i in enumerate(lst):
    if len(i) == 1:
        continue
    ct = 0
    for a in range(len(i) // 2 + 1):
        if i[a] != i[len(i) - a - 1]:
            ct += 1
            index = a
    if ct == 0:
        continue
    if ct < 2:
        if index == 0:
            new = i[-1] + i[1:]
            lst[k] = new
        else:
            new = i[0:index] + i[len(i) - index - 1] + i[index + 1:]
            lst[k] = new
    else:
        for b, c in enumerate(i):
            if c != '0':
                if b < len(i) - 1:
                    new = i[0:b] + '0' + i[b+1:]
                else:
                    new = i[0:b] + '0'
                lst[k] = new
                break
for ans in lst:
    print(ans)
