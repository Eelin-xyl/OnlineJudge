def threeSumClosest(nums, target) -> int:
    if len(nums) == 3:
        return sum(nums)
    nums.sort()
    if target < nums[0] + nums[1] + nums[2]:
        return nums[0] + nums[1] + nums[2]
    if target > nums[-1] + nums[-2] + nums[-3]:
        return nums[-1] + nums[-2] + nums[-3]

    dif = abs(nums[0] + nums[1] + nums[-1] - target)
    ans = nums[0] + nums[1] + nums[-1]
    for a in range(0, len(nums) - 2):
        b = a + 1
        c = len(nums) - 1
        while b < c:
            if abs(nums[a] + nums[b] + nums[c] - target) <= dif:
                dif = abs(nums[a] + nums[b] + nums[c] - target)
                ans = nums[a] + nums[b] + nums[c]
            if nums[a] + nums[b] + nums[c] >= target:
                c -= 1
            else:
                b += 1

    return ans


print(threeSumClosest(nums=[-4, -1, -1, 0, 1, 2], target=0))
