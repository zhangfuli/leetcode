# https://blog.csdn.net/weixin_42784951/article/details/88963758

class Solution:
    def trap(self, height):
        res = 0
        # 递减栈
        stack = []
        for i in range(len(height)):
            while stack and stack[-1][0] < height[i]:
                last_height, last_index = stack.pop()
                if stack:
                    res += (i - stack[-1][1] - 1) * (min(height[i], stack[-1][0]) - last_height)
            stack.append([height[i], i])
        return res


solution = Solution()
solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
