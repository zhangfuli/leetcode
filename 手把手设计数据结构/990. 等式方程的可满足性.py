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
    def equationsPossible(self, equations):
        uf = UF(26)
        for i in range(len(equations)):
            if equations[i][1] == '=':
                uf.union(ord(equations[i][0]) - ord('a'), ord(equations[i][3]) - ord('a'))
        for i in range(len(equations)):
            if equations[i][1] != '=':
                if uf.connected(ord(equations[i][0]) - ord('a'), ord(equations[i][3]) - ord('a')):
                    return False
        return True
