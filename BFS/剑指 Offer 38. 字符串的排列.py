import itertools


class Solution:
    def __init__(self):
        self.result = []
    def permutation(self, s):
        result = []
        for pernumtation in itertools.permutations(s):
            result.append(''.join(list(pernumtation)))
        return list(set(result))

    def permutation_dfs(self, s):
        self.backtrack(s, '', [])
        return list(set(self.result))

    def backtrack(self, s, track, index):
        if len(track) == len(s):
            self.result.append(track[:])
            return None

        for i in range(len(s)):
            if i not in index:
                track += s[i]
                index.append(i)
                self.backtrack(s, track, index)
                index.pop(-1)
                track = track[:-1]

#     if 满足结束条件:
#         result.add(路径)
#         return
#
#     for 选择 in 选择列表:
#         做选择
#         backtrack(路径, 选择列表)
#         撤销选择


solution = Solution()
print(solution.permutation_dfs("abc"))