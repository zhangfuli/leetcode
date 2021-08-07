# 给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。
#
# 示例 1:
#
# 输入: s1 = "sea", s2 = "eat"
# 输出: 231
# 解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
# 在 "eat" 中删除 "t" 并将 116 加入总和。
# 结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。

class Solution:
    def minimumDeleteSum(self, s1, s2):
        dp = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

        res = 0
        # base case
        dp[0][0] = 0
        for i in range(1, len(s1) + 1):
            dp[i][0] = ord(s1[i - 1]) + dp[i - 1][0]
        for j in range(1, len(s2) + 1):
            dp[0][j] = ord(s2[j - 1]) + dp[0][j - 1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),
                        dp[i][j - 1] + ord(s2[j - 1])
                    )

        return dp[-1][-1]


solution = Solution()
solution.minimumDeleteSum(
    "ccaccjp",
    "fwosarcwge"
)
