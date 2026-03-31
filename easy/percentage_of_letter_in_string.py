class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter not in s:
            return 0
        tam  = s.count(letter)

        n = (tam/len(s))*100

        return int(n)