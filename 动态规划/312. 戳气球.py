# https://mp.weixin.qq.com/s/I0yo0XZamm-jMpG-_B3G8g
class Solution:
    def maxCoins(self, nums):
        # i-j之间最大的分数，不包含i，j
        nums = [1] + nums + [1]
        dp = [[0 for j in range(len(nums))] for i in range(len(nums))]

        # base case 对角线上都为0
        for i in range(len(nums)):
            dp[i][i] = 0

        for i in range(len(nums), -1, -1):
            for j in range(i + 1, len(nums)):
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j])
        print(dp[0][len(nums) - 1])
        return dp[0][len(nums) - 1]


solution = Solution()
solution.maxCoins([3, 1, 5, 8])
