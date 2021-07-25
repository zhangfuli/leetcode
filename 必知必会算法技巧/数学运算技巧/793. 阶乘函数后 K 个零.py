# f(x)是x!末尾是 0 的数量。（回想一下x! = 1 * 2 * 3 * ... * x，且 0! = 1 ）
#
# 例如，f(3) = 0，因为 3! = 6 的末尾没有 0 ；
# 而 f(11) = 2，因为 11!= 39916800 末端有 2 个 0 。
# 给定K，找出多少个非负整数 x，能满足 f(x) = K 。
#
# 示例 1：
#
# 输入：K = 0
# 输出：5
# 解释：0!, 1!, 2!, 3!, and 4!均符合 K = 0 的条件

class Solution:
    def f(self, n):
        res = 0
        divide = 5
        while divide <= n:
            res += n // divide
            divide *= 5
        return res

    def left_bound(self, k):
        left, right = 0, int(10e9)
        # 寻找做左边界
        while left <= right:
            mid = int(left + (right - left) / 2)
            if self.f(mid) == k:
                right = mid - 1
            elif self.f(mid) < k:
                left = mid + 1
            elif self.f(mid) > k:
                right = mid - 1

        if left > int(10e9) or self.f(left) != k:
            return -1
        return left

    def right_bound(self, k):
        left, right = 0, int(10e9)
        # 寻找做右边界
        while left <= right:
            mid = int(left + (right - left) / 2)
            if self.f(mid) == k:
                left = mid + 1
            elif self.f(mid) < k:
                left = mid + 1
            elif self.f(mid) > k:
                right = mid - 1


        if right < 0 or self.f(right) != k:
            return -1
        return right

    def preimageSizeFZF(self, k):
        left = self.left_bound(k)
        right = self.right_bound(k)
        print(left)
        print(right)
        if left == -1 or right == -1:
            return 0
        return right - left + 1


solution = Solution()
print(solution.preimageSizeFZF(1000000000))
