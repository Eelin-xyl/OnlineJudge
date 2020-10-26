nums = [1, 0, -1, 0, -2, 2]
target = 0
nums.sort()
ans = []
n = len(nums)
for a in range(0, n - 3):
    if a > 0 and nums[a] == nums[a - 1]:
        continue
    if sum(nums[a : a + 4]) > target:
        break
    if nums[a] + sum(nums[-3:]) < target:
        continue

    for b in range(a + 1, n - 2):
        if b > a + 1 and nums[b] == nums[b - 1]:
            continue
        if nums[a] + sum(nums[b : b + 3]) > target:
            break
        if nums[a] + nums[b] + sum(nums[-2:]) < target:
            continue

        for c in range(b+1,n-1):
            if c > b + 1 and nums[c] == nums[c-1]:
                continue
            # a b c d 最小的组合情况
            if nums[a] + nums[b] + sum(nums[c:c + 2]) > target:
                break
            # a b c d 最大的组合情况
            if nums[a] + nums[b] + nums[c] + nums[-1] < target:
                continue

            for d in range(c+1,n):
                if d > c + 1 and nums[d] == nums[d-1]:
                    continue
                if nums[a] + nums[b] + nums[c] + nums[d] > target:
                    break
                if nums[a] + nums[b] + nums[c] + nums[d] == target:
                    ans.append([nums[a], nums[b], nums[c], nums[d]])
print(ans)
