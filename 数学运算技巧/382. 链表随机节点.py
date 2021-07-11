# Definition for singly-linked list.
import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        """
        cnt = 0
        cur = self.head
        reserve = 0
        while cur != None:
            cnt += 1
            rdm = random.randint(1, cnt)
            if rdm == cnt:
                reserve = cur.val
            cur = cur.next
        return reserve

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
