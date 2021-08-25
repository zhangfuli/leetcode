# 给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和 '*'的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
# 示例 1：
# 输入：s = "aa" p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#
# 示例 2:
# 输入：s = "aa" p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
# 示例3：
# 输入：s = "ab" p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）


class Solution:
    def isMatch(self, s, p):
        if len(p) == 0:
            return 0 == len(s)
        first_match = len(s) > 0 and p[0] in {s[0], '.'}

        # 处理 *
        if len(p) >= 2 and p[1] == '*':
            # 匹配 0 或者 匹配多个
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        # 处理 .
        return first_match and self.isMatch(s[1:], p[1:])