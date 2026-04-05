class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        lista = [[]]

        for sub in nums:
            lista += [curr + [sub] for curr in lista]

        return lista    