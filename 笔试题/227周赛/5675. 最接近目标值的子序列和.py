from functools import lru_cache


class Solution:
    def __init__(self):
        self.res = float('INF')

    def minAbsDifference(self, nums, goal):
        @lru_cache()
        def getSum(cur, cur_sum, goal):
            if len(nums) == cur + 1:
                self.res = min(self.res, abs(cur_sum - goal))
                return None

            self.res = min(self.res, abs(cur_sum - goal))
            if self.res == 0:
                return None
            getSum(cur + 1, cur_sum + 1 * nums[cur + 1], goal)
            # self.getSum(nums, total_len, cur + 1, cur_sum - 1 * nums[cur + 1], goal)
            if self.res == 0:
                return None
            getSum(cur + 1, cur_sum + 0 * nums[cur + 1], goal)

        getSum(-1, 0, goal)
        return self.res


solution = Solution()
print(solution.minAbsDifference([5, -7, 3, 5], 6))
