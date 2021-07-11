# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.hashmap = {}

    def rob(self, root):
        if root == None:
            return 0

        if root in self.hashmap:
            return self.hashmap[root]

        do_it = root.val + (
            0 if root.left == None else self.rob(root.left.left) + self.rob(root.left.right)
        ) + (
                    0 if root.right == None else self.rob(root.right.left) + self.rob(root.right.right)
                )

        undo_it = self.rob(root.left) + self.rob(root.right)
        self.hashmap[root] = max(do_it, undo_it)
        return self.hashmap[root]

# solution = Solution()
# solution.rob()
