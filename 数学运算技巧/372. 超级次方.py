class Solution:
    def getPow(self, a, b):
        if len(b) != 0:
            return ((a ** b[-1]) * self.getPow(a, b[:-1]) ** 10) % 1337
        else:
            return 1

    def superPow(self, a, b):
        return self.getPow(a, b) % 1337


solution = Solution()
print(solution.getPow(2147483647, [2, 0, 0]))
