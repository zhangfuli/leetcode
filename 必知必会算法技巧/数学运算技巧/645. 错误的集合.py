# 集合 s 包含从 1 到n的整数。
# 不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，
# 导致集合丢失了一个数字并且 有一个数字重复 。
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。
# 请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
#
# 示例 1：
# 输入：nums = [1,2,2,4]
# 输出：[2,3]

class Solution:
    def findErrorNums(self, nums):
        global dup
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -1 * nums[abs(nums[i]) - 1]
            else:
                dup = abs(nums[i])

        for i in range(len(nums)):
            if nums[i] > 0:
                return [dup, i + 1]


solution = Solution()
solution.findErrorNums([1, 2, 2, 4])
