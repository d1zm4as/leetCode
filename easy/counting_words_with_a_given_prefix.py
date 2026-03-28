class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        

        
        cont = 0

        for x in words:
            if x.startswith(pref):
                
                cont+=1
        return cont