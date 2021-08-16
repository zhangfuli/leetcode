# 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由M x N 个房间组成的二维网格。
# 我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；
# 其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
# 为了尽快到达公主，骑士决定每次只向右或向下移动一步。
#
#
# 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
# 例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。
#
# -2(K) -3	  3
# -5	-10	  1
# 10	30	-5(P)

#
# 对于 dp[i][j]，我们只要关心 dp[i][j+1] 和 dp[i+1][j] 的最小值 minn。
# 记当前格子的值为 dungeon(i,j)，那么在坐标 (i,j)(i,j) 的初始值只要达到 minn−dungeon(i,j) 即可。
# 同时，初始值还必须大于等于 11。这样我们就可以得到状态转移方程：
#
# dp[i][j]=max(min(dp[i+1][j],dp[i][j+1])−dungeon(i,j),1)


class Solution:
    def calculateMinimumHP(self, dungeon):
        # 从左上角到右下角最少需要多少生命值
        n, m = len(dungeon), len(dungeon[0])
        dp = [[float('INF') for j in range(m + 1)] for i in range(n + 1)]

        # base case
        dp[n][m - 1] = dp[n - 1][m] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i][j + 1], dp[i + 1][j])
                dp[i][j] = max(minn - dungeon[i][j], 1)

        for i in range(len(dp)):
            print(dp[i])
        return dp[0][0]


solution = Solution()
solution.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
