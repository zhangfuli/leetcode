# 给定一个整数 n，返回 n! 结果尾数中零的数量。
#
# 示例 1:
#
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。

# 找 5 的个数

class Solution:
    def trailingZeroes(self, n: int):
        res = 0
        divide = 5
        while divide <= n:
            res += n // divide
            divide *= 5
        return res