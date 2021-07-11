class Solution:
    def maxA(self, n):
        # dp[i] 表示 i 次操作后最多能显示多少个 A
        dp = [0 for i in range(n + 1)]
        for i in range(1, n + 1):

            # 只敲了一个A
            dp[i] = dp[i - 1] + 1
            for j in range(2, i, 1):
                dp[i] = max(
                    dp[i],
                    # 扣除c-a, c-c
                    dp[j - 2] * (i - j + 1)
                )
        print(dp)
        return dp[n]


solution = Solution()
solution.maxA(10)
