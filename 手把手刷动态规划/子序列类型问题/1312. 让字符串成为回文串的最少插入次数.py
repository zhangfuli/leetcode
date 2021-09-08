# 给你一个字符串s，每一次操作你都可以在字符串的任意位置插入任意字符。
# 请你返回让s成为回文串的最少操作次数。
# 「回文串」是正读和反读都相同的字符串。
#
#
# 示例 1：
#
# 输入：s = "zzazz"
# 输出：0
# 解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。

class Solution:
    def minInsertions(self, s):
        # dp[i][j] 表示 从s[i]到s[j]插入的最小个数
        dp = [[0 for j in range(len(s) + 1)] for i in range(len(s) + 1)]

        # base case
        for i in range(len(s) + 1):
            dp[i][i] = 0

        for i in range(len(s), -1, -1):
            for j in range(i + 1, len(s) + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i + 1][j],
                        dp[i][j - 1]
                    ) + 1
        return dp[1][-1]


solution = Solution()
print(solution.minInsertions("zzazz"))
