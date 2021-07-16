## [2,1,2,4,3]

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        mon_stack = [-1 for i in range(len(nums2))]
        stack = []

        # 倒着往栈里放
        for i in range(len(nums2) - 1, -1 ,-1):

            # 判定个子高矮
            while len(stack) != 0 and stack[-1] < nums2[i]:
                # 矮个子起开
                stack.pop(-1)
            # nums[i] 身后的 next great number
            if len(stack) != 0:
                mon_stack[i] = stack[-1]
            stack.append(nums2[i])

        res = []
        for i in range(len(nums1)):
            res.append(mon_stack[nums2.index(nums1[i])])
        return res