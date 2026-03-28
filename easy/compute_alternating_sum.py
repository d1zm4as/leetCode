class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        soma = 0

        cont = 0
        
        for x in nums:
            if cont %2==0:
                soma+=x
            else: 
                soma-=x
            cont+=1
        return soma