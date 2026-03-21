class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = {}

        for idx in range(len(nums)):
            item = nums[idx]
            if item in memo and abs(idx-memo[item])<=k:
                return True

            memo[item] = idx
    
        return False

    

# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         if len(nums) == len(set(nums)):
#             return False
#         else:
#             for i in range(len(nums)):
#                 if nums[i] in nums[i+1 : i+k+1]:
#                     return True
#             return False
# its faster to check the indexes than to check via hashmap