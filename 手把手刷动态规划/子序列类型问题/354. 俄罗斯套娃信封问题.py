# 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
# 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
# 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
# 注意：不允许旋转信封。
# 示例 1：
# 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出：3
# 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

# 先对宽度 w 进行升序排序，如果遇到 w 相同的情况，则按照高度 h 降序排序。
# 之后把所有的 h 作为一个数组，在这个数组上计算 LIS(最长递增子序列) 的长度就是答案。
class Solution:
    def maxEnvelopes(self, envelopes):
        sort_env = sorted(envelopes, key=lambda d: (d[0], -d[1]))
        nums = [sort_env[i][1] for i in range(len(sort_env))]
        print(nums)
        # 声明以及base case
        dp = [1 for i in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            for j in range(1, i + 1):
                if nums[i - 1] > nums[j - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)


solution = Solution()
solution.maxEnvelopes(
    [[1, 15], [7, 18], [7, 6], [7, 100], [2, 200], [17, 30], [17, 45], [3, 5], [7, 8], [3, 6], [3, 10], [7, 20],
     [17, 3], [17, 45]])
