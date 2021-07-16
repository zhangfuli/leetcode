class Solution:
    def __init__(self):
        self.hashmap = {}
    def count(self, left, right):
        if left >= right:
            return 1
        res = 0
        for mid in range(left, right):
            if (left, mid) in self.hashmap:
                left_count = self.hashmap[(left, mid)]
            else:
                left_count = self.count(left, mid)
                self.hashmap[(left, mid)] = left_count
            if (mid + 1, right) in self.hashmap:
                right_count = self.hashmap[(mid + 1, right)]
            else:
                right_count = self.count(mid + 1, right)
                self.hashmap[(mid + 1, right)] = right_count

            res += left_count * right_count
        return res
    def numTrees(self, n):
        res = self.count(0, n)
        return res


solution = Solution()
print(solution.numTrees(1))