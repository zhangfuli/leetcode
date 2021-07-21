# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


class Solution:
    def __init__(self):
        self.res = []

    def backtrack(self, nums, track, k):
        if k <= len(nums):
            self.res.append(track[:])

        for i in range(k, len(nums)):
            if nums[i] not in track:
                track.append(nums[i])
                self.backtrack(nums, track, i + 1)
                track.pop(-1)

    def subsets(self, nums):
        self.backtrack(nums, [], 0)
        return self.res


solution = Solution()
print(solution.subsets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]))
