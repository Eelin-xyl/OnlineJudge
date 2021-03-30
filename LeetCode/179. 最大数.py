def largestNumber(nums):
    if len(nums) == 1:
        return str(nums[0])

    for i in range(len(nums)):
        nums[i] = str(nums[i])

    nums.sort()
    nums.reverse()


print(largestNumber([3, 5, 30, 34, 9]))
