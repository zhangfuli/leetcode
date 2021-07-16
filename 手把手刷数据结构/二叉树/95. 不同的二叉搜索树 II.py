# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTree(self, left, right):
        res = []
        if left > right:
            return [None]

        for mid in range(left, right + 1):
            root_lefts = self.generateTree(left, mid - 1)
            root_rights = self.generateTree(mid + 1, right)
            for root_left in root_lefts:
                for root_right in root_rights:
                    root = TreeNode(mid)
                    root.left = root_left
                    root.right = root_right
                    print(root)
                    res.append(root)
        return res

    def generateTrees(self, n):
        return self.generateTree(1, n)

solution = Solution()
solution.generateTrees(3)
