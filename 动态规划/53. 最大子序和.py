class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        # base case
        dp = [nums[i - 1] for i in range(len(nums) + 1)]
        dp[0] = 0
        for i in range(1, len(nums) + 1):
            dp[i] = max(dp[i], dp[i - 1] + nums[i - 1])
        print(dp)
        return max(dp[1:])


solution = Solution()
solution.maxSubArray([])
