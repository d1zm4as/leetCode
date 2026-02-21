def check_pali(s: str) -> bool:
    return s == s[::-1]

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if check_pali(s):
            return 1
        return 2