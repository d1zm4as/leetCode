class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        lista = []
        for idx,x in enumerate(nums):
            if x == target:
                lista.append(idx)
        return lista