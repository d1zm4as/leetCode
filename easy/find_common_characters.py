from collections import Counter

class Solution:
    
    def commonChars(self, words: List[str]) -> List[str]:
        atual =Counter(words[0])
        cont = 0
        lista = []
        for x in words[1:]:
            atual -= atual - Counter(x)
        for x in atual:
            while cont < atual[x]:
                lista.append(x)
                cont+=1
            cont = 0
        return lista