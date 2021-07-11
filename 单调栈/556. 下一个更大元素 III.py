class Solution:
    def nextGreaterElement(self, n):
        nums = list(str(n))
        swap_1 = len(nums) - 2
        while swap_1 >= 0:
            if nums[swap_1] >= nums[swap_1 + 1]:
                swap_1 -= 1
            else:
                break
        if swap_1 == -1:
            return -1

        swap_2 = len(nums) - 1
        while swap_2 >= 0:
            if nums[swap_1] < nums[swap_2]:
                break
            swap_2 -= 1
        nums[swap_1], nums[swap_2] = nums[swap_2], nums[swap_1]
        print(nums)
        after = nums[-1:swap_1:-1]
        nums = nums[:swap_1 + 1] + after
        res = int(''.join(nums))
        if res >= 2 ** 31:
            return -1
        return res


solution = Solution()
print(solution.nextGreaterElement(4765321))
print(2 ** 31)
