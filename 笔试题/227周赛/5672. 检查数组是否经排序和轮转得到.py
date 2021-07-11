class Solution:

    def run(self, nums, K):
        another = nums[K:] + nums[:K]
        print(another)
        return another

    def check(self, nums):
        for i in range(len(nums)):
            if self.run(nums, i) == sorted(nums):
                return True
        return False


solution = Solution()
solution.check([3, 4, 5, 1, 2])
