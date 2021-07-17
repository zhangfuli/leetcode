class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                continue
            else:
                nums[left] = nums[right]
                left += 1
        for i in range(left, len(nums)):
            nums[i] = 0