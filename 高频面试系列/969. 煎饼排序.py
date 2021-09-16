# 给你一个整数数组 arr ，请使用煎饼翻转完成对数组的排序。
# 一次煎饼翻转的执行过程如下：
# 选择一个整数 k ，1 <= k <= arr.length
# 反转子数组 arr[0...k-1]（下标从 0 开始）
# 例如，arr = [3,2,1,4] ，选择 k = 3 进行一次煎饼翻转，反转子数组 [3,2,1] ，得到 arr = [1,2,3,4] 。
# 以数组形式返回能使arr有序的煎饼翻转操作所对应的k值序列。任何将数组排序且翻转次数在10 * arr.length 范围内的有效答案都将被判断为正确。
#
# 示例 1：
# 输入：[3,2,4,1]
# 输出：[4,2,4,3]
# 解释：
# 我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
# 初始状态 arr = [3, 2, 4, 1]
# 第一次翻转后（k = 4）：arr = [1, 4, 2, 3]
# 第二次翻转后（k = 2）：arr = [4, 1, 2, 3]
# 第三次翻转后（k = 4）：arr = [3, 2, 1, 4]
# 第四次翻转后（k = 3）：arr = [1, 2, 3, 4]，此时已完成排序。


class Solution:
    def pancakeSort(self, arr):
        res = []
        while len(arr) > 2:
            max_value = max(arr)
            max_index = arr.index(max_value)
            arr = arr[:max_index + 1][::-1] + arr[max_index + 1:]
            arr = arr[::-1]
            res.extend([max_index + 1, len(arr)])
            arr.pop(-1)

        if len(arr) == 2:
            if arr[1] < arr[0]:
                res.append(2)
        return res


solution = Solution()
print(solution.pancakeSort([3, 2, 4, 1]))
