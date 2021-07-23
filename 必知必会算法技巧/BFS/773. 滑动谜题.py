# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用0来表示.
# 一次移动定义为选择0与一个相邻的数字（上下左右）进行交换.
# 最终当板board的结果是[[1,2,3],[4,5,0]]谜板被解开。
# 给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
# 示例：
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
import copy
import itertools
from queue import Queue


class Solution:
    def slidingPuzzle(self, board):
        q = Queue()
        q.put(copy.deepcopy(board))
        depth = 0
        hashmap = {}
        hashmap[self.str_board(board)] = 1
        while q.qsize() > 0:
            size = q.qsize()
            for i in range(size):
                cur = q.get()
                if self.str_board(cur) == '123450':
                    return depth

                # 上下左右移动
                up = self.up(copy.deepcopy(cur))
                if self.str_board(up) not in hashmap:
                    hashmap[self.str_board(up)] = 1
                    q.put(copy.deepcopy(up))

                down = self.down(copy.deepcopy(cur))
                if self.str_board(down) not in hashmap:
                    hashmap[self.str_board(down)] = 1
                    q.put(copy.deepcopy(down))

                left = self.left(copy.deepcopy(cur))
                if self.str_board(left) not in hashmap:
                    hashmap[self.str_board(left)] = 1
                    q.put(copy.deepcopy(left))

                right = self.right(copy.deepcopy(cur))
                if self.str_board(right) not in hashmap:
                    hashmap[self.str_board(right)] = 1
                    q.put(copy.deepcopy(right))
            depth += 1
        return -1

    def str_board(self, board):
        res = ''
        for i in range(len(board)):
            for j in range(len(board[i])):
                res += str(board[i][j])
        return res

    def up(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    if i != 0:
                        board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
                        break
        return board

    def down(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    if i != len(board) - 1:
                        board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
                        break
        return board

    def left(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    if j != 0:
                        board[i][j - 1], board[i][j] = board[i][j], board[i][j - 1]
                        break
        return board

    def right(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    if j != len(board[i]) - 1:
                        board[i][j + 1], board[i][j] = board[i][j], board[i][j + 1]
                        break
        return board

    def test(self, board):
        print(list(itertools.chain.from_iterable(board)))


solution = Solution()
print(solution.slidingPuzzle([[1, 2, 3], [5, 4, 0]]))
