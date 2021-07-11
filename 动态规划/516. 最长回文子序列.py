class Solution:
    def longestPalindromeSubseq(self, s):
        # dp[i][j] 代表从s[i]～s[j]最长子序列的长度
        dp = [[0 for j in range(len(s) + 1)] for i in range(len(s) + 1)]
        if len(s) == 0 or len(s) == 1:
            return len(s)
        if len(s) == 2:
            if s[0] == s[1]:
                return 2
            else:
                return 1
        # base case 对角线都是1
        for i in range(0, len(s) + 1):
            dp[i][i] = 1

        # 反着遍历
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j - 1]
                    )
        print(dp[0][len(s) - 1])

        return dp[0][len(s) - 1]


solution = Solution()
solution.longestPalindromeSubseq(
    'euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew')
