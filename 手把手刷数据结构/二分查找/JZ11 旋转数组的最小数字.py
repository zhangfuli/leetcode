# 有一个长度为 n 的非降序数组，比如[1,2,3,4,5]，将它进行旋转，即把一个数组最开始的若干个元素搬到数组的末尾，变成一个旋转数组，比如变成了[3,4,5,1,2]，或者[4,5,1,2,3]这样的。请问，给定这样一个旋转数组，求数组中的最小值。
# 时间复杂度 logn

class Solution:
    def minNumberInRotateArray(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = int(left + (right - left) // 2)
            if nums[right] == nums[mid]:
                right -= 1
            elif nums[right] < nums[mid]:
                left = mid + 1
            elif nums[right] > nums[mid]:
                right = mid
        return nums[right]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minNumberInRotateArray([1, 0, 1, 1, 1]))