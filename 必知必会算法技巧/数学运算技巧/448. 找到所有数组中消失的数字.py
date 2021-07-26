# 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
# 请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
#
# 示例 1：
#
# 输入：nums = [4,3,2,7,8,2,3,1]
# 输出：[5,6]

class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -1 * nums[abs(nums[i]) - 1]
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res

solution = Solution()
solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
