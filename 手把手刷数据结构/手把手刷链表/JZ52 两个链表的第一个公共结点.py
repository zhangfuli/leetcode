# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            if p1 != None:
                p1 = p1.next
            else:
                p1 = pHead2
            if p2 != None:
                p2 = p2.next
            else:
                p2 = pHead1
        return p1