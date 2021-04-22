def isUgly(n: int) -> bool:
    if n == 1 or n == 2 or n == 3 or n == 5:
        return True

    p = n
    while n != 1:
        if n % 2 == 0:
            n /= 2
        if n % 3 == 0:
            n /= 3
        if n % 5 == 0:
            n /= 5
        if p == n:
            return False
        p = n
    return True


print(isUgly(n=1))
