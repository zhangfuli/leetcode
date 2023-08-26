# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 整数除法仅保留整数部分。
#
# 示例 1：
# 输入：s = "3+2*2"
# 输出：7
#
# 示例 2：
# 输入：s = " 3/2 "
# 输出：1
import re


class Solution:
    def calculate(self, s):
        s = ''.join(re.findall('[\d()\+\-\*/]', s))
        s = s.replace('/', '//')
        return int(eval(s))


solution = Solution()
print(solution.calculate("14/3*2"))
