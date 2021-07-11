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
