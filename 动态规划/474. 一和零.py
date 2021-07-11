class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[[0 for k in range(n + 1)] for j in range(m + 1)] for i in range(len(strs) + 1)]

        # base case
        # dp[0][:][:] = 0
        # dp[]
        max_value = -1
        for i in range(1, len(strs) + 1):
            count_0 = strs[i - 1].count('0')
            count_1 = strs[i - 1].count('1')
            for _m in range(m + 1):
                for _n in range(n + 1):
                    # 放入背包，容量溢出
                    if _m - count_0 < 0 or _n - count_1 < 0:
                        # 不放入背包
                        dp[i][_m][_n] = dp[i - 1][_m][_n]
                    else:
                        # 放入或者不放入
                        dp[i][_m][_n] = max(
                            dp[i - 1][_m - count_0][_n - count_1] + 1,  # 放入
                            dp[i - 1][_m][_n]  # 不放入
                        )
                    if m == _m and n == _n:
                        max_value = max(max_value, dp[i][_m][_n])
        return max_value

solution = Solution()
solution.findMaxForm(["10", "0001", "111001", "1", "0"], 50, 50)
