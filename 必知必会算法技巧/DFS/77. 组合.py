# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 示例 1：
#
# 输入：n = 4, k = 2
# 输出：
# [
#     [2,4],
#     [3,4],
#     [2,3],
#     [1,2],
#     [1,3],
#     [1,4],
# ]

class Solution:
    def __init__(self):
        self.res = []

    def backtrack(self, nums, track, k, K):
        if len(track) == K:
            self.res.append(track[:])
            return
        for i in range(k, len(nums)):
            if nums[i] not in track:
                track.append(nums[i])
                self.backtrack(nums, track, i + 1, K)
                track.pop(-1)

    def combine(self, n: int, k: int):
        nums = [i + 1 for i in range(n)]
        self.backtrack(nums, [], 0, k)
        return self.res


solution = Solution()
print(solution.combine(4, 2))
