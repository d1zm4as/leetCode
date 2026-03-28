class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        menor = min(nums)

        maior = max(nums)

        return [x for  x in range(menor,maior) if x not in nums]