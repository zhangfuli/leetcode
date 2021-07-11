class Solution:
    def isMonotonic(self, A):
        left = True
        right = True
        for i in range(len(A) - 1):
            if A[i] <= A[i + 1]:
                continue
            else:
                left = False
        for i in range(len(A) - 1, 0, -1):
            if A[i] <= A[i - 1]:
                continue
            else:
                right = False
        print(left)
        print(right)
        if left == False and right == False:
            return False
        else:
            return True


solution = Solution()
solution.isMonotonic([3, 2, 3, 1])
