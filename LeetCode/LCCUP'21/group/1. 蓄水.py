from typing import List
import math


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:

        l = len(bucket)
        shang = float("inf")
        for a in range(l):
            if bucket[a] >= vat[a]:
                continue
            if bucket[a] == 0:
                continue
            shang = min(shang, math.ceil(vat[a] / bucket[a]))

        if shang == float("inf"):
            return 1

        n = 0
        for b in range(l):
            if bucket[b] >= vat[b]:
                continue
            if bucket[b] == 0:
                bucket[b] += 1
                n += 1
            n += math.ceil(vat[b] / shang) - bucket[b]

        return shang + n


if __name__ == "__main__":
    print(Solution.storeWater(Solution, bucket=[1, 3], vat=[6, 8]))
