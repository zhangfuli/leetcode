# 给你一个按升序排序的整数数组 num（可能包含重复数字），
# 请你将它们分割成一个或多个长度至少为 3 的子序列，其中每个子序列都由连续整数组成。
# 如果可以完成上述分割，则返回 true ；否则，返回 false 。
#
# 示例 1：
# 输入: [1,2,3,3,4,5]
# 输出: True
# 解释:
# 你可以分割出这样两个连续子序列 :
# 1, 2, 3
# 3, 4, 5


class Solution:
    def isPossible(self, nums):
        sub_num = []
        for i in range(len(nums)):
            for sub in sub_num:
                if sub[-1] + 1 == nums[i]:
                    sub.append(nums[i])
                    break
            else:
                sub_num.insert(0, [nums[i]])
        print(sub_num)
        return all(len(sub) >= 3 for sub in sub_num)


solution = Solution()
print(solution.isPossible([1, 2, 3, 3, 4, 5]))
