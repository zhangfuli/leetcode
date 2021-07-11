# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.hashmap = {}
    def traverse(self, root):
        if root == None:
            return "#"
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        tree = str(root.val) + ',' + left + ',' + right
        if tree in self.hashmap:
            self.hashmap[tree].append(root)
        else:
            self.hashmap[tree] = []
        return tree

    def findDuplicateSubtrees(self, root):
        self.traverse(root)
        result = []
        for i in self.hashmap:
            if len(self.hashmap[i]) > 0:
                result.append(self.hashmap[i][0])
        print(result)
        return result