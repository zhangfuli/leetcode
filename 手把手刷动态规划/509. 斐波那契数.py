class Solution:
    def fib(self, n):
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [0 for i in range(n + 1)]
        dp[1], dp[2] = 1, 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


solution = Solution()
solution.fib(4)
