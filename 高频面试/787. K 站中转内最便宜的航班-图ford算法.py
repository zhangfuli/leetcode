# 有 n 个城市通过一些航班连接。给你一个数组flights ，
# 其中flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 toi 抵达 pricei。
#
# 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。
# 如果不存在这样的路线，则输出 -1。

# 输入:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# 输出: 200

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        dist = [float('inf')] * n  # dist[v]表示到达v的最小花费
        dist[src] = 0

        for i in range(k + 1):  # 对每条边做 k+1 次松弛操作
            dist_old = [_ for _ in dist]
            for u, v, w in flights:
                dist[v] = min(dist[v], dist_old[u] + w)

        if dist[dst] != float('inf'):
            return dist[dst]
        else:
            return -1
