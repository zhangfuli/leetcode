class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def valid(board, r, c, n):
            for i in range(9):
                if board[r][i] == n:
                    return False
                if board[i][c] == n:
                    return False
                if board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == n:
                    return False
            return True

        def backtrack(board, r, c):
            m = n = 9
            if c == n:
                return backtrack(board, r + 1, 0)
            if r == m:
                return True

            for i in range(r, m):
                for j in range(c, n):
                    if board[i][j] != '.':
                        return backtrack(board, i, j + 1)

                    for ch in range(1, 10):
                        ch = str(ch)
                        if not valid(board, i, j, ch):
                            continue
                        board[i][j] = str(ch)
                        if backtrack(board, i, j + 1):
                            return True
                        board[i][j] = '.'
                    return False
            return False

        backtrack(board, 0, 0)
