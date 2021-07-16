class Solution:
    # 删除排序数组中的重复项目  原地修改
    def removeDuplicates(self, nums):
        slow = 0
        for fast in range(0, len(nums)):
            if nums[slow] == nums[fast]:
                continue
            else:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1