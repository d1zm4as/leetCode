from collections import Counter


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        a = Counter(nums)
        for x in nums:
            if a[x] == 1 and x & 1 == 0:
                return x
        return -1
