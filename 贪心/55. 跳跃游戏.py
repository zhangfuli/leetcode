class Solution:
    def canJump(self, nums):
        far = 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            # 跳不动了，没有跳到i这个位置
            if far <= i:
                return False
        print(far)
        print(len(nums))
        # 跳到或者跳过最后一个位置
        return far >= len(nums) - 1


solution = Solution()
solution.canJump([3, 2, 1, 0, 4])
