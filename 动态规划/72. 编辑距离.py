class Solution:
    def __init__(self):
        self.dp_data = {}

    def minDistance1(self, word1, word2):
        def dp(i, j):
            # base case
            if i == -1:
                self.dp_data[(-1, j)] = j + 1
                return j + 1
            if j == -1:
                self.dp_data[(i, -1)] = i + 1
                return i + 1
            if (i, j) in self.dp_data:
                return self.dp_data[(i, j)]
            if word1[i] == word2[j]:
                self.dp_data[(i, j)] = dp(i - 1, j - 1)  # 两位置相同什么也不做
            else:
                self.dp_data[(i, j)] = min(
                    dp(i - 1, j) + 1,  # i 删除
                    dp(i, j - 1) + 1,  # i 后 插入
                    dp(i - 1, j - 1) + 1  # 替换
                )
            return self.dp_data[(i, j)]

        dp(len(word1) - 1, len(word2) - 1)
        return self.dp_data[(len(word1) - 1, len(word2) - 1)]

    def minDistance2(self, word1, word2):
        dp = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        for i in range(len(word2) + 1):
            dp[0][i] = i
        for j in range(len(word1) + 1):
            dp[j][0] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # 删除
                        dp[i][j - 1] + 1,  # 插入
                        dp[i - 1][j - 1] + 1  # 替换
                    )

        return dp[len(word1)][len(word2)]


solution = Solution()
print(solution.minDistance2("horse", "ros"))
