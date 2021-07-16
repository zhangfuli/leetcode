class Solution:
    def f(self, weights, x):
        day = 0
        surplus = x

        i = 0
        while i < len(weights):
            if surplus >= weights[i]:
                surplus -= weights[i]
            else:
                day += 1
                surplus = x
                i -= 1
            i += 1
        if surplus < x:
            day += 1

        return day

    def shipWithinDays(self, weights, days):
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = int(left + (right - left) / 2)
            if self.f(weights, mid) == days:
                right = mid - 1
            elif self.f(weights, mid) > days:
                left = mid + 1
            elif self.f(weights, mid) < days:
                right = mid - 1
        return left


solution = Solution()
print(solution.f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))
