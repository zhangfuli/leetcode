class Solution:
    def maxEnvelopes(self, envelopes):
        if len(envelopes) == 0:
            return 0
        # 第一个元素升序，第二个元素降序
        sorted_env = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        nums = [i[1] for i in sorted_env]
        # base case
        dp = [1 for i in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


solution = Solution()
solution.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3], [6, 5]])
