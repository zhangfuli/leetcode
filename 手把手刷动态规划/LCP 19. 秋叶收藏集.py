class Solution:
    def minimumOperations(self, leaves):
        r, ry, ryr = 1 if leaves[0] == 'y' else 0, float('inf'), float('inf')
        print(r)
        print(ry)
        print(ryr)
        for i in range(1, len(leaves)):
            if leaves[i] == 'r':
                r, ry, ryr = r, min(r, ry) + 1, min(ry, ryr)
            else:
                r, ry, ryr = r + 1, min(r, ry), min(ry, ryr)+1
        return ryr


solution = Solution()
print(solution.minimumOperations("y"))