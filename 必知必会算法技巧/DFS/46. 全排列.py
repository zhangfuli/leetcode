# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序返回答案。
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def __init__(self):
        self.res = []

    def backtrack(self, track, nums):
        if len(track) == len(nums):
            self.res.append(track[:])
            return

        for i in range(len(nums)):
            if nums[i] not in track:
                track.append(nums[i])
                self.backtrack(track, nums)
                track.pop(-1)

    def permute(self, nums):
        self.backtrack([], nums)
        return self.res

solution = Solution()
solution.permute([0,1])
