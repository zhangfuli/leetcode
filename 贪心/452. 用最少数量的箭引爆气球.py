class Solution:
    # 与435不同的为 重叠区间的判定问题
    def isInterval(self, list1, list2):
        if list1[1] < list2[0]:
            return False
        if list2[1] < list1[0]:
            return False
        return True

    def findMinArrowShots(self, intervals):
        sort_intervals = sorted(intervals, key=lambda d: (d[1], d[0]))
        inter_list = []
        for interval in sort_intervals:
            if len(inter_list) == 0:
                inter_list.append(interval)
            if not self.isInterval(inter_list[-1], interval):
                inter_list.append(interval)
        print(sort_intervals)
        print(inter_list)
        print(len(intervals) - len(inter_list))
        return len(inter_list)


solution = Solution()
solution.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]])
