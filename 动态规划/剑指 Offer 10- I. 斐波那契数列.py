class Solution:
    def __init__(self):
        self.a = [0 for i in range(100000)]
    def fib(self, n):
        # print(self.a)
        if n == 0 or n == 1:
            self.a[n] = n
            return n
        else:
            if self.a[n] != 0:
                return self.a[n]
            else:
                self.a[n] = Solution.fib(self, n - 1) + Solution.fib(self, n - 2)
            return self.a[n] % 1000000007


a = Solution()
print(a.fib(37))
