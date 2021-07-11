# Definition for singly-linked list.
# 双指针
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        a_list = []
        while head != None:
            a_list.append(head.val)
            head = head.next
        print(a_list)
        right = len(a_list) - 1
        for left in range(0, len(a_list)):
            if a_list[left] != a_list[right]:
                return False
            right -= 1
        return True


head = None
for i in range(7, 0, -1):
    tmp = ListNode(i, head)
    head = tmp

a = Solution()
a.isPalindrome(head)
