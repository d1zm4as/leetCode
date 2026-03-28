class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, s: int) -> int:
        n = sum(int(x) for x in str(s))
        ans  = s/n
        return n if ans == int(s/n) else -1
