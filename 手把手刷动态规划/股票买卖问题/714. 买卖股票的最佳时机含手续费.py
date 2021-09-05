# 给定一个整数数组prices，其中第i个元素代表了第i天的股票价格；
# 整数fee 代表了交易股票的手续费用。
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。
# 如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 返回获得利润的最大值。
# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
#
# 示例 1：
# 输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出：8
# 解释：能够达到的最大利润:
# 在此处买入prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润:((8 - 1) - 2) + ((9 - 4) - 2) = 8

class Solution:
    def maxProfit(self, prices, fee):
        # k 趋近于无穷时 k - 1 -> k 所以删除 k
        dp = [[-1 * float('INF') for z in {0, 1}] for i in range(len(prices) + 1)]
        for i in range(len(prices) + 1):
            dp[i][0] = 0

        for i in range(1, len(prices) + 1):
            dp[i][0] = max(
                # 前一天没股票
                dp[i - 1][0],
                # 前一天有股票，今天卖了
                dp[i - 1][1] + prices[i - 1] - fee
            )
            dp[i][1] = max(
                # 前一天有股票
                dp[i - 1][1],
                # 前一天没有股票，今天买入
                dp[i - 1][0] - prices[i - 1]
            )
        return dp[-1][0]


solution = Solution()
print(solution.maxProfit([1, 3, 2, 8, 4, 9], 2))
