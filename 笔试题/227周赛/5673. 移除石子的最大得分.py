class Solution:
    def __init__(self):
        self.res = 0

    def getStone(self, nums):
        nums.sort()
        if nums[1] != 0:
            nums[1] -= 1
            nums[2] -= 1
            self.res += 1
            self.getStone(nums)
        else:
            return None

    def maximumScore(self, a, b, c):
        self.getStone([a, b, c])
        return self.res


solution = Solution()
print(solution.maximumScore(2, 4, 6))
