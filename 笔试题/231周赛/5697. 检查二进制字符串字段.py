import re


class Solution:
    def checkOnesSegment(self, s):
        s = "0" + s + "0"
        print(s)
        num = 0
        left = 0
        for right in range(len(s)):
            if s[right] == '1' and s[left] == '1':
                continue
            if s[right] == '1' and s[left] == '0':
                left = right
                num += 1
            if s[right] == '0' and s[left] == '1':
                left = right
        print(num)
        if num == 1:
            return True
        return False

    def checkOnesSegment2(self, s):
        res = re.split("[0]+", s)
        res2 = []
        for i in range(len(res)):
            if res[i] == '':
                continue
            else:
                res2.append(res[i])
        print(res2)
        if len(res2) == 1:
            return True
        return False


solution = Solution()
print(solution.checkOnesSegment("11000110"))