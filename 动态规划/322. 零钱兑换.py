# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 你可以认为每种硬币的数量是无限的。
#
# 示例 1：
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1


class Solution:
    def __init__(self):
        self.dp_data = {}

    def coinChange1(self, coins, amount):
        dp = [float('INF') for i in range(amount + 1)]

        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i - coin], dp[i]) + 1
        if dp[amount] == float('INF'):
            return -1
        else:
            return dp[amount]

    def coinChange2(self, coins, amount):
        # 输入一个目标金额n，返回凑出目标金额n的最少硬币数量
        def dp(n):
            if n < 0:
                return -1
            if n == 0:
                self.dp_data[0] = 0
                return 0

            res = float('INF')
            for i in coins:
                if (n - i) in self.dp_data:
                    subproblem = self.dp_data[n - i]
                else:
                    subproblem = dp(n - i)
                if subproblem == -1:
                    continue
                res = min(res, subproblem + 1)
            if res == float('INF'):
                res = -1

            self.dp_data[n] = res
            return self.dp_data[n]

        return dp(amount)


solution = Solution()
print(solution.coinChange1([1, 3, 5], 11))
