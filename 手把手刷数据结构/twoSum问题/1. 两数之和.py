# 给定一个整数数组 nums和一个整数目标值 target，
# 请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
#
#
# 示例 1：
#
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。


class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            another_num = target - nums[i]
            if another_num in hashmap:
                return [hashmap[another_num], i]
            hashmap[nums[i]] = i
