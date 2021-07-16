# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.successor = None
    def reverseListN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head

        last = self.reverseListN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
