nums = [4, 5, 6, 7, 0, 1, 2]
target = 3


l = 0
r = len(nums) - 1

while l <= r:
    mid = (l + r) // 2                                  # index as mid
    if nums[mid] == target:
        print(mid)                                      # got target
        break
    if nums[0] <= nums[mid]:                            # 0-mid belongs to improve list
        if nums[0] <= target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    else:                                               # mid-l belongs to improve list
        if nums[mid] < target <= nums[len(nums) - 1]:
            l = mid + 1
        else:
            r = mid - 1
else:
    print(-1)
