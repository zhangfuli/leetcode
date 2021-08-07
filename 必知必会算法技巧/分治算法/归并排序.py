# 归并排序采用分而治之的原理：
# 一、将一个序列从中间位置分成两个序列；
# 二、在将这两个子序列按照第一步继续二分下去；
# 三、直到所有子序列的长度都为1，也就是不可以再二分截止。这时候再两两合并成一个有序序列即可。
# O(nlogn) 稳定排序 辅助空间O(n)

def merge(left, right):
    res = []
    h = j = 0
    while j < len(left) and h < len(right):
        if left[j] < right[h]:
            res.append(left[j])
            j += 1
        else:
            res.append(right[h])
            h += 1

    if j == len(left):
        for i in right[h:]:
            res.append(i)
    else:
        for i in left[j:]:
            res.append(i)
    return res


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])
    return merge(left, right)


if __name__ == '__main__':
    nums = [14, 2, 34, 43, 21, 19]
    print(merge_sort(nums))
