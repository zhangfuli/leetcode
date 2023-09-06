# 输入一颗二叉树的根节点root和一个整数expectNumber，找出二叉树中结点值的和为expectNumber的所有路径。
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
# @param target int整型
# @return int整型二维数组
#
class Solution:
    def __init__(self):
        self.res = []
    def FindPath(self, root, target):
        if root is None:
            return self.res
        self.dfs(root, target, [])
        return self.res

    def dfs(self, root, target, path):
        if root is None:
            return 0

        path.append(root.val)
        if root.val == target and root.left is None and root.right is None:
            self.res.append(path[:])

        self.dfs(root.left, target - root.val, path)
        self.dfs(root.right, target - root.val, path)
        path.pop()
