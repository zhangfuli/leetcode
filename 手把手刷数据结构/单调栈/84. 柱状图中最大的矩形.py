# 计算每个柱子出的最大面积的时候是分别找到左边第一个比它小的柱子位置x和右边第一个比它小的柱子y来计算的。
# 当我们弹出一个元素的时候，因为是单调递增栈因此栈顶元素值一定是它左边第一个小于它的元素，
# 使它弹出的那个元素一定是它右边第一个小于它的值

class Solution:
    def largestRectangleArea(self, heights):
        # 递增栈
        stack = [[0, -1]]
        heights.append(0)

        S = [0] * len(heights)
        for i in range(len(heights)):
            while stack and stack[-1][0] > heights[i]:
                last_height, last_index = stack.pop(-1)
                S[last_index] = last_height * (i - stack[-1][1] - 1)
            stack.append([heights[i], i])
        return max(S)


solution = Solution()
print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
