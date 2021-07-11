class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for c in set(s):
            l = s.index(c)
            r = s.rindex(c)
            if l < r - 1:
                ans += len(set(s[l + 1:r]))
        return ans
