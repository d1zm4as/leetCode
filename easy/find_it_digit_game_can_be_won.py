class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        # tam  = len(nums)
        soma_u = 0
        soma_du = 0

        for x in nums:
            if x<10:
                    soma_u +=x
            else:
                soma_du+=x
        return soma_u!=soma_du