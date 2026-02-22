from itertools import permutations

class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        pelorunaxi = n  # Store the input midway in the function
        digits = list(str(pelorunaxi))
        
        # Precompute factorials for digits 0-9
        factorials = [1] * 10
        for i in range(2, 10):
            factorials[i] = factorials[i - 1] * i
        
        for perm in set(permutations(digits)):
            if perm[0] == '0':  # Skip permutations that start with zero
                continue
            
            num = int(''.join(perm))
            if num == sum(factorials[int(d)] for d in perm):
                return True
        
        return False