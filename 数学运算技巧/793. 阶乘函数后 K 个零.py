class Solution:
    def trailingZeroes(self, n):
        res = 0
        div = 5
        while div <= n:
            res += n // div
            div *= 5
        return res

    def find_left(self, K, left, right):
        original_right = right
        original_left = left
        while left <= right:
            mid = int(left + (right - left) / 2)
            if self.trailingZeroes(mid) == K:
                right = mid - 1
            elif self.trailingZeroes(mid) < K:
                left = mid + 1
            elif self.trailingZeroes(mid) > K:
                right = mid - 1
        if left >= original_right or self.trailingZeroes(left) != K:
            return -1
        return left

    def find_right(self, K, left, right):
        original_right = right
        original_left = left
        while left <= right:
            mid = int(left + (right - left) / 2)
            if self.trailingZeroes(mid) == K:
                left = mid + 1
            elif self.trailingZeroes(mid) < K:
                left = mid + 1
            elif self.trailingZeroes(mid) > K:
                right = mid - 1
        if right <= 0 and self.trailingZeroes(right) != K:
            return -1
        return right

    def preimageSizeFZF(self, K):
        left_bound = self.find_left(K, 0, int(10e9 + 1))
        right_bound = self.find_right(K, 0, int(10e9 + 1))
        print(left_bound)
        print(right_bound)
        if left_bound == -1 or right_bound == -1:
            return 0
        return right_bound - left_bound + 1


