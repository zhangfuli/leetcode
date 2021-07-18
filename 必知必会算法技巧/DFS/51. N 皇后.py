import copy


class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n):
        res = []
        board = [['.'] * n for i in range(n)]
        self.backtrack(board, 0)
        for i in self.res:
            b = []
            for j in i:
                b.append(''.join(j))
            res.append(b)
        print(res)
        return res

    def backtrack(self, board, row):
        if row == len(board):
            self.res.append(copy.deepcopy(board))
            return None

        for col in range(len(board[row])):
            if not self.is_valid(board, row, col):
                continue

            board[row][col] = 'Q'
            self.backtrack(board, row + 1)
            board[row][col] = '.'

    def is_valid(self, board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # 右斜
        right_row = row
        right_col = col
        while right_row > 0 and right_col > 0:
            right_row -= 1
            right_col -= 1
        while right_row < len(board) - 1 and right_col < len(board) - 1:
            if board[right_row][right_col] == 'Q':
                return False
            right_row += 1
            right_col += 1

        # print(right_row)
        # print(right_col)

        # 左斜
        left_row = row
        left_col = col
        while left_row > 0 and left_col < len(board) - 1:
            left_row -= 1
            left_col += 1
        while left_row < len(board) - 1 and left_col > 0:
            if board[left_row][left_col] == 'Q':
                return False
            left_row += 1
            left_col -= 1
        return True


solution = Solution()
solution.solveNQueens(4)
# board = [[0 for j in range(5)] for i in range(5)]
# solution.is_valid(board, 3, 4)
