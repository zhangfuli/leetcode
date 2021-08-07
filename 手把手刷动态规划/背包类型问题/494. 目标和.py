# 给你一个整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加'+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
# 示例 1：
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3


# 首先，如果我们把 nums 划分成两个子集 A 和 B，分别代表分配 + 的数和分配 - 的数，那么他们和 target 存在如下关系：
#
# sum(A) - sum(B) = target
# sum(A) = target + sum(B)
# sum(A) + sum(A) = target + sum(B) + sum(A)
# 2 * sum(A) = target + sum(nums)
# 综上，可以推出 sum(A) = (target + sum(nums)) / 2，
# 也就是把原问题转化成：nums 中存在几个子集 A，使得 A 中元素的和为 (target + sum(nums)) / 2

class Solution:
    def findTargetSumWays(self, nums, target):
        if sum(nums) < target or (target + sum(nums)) % 2 != 0:
            return 0
        sum_a = (target + sum(nums)) // 2
        # 前i个物品凑成j的种类
        dp = [[0 for j in range(sum_a + 1)] for i in range(len(nums) + 1)]

        # base case
        for i in range(len(nums) + 1):
            dp[i][0] = 1
        # for j in range(sum_a + 1):
        #     dp[0][j] = 1
        # dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            for j in range(sum_a + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


solution = Solution()
solution.findTargetSumWays([1, 1, 1, 1, 1], 3)
