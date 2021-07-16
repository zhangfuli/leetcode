# 假设从头结点到环形入口节点 的节点数为x。
# 环形入口节点到 fast指针与slow指针相遇节点 节点数为y。
# 从相遇节点 再到环形入口节点节点数为 z。

# slow指针走过的节点数为: x + y
# fast指针走过的节点数： x + y + n (y + z)，n为fast指针在环内走了n圈才遇到slow指针， （y+z）为 一圈内节点的个数
# 因为fast指针是一步走两个节点，slow指针一步走一个节点， 所以 fast指针走过的节点数 = slow指针走过的节点数 * 2
# (x + y) * 2 = x + y + n (y + z)

# 两边消掉一个（x+y）: x + y = n (y + z)
# 因为我们要找环形的入口，那么要求的是x，因为x表示 头结点到 环形入口节点的的距离。
# 所以我们要求x ，将x单独放在左面：x = n (y + z) - y
# 在从n(y+z)中提出一个 （y+z）来，整理公式之后为如下公式：x = (n - 1) (y + z) + z 注意这里n一定是大于等于1的，因为 fast指针至少要多走一圈才能相遇slow指针

# 先拿n为1的情况来举例，意味着fast指针在环形里转了一圈之后，就遇到了 slow指针了。
# 当 n为1的时候，公式就化解为 x = z


class Solution:
    def detectCycle(self, head):
        hascycle = False
        if head == None:
            return None
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                hascycle = True
                break
        if hascycle:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
        else:
            return None
