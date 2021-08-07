# 给你一个 只包含正整数 的 非空 数组nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 示例 1：
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
class Solution:
    def canPartition(self, nums):
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [[False for j in range(target + 1)] for i in range(len(nums) + 1)]

        # base case
        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(target + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]