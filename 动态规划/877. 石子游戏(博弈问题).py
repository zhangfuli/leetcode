# dp[i][j].fir 表示，对于 piles[i...j] 这部分石头堆，先手能获得的最高分数。
# dp[i][j].sec 表示，对于 piles[i...j] 这部分石头堆，后手能获得的最高分数。
#
# 举例理解一下，假设 piles = [3, 9, 1, 2]，索引从 0 开始
# dp[0][1].fir = 9 意味着：面对石头堆 [3, 9]，先手最终能够获得 9 分。
# dp[1][3].sec = 2 意味着：面对石头堆 [9, 1, 2]，后手最终能够获得 2 分。

class Solution:
    def stoneGame(self, piles):

        dp = [[piles[i], 0] for i in range(len(piles))]

        for i in range(len(piles), -1, -1):
            for j in range(i + 1, len(piles)):
                left_fir = dp[j][1] + piles[i]
                right_fir = dp[j - 1][1] + piles[j]
                if left_fir > right_fir:
                    dp[j] = [left_fir, dp[j][0]]
                else:
                    dp[j] = [right_fir, dp[j - 1][0]]
        return dp[-1][0] > dp[-1][1]

    def stoneGame2(self, piles):
        dp = [[[0, 0] for j in range(len(piles) + 1)] for i in range(len(piles) + 1)]

        # base case
        for i in range(1, len(piles) + 1):
            dp[i][i][0] = piles[i - 1]

        for i in range(len(piles), 0, -1):
            for j in range(i + 1, len(piles) + 1):
                if dp[i + 1][j][1] + piles[i - 1] > dp[i][j - 1][1] + piles[j - 1]:
                    dp[i][j] = [
                        dp[i + 1][j][1] + piles[i - 1],
                        dp[i + 1][j][0]
                    ]
                else:
                    dp[i][j] = [
                        dp[i][j - 1][1] + piles[j - 1],
                        dp[i][j - 1][0]
                    ]
        print(dp)
        return dp[1][len(piles)][0] > dp[1][len(piles)][1]


solution = Solution()
solution.stoneGame2([5, 3, 4, 5])
