# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
#
# 示例1：
#
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的

class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        return max(
            self.robRange(nums[0:len(nums) - 1]),
            self.robRange(nums[1:len(nums)])
        )

    def robRange(self, nums):
        # 抢到第i间房间，能抢到的金额
        dp = [0 for i in range(len(nums) + 1)]

        # base case
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            dp[i] = max(
                dp[i - 1],  # 第i个不抢
                dp[i - 2] + nums[i - 1]  # 第i个抢
            )
        # print(dp)
        return dp[-1]


solution = Solution()
print(solution.rob([2, 3, 2]))
