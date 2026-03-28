class Solution:
    def scoreOfString(self, s: str) -> int:
        # memo  = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        soma = 0
        ant = s[0]
        for x in s[1:]:
            soma+= abs(ord(ant)-ord(x))
            ant = x
        return soma
            