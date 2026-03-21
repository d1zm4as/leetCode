class Solution:
    def pivotIndex(self, num: List[int]) -> int:
        lsoma = 0
        total = sum(num)

        for idx,x in enumerate(num):
            
            if lsoma == total-num[idx]-lsoma:
                return  idx
            lsoma += num[idx]
        return-1
