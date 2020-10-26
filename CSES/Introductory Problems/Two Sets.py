n = int(input())

if n*(n + 1) % 4 != 0:
    print('NO')
else:
    print("YES")
    if n % 2 == 1:       #奇数情况
        d = (n - 1) // 2 #对数
        m = n - 1        #去尾
        print(d + 1)
        for i in range(d // 2 + 1):
            print(i + 1, end = " ")
            print(m - i, end = " ")
        print()
        print(d)
        for i in range(d // 2):
            print(i + d // 2 + 2, end=" ")
            print(m - 1 - d // 2 - i, end=" ")
        print(n)

    else:             #偶数情况
        d = n // 2    #对数
        print(d)
        for i in range(d // 2):
            print(i + 1, end=" ")
            print(n - i, end=" ")
        print()
        print(d)
        for i in range(d // 2):
            print(i + d // 2 + 1, end=" ")
            print(n - d // 2 - i, end=" ")