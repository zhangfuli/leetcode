n, m = list(map(int, input().strip().split()))
nums = list(map(int, input().strip().split()))
tree = []
for i in range(n + 1):
    tree.append([0 for j in range(n + 1)])
for i in range(m):
    left, right = list(map(int, input().strip().split()))
    tree[left][right] = 1
    tree[right][left] = 1


class Solution:
    def __init__(self):
        self.res = []

    def near(self, tree, track, n):
        for i in range(len(track)):
            if tree[track[i]][n] == 1:
                return True
        return False

    def find_sub_tree(self, tree, n):
        self.backtrack(tree, [], n)
        return self.res

    def backtrack(self, tree, track, n):
        self.res.append(track[:])
        for i in range(1, n + 1):
            if i in track:
                continue

            # 如果i 节点的相邻节点在则continue
            if self.near(tree, track, i):
                continue

            track.append(i)
            self.backtrack(tree, track, n)
            track.pop()

solution = Solution()
res = solution.find_sub_tree(tree, n)
res2 = []
max_value = -1
a = -1
for i in res:
    value = 0
    for j in i:
        value += nums[j - 1]
    if value > max_value:
        max_value = value
        res2.append(i)

print(str(max_value) + " " + str(a))

