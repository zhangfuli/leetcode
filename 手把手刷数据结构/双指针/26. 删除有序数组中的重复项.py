class Solution:
    def removeDuplicates(self, nums):
        left = 0
        for right in range(0, len(nums)):
            if nums[left] == nums[right]:
                continue
            else:
                left += 1
                nums[left] = nums[right]
        return left + 1

