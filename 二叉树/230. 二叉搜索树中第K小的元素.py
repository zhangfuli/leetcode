# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder = []
    def inOrder(self, root):
        if root == None:
            return None
        self.inOrder(root.left)
        self.inorder.append(root.val)
        self.inOrder(root.rught)
    def kthSmallest(self, root, k):
        self.inOrder(root)
        return self.inorder[k - 1]
        