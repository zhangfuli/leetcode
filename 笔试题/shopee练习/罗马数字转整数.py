#
#
# @param s string字符串
# @return int整型
#
class Solution:
    def romanToInt(self, s):
        # write code here
        hashmap_0 = {'I': 1, "V": 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        hashmap_1 = {"IV": 4, "IX": 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        res = 0
        while len(s) != 0:
            i = len(s) - 1
            if i - 1 >= 0 and s[i-1:i+1] in hashmap_1:
                res += hashmap_1[s[i-1:i+1]]
                i = i - 1
                s = s[:i]
                print(s)
            else:
                res += hashmap_0[s[i]]
                s = s[:i]
                print(s)
        return res






solution = Solution()
solution.romanToInt("VIV")