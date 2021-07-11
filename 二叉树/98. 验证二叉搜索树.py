# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        return self.validBST(root, None, None)

    def validBST(self, root, min_node, max_node):
        if root == None:
            return True
        if min_node != None and min_node.val >= root.val:
            return False
        if max_node != None and max_node.val <= root.val:
            return False
        return self.validBST(root.left, min_node, root) and self.validBST(root.right, root, max_node)
