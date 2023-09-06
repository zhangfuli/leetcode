class Solution:
    def findAnagrams(self, s, p):
        need = {}
        window = {}

        for i in range(len(p)):
            need[p[i]] = need.get(p[i], 0) + 1

        left = 0
        valid = 0
        res = []
        for right in range(len(s)):
            if s[right] in need:
                window[s[right]] = window.get(s[right], 0) + 1
                if window[s[right]] == need[s[right]]:
                    valid += 1
            # 判断左窗口是否要收缩
            while right - left + 1 >= len(p):
                if valid == len(need):
                    res.append(left)

                if s[left] in need:
                    if window[s[left]] == need[s[left]]:
                        valid -= 1
                    window[s[left]] -= 1
                left += 1

        return res


solution = Solution()
print(solution.findAnagrams("abab", "ab"))
