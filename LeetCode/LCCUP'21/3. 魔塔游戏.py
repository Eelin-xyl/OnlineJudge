def magicTower(nums) -> int:
    if sum(nums) < 0:
        return -1
    hp = 1
    ans = 0
    ps = []
    k = 0
    while k < len(nums):
        hp += nums[k]
        ps.append(nums[k])
        if hp <= 0:
            ans += 1
            mi = min(ps)
            ps.remove(mi)
            hp -= mi
            nums.append(mi)
            nums.remove(mi)
            continue
        k += 1

    return ans


print(magicTower(nums=[100, 100, 100, -60, -140, -50, -250, -50, 100, 150]))
