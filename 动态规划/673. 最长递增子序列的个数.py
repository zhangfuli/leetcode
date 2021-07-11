class Solution:
    def LIS(self, nums):
        # 最长递增子序列
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def findNumberOfLIS(self, nums):
        # 最长递增子序列
        dp = [1 for i in range(len(nums))]
        count = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i + 1):
                if nums[j] < nums[i]:
                    if dp[i] == dp[j] + 1:
                        count[i] += count[j]
                    elif dp[i] < dp[j] + 1:
                        count[i] = count[j]
                    dp[i] = max(dp[i], dp[j] + 1)
        res = 0
        for i in range(len(nums)):
            if dp[i] == max(dp):
                res += count[i]
        print(dp)
        print(count)
        return res


solution = Solution()
solution.findNumberOfLIS(
    [1, 2, 4, 3, 5, 4, 7, 2])
