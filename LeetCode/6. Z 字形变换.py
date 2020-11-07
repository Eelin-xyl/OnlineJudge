s = 'PAYPALISHIRING'
numRows = 3

ans = list()
i = 0
while i < len(s):
    line = list()
    for _ in range(numRows):
        if i >= len(s):
            break
        line.append(s[i])
        i += 1
    for _ in range(numRows - len(line)):
        line.append(' ')
    ans.append(line)

    if line[-1] == ' ':
        break
    step = [' ']
    for _ in range(numRows - 2):
        if i >= len(s):
            break
        step.append(s[i])
        i += 1
    for _ in range(numRows - len(step)):
        step.append(' ')
    step.reverse()
    ans.append(step)

res = ''
for a in range(numRows):
    for b in range(len(ans)):
        if ans[b][a] != ' ':
            res += ans[b][a]
print(res)