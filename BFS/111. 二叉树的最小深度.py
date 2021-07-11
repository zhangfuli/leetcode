# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue


class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        q = Queue()
        q.put(root)
        depth = 1
        while q.qsize() > 0:
            size = q.qsize()
            for i in range(size):
                cur = q.get()
                if cur.left == None and cur.right == None:
                    return depth
                if cur.left != None:
                    q.put(cur.left)
                if cur.right != None:
                    q.put(cur.right)
            depth += 1

        return None
