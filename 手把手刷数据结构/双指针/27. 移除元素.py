class Solution:
    def removeElement(self, nums, val):
        left = 0
        for right in range(len(nums)):
            if nums[right] == val:
                continue
            else:
                nums[left] = nums[right]
                left += 1
        return left