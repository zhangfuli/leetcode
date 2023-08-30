class Solution:
    def shipWithinDays(self, weights, days):
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = int(left + (right - left) / 2)
            if self.shipContainer(weights, mid) == days:
                right = mid - 1
            elif self.shipContainer(weights, mid) > days:
                left = mid + 1
            elif self.shipContainer(weights, mid) < days:
                right = mid - 1
        return left

    def shipContainer(self, weights, container):
        day = 0
        free = container
        for i in range(len(weights)):
            if free - weights[i] >= 0:
                free -= weights[i]
            else:
                free = container - weights[i]
                day += 1
        day += 1
        return day


solution = Solution()
print(solution.f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))
