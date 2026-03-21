def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums) # Handle cases where k is greater than the length of the array
    nums[:] = nums[-k:] + nums[:-k] # Rotate the array by slicing and concatenating