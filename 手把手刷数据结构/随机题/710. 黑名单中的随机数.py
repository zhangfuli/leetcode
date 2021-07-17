import random


class Solution:

    def __init__(self, N, blacklist):
        # 共有N个数字，其中黑名单上有len(blacklist)个数字,白名单上有N-len(blacklist)个数字
        self.white_len = N - len(blacklist)
        # 为了随机取得white_len个白名单数字中的一个，使用映射关系处理前white_len个位置中黑名单上的数字
        # 把不在前white_len位置内的白名单中的数字映射至前white_len位置内（利用其内原有的黑名单中的数字的位置）
        # black_lt：在前white_len之内的黑名单中的数字
        # white_gt：在white_len之后的白名单中的数字
        # 使用map将black_lt中的元素一一映射至white_gt
        black_lt = {i for i in blacklist if i < self.white_len}
        white_gt = {j for j in range(self.white_len, N)} - set(blacklist)
        self.map = dict(zip(black_lt, white_gt))

    def pick(self) -> int:
        # 在前white_len个数字中随机选取
        res = random.randint(0, self.white_len - 1)
        # 如res是map的key，说明这个位置是黑名单中的数字，通过映射取出其对应的白名单的数字
        if res in self.map:
            return self.map[res]
        else:  # 如res不是map的key，说明这个位置是白名单中的数字，直接返回
            return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
