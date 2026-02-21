class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0
        current_consecutive_ones = 0
        
        for num in nums:
            if num == 1:
                current_consecutive_ones += 1
            else:
                max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)
                current_consecutive_ones = 0
        
        return max(max_consecutive_ones, current_consecutive_ones)