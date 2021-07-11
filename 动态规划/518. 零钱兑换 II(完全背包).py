# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。

class Solution:
    def change(self, amount, coins):
        dp = [[0 for j in range(amount + 1)] for i in range(len(coins) + 1)]
        # base case
        # dp[i][j]  前i种coin 装满j的个数
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        print(dp)
        return dp[len(coins)][amount]


solution = Solution()
print(solution.change(5, [1, 2, 5]))
