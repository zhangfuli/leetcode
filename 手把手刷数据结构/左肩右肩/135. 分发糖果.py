class Solution:
    def candy(self, ratings):
        sugar = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                sugar[i] = sugar[i - 1] + 1
        print(sugar)
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                sugar[i] = max(sugar[i + 1] + 1, sugar[i])
        print(sugar)
        return sum(sugar)


solution = Solution()
solution.candy([1, 3, 4, 5, 2])
