# 给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。
#
# 示例 1:
#
# 输入: s1 = "sea", s2 = "eat"
# 输出: 231
# 解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
# 在 "eat" 中删除 "t" 并将 116 加入总和。
# 结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。

class Solution:
    def minimumDeleteSum(self, s1, s2):
        return None