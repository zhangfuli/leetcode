class Solution:
    # 辅助函数，若限制最大子数组和为 max，
    # 计算 nums 至少可以被分割成几个子数组
    def split(self, nums, max_value):
        m = 1

        # 记录子数组元素和
        s = 0
        for i in range(len(nums)):
            if s + nums[i] > max_value:
                m += 1
                s = nums[i]
            else:
                s += nums[i]
        return m

    def splitArray(self, nums, m):
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = int(left + (right - left) / 2)
            if self.split(nums, mid) == m:
                right = mid - 1
            elif self.split(nums, mid) < m:
                right = mid - 1
            elif self.split(nums, mid) > m:
                left = mid + 1
        return left
