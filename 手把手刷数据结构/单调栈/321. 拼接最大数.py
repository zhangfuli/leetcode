# 给定长度分别为m和n的两个数组，其元素由0-9构成，表示两个自然数各位上的数字。
# 现在从这两个数组中选出 k (k <= m + n)个数字拼接成一个新的数，
# 要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
#
# 求满足该条件的最大数。结果返回一个表示该最大数的长度为k的数组。
# 说明: 请尽可能地优化你算法的时间和空间复杂度。
#
# 示例1:
#
# 输入:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# 输出:
# [9, 8, 6, 5, 3]

# 从 nums1 中 取 min(i, len(nums1))min(i,len(nums1)) 个数形成新的数组 A（取的逻辑同第一题），其中 i 等于 0,1,2, ... k。
# 从 nums2 中 对应取 min(j, len(nums2))min(j,len(nums2)) 个数形成新的数组 B（取的逻辑同第一题），其中 j 等于 k - i。
# 将 A 和 B 按照上面的 merge 方法合并
# 上面我们暴力了 k 种组合情况，我们只需要将 k 种情况取出最大值即可。


class Solution:
    def merge(self, nums1, nums2):
        res = []
        while len(nums1) != 0 or len(nums2) != 0:
            if nums1 > nums2:
                temp = nums1
            else:
                temp = nums2
            res.append(temp.pop(0))
        return res

    def get_max_num(self, nums, k):
        stack = []
        remove = len(nums) - k
        for i in range(len(nums)):
            while len(stack) != 0 and stack[-1] < nums[i] and remove > 0:
                stack.pop()
                remove -= 1
            stack.append(nums[i])
        return stack[:k]

    def maxNumber(self, nums1, nums2, k):
        res = []
        for i in range(0, k + 1):
            nums1_max = self.get_max_num(nums1, i)
            nums2_max = self.get_max_num(nums2, k - i)
            m = self.merge(nums1_max, nums2_max)
            if len(m) == k:
                res.append(m)
        return max(res)


solution = Solution()
print(solution.maxNumber([6, 7], [6, 0, 4], 5))
