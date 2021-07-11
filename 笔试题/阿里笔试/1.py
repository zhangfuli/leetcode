case = int(input().strip())
while case:
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    # nums = nums[:n]
    max_value = max(nums)
    min_value = min(nums)
    all_nums = [0 for i in range(n + k + 1)]
    for i in range(len(nums)):
        all_nums[nums[i]] = 1
    for i in range(min_value, len(all_nums)):
        if all_nums[i] != 0:
            continue
        else:
            k -= 1
            if k == 0:
                print(str(i).strip())

    case -= 1

