class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
       
        a = "".join([str(x)for x in d])
        b= int(a)+1
        return [int(x) for x in str(b)]
