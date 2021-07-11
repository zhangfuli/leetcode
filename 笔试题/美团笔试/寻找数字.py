import re

s = input().strip()

nums = re.findall('(\d+)', s)
nums = list(map(int, nums))
nums.sort()

for i in range(len(nums)):
    print(nums[i])
