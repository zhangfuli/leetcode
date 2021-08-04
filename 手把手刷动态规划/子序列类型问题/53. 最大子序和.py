# 给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组[4,-1,2,1]的和最大，为6 。
class Solution:
    def maxSubArray(self, nums):
        # 以 nums[i] 为结尾的「最大子数组和」为 dp[i]。
        # 以 nums[3] 为例， 其连续子数组为-2，1，-3，4/1，-3，4/-3，4/4
        dp = [0] * (len(nums))
        # base case
        for i in range(len(nums)):
            dp[i] = nums[i]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        print(dp)
        return max(dp)


solution = Solution()
solution.maxSubArray([-1])
