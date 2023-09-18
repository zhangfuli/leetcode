class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        res = []
        i, j = 0, 0

        # 起点
        a, b = 0, 0
        row, col = len(matrix) - 1, len(matrix[0]) - 1
        m, n = (row + 1), (col + 1)
        k = 0
        while k < m * n:
            res.append(matrix[i][j])

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
