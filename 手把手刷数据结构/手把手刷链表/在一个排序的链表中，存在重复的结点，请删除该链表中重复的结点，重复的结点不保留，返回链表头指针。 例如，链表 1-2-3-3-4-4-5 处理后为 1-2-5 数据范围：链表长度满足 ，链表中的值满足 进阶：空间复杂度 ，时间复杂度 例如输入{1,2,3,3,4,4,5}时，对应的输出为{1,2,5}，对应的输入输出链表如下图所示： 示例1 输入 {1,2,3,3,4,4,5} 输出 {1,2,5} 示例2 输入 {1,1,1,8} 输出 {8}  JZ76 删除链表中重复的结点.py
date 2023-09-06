# 题目的主要信息：
# 在一个非降序的链表中，存在重复的节点，删除该链表中重复的节点
# 重复的节点一个元素也不保留

class Solution:
    def deleteDuplication(self , pHead: ListNode) -> ListNode:
        #空链表
        if pHead == None:
            return None
        res = ListNode(0)
        #在链表前加一个表头
        res.next = pHead
        cur = res
        while cur.next and cur.next.next:
            #遇到相邻两个节点值相同
            if cur.next.val == cur.next.next.val:
                temp = cur.next.val
                #将所有相同的都跳过
                while cur.next != None and cur.next.val == temp:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        #返回时去掉表头
        return res.next
