# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse_list(self, head):
        if head.next == None:
            return head
        last = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return last

    def nextLargerNodes(self, head):
        head = self.reverse_list(head)
        stack = []
        res = []
        while head != None:
            print(head.val)
            while len(stack) != 0 and stack[-1] <= head.val:
                stack.pop(-1)
            if len(stack) == 0:
                res.insert(0, 0)
            else:
                res.insert(0, stack[-1])
            stack.append(head.val)
            head = head.next
        print(res)
        return res
