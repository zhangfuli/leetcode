# 数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]

class Solution:
    def __init__(self):
        self.res = []

    def backtrack(self, nums, track, n):
        if len(track) == 2 * n:
            if track.count('(') == track.count(')'):
                self.res.append(''.join(track))
            return

        for i in range(len(nums)):
            if track.count('(') >= track.count(')'):
                track.append(nums[i])
                self.backtrack(nums, track, n)
                track.pop(-1)

    def generateParenthesis(self, n: int):
        nums = ['(', ')']
        self.backtrack(nums, [], n)
        return self.res


solution = Solution()
print(solution.generateParenthesis(1))
