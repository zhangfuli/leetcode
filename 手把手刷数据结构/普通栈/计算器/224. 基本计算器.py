# 给你一个字符串表达式s，请你实现一个基本计算器来计算并返回它的值。
#
# 示例 1：
# 输入：s = "1 + 1"
# 输出：2
#
# 示例 2：
# 输入：s = " 2-1 + 2 "
# 输出：3
#
# 示例 3：
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
import re


import re
from queue import Queue


class Solution:
    # 1+11-3
    def cal(self, s):
        print(s)
        if s[0] == '+':
            s = s[1:]
        nums = []
        right = len(s)
        for left in range(len(s) - 1, -1, -1):
            if s[left] == '+':
                nums.append(int(s[left + 1: right]))
                right = left
            elif s[left] == '-':
                nums.append(-1 * int(s[left + 1: right]))
                right = left

        if s[0] != '-':
            nums.append(int(s[:right]))

        return sum(nums)

    def calculate(self, s):
        s = ''.join(re.findall('[\d()+-]', s))
        print(s)
        stack = []

        for i in range(len(s)):
            if s[i] != ')':
                stack.append(s[i])
            elif s[i] == ')':
                # do something
                exp = ""
                while stack[-1] != '(':
                    exp = str(stack.pop()) + exp
                stack.pop()
                sub_cal = self.cal(exp)
                if len(stack) > 0:
                    if stack[-1] == '-':
                        if sub_cal < 0:
                            stack.pop()
                            stack.append('+')
                            sub_cal = -1 * sub_cal
                    elif stack[-1] == '+':
                        if sub_cal < 0:
                            stack.pop()
                stack.append(str(sub_cal))

        return self.cal(''.join(stack))


# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
solution = Solution()
# print(solution.cal("5-6"))

print(solution.calculate("1-(2+3-(4+(5-(1-(2+4-(5+6))))))"))
