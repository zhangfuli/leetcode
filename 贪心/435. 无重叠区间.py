# 正确的思路其实很简单，可以分为以下三步：
#
# 从区间集合 intvs 中选择一个区间 x，这个 x 是在当前所有区间中结束最早的（end 最小）。
# 把所有与 x 区间相交的区间从区间集合 intvs 中删除。
# 重复步骤 1 和 2，直到 intvs 为空为止。之前选出的那些 x 就是最大不相交子集。

class Solution:
    def isInterval(self, list1, list2):
        if list1[1] <= list2[0]:
            return False
        if list2[1] <= list1[0]:
            return False
        return True

    def eraseOverlapIntervals(self, intervals):
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
solution.eraseOverlapIntervals([[1,2],[3,4],[5,6],[7,8]])
