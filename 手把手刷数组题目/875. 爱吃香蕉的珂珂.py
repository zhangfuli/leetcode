class Solution:
    # 递减函数
    def f(self, piles, x):
        hour = 0
        for i in range(len(piles)):
            if piles[i] % x == 0:
                hour += piles[i] // x
            else:
                hour += piles[i] // x + 1
        return hour

    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        while left <= right:
            mid = int(left + (right - left) / 2)
            if self.f(piles, mid) <= h:
                right = mid - 1
            elif self.f(piles, mid) > h:
                left = mid + 1
        return left



