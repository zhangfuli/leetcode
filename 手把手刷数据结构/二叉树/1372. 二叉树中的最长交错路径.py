# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = -1

    def longestZigZag(self, root):
        if root is None:
            return 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return -1, -1

        ll, lr = self.dfs(root.left)
        rl, rr = self.dfs(root.right)
        self.res = max(self.res, 1 + lr, 1 + rl)
        return 1 + lr, 1 + rl
