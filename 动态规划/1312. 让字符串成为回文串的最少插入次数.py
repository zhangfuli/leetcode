class Solution:
    def minInsertions(self, s):
        # dp[i][j] 表示 从s[i]到s[j]插入的最小个数
        dp = [[0 for j in range(len(s) + 1)] for i in range(len(s) + 1)]

        # base case
        for i in range(len(s) + 1):
            dp[i][i] = 0

        # 从下往上，从右往左遍历
        for i in range(len(s), -1, -1):
            print(i)
            for j in range(i + 1, len(s) + 1):
                print(j)
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i + 1][j],
                        dp[i][j - 1]
                    ) + 1
        print(dp[0][len(s)])
        print(dp[1][len(s)])
        return dp[1][len(s)]


solution = Solution()
solution.minInsertions('mbadm')
