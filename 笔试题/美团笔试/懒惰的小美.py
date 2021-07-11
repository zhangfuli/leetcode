n, m = list(map(int, input().strip().split(' ')))
nums = []
for i in range(n):
    nums.append(list(map(int, input().strip().split(' '))))

res = []

for i in range(m):
    temp = []
    for num in nums:
        temp.append(num[i])
    res.append(temp)

for i in range(len(res)):
    print(' '.join(list(map(str, res[i]))))
