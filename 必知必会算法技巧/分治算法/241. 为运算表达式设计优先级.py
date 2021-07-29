# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。
# 你需要给出所有可能的组合的结果。有效的运算符号包含 +,-以及*。
#
# 示例1:
#
# 输入: "2-1-1"
# 输出: [0, 2]
# 解释:
# ((2-1)-1) = 0
# (2-(1-1)) = 2

# List<Integer> diffWaysToCompute("(1 + 2 * 3) - (4 * 5)") {
#     List<Integer> res = new LinkedList<>();
#     /****** 分 ******/
#     List<Integer> left = diffWaysToCompute("1 + 2 * 3");
#     List<Integer> right = diffWaysToCompute("4 * 5");
#     /****** 治 ******/
#     for (int a : left)
#       for (int b : right)
#           res.add(a - b);
#
#     return res;
# }
import re


class Solution:
    def __init__(self):
        self.hashmap = {}

    def diffWaysToCompute(self, expression):
        # base case
        if not re.search("[+\-*]", expression):
            return [int(expression)]

        res = []
        for i in range(len(expression)):
            if expression[i] == '+':
                if expression[:i] in self.hashmap:
                    left = self.hashmap[expression[:i]]
                else:
                    left = self.diffWaysToCompute(expression[:i])
                    self.hashmap[expression[:i]] = left
                if expression[i + 1:] in self.hashmap:
                    right = self.hashmap[expression[i + 1:]]
                else:
                    right = self.diffWaysToCompute(expression[i + 1:])
                    self.hashmap[expression[i + 1:]] = right
                for j in range(len(left)):
                    for z in range(len(right)):
                        res.append(left[j] + right[z])

            elif expression[i] == '-':
                if expression[:i] in self.hashmap:
                    left = self.hashmap[expression[:i]]
                else:
                    left = self.diffWaysToCompute(expression[:i])
                    self.hashmap[expression[:i]] = left
                if expression[i + 1:] in self.hashmap:
                    right = self.hashmap[expression[i + 1:]]
                else:
                    right = self.diffWaysToCompute(expression[i + 1:])
                    self.hashmap[expression[i + 1:]] = right
                for j in range(len(left)):
                    for z in range(len(right)):
                        res.append(left[j] - right[z])

            elif expression[i] == '*':
                if expression[:i] in self.hashmap:
                    left = self.hashmap[expression[:i]]
                else:
                    left = self.diffWaysToCompute(expression[:i])
                    self.hashmap[expression[:i]] = left
                if expression[i + 1:] in self.hashmap:
                    right = self.hashmap[expression[i + 1:]]
                else:
                    right = self.diffWaysToCompute(expression[i + 1:])
                    self.hashmap[expression[i + 1:]] = right
                for j in range(len(left)):
                    for z in range(len(right)):
                        res.append(left[j] * right[z])
        return res


solution = Solution()
print(solution.diffWaysToCompute("11"))
