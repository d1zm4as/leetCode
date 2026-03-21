class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lista = [int(x) for x in str(n)]
        soma = sum(lista)
        mult = 1
        for x in lista:
            mult*=x
        return mult-soma
