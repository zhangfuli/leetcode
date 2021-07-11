# # 当前状态为 (K 个鸡蛋，N 层楼)
# # 返回这个状态下的最优结果
# def dp(K, N):
#     int res
#     for 1 <= i <= N:
#         res = min(res, 这次在第 i 层楼扔鸡蛋)
#     return res

class Solution:
    # 鸡蛋没碎还可以继续用
    def superEggDrop1(self, K, N):  # 超时
        hashmap = {}

        # 当前状态为 K 个鸡蛋，面对 N 层楼
        # 返回这个状态下的最优结果
        def dp(K, N):
            # base case
            if (K, N) in hashmap:
                return hashmap[(K, N)]
            if N == 0:
                hashmap[(K, 0)] = 0
                return 0
            # 只有一个鸡蛋，只敢一层一层的尝试
            if K == 1:
                hashmap[(K, N)] = N
                return N
            res = float('INF')
            # 穷举所有可能的选择
            for i in range(1, N + 1):
                res = min(res,
                          # # 最坏情况下的最少扔鸡蛋次数
                          max(
                              dp(K - 1, i - 1),  # 鸡蛋碎了
                              dp(K, N - i)  # 鸡蛋没碎
                          ) + 1)  # 尝试了一次
            hashmap[(K, N)] = res
            return res

        return dp(K, N)

    def superEggDrop(self, K, N):
        # 当前有 k 个鸡蛋，可以尝试扔 m 次
        # 这个状态下，最坏情况下最多能确切测试一栋 n 层的楼
        dp = [[0 for j in range(N + 1)] for i in range(K + 1)]
        # base case
        m = 0
        while dp[K][m] < N:
            m += 1
            for k in range(1, K + 1):
                dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1
        return m


solution = Solution()
solution.superEggDrop1(2, 6)
