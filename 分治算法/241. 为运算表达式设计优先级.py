class Solution:
    def __init__(self):
        self.res = []

    def diffWaysToCompute(self, expression):
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i in range(len(expression)):
            if expression[i] == '+':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for i in range(len(left)):
                    for j in range(len(right)):
                        res.append(left[i] + right[j])
            elif expression[i] == '-':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for i in range(len(left)):
                    for j in range(len(right)):
                        res.append(left[i] - right[j])
            elif expression[i] == '*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for i in range(len(left)):
                    for j in range(len(right)):
                        res.append(left[i] * right[j])
            elif expression[i] == '/':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for i in left:
                    for j in right:
                        res.append(left[i] / right[j])
        return res


solution = Solution()
print(solution.diffWaysToCompute("2*3-4*5"))
