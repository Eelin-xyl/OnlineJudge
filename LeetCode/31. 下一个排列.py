nums = [1, 2, 3]

s = nums.copy()
s.sort()
s.reverse()
if s != nums and len(nums) > 1:
    b = float('-inf')
    for j in range(len(nums) - 1, -1, -1):
        if nums[j] < b:
            b = nums[j] 
            break
        b = nums[j]
    for a in range(len(nums) - 1, j - 1, -1):
        if nums[j] < nums[a]: break
    nums[j] = nums[a]
    nums[a] = b
    k = -1
    j += 1
    for i in range(j, (len(nums) - j) // 2 + j):
        t = nums[i]
        nums[i] = nums[k]
        nums[k] = t
        k -= 1
else:
    nums.reverse()
print(nums)