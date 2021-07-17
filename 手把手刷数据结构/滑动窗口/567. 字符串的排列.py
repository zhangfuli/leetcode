class Solution:
    def checkInclusion(self, s1, s2):
        need = {}
        window = {}

        for i in range(len(s1)):
            need[s1[i]] = need.get(s1[i], 0) + 1

        left = 0
        valid = 0

        for right in range(len(s2)):
            c = s2[right]
            if c in need:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                if window[c] == need[c]:
                    valid += 1
            while right - left + 1 >= len(s1):
                if valid == len(need):
                    return True
                d = s2[left]
                if d in need:
                    if need[d] == window[d]:
                        valid -= 1
                    window[d] -= 1
                left += 1
        return False


solution = Solution()
print(solution.checkInclusion("ab", "eidbaoo"))
