class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lista = [0]*len(indices)

        for x in range(len(indices)):
            lista[indices[x]] = s[x]

        return "".join(lista)
