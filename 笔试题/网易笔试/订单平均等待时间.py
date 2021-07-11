#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param orders int整型二维数组
# @return double浮点型
#
class Solution:
    def averageWaitingTime(self, orders):
        prevend = 0
        wait = 0
        waitsum = 0
        for i in range(len((orders))):
            if orders[i][0] > prevend:
                wait = orders[i][1]
                prevend = orders[i][0] + orders[i][1]
            else:
                wait = orders[i][1] + prevend - orders[i][0]
                prevend = prevend + orders[i][1]
            waitsum += wait
        return waitsum / len(orders)


solution = Solution()
print(solution.averageWaitingTime([[1, 2], [1, 3], [4, 3]]))
