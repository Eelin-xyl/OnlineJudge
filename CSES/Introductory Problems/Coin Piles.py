n = int(input())
l = []
for _ in range(n):
    ab = input().split()
    l.append([int(ab[0]), int(ab[1])])
for i in l:
    a, b = max(i[0], i[1]), min(i[0], i[1])
    if a > 2 * b:
        print("NO")
        continue
    if a == 2 * b:
        print("YES")
        continue
    if a == b and a % 3 != 0:
        print("NO")
        continue
    k = a - b
    if (b - k) % 3 == 0:
        print("YES")
        continue
    k = 2 * b - a
    if k % 3 == 0:
        print("YES")
        continue
    print("NO")