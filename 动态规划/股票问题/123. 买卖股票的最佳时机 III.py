# 每天都有三种「选择」：买入、卖出、无操作

class Solution:
    # k 交易次数
    def maxProfit(self, prices):
        return max(self.maxProfitK(prices, 4), self.maxProfitK(prices, 2))

    def maxProfitK(self, prices, k):
        # dp[i][j][0,1] = value
        # 第i天，操作次数为j，当前是否持有股票，最大价值为value
        dp = [[[-1 * float('INF') for k in range(2)] for j in range(k + 1)] for i in range(len(prices) + 1)]

        # base case
        for i in range(len(prices) + 1):
            dp[i][0][0] = 0
        for j in range(k + 1):
            dp[0][j][0] = 0

        for i in range(1, len(prices) + 1):
            for j in range(1, k + 1):
                dp[i][j][0] = max(
                    dp[i - 1][j][0],  # 第i天没买入
                    dp[i - 1][j - 1][1] + prices[i - 1],  # 第i天卖出
                )

                dp[i][j][1] = max(
                    dp[i - 1][j - 1][0] - prices[i - 1],  # 第i天买入
                    dp[i - 1][j][1],  # 第i天没买入
                )
        # print(dp[len(prices)][k][0])
        if dp[len(prices)][k][0] < 0:
            return 0
        return dp[len(prices)][k][0]


solution = Solution()
solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
