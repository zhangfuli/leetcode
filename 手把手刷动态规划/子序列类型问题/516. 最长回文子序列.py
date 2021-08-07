# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
# 示例 1：
#
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb"

class Solution:
    def longestPalindromeSubseq(self, s):
        # dp[i][j] 代表从s[i]～s[j]最长子序列的长度
        dp = [[0 for j in range(len(s) + 1)] for i in range(len(s) + 1)]

        # base case
        for i in range(1, len(s) + 1):
            dp[i][i] = 1

        for i in range(len(s), 0, -1):
            for j in range(i + 1, len(s) + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(
                        dp[i][j - 1],
                        dp[i + 1][j]
                    )

        # for i in range(len(s) + 1):
        #     print(dp[i])
        return dp[1][-1]


solution = Solution()
solution.longestPalindromeSubseq("cddb")
