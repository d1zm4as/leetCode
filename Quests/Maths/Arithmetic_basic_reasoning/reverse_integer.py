class Solution:
    def reverse(self, n: int) -> int:
        sign = -1 if n<0 else 1
        
        n = abs(n)
        
        n = str(n)
        
        n = int(n[::-1])

        if n <= -2147483648 or n>= 2147483647:
            return 0
        return n*sign