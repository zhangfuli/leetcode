class Solution:
    def hammingWeight(self, n):
        res = 0
        # print(str(n))
        # n = int(str(n), 2)
        # print(n)
        # bin(n)
        while n != 0:
            n = n & (n - 1)
            res += 1
        print(res)
        return res