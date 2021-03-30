def maxArea(height):
    if len(height) == 0 or len(height) == 1:
        return 0
    if len(height) == 2:
        return min(height[0], height[1])

    mx = 0
    a = 0
    b = len(height) - 1
    while a < b:
        mx = max(mx, (b - a) * min(height[a], height[b]))
        if b - a == 1:
            break
        if height[a] < height[b]:
            a += 1
        else:
            b -= 1
    return mx


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
