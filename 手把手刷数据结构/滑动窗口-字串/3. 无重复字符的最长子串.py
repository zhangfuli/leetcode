# 给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。
#
#
# 示例1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。


class Solution:
    def lengthOfLongestSubstring(self, s):
        window = {}
        left = 0
        ans = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            while window[s[right]] > 1:
                if s[left] in window:
                    window[s[left]] -= 1
                left += 1
            ans = max(right - left + 1, ans)
        return ans
