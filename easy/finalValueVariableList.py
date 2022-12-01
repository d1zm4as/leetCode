class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        valor = 0

        for x in operations:
            if "+" in x:
               valor+=1
            else:
                valor-=1
        return valor
