class Solution:
    def thirdMax(self, n: List[int]) -> int:
        
        lista = sorted(list(set(n)))

        return lista[-3] if len(lista) >=3 else lista[-1]