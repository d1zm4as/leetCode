from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cont = Counter(arr)
        luckys = []
        for x in arr:
            if x==cont[x]:
                luckys.append(x)

        return max(luckys) if luckys else -1