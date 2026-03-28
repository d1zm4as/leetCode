class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        b = num
        for _ in range(2):
            a = str(b)
            a = a[::-1]
            b = int(a)
        return num == b