# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
# 例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#
# 示例 1：
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
class Solution:
    def lengthOfLIS(self, nums):
        # 以i为结尾的 的最长递增子序列
        dp = [1 for i in range(len(nums) + 1)]

        # base case
        for i in range(len(nums) + 1):
            dp[i] = 1

        for i in range(1, len(nums) + 1):
            for j in range(1, i + 1):
                if nums[i - 1] > nums[j - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        print(dp)
        return max(dp)


solution = Solution()
solution.lengthOfLIS(
    [1, 3, 6, 7, 9, 4, 10, 5, 6]
)
