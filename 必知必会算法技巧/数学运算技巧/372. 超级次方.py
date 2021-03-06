# 你的任务是计算a^b对1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
#
# 示例 1：
# 输入：a = 2, b = [3]
# 输出：8
#
# 示例 2：
# 输入：a = 2, b = [1,0]
# 输出：1024

class Solution:
    def superPow(self, a, b):
        c = [str(b[i]) for i in range(len(b))]
        return pow(a, int(''.join(c)), 1337)


solution = Solution()
solution.superPow(2, [3])
