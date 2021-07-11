class Solution:
    def minElements(self, nums, limit, goal):
        _sum = sum(nums)
        # print(_sum)
        p = abs(goal - _sum)
        if p % limit == 0:
            return p // limit
        return p // limit + 1


solution = Solution()
print(solution.minElements([1,  1, 1], 100, 3))
