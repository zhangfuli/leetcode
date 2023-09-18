# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right == None:
            return False
        return self.traverse(root.left, root.right)

    def traverse(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        if node1 == None or node2 == None:
            return False

        if node1.val == node2.val:
            return self.traverse(node1.left, node2.right) and self.traverse(node1.right, node2.left)
        else:
            return False