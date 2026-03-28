class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        lista = []
        cont = 0
        for w in words:
            if x in w:
                lista.append(cont)
            cont+=1
        return lista