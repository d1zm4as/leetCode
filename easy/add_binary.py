class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers
        num_a = int(a, 2)
        num_b = int(b, 2)
        
        # Sum the two numbers
        total = num_a + num_b
        
        # Convert the sum back to a binary string and remove the '0b' prefix
        return bin(total)[2:]