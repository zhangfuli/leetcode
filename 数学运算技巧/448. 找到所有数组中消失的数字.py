# 当前元素是nums[i]，那么我们把第nums[i]−1 位置的元素乘以 -1，表示这个该位置出现过
# 如果第 nums[i]−1 位置的元素已经是负数了，表示nums[i]已经出现过了，就不用再把第nums[i]−1 位置的元素乘以 -1
# 对数组中的每个位置遍历一遍，如果i位置的数字是正数，说明i未出现过


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
print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
