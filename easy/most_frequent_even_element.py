from collection import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_nums = [num for num in nums if num % 2 == 0]
        if not even_nums:
            return -1
        
        count = Counter(even_nums)
        max_freq = max(count.values())
        
        most_frequent_evens = [num for num, freq in count.items() if freq == max_freq]
        
        return min(most_frequent_evens)