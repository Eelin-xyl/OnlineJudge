nums = [0, 0, 0, 0, 0]
goal = 0

ans = 0
l = 1
while l <= len(nums):
    for i in range(l - 1, len(nums)):
        if sum(nums[i - l + 1: i + 1]) == goal:
            ans += 1
    l += 1
print(ans)
