# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next
        right = len(nums)
        for left in range(0, len(nums)):
            if nums[left] == nums[right - 1]:
                right -= 1
            else:
                return False
        return True