# 给定一个数组 prices ，它的第i个元素prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
#
#
# 示例 1：
#
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# 注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

class Solution:
    def maxProfit(self, prices):
        return self.maxProfitK(prices, 2)
        # return result

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
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
