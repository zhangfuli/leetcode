class Solution:
    def __init__(self):
        self.dp_data = {}
    # 返回text1[i:] 的LCS
    def longestCommonSubsequence1(self, text1, text2):
        def dp(i, j):
            # base case
            if i == len(text1):
                self.dp_data[(i, j)] = 0
                return 0
            if j == len(text2):
                self.dp_data[(i, j)] = 0
                return 0
            if (i, j) in self.dp_data:
                return self.dp_data[(i, j)]
            if text1[i] == text2[j]:
                self.dp_data[(i, j)] = dp(i + 1, j + 1) + 1
            else:
                self.dp_data[(i, j)] = max(
                    dp(i, j + 1),
                    dp(i + 1, j),
                    dp(i + 1, j + 1)
                )
            return self.dp_data[(i, j)]

        return dp(0, 0)

    def longestCommonSubsequence2(self, text1, text2):
        dp = [[float('INF') for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        # base case
        for i in range(len(text1) + 1):
            dp[i][0] = 0
        for j in range(len(text2) + 1):
            dp[0][j] = 0
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                # 在最长公共子序列中
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 不在最长公共子序列中
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )
        return dp[len(text1)][len(text2)]


solution = Solution()
print(solution.longestCommonSubsequence2('abcde', 'ace'))
