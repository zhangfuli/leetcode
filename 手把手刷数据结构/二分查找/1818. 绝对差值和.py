from typing import List
import bisect


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        const_mod = 1000000007
        n = len(nums1)
        arr = sorted(nums1)
        sum, maxDiff = 0, 0
        for i in range(n):
            preDiff = abs(nums1[i] - nums2[i])
            j = bisect.bisect_left(arr, nums2[i])
            if j < n:
                maxDiff = max(maxDiff, preDiff - (arr[j] - nums2[i]))
            if j > 0:
                maxDiff = max(maxDiff, preDiff - (nums2[i] - arr[j - 1]))
            sum = (sum + preDiff) % const_mod
        sum = (sum - maxDiff + const_mod) % const_mod
        return sum
