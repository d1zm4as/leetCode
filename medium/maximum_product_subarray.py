class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        mmaior  = mmenor = resultado = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                mmaior, mmenor = mmenor, mmaior
            
            mmaior = max(nums[i], mmaior * nums[i])
            mmenor = min(nums[i], mmenor * nums[i])
            
            resultado = max(resultado, mmaior)
        return resultado