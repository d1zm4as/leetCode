class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        dir = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        return sum([dir[x] for x in s])
