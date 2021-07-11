class Solution:
    # 记录nums[0,i]的和
    def preSum(self, nums):
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[i] + nums[i])
        return presum

    def subarraySum1(self, nums, k):
        presum = self.preSum(nums)
        res = 0
        print(presum)
        for i in range(len(nums)):
            for j in range(i + 1):
                if presum[i + 1] - presum[j] == k:
                    res += 1
        return res

    # 需要前缀和8就能找到和为k的子数组了，之前的暴力解法需要遍历数组去数有几个8
    # 优化解法借助哈希表可以直接得知有几个前缀和为8
    def subarraySum(self, nums, k):
        # base case
        hashmap = {
            0: 1
        }
        presum_i = 0
        res = 0
        for i in range(len(nums)):
            presum_i += nums[i]
            presum_j = presum_i - k
            if presum_j in hashmap:
                res += hashmap[presum_j]

            if presum_i in hashmap:
                hashmap[presum_i] += 1
            else:
                hashmap[presum_i] = 1
            print(hashmap)
        return res


solution = Solution()
print(solution.subarraySum([1, 1, 1], 2))
