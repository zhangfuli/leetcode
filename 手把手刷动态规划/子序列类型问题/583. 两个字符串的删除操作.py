# 给定两个单词word1和word2，找到使得word1和word2相同所需的最小步数，
# 每步可以删除任意一个字符串中的一个字符。
# 示例：
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

# 最长公共子序列问题, 见1143 最长公共子序列

class Solution:
    def minDistance(self, word1, word2):
        dp = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        # base case
        # dp[i][0] = 0
        # dp[0][j] = 0

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )
        print(dp[-1][-1])
        print(len(word1) + len(word2) - 2 * dp[-1][-1])
        return len(word1) + len(word2) - 2 * dp[-1][-1]


solution = Solution()
solution.minDistance("sea", "eat")
