# 给定一个整数数组nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
#
# 示例 1：
#
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
#

class Solution:
    def __init__(self):
        self.res = False

    # 数字视角，是否放入桶
    def canPartitionKSubsets(self, nums, k) -> bool:
        def backtrack(nums, bucket, index, target):
            if index == len(nums):
                for i in range(len(bucket)):
                    if bucket[i] != target:
                        self.res = False
                self.res = True
                return

            for i in range(len(bucket)):
                if bucket[i] + nums[index] <= target:
                    bucket[i] += nums[index]
                    backtrack(nums, bucket, index + 1, target)
                    bucket[i] -= nums[index]

        if sum(nums) % k != 0:
            return False
        if k > len(nums):
            return False

        nums.sort(reverse=True)
        print(nums)
        target = sum(nums) // k
        bucket = [0 for i in range(k)]
        backtrack(nums, bucket, 0, target)
        return self.res

