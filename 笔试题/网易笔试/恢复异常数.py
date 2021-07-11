#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 函数：求出异常数的位置和原来的值
# @param fuzzyArray int整型一维数组 含有异常数的数组
# @return int整型一维数组
#
class Solution:
    def fuzzyNumber(self, fuzzyArray):
        if fuzzyArray.count(-1) > 1:
            return [-1, -1]

        a = 0
        b = 0
        index = 0
        for i in range(1, len(fuzzyArray) + 1):
            a ^= i
            if fuzzyArray[i - 1] != -1:
                b ^= fuzzyArray[i - 1]
            else:
                index = i - 1
        # print(a ^ b)
        # print(index)
        return [index, a ^ b]


solution = Solution()
print(solution.fuzzyNumber([1, 5, 3, -1, 2]))
