class MonotonicQueue:
    def __init__(self):
        self.queue = []

    # 在队尾添加元素 n  把前面的都压死
    def push(self, n):
        while len(self.queue) != 0 and self.queue[-1] < n:
            self.queue.pop(-1)
        self.queue.append(n)

    def max_value(self):
        return self.queue[0]

    # 队头元素如果是 n，删除它
    def pop(self, n):
        if self.queue[0] == n:
            self.queue.pop(0)


class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        if len(nums) <= k:
            return [max(nums)]
        mon_queue = MonotonicQueue()
        for i in range(len(nums)):
            if i < k - 1:
                mon_queue.push(nums[i])
            else:
                mon_queue.push(nums[i])
                res.append(mon_queue.max_value())
                mon_queue.pop(nums[i - k + 1])
        return res


solution = Solution()
print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
