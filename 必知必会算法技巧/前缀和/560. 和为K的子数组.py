# 给定一个整数数组和一个整数k，你需要找到该数组中和为k的连续的子数组的个数。
#
# 示例 1 :
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
class Solution:
    def subarraySum(self, nums, k):
        # preSum = [0]
        # for i in range(len(nums)):
        #     preSum.append(preSum[-1] + nums[i])
        # # print(preSum)
        # res = 0
        # for i in range(len(preSum)):
        #     for j in range(i + 1, len(preSum)):
        #         if preSum[j] - preSum[i] == k:
        #             res += 1
        # return res

        hashmap = {}
        hashmap[0] = 1
        res = 0
        sum_i = 0
        for i in range(len(nums)):
            sum_i += nums[i]
            # 这里是减
            sum_j = sum_i - k
            if sum_j in hashmap:
                res += hashmap[sum_j]
            hashmap[sum_i] = hashmap.get(sum_i, 0) + 1
        return res


solution = Solution()
print(solution.subarraySum([1, 1, 1], 2))
