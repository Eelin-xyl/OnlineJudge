def minAbsoluteSumDiff(nums1, nums2) -> int:
    ans = []
    mx = 0
    key = 0
    for i in range(len(nums1)):
        ab = abs(nums1[i] - nums2[i])
        if ab >= mx:
            key = i
            mx = ab
        ans.append(ab)
    if mx == 0:
        return sum(ans) % (10**9 + 7)
    k = nums2[key]
    n = sorted(nums1)
    if k <= n[0]:
        t = n[0]
    if k >= n[-1]:
        t = n[-1]
    mi = float('inf')
    j = 0
    while j < len(n):
        if abs(k - n[j]) <= mi:
            mi = abs(k - n[j])
        else:
            break
        j += 1
    ans[key] = mi

    return sum(ans) % (10**9 + 7)


print(minAbsoluteSumDiff(nums1=[1, 10, 4, 4, 2, 7], nums2=[9, 3, 5, 1, 7, 4]))
