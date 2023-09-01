class Solution:
    def threeSum(self, nums):
        ans = []
        if nums is None or len(nums) < 3:
            return ans

        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 滑动指针
            left = i + 1
            right = len(nums) - 1
            while left < right:
                a_sum = nums[i] + nums[left] + nums[right]
                if a_sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    # 尽可能接近
                    while left < right and  nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif a_sum < 0:
                    # 要让一个数 大一点
                    left += 1
                elif a_sum > 0:
                    right -= 1
        return ans