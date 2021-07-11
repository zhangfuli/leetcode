# O(n*(log n))
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  # 找到一个基准值
        # 遍历整个列表，将小于这个基准值的元素放到一个子列表中
        less = [i for i in array[1:] if i <= pivot]
        # 遍历整个列表，将大于这个基准值的元素放到一个子列表中
        greater = [i for i in array[1:] if i > pivot]
        # 首先，明确我们对元素为0个/1个的列表无需要排序
        # 使用函数递归
        # 目标：让我们在一个基准值的一侧变为有序，然后依次返回，让我们的每个基准值的两侧都变得有序
        return quicksort(less) + [pivot] + quicksort(greater)


# 这是一些测试样例
print(quicksort([2, 5, 5, 3, 9, 7, 11]))
print(quicksort([152, 134, 38796, 7438415, 1, 2272, 34345, 24, 127]))
