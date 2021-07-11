# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        root = TreeNode()
        root.val = postorder[-1]
        root_index_inorder = inorder.index(root.val)

        left_inorder = inorder[:root_index_inorder]
        right_inorder = inorder[root_index_inorder + 1:]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_postorder):len(postorder) - 1]


        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root