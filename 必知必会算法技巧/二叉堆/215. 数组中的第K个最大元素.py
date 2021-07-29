# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
import heapq


class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]


solution = Solution()
solution.findKthLargest([3, 2, 1, 5, 6, 4], 2)
