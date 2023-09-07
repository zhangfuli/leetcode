# m * n 的二维数组 顺时针打印
class Solution:
    def printList(self, m, n):
        if m == 0 or n == 0:
            return []

        num = [[i + j for j in range(n)] for i in range(m)]
        print(num)
        res = []
        i, j = 0, 0

        # 起点
        a, b = 0, 0
        row, col = len(num) - 1, len(num[0]) - 1
        k = 0
        while k < m * n:
            res.append(num[i][j])

            # 往右走
            if i == a and j < col:
                j += 1
            # 往下走
            elif i < row and j == col:
                i += 1
            # 往左走
            elif i == row and j > b:
                j -= 1
            # 往上走
            elif i > a and j == b:
                i -= 1

                if i - 1 == a:
                    a += 1
                    b += 1
                    row -= 1
                    col -= 1
            k += 1
        return res
# 0 1 2 3
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7


if __name__ == '__main__':
    solution = Solution()
    print(solution.printList(5, 4))