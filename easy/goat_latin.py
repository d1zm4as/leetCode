class Solution:
    def goated(self,s):
        vog = set("aeiouAEIOU")
        if s[0] in vog:
            return s+"ma"
        return s[1:]+s[0]+"ma" 
        
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        idx = 1
        lista = []
        for x in sentence:
            lista.append(self.goated(x)+idx*"a")
            idx+=1

        return " ".join(lista)