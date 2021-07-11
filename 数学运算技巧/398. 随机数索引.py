import random

class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        cnt = 0
        res = None
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                cnt += 1
                rdm = random.randint(1, cnt)
                if rdm == cnt:
                    res = i
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)