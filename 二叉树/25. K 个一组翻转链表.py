# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def __init__(self):
        self.successor = None

    # [a,b)
    def reverseMN(self, a, b):
        pre, cur, nxt = None, a, a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reverseKGroup(self, head, k):
        if head == None:
            return head
        a = b = head
        for i in range(0, k):
            if b == None:
                return head
            b = b.next
        new_head = self.reverseMN(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head

