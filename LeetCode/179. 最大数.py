def largestNumber(nums):
    if len(nums) == 1:
        return str(nums[0])

    for i in range(len(nums)):
        nums[i] = str(nums[i])

    nums.sort()
    nums.reverse()
    nums.append('*')

    ans = ''
    a = '9'
    k = 0
    nub = []
    while k != len(nums):
        if nums[k][0] == a:
            nub.append(nums[k])
        else:
            if (len(nub) == 1):
                ans += nub[0]
            else:
                sig = []
                for i in range(len(nub) - 1, -1, -1):
                    if len(nub[i]) == 1:
                        sig.append(nub[i])
                    else:
                        break
                nub = nub[0: i + 1]
                for x, v in enumerate(nub):
                    for j in v:
                        if int(j) < int(a):
                            nub = nub[0: x] + sig + nub[x: len(nub)]
                            break
                    else:
                        continue
                    break
                for j in nub:
                    ans += j
            nub = [nums[k]]
            a = nums[k][0]
        k += 1

    return ans


print(largestNumber([10, 2]))
