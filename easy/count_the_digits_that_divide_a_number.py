class Solution:
    def countDigits(self, num: int) -> int:
        cont = 0

        for x in str(num):
            if num%int(x)==0:
                cont+=1
        return cont