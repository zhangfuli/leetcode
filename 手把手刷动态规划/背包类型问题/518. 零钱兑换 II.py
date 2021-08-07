# # 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
# # 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
# # 假设每一种面额的硬币有无限个。
# # 题目数据保证结果符合 32 位带符号整数。
# #
# # 示例 1：
# # 输入：amount = 5, coins = [1, 2, 5]
# # 输出：4
# # 解释：有四种方式可以凑成总金额：
# # 5=5
# # 5=2+2+1
# # 5=2+1+1+1
# # 5=1+1+1+1+1
#
class Solution:
    def change(self, amount, coins):
        # dp[i][j]  前i种coin 装满j的个数
        dp = [[0 for j in range(amount + 1)] for i in range(len(coins) + 1)]

        # base case
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for j in range(amount + 1):
            dp[0][j] = 0

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        for i in range(len(coins) + 1):
            print(dp[i])

        return dp[-1][-1]


solution = Solution()
solution.change(5, [1, 2, 4])
