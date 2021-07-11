class Solution:
    def countPrimes(self, n):
        if n == 0 or n == 1 or n == 2:
            return 0
        is_prim = [True for i in range(n)]
        for i in range(2, n):
            if is_prim[i]:
                j = i * i
                while j < n:
                    is_prim[j] = False
                    j += i
        print(is_prim)
        return is_prim.count(True) - 2


solution = Solution()
print(solution.countPrimes(3))
