# 有三种葡萄，每种分别有a,b,c颗。
# 有三个人，第一个人只吃第1,2种葡萄，
# 第二个人只吃第2,3种葡萄，
# 第三个人只吃第1,3种葡萄。
# 适当安排三个人使得吃完所有的葡萄,并且且三个人中吃的最多的那个人吃得尽量少。


case = int(input().strip())
while case:
    nums = list(map(int, input().strip().split(' ')))
    nums.sort()
    print(max((sum(nums) + 2) // 3, (nums[2] + 1) // 2))
    case -= 1
