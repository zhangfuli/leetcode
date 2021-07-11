# int[] arr = {1,2,3,4,5};
# int n = arr.length, index = 0;
# while (true) {
#     print(arr[index % n]);
#     index++;
# }
# 数组取模来模拟环形


class Solution:
    def nextGreaterElements(self, nums):
        stack = []
        res = []
        n = len(nums)
        for i in range(2 * n - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= nums[i % n]:
                stack.pop()
            if len(stack) == 0:
                res.insert(0, -1)
            else:
                res.insert(0, stack[-1])
            stack.append(nums[i % n])
        print(res)
        return res[:n]


solution = Solution()
solution.nextGreaterElements([2, 1, 2, 4, 3])
