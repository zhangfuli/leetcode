# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能从s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
#
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
#
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
# 示例 1：
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]

class Solution:
    def __init__(self):
        self.res = []

    def backtrack(self, s, track):
        if len(s) == 0 and len(track) == 4:
            if '.'.join(track) not in self.res:
                self.res.append('.'.join(track))
            return
        if len(track) > 4:
            return

        for i in range(1, 4):
            sub_str = s[:i]
            if len(sub_str) != 0 and int(sub_str) <= 255:
                if not (len(sub_str) > 1 and sub_str[0] == '0'):
                    track.append(s[:i])
                    self.backtrack(s[i:], track)
                    track.pop(-1)

    def restoreIpAddresses(self, s):
        self.backtrack(s, [])
        return self.res


solution = Solution()
solution.restoreIpAddresses("010010")
