class Solution:
    def canPartition(self, nums):
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        if len(nums) < 2:
            return False

        # 存放是否能放满sum/2
        dp = [[-1 for j in range(int(sum_nums / 2) + 1)] for i in range(len(nums) + 1)]

        for i in range(int(sum_nums / 2) + 1):
            dp[0][i] = False
        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, int(sum_nums / 2) + 1):
                if j - nums[i - 1] < 0:
                    # 背包容量不足
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 不放第i个 or 放第i个
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        return dp[len(nums)][int(sum_nums / 2)]


solution = Solution()
print(solution.canPartition([2, 13, 1]))
