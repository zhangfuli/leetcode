class Solution:
    def palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):
            # 从中心往两边扩散
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i + 1)

            if len(res) < len(s1):
                res = s1
            if len(res) < len(s2):
                res = s2
        return res


solution = Solution()
print(solution.longestPalindrome("babad"))
