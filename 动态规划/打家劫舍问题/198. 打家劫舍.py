class Solution:
    def rob(self, nums):
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
        print(dp)
        return dp[len(nums)]


solution = Solution()
solution.rob([2, 7, 9, 3, 1])
