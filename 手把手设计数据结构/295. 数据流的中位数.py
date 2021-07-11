import bisect


class MedianFinder:

    def __init__(self):
        self.nums = []


    def addNum(self, num):
        bisect.insort(self.nums, num)


    def findMedian(self):
        mid = len(self.nums) // 2

        if len(self.nums) % 2 == 1:
            return self.nums[mid]
        else:
            return (self.nums[mid - 1] + self.nums[mid]) / 2