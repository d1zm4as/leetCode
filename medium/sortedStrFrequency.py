from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        l,c = list(s),Counter(s)
        l.sort(key=lambda x:(-c[x],x))
        return "".join(l)
