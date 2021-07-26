# 统计所有小于非负整数 n 的质数的数量。
#
# 示例 1：
#
# 输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
class Solution:
    def countPrimes(self, n):
        if n == 0 or n == 1 or n == 2:
            return 0
        is_prim = [True for i in range(n)]
        for i in range(2, n):
            if is_prim:
                j = i * i
                while j < n:
                    is_prim[j] = False
                    j += i
        return is_prim.count(True) - 2
