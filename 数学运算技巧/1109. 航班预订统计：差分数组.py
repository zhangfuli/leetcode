class Solution:
    def corpFlightBookings(self, bookings, n):
        diff = [0] * n
        for t in range(len(bookings)):
            i, j, temp = bookings[t]
            diff[i - 1] += temp
            if j < n:  # 越界情况特殊判断
                diff[j] -= temp
        print(diff)
        res = [diff[0]]
        for i in range(1, len(diff)):
            res.append(diff[i] + res[-1])
        return res


solution = Solution()
solution.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5)
