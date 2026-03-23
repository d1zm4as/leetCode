from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1, s2) -> List[str]:
        return [word for word, count in Counter((s1+" "+s2).split()).items() if count == 1]


