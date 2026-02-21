from bisect import bisect_left

from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        result = []

        for num in nums:
            index = bisect_left(sorted_nums, num)
            result.append(index)

        return result