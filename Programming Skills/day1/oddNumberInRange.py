class Solution:
    def countOdds(self, low: int, high: int) -> int:
      
        ans=(high-low)//2
        return ans if high%2==0 and low%2==0 else ans+1
