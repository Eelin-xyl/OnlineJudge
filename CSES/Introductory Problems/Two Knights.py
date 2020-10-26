n = int(input())  
for i in range(1, n + 1):
    al = int((i ** 4 - i ** 2) / 2)
    ct = 4 * i ** 2 - 12 * i + 8
    print(al - ct)