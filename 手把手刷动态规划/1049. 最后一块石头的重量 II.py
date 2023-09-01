class Solution:
    def lastStoneWeightII(self, stones):
        stones_sum = sum(stones)
        # dp[i][j] 前i个stone装进容量为j的袋子最大能装多少
        dp = [[0 for j in range(stones_sum // 2 + 1)] for i in range(len(stones) + 1)]

        # base case

        # dp
        for i in range(1, len(stones) + 1):
            for j in range(stones_sum // 2 + 1):
                if j - stones[i - 1] >= 0:
                    dp[i][j] = max(
                        dp[i - 1][j - stones[i - 1]] + stones[i - 1],  # 放入
                        dp[i - 1][j]  # 不放
                    )
                else:
                    dp[i][j] = dp[i - 1][j]
        for i in range(len(stones) + 1):
            print(dp[i])
        return stones_sum - 2 * dp[len(stones)][stones_sum // 2]


solution = Solution()
solution.lastStoneWeightII([1, 2])
