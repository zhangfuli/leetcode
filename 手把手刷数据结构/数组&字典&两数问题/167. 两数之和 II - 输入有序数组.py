class Solution:
    def twoSum(self, numbers, target):
        hashmap = {}
        for i in range(len(numbers)):
            another_num = target - numbers[i]
            if another_num in hashmap:
                return sorted([i + 1, hashmap[another_num] + 1])
            else:
                hashmap[numbers[i]] = i
