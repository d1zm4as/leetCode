class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        a = set(nums1)
        b = set(nums2)
        common = a.intersection(b)
        if common:
            return min(common)
        else:
            return min(min(nums1), min(nums2)) * 10 + max(min(nums1), min(nums2))     