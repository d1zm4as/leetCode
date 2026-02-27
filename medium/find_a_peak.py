class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maior = max(nums)
        return nums.index(maior)