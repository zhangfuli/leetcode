class Solution:
    def minWindow(self, s, t):
        need = {}
        window = {}
        for i in range(len(t)):
            if t[i] in need:
                need[t[i]] += 1
            else:
                need[t[i]] = 1

        start = 0
        res_len = len(s)
        valid = 0

        left = 0
        for right in range(0, len(s)):
            if s[right] in need:
                if s[right] in window:
                    window[s[right]] += 1
                else:
                    window[s[right]] = 1

                if window[s[right]] == need[s[right]]:
                    valid += 1

            while valid == len(need):
                if res_len > right - left:
                    res_len = right - left
                    start = left

                c = s[left]
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
                left += 1
        if res_len + 1 > len(s):
            return ""
        return s[start: start + res_len + 1]


solution = Solution()
print(solution.minWindow("a", "aa"))
