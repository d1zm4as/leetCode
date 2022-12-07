class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r = ''
        for x in t:
            if t.count(x)>s.count(x) and x not in r:
                r+=x
        return r
