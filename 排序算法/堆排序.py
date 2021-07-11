# a.将无需序列构建成一个堆，根据升序降序需求选择大顶堆或小顶堆;
# b.将堆顶元素与末尾元素交换，将最大元素"沉"到数组末端;
# c.重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，反复执行调整+交换步骤，直到整个序列有序。
# 完全二叉树，根>=节点
# 不稳定排序
# 平均O(nlogn)  最好O(nlogn) 最坏O(nlogn)  空间O(1)

def heapify(nums, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and nums[largest] < nums[left]:
        largest = left
    if right < n and nums[largest] < nums[right]:
        largest = right

    if largest != i:
        nums[largest], nums[i] = nums[i], nums[largest]
        heapify(nums, n, largest)


def heapSort(nums):
    n = len(nums)

    # 构造大顶堆
    for i in range(n - 1, -1, -1):
        heapify(nums, n, i)

    # 交换元素
    for i in range(n - 1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


nums = [12, 11, 13, 5, 6, 7, 11]
heapSort(nums)
n = len(nums)
print("排序后")
print(nums)
