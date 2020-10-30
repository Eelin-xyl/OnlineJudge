grid = [[0,1]]

ans = 0
for i in range(len(grid)):
    if grid[i][0] == 1:
        ans += 1
        if len(grid[i]) != 1 and grid[i][1] == 0:
            ans +=1
        if len(grid[i]) == 1:   
            ans += 1
            continue
    if len(grid[i]) == 1:   continue
    if grid[i][len(grid[i]) - 1] == 1:
        ans += 1
        if grid[i][len(grid[i]) - 2] == 0:
            ans += 1
    if len(grid[i]) == 2:   continue
    for j in range(1, len(grid[i]) - 1):
        if grid[i][j] == 0:
            continue
        if grid[i][j - 1] == 0:
            ans += 1
        if grid[i][j + 1] == 0:
            ans += 1
            
g = []
c = []
a = 0
b = 0
while a < len(grid[0]):
    while b < len(grid):
        c.append(grid[b][a])
        b += 1
    g.append(c)
    c = []
    a += 1
    b = 0
for i in range(len(g)):
    if g[i][0] == 1:
        ans += 1
        if len(g[i]) != 1 and g[i][1] == 0:
            ans +=1
        if len(g[i]) == 1:   
            ans += 1
            continue
    if len(g[i]) == 1:  continue
    if g[i][len(g[i]) - 1] == 1:
        ans += 1
        if g[i][len(g[i]) - 2] == 0:
            ans += 1
    if len(g[i]) == 2:  continue
    for j in range(1, len(g[i]) - 1):
        if g[i][j] == 0:
            continue
        if g[i][j - 1] == 0:
            ans += 1
        if g[i][j + 1] == 0:
            ans += 1
print(ans)