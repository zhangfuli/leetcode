class Solution:
    def __init__(self):
        self.dp_data = {}

    def minimumDeleteSum1(self, s1, s2):
        def dp(i, j):
            # base case
            if i == len(s1):
                res = 0
                for s2_index in s2[j:]:
                    res += ord(s2_index)
                self.dp_data[(i, j)] = res
                return self.dp_data[(i, j)]
            if j == len(s2):
                res = 0
                for s1_index in s1[i:]:
                    res += ord(s1_index)
                self.dp_data[(i, j)] = res
                return self.dp_data[(i, j)]
            if (i, j) in self.dp_data:
                return self.dp_data[(i, j)]
            if s1[i] == s2[j]:
                return dp(i + 1, j + 1)
            else:
                return min(
                    dp(i + 1, j) + ord(s1[i]),
                    dp(i, j + 1) + ord(s2[j])
                )

        return dp(0, 0)

    def minimumDeleteSum(self, s1, s2):
        dp = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
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
                        dp[i][j - 1] + ord(s2[j - 1]),
                    )
        return dp[len(s1)][len(s2)]


solution = Solution()
print(solution.minimumDeleteSum('ccaccjp', 'fwosarcwge'))
