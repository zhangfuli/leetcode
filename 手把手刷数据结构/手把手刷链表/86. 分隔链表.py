class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int):
        small = ListNode()
        big = ListNode()
        p1, p2 = small, big

        while head != None:
            if head.val < x:
                p1.next = head
                p1 = p1.next
                head = head.next
                p1.next = None
            else:
                p2.next = head
                p2 = p2.next
                head = head.next
                p2.next = None
        p1.next = big.next
        return small.next
