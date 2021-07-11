class Solution:
    def lck(self, word1, word2):
        dp = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        # base case 若word1 or word2的长度为0, 则lck = 0
        for i in range(len(word1) + 1):
            dp[i][0] = 0
        for j in range(len(word2) + 1):
            dp[0][j] = 0
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                # 在lck
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 不在lck
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )
        return dp[len(word1)][len(word2)]

    def minDistance(self, word1, word2):
        lck_len = self.lck(word1, word2)
        return len(word1) + len(word2) - 2 * lck_len
