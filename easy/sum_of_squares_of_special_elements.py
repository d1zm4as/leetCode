class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        tam = len(nums)

        soma = 0

        for i in range(tam):
            if tam%(i+1)==0:
                soma += nums[i]**2
        return soma