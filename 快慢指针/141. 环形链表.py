# 快慢指针

class Solution:

    # 判断链表中是否有环
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

