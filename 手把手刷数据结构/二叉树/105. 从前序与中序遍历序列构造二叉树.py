# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        val = preorder[0]
        val_index = inorder.index(val)

        node = TreeNode(val)

        left_nums_inorder = inorder[:val_index]
        right_nums_inorder = inorder[val_index + 1:]

        left_nums_preorder = preorder[1: len(left_nums_inorder) + 1]
        right_nums_preorder = preorder[len(left_nums_preorder) + 1:]

        node.left = self.buildTree(left_nums_preorder, left_nums_inorder)
        node.right = self.buildTree(right_nums_preorder, right_nums_inorder)
        return node