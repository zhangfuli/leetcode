# 电子游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。
# 给定一个字符串ring，表示刻在外环上的编码；给定另一个字符串key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。
# 最初，ring的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使key的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完key中的所有字符。
# 旋转ring拼出 key 字符key[i]的阶段中：
# 您可以将ring顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串ring的一个字符与 12:00 方向对齐，并且这个字符必须等于字符key[i] 。
# 如果字符key[i]已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作1 步。按完之后，您可以开始拼写key的下一个字符（下一阶段）, 直至完成所有拼写。
#
# 输入: ring = "godding", key = "gd"
# 输出: 4
# 解释:
# 对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。
# 对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
# 当然, 我们还需要1步进行拼写。
# 因此最终的输出是 4
import re


class Solution:
    def __init__(self):
        self.hashmap = {}

    def backtrack(self, ring, ring_idx, key, key_idx):
        if key_idx == len(key):
            return 0
        if (ring_idx, key_idx) in self.hashmap:
            return self.hashmap[(ring_idx, key_idx)]

        index_list = [i.start() for i in re.finditer(key[key_idx], ring)]

        res = float('INF')
        for i in index_list:
            delta = abs(ring_idx - i)
            # 顺时针还是逆时针
            delta = min(delta, len(ring) - delta)
            next_step = self.backtrack(ring, i, key, key_idx + 1)
            res = min(res, 1 + delta + next_step)
        self.hashmap[(ring_idx, key_idx)] = res
        return res

    def findRotateSteps(self, ring, key):
        return self.backtrack(ring, 0, key, 0)


solution = Solution()
print(solution.findRotateSteps("godding", "godding"))
