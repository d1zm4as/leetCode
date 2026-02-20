class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        f = s[:k]

        l = s[k:]

        return f[::-1]+l
        