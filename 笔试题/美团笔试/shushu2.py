n, K = list(map(int, input().strip().split()))
nums = list(map(int, input().strip().split()))


def find_more(nums):
    hashmap = {}
    max_value = 0
    for i in range(len(nums)):
        if nums[i] in hashmap:
            if hashmap.get(nums[i]) >= (len(nums) + 1) / 2:
                return nums[i]
            hashmap[nums[i]] += 1
            max_value = max(max_value, hashmap[nums[i]])
        else:
            hashmap[nums[i]] = 1
            max_value = max(max_value, hashmap[nums[i]])

    res = []
    for key in hashmap:
        if hashmap[key] == max_value:
            res.append(key)
    if len(res) == 0:
        return min(nums)
    else:
        return min(res)


for i in range(len(nums) - K + 1):
    print(find_more(nums[i: i + K]))

