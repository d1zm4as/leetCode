class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip("0") if "0" in num else num