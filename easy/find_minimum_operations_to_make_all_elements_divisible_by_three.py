class Solution:

  
    def minimumOperations(self, nums: List[int]) -> int:
        cont = 0
        for n in nums:
            if n-1==0 or (n+1)%3==0 or (n-1)%3==0 :
                cont+=1
        return cont