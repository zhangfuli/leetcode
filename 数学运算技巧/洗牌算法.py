import random


class Solution:
    def shuffle(self, nums):
        for i in range(len(nums)):
            # randint [i, n]
            rdm = random.randint(i, len(nums) - 1)
            nums[rdm], nums[len(nums) - 1] = nums[len(nums) - 1], nums[rdm]
        return nums


solution = Solution()
print(solution.shuffle([0, 1, 2, 3, 4, 5]))
