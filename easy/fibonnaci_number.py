# class Solution:
#     def fib(self, n: int) -> int:
#         a = list(range(100))
#         a[0],a[1] = 0,1
#         if n <= 1:
#             return n
#         for i in range(2,n+1):
#             a[i] = a[i-1] + a[i-2]
#         return a[n]
# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def fib(self, n: int) -> int:
        a,b = 0,1
        for i in range(0, n):a, b = b, a + b
        return a