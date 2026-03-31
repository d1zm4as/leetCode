from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        # ref = set(s)
        for x in s:
            if c[x]==1:
                return s.index(x)
        return -1