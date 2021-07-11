class Solution:
    def minRemoveToMakeValid(self, s):
        removes = [-1]
        l_paren = []
        for i in range(len(s)):
            if s[i] == '(':
                l_paren.append(i)
            elif s[i] == ')':
                if len(l_paren) == 0:
                    removes.append(i)
                else:
                    l_paren.pop()

        print(removes)
        print(l_paren)
        removes = removes + l_paren + [len(s) + 1]
        print(removes)

        ans = []
        for idx in range(len(removes) - 1):
            ans += s[removes[idx] + 1: removes[idx + 1]]
        return ''.join(ans)

    def remove_parentheses(self, s):
        if len(s) == 0:
            return ''
        # 用于记录需要删除的括号
        _remove = []

        # 用于记录括号匹配情况
        _stack = []
        for i in range(len(s)):
            if s[i] == '(':
                _stack.append(i)
            elif s[i] == ')':
                if len(_stack) == 0:
                    _remove.append(i)
                else:
                    _stack.pop(-1)
        print(_remove)

        # 未匹配的以及要删除的
        _remove = _remove + _stack

        # 根据index 删除
        res = ''
        for i in range(len(s)):
            if i in _remove:
                continue
            else:
                res += s[i]
        print(res)
        return res


solution = Solution()
solution.remove_parentheses("a)b(c)d")
