from collections import Counter
class Solution:
    def sumOfUnique(self, arr: List[int]) -> int:
        cont = Counter(arr)
        luckys = []
        for x in arr:
            if cont[x]==1:
                luckys.append(x)

        return sum(luckys)