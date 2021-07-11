#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 得到分解自然数之和的最小值
# @param n int整型 自然数n
# @return int整型
#
class Solution:
    def getSu(self, n):
        res = []
        for i in range(1, n + 1):
            if n % i == 0:
                res.append(i)
        return res

    def getMinSum(self, n):
        if n == 0 or n == 1:
            return n
        res = self.getSu(n)
        min_sum = 0
        while len(res) > 2:
            min_sum += res[1]
            n = n // res[1]
            res = self.getSu(n)
        min_sum += res[1]
        return min_sum


