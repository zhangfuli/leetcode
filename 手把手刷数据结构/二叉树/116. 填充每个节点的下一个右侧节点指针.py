"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root):
        if root is None or root.left is None or root.right is None:
            return root

        self.traverse(root.left, root.right)
        return root

    def traverse(self, node1, node2):
        if node1 is None or node2 is None:
            return None

        node1.next = node2
        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        self.traverse(node1.right, node2.left)
