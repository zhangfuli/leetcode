# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        result = ListNode()
        p = result
        heap = []
        for lst in lists:
            if lst is not None:
                heap.append([lst.val, lst])
        while len(heap) != 0:
            heap = sorted(heap, key=lambda d:(d[0]))
            [val, lst] = heap.pop(0)
            p.next = ListNode(val)
            p = p.next
            lst = lst.next
            if lst != None:
                heap.append([lst.val, lst])
        return result.next

if __name__ == '__main__':
    p1 = ListNode(1, ListNode(4, ListNode(5)))
    p2 = ListNode(1, ListNode(3, ListNode(4)))
    p3 = ListNode(2, ListNode(6))
    a = [[3,3,3],[4,4]]
    for i in a:
        print(i)
    solution = Solution()
    result = solution.mergeKLists([p1, p2, p3])
    while result != None:
        print(result.val)
        result = result.next

# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#     1->4->5,
#           1->3->4,
#                 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6