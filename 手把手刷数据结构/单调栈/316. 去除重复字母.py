# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。
# 需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
#
# 示例 1：
# 输入：s = "bcabc"
# 输出："abc"

# 具体算法：
#
# 建立一个字典。其中 key 为 字符 c，value 为其出现的剩余次数。
# 从左往右遍历字符串，每次遍历到一个字符，其剩余出现次数 - 1.
# 对于每一个字符，如果其对应的剩余出现次数大于 1，我们可以选择丢弃（也可以选择不丢弃），否则不可以丢弃。
# 是否丢弃的标准和上面题目类似。如果栈中相邻的元素字典序更大，那么我们选择丢弃相邻的栈中的元素。
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        remain = collections.Counter(s)

        for i in range(len(s)):
            if s[i] not in stack:
                while len(stack) != 0 and stack[-1] > s[i] and remain[stack[-1]] > 0:
                    stack.pop()
                stack.append(s[i])
            remain[s[i]] -= 1
        return ''.join(stack)


solution = Solution()
print(solution.removeDuplicateLetters("bbcaac"))
