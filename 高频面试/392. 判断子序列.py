class Solution:
    def isSubsequence(self, s, t):
        # if len(s) == 0:
        #     return True
        j = 0
        for i in range(len(t)):
            if j < len(s) and t[i] == s[j]:
                j += 1
        return j == len(s)


solution = Solution()
print(solution.isSubsequence("", "abc"))
