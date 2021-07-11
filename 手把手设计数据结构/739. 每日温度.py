class Solution:
    def dailyTemperatures(self, temperatures):
        mon_stack = [0 for i in range(len(temperatures))]

        # 这里放元素索引，而不是元素
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop(-1)
            if len(stack) != 0:
                mon_stack[i] = stack[-1] - i
            stack.append(i)
        return mon_stack


solution = Solution()
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
