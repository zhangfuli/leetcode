# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root_val = preorder[0]

        # 把前序遍历结果的第二个元素作为左子树的根节点的值
        left_root =  preorder[1]

        # 后序遍历结果中寻找左子树根节点的值，从而确定了左子树的索引边界，进而确定右子树的索引边界，递归构造左右子树即可。
        left_root_idx = postorder.index(left_root)

        left_preorder = preorder[1:1+left_root_idx+1]
        right_preorder = preorder[2+left_root_idx:]

        left_postorder = postorder[:left_root_idx+1]
        right_postorder = postorder[left_root_idx+1:len(postorder)-1]

        root = TreeNode(root_val)
        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)
        return root
