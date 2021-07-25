# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
#
# 如果存在一个整数 x 使得n == 2x ，则认为 n 是 2 的幂次方。
#
# 示例 1：
#
# 输入：n = 1
# 输出：true
# 解释：20 = 1

class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        return n & (n - 1) == 0
