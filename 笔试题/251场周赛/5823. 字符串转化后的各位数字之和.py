class Solution:
    def getLucky(self, s, k):
        t1 = ''
        for i in range(len(s)):
            t1 += str(ord(s[i]) - ord('a') + 1)

        temp = t1
        print(temp)
        for i in range(k):
            t2 = 0
            for j in range(len(temp)):
                t2 += int(temp[j])
            temp = str(t2)
            print(temp)

        return int(temp)


solution = Solution()
solution.getLucky('zbax', 2)
