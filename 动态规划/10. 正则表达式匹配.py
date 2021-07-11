class Solution:
    def isMatch1(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return 0 == len(s)

        first_match = (len(s) > 0) and p[0] in {s[0], '.'}
        # 先处理 `*`
        if len(p) >= 2 and p[1] == '*':
            # 匹配0个 | 多个
            return self.isMatch1(s, p[2:]) or (first_match and self.isMatch1(s[1:], p))

        # 处理 `.` ，匹配一个
        return first_match and self.isMatch1(s[1:], p[1:])

    def isMatch2(self, s, p):
        hashmap = {}

        def dp(i, j):
            if (i, j) in hashmap:
                return hashmap[(i, j)]
            if j == len(p):
                hashmap[(i, j)] = i == len(s)
                return hashmap[(i, j)]
            first = i < len(s) and (p[j] in {s[i], '.'})

            if j <= len(p) - 2 and p[j + 1] == '*':
                # 匹配 0 个或多个
                ans = dp(i, j + 2) or (first and dp(i + 1, j))
                hashmap[(i, j)] = ans
                return ans

            ans = first and dp(i + 1, j + 1)
            hashmap[(i, j)] = ans
            return ans

        print(hashmap)
        return dp(0, 0)


solution = Solution()
solution.isMatch2("aa", "a")
