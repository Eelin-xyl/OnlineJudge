def isMatch(s, p):
    p += '+'
    p = p.split('*')
    dic = {}
    for i in p:
        for j in i:
            if j not in dic:
                dic[j] = 1
            else:
                dic[j] += 1
        dic[j] = float('inf')
    del dic['+']
    for v in s:
        if v not in dic or dic[v] == 0:
            if '.' in dic and dic['.'] >0:
                dic['.'] -= 1
            else:
                return False
        elif dic[v] == 0:
            return False
        else:
            dic[v] -= 1
    for k in dic:
        if dic[k] == float('inf'):
            continue
        if k not in s and k != '.':
            return False
        if dic[k] != 0 and dic[k] != float('inf'):
            return False
    return True

print(isMatch(s = "aaba", p = "ab*a*c*a"))