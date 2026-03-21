class Solution:
    def twoSum(self, num: List[int], t: int) -> List[int]:
        lista = {}
        for idx,x in enumerate(num):
            diff = t-x
            if diff in lista: return [lista[diff],idx]
            lista[x] = idx
