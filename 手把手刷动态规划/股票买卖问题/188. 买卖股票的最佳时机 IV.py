# 给定一个整数数组prices ，它的第 i 个元素prices[i] 是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

# 示例 1：
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。


class Solution:
    def maxProfit(self, k, prices):
        return self.maxProfitK(prices, k * 2)

    def maxProfitK(self, prices, k):
        # dp[i][j][{0,1}]  第i天, 进行了j次交易, 当前是否持有股票 的收益
        # 0-没有股票
        # 1-有股票
        dp = [[[-1 * float('INF') for z in {0, 1}] for j in range(k + 1)] for i in range(len(prices) + 1)]

        # base case
        for i in range(len(prices) + 1):
            dp[i][0][0] = 0
        for j in range(k + 1):
            dp[0][j][0] = 0

        res = -1 * float('INF')

        for i in range(1, len(prices) + 1):
            for j in range(1, k + 1):
                if dp[i - 1][j - 1][1] != -1 * float('INF'):
                    dp[i][j][0] = max(
                        # 前一天没股票
                        dp[i - 1][j][0],
                        # 前一天有股票，今天卖了
                        dp[i - 1][j - 1][1] + prices[i - 1]
                    )
                    res = max(res, dp[i][j][0])

                if dp[i - 1][j - 1][0] != -1 * float('INF'):
                    dp[i][j][1] = max(
                        # 前一天有股票
                        dp[i - 1][j][1],
                        # 前一天没有股票，今天买入
                        dp[i - 1][j - 1][0] - prices[i - 1]
                    )
                    res = max(res, dp[i][j][0])

        if res < 0:
            return 0
        return res


solution = Solution()
print(solution.maxProfit(2, [2, 4, 1]))
