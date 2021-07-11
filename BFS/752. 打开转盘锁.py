import queue


class Solution:
    def openLock(self, deadends, target):
        hashmap = {}
        s = '0000'
        q = queue.Queue()
        depth = 0
        q.put(s)
        hashmap[s] = 1
        while q.qsize() > 0:
            size = q.qsize()
            for i in range(size):
                _s = q.get()
                # print(_s)
                if _s == target:
                    return depth
                if _s in deadends:
                    continue
                for j in range(4):
                    n1 = self.up(_s, j)
                    # print("n1:" + n1)
                    n2 = self.down(_s, j)
                    # print("n2:" + n2)
                    if n1 not in hashmap:
                        q.put(n1)
                        hashmap[n1] = 1
                    if n2 not in hashmap:
                        q.put(n2)
                        hashmap[n2] = 1
                # if _s in hashmap:
                #     continue
            depth += 1
            # if depth > 20:
            #     return -1
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
print(solution.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"],
                        "8888"))
# print(solution.openLock(["8888"],
#                         "0009"))
