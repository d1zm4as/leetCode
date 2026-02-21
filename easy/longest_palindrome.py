
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        result = 0
        odd = False
        for c in count:
            if count[c] % 2 == 0:
                result += count[c]
            else:
                result += count[c] - 1
                odd = True

        if odd:
            result += 1

        return result