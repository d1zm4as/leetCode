class Solution:
    def pivotInteger(self, n: int) -> int:
        num = list(range(n+1))

        idx = 1
        for x in num:
            if sum(num[:idx+1]) == sum(num[idx:]):
                return num[idx]
            idx+=1
        
        return -1




# class Solution:
#     def pivotInteger(self, n: int) -> int:
#         s=(n*(n + 1)) // 2
#         solv=sqrt(s)
#         if int(solv) !=  solv:
#             return -1
#         return int(solv)