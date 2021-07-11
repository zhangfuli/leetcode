class Solution:
    # 动态规划
    def jump_1(self, nums):
        # 返回从i跳到最后一个位置至少需要多少步
        dp = [float('INF') for i in range(len(nums))]
        # base case
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= len(nums) - 1 - i:
                dp[i] = 1
            else:
                dp[i] = min(dp[i: i + nums[i] + 1]) + 1
        print(dp)
        return dp[0]

    # 贪心
    def jump(self, nums):
        n = len(nums)
        end, farthest = 0, 0
        jumps = 0
        for i in range(n-1):
            farthest = max(nums[i] + i, farthest)
            if end == i:
                jumps += 1
                end = farthest
        return jumps



solution = Solution()
solution.jump([1, 2, 3])
