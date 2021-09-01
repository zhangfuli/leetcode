# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组nums中。
# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。
# 这里的 i - 1 和 i + 1 代表和i相邻的两个气球的序号。
# 如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
# 求所能获得硬币的最大数量。

# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

# 假设这个区间是个开区间，最左边索引 i，最右边索引 j
# 我这里说 “开区间” 的意思是，我们只能戳爆 i 和 j 之间的气球，i 和 j 不要戳
#
# DP思路是这样的，就先别管前面是怎么戳的，你只要管这个区间最后一个被戳破的是哪个气球
# 这最后一个被戳爆的气球就是 k
#
# k是这个区间   最后一个   被戳爆的气球！！！！！

# total = dp[i][k] + val[i] * val[k] * val[j] + dp[k][j]


class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        print(nums)

        # i-j之间最大的分数，不包含i，j
        dp = [[0 for j in range(len(nums))] for i in range(len(nums))]

        # base case
        for i in range(len(nums)):
            dp[i][i] = 0

        for i in range(len(nums), -1, -1):
            for j in range(i + 1, len(nums)):
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]
                    )
        return dp[0][-1]


solution = Solution()
solution.maxCoins([3, 1, 5, 8])
