def orchestraLayout(num: int, Xpos: int, Ypos: int) -> int:
    if num == 1:
        return 1
    grid = [[] for _ in range(num)]
    i = 1
    n = 0
    while num - i > 0:
        n += 2
        i += 1
    x = 0
    y = 0
    a = 0
    while a <= n:
        if x == Xpos and y == Ypos:
            break
        # while x += 1:


print(orchestraLayout(num=4, Xpos=1, Ypos=2))
