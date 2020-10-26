A = [2,2,2]

def up(index):
    if index == len(A) - 1:
        return index
    while index + 1 < len(A) and A[index + 1] > A[index]:
            index += 1
    return index

def down(index):
    if index == len(A) - 1:
        return index
    while index + 1 < len(A) and A[index + 1] < A[index]:
            index += 1
    return index

ans = 0
cur = 0
i = 0
while i < len(A):
    if up(i) != i:
        start = i
        i = up(i)
        if down(i) != i:
            cur = down(i) - start + 1
            ans = max(ans, cur)
            cur = 0
    i += 1
print(ans)