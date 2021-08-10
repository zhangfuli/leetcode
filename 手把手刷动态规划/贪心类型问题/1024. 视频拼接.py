# 你将会获得一系列视频片段，这些片段来自于一项持续时长为T秒的体育赛事。这些片段可能有所重叠，也可能长度不一。
# 视频片段clips[i]都用区间进行表示：开始于clips[i][0]并于clips[i][1]结束。我们甚至可以对这些片段自由地再剪辑，
# 例如片段[0, 7]可以剪切成[0, 1] +[1, 3] + [3, 7]三部分。
# 我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。
# 返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。
# 示例 1：
#
# 输入：clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
# 输出：3
# 解释：
# 我们选中 [0,2], [8,10], [1,9] 这三个片段。
# 然后，按下面的方案重制比赛片段：
# 将 [1,9] 再剪辑为 [1,2] + [2,8] + [8,9] 。
# 现在我们手上有 [0,2] + [2,8] + [8,10]，而这些涵盖了整场比赛 [0, 10]

# 比较所有起点小于 clips[0][1] 的区间，根据贪心策略，它们中终点最大的那个区间就是第二个会被选中的视频

class Solution:
    def videoStitching(self, clips, time):
        sorted_clips = sorted(clips, key=lambda d: (d[0], -d[1]))
        print(sorted_clips)
        next_start, next_end = sorted_clips[0]
        if next_start != 0:
            return -1

        res = 1
        while next_end < time:
            start = next_start
            end = next_end
            res += 1
            if res > time:
                return -1
            for i in range(len(sorted_clips)):
                next = [j for j in range(start, end + 1)]
                if clips[i][0] in next:
                    if clips[i][1] > next_end:
                        next_start, next_end = clips[i]
            print(next_start, next_end)
        print(res)
        return res


solution = Solution()
solution.videoStitching(
    [[8, 10], [17, 39], [18, 19], [8, 16], [13, 35], [33, 39], [11, 19], [18, 35]],
    20
)
