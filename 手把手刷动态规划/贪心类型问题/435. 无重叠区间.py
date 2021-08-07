# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
# 注意:
# 可以认为区间的终点总是大于它的起点。
# 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
#
# 示例 1:
#
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。

class Solution:
    def isInterval(self, list1, list2):
        if list1[1] <= list2[0]:
            return False
        if list2[1] <= list1[0]:
            return False
        return True

    def eraseOverlapIntervals(self, intervals):
        # 选择最早结束的时间
        sorted_intervals = sorted(intervals, key=lambda d: (d[1], d[0]))

        un_intervals = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            if not self.isInterval(un_intervals[-1], sorted_intervals[i]):
                un_intervals.append(sorted_intervals[i])
        print(un_intervals)
        return len(sorted_intervals) - len(un_intervals)


solution = Solution()
solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
