# 给定一个非负整数数组nums ，你最初位于数组的 第一个下标 。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标。
#
# 示例1：
#
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

# 每一步都计算一下从当前位置最远能够跳到哪里，
# 然后和一个全局最优的最远位置 farthest 做对比，通过每一步的最优解，更新全局最优解，这就是贪心。

class Solution:
    def canJump(self, nums):
        far = 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            # 跳不动了，没有跳到i这个位置
            print(far)
            if far <= i:
                return False
        print(far)
        print(len(nums))
        return far >= len(nums) - 1


solution = Solution()
print(solution.canJump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))
