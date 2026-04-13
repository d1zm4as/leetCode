class Solution:
    def largestEven(self, s: str) -> str:
        if not s:
            return ""

        while s:
            if s[-1] in "02468":
                return s
            else:
                # s = s[0:-1]
                s = s[:-1]

        return s
