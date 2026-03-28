class Solution:
    def isBalanced(self, num: str) -> bool:
        par = 0
        impar = 0
        cont = 0

        for x in num:
            if cont%2==0:
                par+=int(x)
            else:
                impar+=int(x)
            cont+=1

        return par == impar