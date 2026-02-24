class Solution:
    def reverse(self, n: int) -> int:
        sign = -1 if n<0 else 1
    
        n = abs(n)
        
        n = str(n)
        
        n = int(n[::-1])

        
        return 0 if n >= 2147483647 else n*sign