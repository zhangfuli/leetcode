class Solution:
    def multiply(self, num1, num2):
        res = 0
        w1 = -1
        for j in range(len(num2) - 1, -1, -1):
            w1 += 1
            w2 = -1
            for i in range(len(num1) - 1, -1, -1):
                w2 += 1
                res += int(num2[j]) * int(num1[i]) * 10 ** (w1+w2)
                print(int(num2[j]) * int(num1[i]) * 10 ** (w1+w2))
        print(res)
        return str(res)


solution = Solution()
solution.multiply("123", "45")
