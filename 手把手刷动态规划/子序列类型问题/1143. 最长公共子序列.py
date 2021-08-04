# 给定两个字符串text1和text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在公共子序列 ，返回 0 。
# 一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
#
# 示例 1：
#
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        # text1[0..i] text2[0..j] 的最大公共子序列
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # base case
        for i in range(len(text1) + 1):
            dp[i][0] = 0
        for j in range(len(text2) + 1):
            dp[0][j] = 0

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )
        print(dp[-1][-1])
        return dp[-1][-1]


solution = Solution()
solution.longestCommonSubsequence("abcde", "ace")
