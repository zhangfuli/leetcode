class UF:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, x):
        while x != self.parent[x]:
            # 进行路径压缩
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return None
        if self.size[p] > self.size[q]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.count -= 1

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return True
        else:
            return False

    def count(self):
        return self.count


class Solution:
    def solve(self, board):
        m = len(board)
        n = len(board[0])
        uf = UF(m * n + 1)
        dummy = m * n

        # 外层
        for i in range(m):
            if board[i][0] == 'O':
                uf.union(n * i, dummy)
            if board[i][n - 1] == 'O':
                uf.union(n * i + n - 1, dummy)

        for j in range(n):
            if board[0][j] == 'O':
                uf.union(n * 0 + j, dummy)
            if board[m - 1][j] == 'O':
                uf.union((m - 1) * n + j, dummy)

        # 内层
        d = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O':
                    for k in range(len(d)):
                        if board[i + d[k][0]][j + d[k][1]] == 'O':
                            uf.union(n * (i + d[k][0]) + (j + d[k][1]), n * i + j)
        for i in range(m):
            for j in range(n):
                if not uf.connected(n * i + j, dummy):
                    board[i][j] = 'X'
