# 给定一个m x n 二维字符网格board 和一个字符串单词word。
# 如果word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母不允许被重复使用。
#
# 例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。
# 示例 1：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true


class Solution:
    def backtrack(self, board, i, j, k, word):
        if not 0 <= i < len(board) or not 0 <= j < len(board[i]) or board[i][j] != word[k]:
            return False

        if k == len(word) - 1:
            return True

        ## 不能重复使用
        board[i][j] = ''
        res = self.backtrack(board, i + 1, j, k + 1, word) \
              or self.backtrack(board, i - 1, j, k + 1, word) \
              or self.backtrack(board, i, j + 1, k + 1, word) \
              or self.backtrack(board, i, j - 1, k + 1, word)

        board[i][j] = word[k]
        return res

    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.backtrack(board, i, j, 0, word):
                    return True
        return False


solution = Solution()
print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                     "ABCCED"))
