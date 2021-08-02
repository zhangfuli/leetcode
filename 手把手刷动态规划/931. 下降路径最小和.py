# 给你一个 n x n 的 方形整数数组matrix ，请你找出并返回通过 matrix 的下降路径的最小和 。
#
# 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。
# 在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素。
# 具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。
#
# 示例 1：
# 输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
# 输出：13
# 解释：下面是两条和最小的下降路径，用加粗标注：
# [[2,1,3],      [[2,1,3],
#  [6,5,4],       [6,5,4],
#  [7,8,9]]       [7,8,9]]
class Solution:
    def minFallingPathSum(self, matrix):
        dp = [[float('INF') for j in range(len(matrix[0]))] for i in range(len(matrix))]

        # base case
        for j in range(len(dp[0])):
            dp[0][j] = matrix[0][j]

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                dp[i][j] = min(
                    dp[i - 1][j],
                    dp[i - 1][max(j - 1, 0)],  # 优雅的控制边界
                    dp[i - 1][min(j + 1, len(matrix[0]) - 1)],
                ) + matrix[i][j]

        for i in range(0, len(matrix)):
            print(dp[i])
        return min(dp[-1])


solution = Solution()
print(solution.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
