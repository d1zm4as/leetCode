class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        tam = 1
        maior = 1

        for n1, n2 in zip(nums, nums[1:]):
            if n2 > n1:
                tam += 1
                maior = max(maior, tam)
            else:
                tam = 1

        return maior
