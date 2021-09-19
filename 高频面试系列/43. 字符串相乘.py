# 给定两个以字符串形式表示的非负整数num1和num2，返回num1和num2的乘积，
# 它们的乘积也表示为字符串形式。
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
#
# 示例2:
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"


class Solution:
    def multiply(self, num1, num2):
        res = 0
        for i in range(len(num1) - 1, -1, -1):
            tmp = 0
            for j in range(len(num2) - 1, -1, -1):
                tmp += int(num1[i]) * int(num2[j]) * pow(10, len(num1) - 1 - i + len(num2) - 1 -j)
            res += tmp
        return str(res)


solution = Solution()
solution.multiply("1", "2")
