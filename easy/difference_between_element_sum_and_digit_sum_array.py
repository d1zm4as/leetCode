class Solution:
    def addDigits(self, n: int) -> int:
        return sum(map(int, str(n))) 
    def differenceOfSum(self, nums: List[int]) -> int:
        total = 0
        dig = 0
        for x in nums:
            total += x
            dig += self.addDigits(x)

        return abs(total - dig)