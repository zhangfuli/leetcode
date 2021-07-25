# 输入一个字符串，打印出该字符串中字符的所有排列。
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
# 示例:
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]

class Solution:
    def __init__(self):
        self.res = []

    def backtrack(self, s, track, visited):
        if len(track) == len(s):
            sub_res = ''.join(track[:])
            if sub_res not in self.res:
                self.res.append(sub_res)
            return

        for i in range(len(s)):
            if i not in visited:
                track.append(s[i])
                visited.append(i)
                self.backtrack(s, track, visited)
                visited.pop(-1)
                track.pop(-1)

    def permutation(self, s):
        self.backtrack(s, [], [])
        return self.res


solution = Solution()
print(solution.permutation('aab'))
