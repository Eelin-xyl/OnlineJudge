def generateParenthesis(n: int):
    ans = list()
    for i in range(1, n + 1):
        a = sum(range(1, i + 1))
        m = n - i
        ans.append(a**m)
        p = '('
        q = ')'
        s = '()'
        for j in range(a**m):
            pass

    t = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    return ans


n = 3
print(generateParenthesis(n))
