class Solution:
    def maximumNumber(self, num, change):
        res = ''
        tu = False
        for i in range(len(num)):
            if not tu:
                if int(num[i]) > change[int(num[i])]:
                    res += num[i]
                elif int(num[i]) < change[int(num[i])]:
                    res += str(change[int(num[i])])
                    tu = True
                elif int(num[i]) == change[int(num[i])]:
                    res += num[i]

            else:
                if int(num[i]) > change[int(num[i])]:
                    res += num[i]
                    break
                elif int(num[i]) < change[int(num[i])]:
                    res += str(change[int(num[i])])
                    tu = True
                elif int(num[i]) == change[int(num[i])]:
                    res += str(change[int(num[i])])
                    tu = True

        res = res + num[len(res):]
        return res


solution = Solution()
print(solution.maximumNumber(
    "214010",
    [6, 7, 9, 7, 4, 0, 3, 4, 4, 7]
))
