# 转化思路 此题可以转化为nums的子集中和为sum(nums)/2+target的个数。证明如下：
#
# 设nums中前面为+号的为sum(a)，num中前面为-号的数字为sum(b)
# sum(a) - sum(b) = target
# sum(a) - sum(b) + sum(a) + sum(b) = target + sum(a) + sum(b)
# 2 * sum(a) = target + sum(nums)
# sum(a) = (target + sum(nums)) /2
# 典型的背包问题模版，外层循环为nums， 状态转移为 dp[j] = dp[j]+ dp[j - num]
# 对上述背包问题的直观理解为，外层循环是nums，内层里面右边dp[j]是用当前num前面的数字可以构造target为j的个数，dp[j-num]是当前num前面的数字可以构造target为j-num的个数,左边dp[j]是用加上当前num可以构造target为j的个数


class Solution:
    def findTargetSumWays(self, nums, S):
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        P = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            for j in range(P, num - 1, -1): dp[j] += dp[j - num]
        return dp[P]

