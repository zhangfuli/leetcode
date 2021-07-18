# 给你一个以字符串表示的非负整数num 和一个整数 k ，移除这个数中的 k 位数字，
# 使得剩下的数字最小。请你以字符串形式返回这个最小的数字。
#
# 示例 1 ：
#
# 输入：num = "1432219", k = 3
# 输出："1219"
# 解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219


# 因此我们的思路就是：
#
# 从左到右遍历
# 对于遍历到的元素，我们选择保留。
# 但是我们可以选择性丢弃前面相邻的元素, 若比本身大则丢弃

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k
        for i in range(len(num)):
            while len(stack) != 0 and stack[-1] > num[i] and k > 0:
                stack.pop(-1)
                k -= 1
            stack.append(num[i])
        res_num = ''.join(stack)[:remain]
        if res_num != '':
            return str(int(res_num))
        else:
            return '0'

solution = Solution()
print(solution.removeKdigits("10", 2))