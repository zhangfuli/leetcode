class Solution:
    def numOfWays(self, n):
        dp = [[0,0] for i in range(n + 1)]
        dp[1][0] = 6
        dp[1][1] = 6
        for i in range(2, n + 1):
            dp[i][0] = dp[i-1][0] * 3 + dp[i-1][1] * 2
            dp[i][1] = dp[i-1][0] * 2 + dp[i-1][1] * 2
        return (dp[n][0] + dp[n][1]) % 1000000007

solution = Solution()
solution.numOfWays(2)