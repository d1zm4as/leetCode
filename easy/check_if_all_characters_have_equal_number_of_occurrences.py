from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a = Counter(s)
        ref = a[s[0]]
        for x in set(s):
            if ref != a[x]:
                return False
        return True