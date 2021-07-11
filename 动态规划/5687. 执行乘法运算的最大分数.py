class Solution:
    def maximumScore(self, nums, multipliers):
        # nums选取的前i个以及后j个的最大值
        dp = [[0 for j in range(len(multipliers) + 1)] for i in range(len(multipliers) + 1)]
        # base case
        dp[0][0] = 0
        # 只拿nums前面的
        for i in range(1, len(multipliers) + 1):
            dp[i][0] = dp[i - 1][0] + nums[i - 1] * multipliers[i - 1]
        # 只拿nums后面的

        for j in range(1, len(multipliers) + 1):
            dp[0][j] = dp[0][j - 1] + nums[len(nums) - j] * multipliers[j - 1]
        for i in range(1, len(multipliers) + 1):
            for j in range(1, len(multipliers) + 1):
                if i + j > len(multipliers):
                    continue
                dp[i][j] = max(
                    dp[i - 1][j] + nums[i - 1] * multipliers[i + j - 1],  # 从前拿
                    dp[i][j - 1] + nums[len(nums) - j] * multipliers[i + j - 1] # 从后拿
                )

        res = -1 * float('INF')
        for i in range(1, len(multipliers) + 1):
            for j in range(1, len(multipliers) + 1):
                if i + j == len(multipliers):
                    res = max(res, dp[i][j])

        print(res)
        return res


solution = Solution()
solution.maximumScore([1, 2, 3], [3, 2, 1])
