# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
# 这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
# 一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
# 输入: [3,2,3,null,3,null,1]
#
# 3
# / \
# 2  3
#  \  \
#   3  1
#
# 输出: 7
# 解释:小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.hashmap = {}

    def rob(self, root):
        if root == None:
            return 0

        if root in self.hashmap:
            return self.hashmap[root]

        do_it = root.val + (
            0 if root.left == None else self.rob(root.left.left) + self.rob(root.left.right)
        ) + (
            0 if root.right == None else self.rob(root.right.left) + self.rob(root.right.right)
        )

        undo_it = self.rob(root.left) + self.rob(root.right)
        result = max(do_it, undo_it)
        self.hashmap[root] = result
        return result
