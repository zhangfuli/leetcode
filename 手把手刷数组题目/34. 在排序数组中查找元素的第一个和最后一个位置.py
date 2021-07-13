class Solution:
    def left_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def right_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if right < 0 or nums[right] != target:
            return -1
        return right

    def searchRange(self, nums, target):
        return [self.left_bound(nums, target), self.right_bound(nums, target)]
