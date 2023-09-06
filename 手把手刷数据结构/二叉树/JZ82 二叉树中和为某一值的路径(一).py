# 给定一个二叉树root和一个值 sum ，判断是否有从根节点到叶子节点的节点值之和等于 sum 的路径。
# 1.该题路径定义为从树的根结点开始往下一直到叶子结点所经过的结点
# 2.叶子节点是指没有子节点的节点
# 3.路径只能从父节点到子节点，不能从子节点到父节点
# 4.总节点数目为n

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @param sum int整型 
# @return bool布尔型
#
class Solution:
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        return self.traverse(root, sum)

    def traverse(self, root, sum):
        if root is None:
            return False
        if sum - root.val == 0 and root.left is None and root.right is None:
            return True

        return self.traverse(root.left, sum - root.val) or self.traverse(root.right, sum - root.val)
# write code here
