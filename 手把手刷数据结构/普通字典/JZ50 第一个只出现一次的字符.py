#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return int整型
#
class Solution:
    def FirstNotRepeatingChar(self, str):
        dic = {}
        for i in range(len(str)):
            if str[i] in dic:
                dic[str[i]] += 1
            else:
                dic[str[i]] = 1

        for i in range(len(str)):
            if dic[str[i]] == 1:
                return i

        return -1

        # write code here
