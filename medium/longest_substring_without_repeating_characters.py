
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        atual = s[0]
        cont = 0
        for x in s[1:]:
            if x not in atual:
                atual += x
            else:
                cont = max(cont, len(atual))
                atual = atual[atual.index(x) + 1:] + x
        return max(cont, len(atual))