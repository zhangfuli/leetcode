# 让快指针先走 n 步，然后快慢指针开始同速前进。
# 这样当快指针走到链表末尾 null 时，慢指针所在的位置就是倒数第 n 个链表节点（n 不会超过链表长度）。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        if head == None:
            return None

        fast = head
        slow = head
        while n != 0:
            fast = fast.next
            n -= 1

        if fast == None:
            return head.next

        while fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
