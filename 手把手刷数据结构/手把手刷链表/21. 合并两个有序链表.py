class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        result = ListNode()
        p = result
        while list1 != None and list2 != None:
            q = ListNode()
            if list1.val <= list2.val:
                q.val = list1.val
                list1 = list1.next
                p.next = q
            else:
                q.val = list2.val
                list2 = list2.next
                p.next = q
            p = p.next
        if list1 is None:
            p.next = list2
        if list2 is None:
            p.next = list1
        return result.next
