# 每天都有三种「选择」：买入、卖出、无操作

class Solution:
    # 当 K = inf  k = k - 1  k恒定不变
    def maxProfit(self, prices, fee):
        dp = [[0, 0] for i in range(len(prices) + 1)]
        dp[0][0] = 0
        dp[0][1] = -1 * float('INF')
        # dp[1][1] = prices[0]
        for i in range(1, len(prices) + 1):
            # tmp = dp[i][0]

            dp[i][0] = max(
                dp[i - 1][0],
                dp[i - 1][1] + prices[i - 1] - fee  # 卖出, 每笔交易不是每次交易
            )

            dp[i][1] = max(
                dp[i - 1][1],
                dp[i - 1][0] - prices[i - 1]
            )
        print(dp)
        print(dp[len(prices)][0])
        return dp[len(prices)][0]


solution = Solution()
solution.maxProfit([1, 3, 2, 8, 4, 9], 2)
