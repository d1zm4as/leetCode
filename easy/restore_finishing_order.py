class Solution:
    def recoverOrder(self, order:List[int], friends:List[int]) -> List[int]:
        lista = []

        for x in order:
            if x in friends:
                lista.append(x)
        return lista