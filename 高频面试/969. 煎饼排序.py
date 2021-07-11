class Solution:
    def __init__(self):
        self.res = []

    def pSort(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return None
        max_value = max(arr)
        max_index = arr.index(max_value)
        self.res.append(max_index + 1)
        arr_2 = arr[:max_index + 1][::-1] + arr[max_index + 1:]
        self.res.append(len(arr))
        arr_3 = arr_2[::-1]
        self.pancakeSort(arr_3[:len(arr_3) - 1])

    def pancakeSort(self, arr):
        self.pSort(arr)
        return self.res
