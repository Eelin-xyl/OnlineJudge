def subsetsWithDup(nums):
    ans = [[]]
    nums.sort()
    for i in range(1, len(nums) + 1):

        for a in range(len(nums) - 2):
            for b in range(a, len(nums) - 1):
                for c in range(b, len(nums) - 2):
                    l = nums[a] + nums[b] + nums[c]
                    if l != ans[-1]:
                        ans.append(l)
    return ans


print(subsetsWithDup([1, 2, 2]))
# [[],[1],[1,2],[1,2,2],[2],[2,2]]
