class Solution:
    
    def reverseVowels(self, s: str) -> str:
        v = set(["a","e","i","o","u","A","E","I","O","U"])

        pos = []
        resto = []
        vog = []

        for idx,x  in enumerate(s):
            if x in v:
                pos.append(idx)
                vog.append(x)
                resto.append("|")
            else:
                resto.append(x)

        for x,y in zip(pos[::-1],vog):
            resto[x] = y

        return "".join(resto)
