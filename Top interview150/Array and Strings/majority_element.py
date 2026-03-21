class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        items  = set(nums)
        maior = 0
        caso = 0
        for x in items:
            if nums.count(x)>maior:
                maior = nums.count(x)
                caso = x

        return caso


# import collections
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n = len(nums)
#         nums.sort()
#         return nums[n//2]
