# 给定一个整数数组，其中第i个元素代表了第i天的股票价格。
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
#
# 示例:
# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

class Solution:
    def maxProfit(self, prices):
        frozen = 1
        # k 趋近于无穷时 k - 1 -> k 所以删除 k
        dp = [[-1 * float('INF') for z in {0, 1}] for i in range(len(prices) + 1)]
        for i in range(len(prices) + 1):
            dp[i][0] = 0

        for i in range(1, len(prices) + 1):
            dp[i][0] = max(
                # 前一天没股票
                dp[i - 1][0],
                # 前一天有股票，今天卖了
                dp[i - 1][1] + prices[i - 1]
            )
            dp[i][1] = max(
                # 前一天有股票
                dp[i - 1][1],
                # 前一天没有股票，今天买入
                dp[i - 1 - frozen][0] - prices[i - 1]
            )
        return dp[-1][0]


solution = Solution()
print(solution.maxProfit([1, 2, 3, 0, 2]))
