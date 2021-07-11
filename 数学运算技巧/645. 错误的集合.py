class Solution:
    def findErrorNums(self, nums):
        a, b = 0, 0
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -1 * nums[abs(nums[i]) - 1]
            else:
                a = abs(nums[i])
        for i in range(len(nums)):
            if nums[i] > 0:
                b = i + 1
        return [a, b]


solution = Solution()
print(solution.findErrorNums([1, 1]))
