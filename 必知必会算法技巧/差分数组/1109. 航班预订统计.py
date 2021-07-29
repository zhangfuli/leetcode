# 这里有n个航班，它们分别从 1 到 n 进行编号。
# 有一份航班预订表bookings ，表中第i条预订记录bookings[i] = [firsti, lasti, seatsi]
# 意味着在从 firsti到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi个座位。
# 请你返回一个长度为 n 的数组answer，其中 answer[i] 是航班 i 上预订的座位总数。
#
# 示例 1：
#
# 输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# 输出：[10,55,45,25,25]
# 解释：
# 航班编号        1   2   3   4   5
# 预订记录 1 ：   10  10
# 预订记录 2 ：       20  20
# 预订记录 3 ：       25  25  25  25
# 总座位数：      10  55  45  25  25
# 因此，answer = [10,55,45,25,25]

# 这样构造差分数组 diff，就可以快速进行区间增减的操作
# 如果你想对区间 nums[i..j] 的元素全部加 3，
# 那么只需要让 diff[i] += 3，然后再让 diff[j+1] -= 3 即可
class Solution:
    def corpFlightBookings(self, bookings, n):
        diff = [0 for i in range(n)]
        for i in range(len(bookings)):
            diff[bookings[i][0] - 1] += bookings[i][2]
            if bookings[i][1] < n:
                diff[bookings[i][1]] -= bookings[i][2]
        print(diff)
        res = [diff[0]]
        for i in range(1, len(diff)):
            res.append(diff[i] + res[-1])
        return res


solution = Solution()
print(solution.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))
