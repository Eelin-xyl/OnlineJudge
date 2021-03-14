matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = len(matrix)
matrix.reverse()
t = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        k = matrix[j][i]
        t[i].append(k)

matrix[:] = t[:]

print(matrix)