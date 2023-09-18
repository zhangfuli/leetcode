# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        if root == None:
            return True
        return abs(self.max_depth(root.left) - self.max_depth(root.right)) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def max_depth(self, root):
        if root == None:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1
