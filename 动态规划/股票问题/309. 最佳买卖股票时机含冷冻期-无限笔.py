# 每天都有三种「选择」：买入、卖出、无操作

class Solution:
    def maxProfit1(self, prices):
        res = self.maxProfitK(prices, len(prices))
        print(res)
        if res < 0:
            return 0
        return res

    def maxProfitK(self, prices, k):
        # dp[i][j][0,1] = value
        # 第i天，操作次数为j，当前是否持有股票，最大价值为value
        dp = [[[-1 * float('INF') for _k in range(2)] for j in range(k + 1)] for i in range(len(prices) + 1)]

        # base case
        for i in range(len(prices) + 1):
            dp[i][0][0] = 0
        for j in range(k + 1):
            dp[0][j][0] = 0

        print(dp)

        res = -1 * float('INF')
        for i in range(1, len(prices) + 1):
            for j in range(1, k + 1):
                if dp[i - 1][j - 1][1] != -1 * float('INF'):
                    dp[i][j][0] = max(
                        dp[i - 1][j][0],  # 第i天没买入
                        dp[i - 1][j - 1][1] + prices[i - 1],  # 第i天卖出
                    )
                    res = max(res, dp[i][j][0])

                if dp[i - 1][j - 1][0] != -1 * float('INF'):
                    dp[i][j][1] = max(
                        dp[i - 1][j - 1][0] - prices[i - 1],  # 第i天买入
                        dp[i - 1][j][1],  # 第i天没买入
                    )
                    res = max(res, dp[i][j][1])

        print(res)
        return res

    # 当 K = inf  k = k - 1  k恒定不变
    def maxProfit(self, prices):
        frozen = 1
        dp = [[0, 0] for i in range(len(prices) + 1)]
        dp[0][0] = 0
        dp[0][1] = -1 * float('INF')
        # dp[1][1] = prices[0]
        for i in range(1, len(prices) + 1):
            # tmp = dp[i][0]

            dp[i][0] = max(
                dp[i - 1][0],
                dp[i - 1][1] + prices[i - 1]  # 卖出
            )

            dp[i][1] = max(
                dp[i - 1][1],
                dp[i - 1 - frozen][0] - prices[i - 1] # 买入 包含冷冻期
            )
        print(dp)
        print(dp[len(prices)][0])
        return dp[len(prices)][0]


solution = Solution()
solution.maxProfit([1,2,3,0,2])
