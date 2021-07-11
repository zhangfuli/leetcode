#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 函数：求出异常数的位置和原来的值
# @param fuzzyArray int整型一维数组 含有异常数的数组
# @return int整型一维数组
#
class Solution:
    def fuzzyNumber(self, fuzzyArray):
        res = [-1 for i in range(len(fuzzyArray) + 1)]
        for i in range(len(fuzzyArray)):
            if fuzzyArray[i] != -1:
                res[fuzzyArray[i]] = fuzzyArray[i]
        if res.count(-1) > 3:
            return [-1, -1]
        else:
            return [res.index(-1, 1, len(res)), fuzzyArray.index(-1)]


solution = Solution()
print(solution.fuzzyNumber([2, -1, 3]))
