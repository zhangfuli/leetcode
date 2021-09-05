# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例1:
#
# 输入：prices = [3,3,5,0,0,3,1,4]
# 输出：6
# 解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
# 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

class Solution:
    def maxProfit(self, prices):
        return self.maxProfitK(prices, 4)

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
print(solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
