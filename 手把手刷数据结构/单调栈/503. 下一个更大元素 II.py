class Solution:
    def nextGreaterElements(self, nums):
        nums = nums + nums
        mon_stack = [-1 for i in range(len(nums))]
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= nums[i]:
                stack.pop(-1)
            if len(stack) != 0:
                mon_stack[i] = stack[-1]
            stack.append(nums[i])
        return mon_stack[:len(nums) // 2]


solution = Solution()
solution.nextGreaterElements([1, 2, 1])
print(solution.nextGreaterElements([1, 2, 1]))
