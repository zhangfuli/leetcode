class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)

        # 左边的最大值与右边的最小值
        max_left, min_right = 0, 0

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2

            # i + j = (m + n + 1) // 2
            j = (m + n + 1) // 2 - i

            x_1 = float("-inf") if i == 0 else nums1[i - 1]
            x = float("inf") if i == m else nums1[i]
            y_1 = float("-inf") if j == 0 else nums2[j - 1]
            y = float("inf") if j == n else nums2[j]

            # 左边的最大值小于右边的最小值
            if x_1 < y:
                max_left, min_right = max(x_1, y_1), min(x, y)
                left += 1
            else:
                right -= 1

        if (m + n) % 2 == 0:
            return (max_left + min_right) / 2
        else:
            return max_left


# 1, 3, 5
# 1, 1, 3, 6, 7