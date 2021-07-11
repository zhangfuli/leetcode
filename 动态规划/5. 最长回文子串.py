class Solution:
    def longestPalindrome(self, s):
        dp = [[False for j in range(len(s) + 1)] for i in range(len(s) + 1)]
        if len(s) == 0 or len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        # base case 对角线都是True; 相邻两个相等也是True
        for i in range(0, len(s) + 1):
            dp[i][i] = True
        for i in range(0, len(s)):
            if s[i - 1] == s[i]:
                dp[i][i + 1] = True
                dp[i + 1][i] = True

        # 如果 a??a   a = a 那么里面的若是回文数则 a??a也是回文数
        for i in range(1, len(s) + 1):
            for j in range(1, i):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j + 1]

        res = s[0]
        max_interval = 1
        for i in range(1, len(s) + 1):
            for j in range(1, i):
                if dp[i][j] == True:
                    if max_interval < i - j + 1:
                        max_interval = i - j + 1
                        res = s[j - 1:i]
        return res


solution = Solution()
solution.longestPalindrome('abcda')