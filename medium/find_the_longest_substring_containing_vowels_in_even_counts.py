s = "eleetminicoworoep"

cont = 0

maior = 0

copy = ""

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        memo = {0: -1}
        temp = 0
        ans = 0
        for idx, x in enumerate(s):
            if x == 'a':
                temp ^= 1 << 0
            elif x == 'e':
                temp ^= 1 << 1
            elif x == 'i':
                temp ^= 1 << 2
            elif x == 'o':
                temp ^= 1 << 3
            elif x == 'u':
                temp ^= 1 << 4

            if temp in memo:
                ans = max(ans, idx - memo[temp])
            else:
                memo[temp] = idx
        return ans
    
print(Solution().findTheLongestSubstring(s))