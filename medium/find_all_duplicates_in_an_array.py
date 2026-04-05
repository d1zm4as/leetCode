from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        lista = []
        a = Counter(nums)
        for x in a:
            if a[x] > 1:
                lista.append(x)
        return lista