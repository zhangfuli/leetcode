class Solution:
    # 从后往前遍历创建单调栈
    def nextGreater(self, nums):
        stack = []
        res = []
        for i in range(len(nums) - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= nums[i]:
                stack.pop(-1)
            if len(stack) == 0:
                res.insert(0, -1)
            else:
                res.insert(0, stack[-1])
            stack.append(nums[i])
        return res

    def nextGreaterElement(self, nums1, nums2):
        stack = self.nextGreater(nums2)
        res = []
        for i in range(len(nums1)):
            res.append(stack[nums2.index(nums1[i])])
        return res


solution = Solution()
print(solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
