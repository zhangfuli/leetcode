# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return None
        left = head
        right = head
        while right != None:
            if left.val == right.val:
                right = right.next
            else:
                left.next = right
                left = right
                right = right.next
        left.next = None
        return head