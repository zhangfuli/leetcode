class Solution(object):
    def longestOnes(self, nums, K):
        max_len = 0
        left = 0
        ones = 0  # 滑动窗口内1的个数
        for right in range(len(nums)):
            if nums[right] == 1:
                ones += 1
            zeros = right - left + 1 - ones
            while zeros > K:  # left 右移
                if nums[left] == 1:
                    ones -= 1
                else:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

    def find_longest_list(self, nums, K):
        max_len = 0
        left = 0
        ones = 0  # 滑动窗口内1的个数
        for right in range(len(nums)):
            if nums[right] == 1:
                ones += 1
            zeros = right - left + 1 - ones
            while zeros > K:  # left 右移
                if nums[left] == 1:
                    ones -= 1
                else:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        print(max_len)
        return max_len


solution = Solution()
solution.find_longest_list([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
