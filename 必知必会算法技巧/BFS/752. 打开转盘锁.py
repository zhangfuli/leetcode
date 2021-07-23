# 你有一个带有四个圆形拨轮的转盘锁。
# 每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
# 每个拨轮可以自由旋转：例如把 '9' 变为'0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
# 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
from queue import Queue


class Solution:
    def openLock(self, deadends, target):
        q = Queue()
        q.put('0000')
        depth = 0
        hashmap = {}
        while q.qsize() > 0:
            size = q.qsize()
            for i in range(size):
                cur = q.get()
                hashmap[cur] = 1
                if cur == target:
                    return depth
                if cur in deadends:
                    continue
                for j in range(4):
                    # 4个钮，分别上下
                    s1 = self.up(cur, j)
                    if s1 not in hashmap:
                        hashmap[s1] = 1
                        q.put(s1)
                    s2 = self.down(cur, j)
                    if s2 not in hashmap:
                        hashmap[s2] = 1
                        q.put(s2)

            depth += 1
        return -1

    def up(self, s, i):
        s_list = list(s)
        if s_list[i] == '9':
            s_list[i] = '0'
        else:
            s_list[i] = str(int(s[i]) + 1)
        return ''.join(s_list)

    def down(self, s, i):
        s_list = list(s)
        if s_list[i] == '0':
            s_list[i] = '9'
        else:
            s_list[i] = str(int(s[i]) - 1)
        return ''.join(s_list)


solution = Solution()
print(solution.openLock(["0000"], "0009"))
