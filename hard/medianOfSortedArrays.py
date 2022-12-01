from statistics import median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for x in nums2:
            nums1.append(x)
        nums1.sort()
        return median(nums1)
