class Solution:
    def advantageCount(self, nums1, nums2):
        sortedA = sorted(nums1)
        sortedB = sorted(nums2)

        # 保证存放顺序
        assigned = {nums2[i]:[] for i in range(len(nums2))}

        # 记录打不过的
        remain = []

        j = 0
        for i in range(len(sortedA)):
            if sortedA[i] > sortedB[j]:
                assigned[sortedB[j]].append(sortedA[i])
                j += 1
            else:
                remain.append(sortedA[i])
        print(assigned)
        print(remain)
        res = []

        for i in range(len(nums2)):
            if len(assigned[nums2[i]]) == 0:
                res.append(remain.pop(-1))
            else:
                res.append(assigned[nums2[i]].pop(-1))
        return res