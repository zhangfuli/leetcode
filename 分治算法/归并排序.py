# void sort(int[] nums, int lo, int hi) {
#     int mid = (lo + hi) / 2;
#     /****** 分 ******/
#     // 对数组的两部分分别排序
#     sort(nums, lo, mid);
#     sort(nums, mid + 1, hi);
#     /****** 治 ******/
#     // 合并两个排好序的子数组
#     merge(nums, lo, mid, hi);
# }