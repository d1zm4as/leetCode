class Solution:

    def countEven(self, num: int) -> int:
        return sum(1 for digit in range(1, num + 1) if sum(int(d) for d in str(digit)) % 2 == 0)