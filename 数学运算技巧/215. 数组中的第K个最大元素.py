import heapq


class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]


solution = Solution()
solution.findKthLargest([3, 2, 1, 5, 6, 4], 2)
