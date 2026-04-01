from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        cont  = Counter(s)
        max_vowel = 0
        max_consonant = 0
        for x in set(s):
            if x in 'aeiou':
                max_vowel = max(max_vowel, cont[x])
            else:
                max_consonant = max(max_consonant, cont[x])
        return max_vowel + max_consonant
        