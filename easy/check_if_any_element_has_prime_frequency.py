from collections import Counter

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class Solution:
    def checkPrimeFrequency(self, arr: List[int]) -> bool:
        frequency = Counter(arr)
        return any(isprime(count) for count in frequency.values())