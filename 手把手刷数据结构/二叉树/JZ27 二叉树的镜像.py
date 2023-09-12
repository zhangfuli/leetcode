# class TreeNode:

# from numpy import left_shift
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot TreeNode类 
# @return TreeNode类
#
class Solution:
    def Mirror(self , pRoot: TreeNode):
        if pRoot == None:
            return None
        self.traverse(pRoot)
        return pRoot
    
    def traverse(self, pRoot):
        if pRoot == None:
            return pRoot
        tmp = pRoot.left
        pRoot.left = pRoot.right
        pRoot.right = tmp

        self.traverse(pRoot.left)
        self.traverse(pRoot.right)
