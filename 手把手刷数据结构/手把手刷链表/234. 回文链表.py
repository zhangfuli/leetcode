# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def isPalindrome(self, head):
    #     nums = []
    #     while head != None:
    #         nums.append(head.val)
    #         head = head.next
    #     right = len(nums)
    #     for left in range(0, len(nums)):
    #         if nums[left] == nums[right - 1]:
    #             right -= 1
    #         else:
    #             return False
    #     return True

    def __init__(self):
            self.left = None

    def isPalindrome(self, head) -> bool:
        self.left = head
        return self.traverse(head)

    def traverse(self, right) -> bool:
        if right is None:
            return True
        res = self.traverse(right.next)
        # 后序遍历代码
        res = (res and (right.val == self.left.val))
        self.left = self.left.next
        return res