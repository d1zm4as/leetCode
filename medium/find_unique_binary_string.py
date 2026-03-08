from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Flip the i-th bit of nums[i] to build a string
        # guaranteed to differ from every input string.
        out = []
        for i in range(len(nums)):
            out.append("1" if nums[i][i] == "0" else "0")
        return "".join(out)
