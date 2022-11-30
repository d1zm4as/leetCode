class Solution:
    def runningSum(self, num: List[int]) -> List[int]:
        
        lista = []
        soma = 0
        for x in num:
            soma+=x
            lista.append(soma)
        return lista
