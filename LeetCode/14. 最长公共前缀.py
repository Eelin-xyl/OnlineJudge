def longestCommonPrefix(strs):
    if strs == []:
        return ''
    if len(strs) == 1:
        return strs[0]

    strs.sort(key=len)
    ans = strs[0]
    i = 1
    while i < len(strs):
        for k, v in enumerate(ans):
            if v != strs[i][k]:
                ans = ans[0:k]
        i += 1
    return ans

    # ans = ''
    # i = 0
    # n = 0
    # a = []
    # while strs[i] != '':
    #     try:
    #         a.append(strs[i][n])
    #     except:
    #         break

    #     if i == len(strs) - 1:
    #         a = set(a)
    #         if len(a) == 1:
    #             ans += a.pop()
    #             i = -1
    #         else:
    #             break
    #         a = []
    #         n += 1
    #     i += 1

    return ans


print(longestCommonPrefix(["flower", "flow", "flight"]))
