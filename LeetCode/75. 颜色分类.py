nums = [2,0,1]
zero = 0
two = len(nums) - 1
i = 0
while i <= two:
    if nums[i] == 2:
        nums[i] = nums[two]
        nums[two] = 2
        two -= 1
        continue
    if nums[i] == 0:
        nums[i] = nums[zero]
        nums[zero] = 0
        zero += 1
    i += 1
print(nums)