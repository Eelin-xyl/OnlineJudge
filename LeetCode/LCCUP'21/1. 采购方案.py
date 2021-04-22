def purchasePlans(nums, target) -> int:
    nums = sorted(nums)
    if nums[0] + nums[1] > target:
        return 0
    ans = 0
    l = 0
    r = len(nums) - 1
    while l < r:
        if (nums[l] + nums[r] <= target):
            ans += r - l
            l += 1
        else:
            r -= 1

    return ans % 1000000007


print(purchasePlans(nums=[2, 2, 2, 1, 1, 9], target=10))
