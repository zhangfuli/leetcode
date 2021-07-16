class Solution:
    def __init__(self):
        self.res = 0
    def maxSumBST(self, root) -> int:
        min_, max_ = float('-inf'), float('inf')

        def dfs(root):
            if not root:
                return max_, min_, 0
            lmin, lmax, lsum = dfs(root.left)
            rmin, rmax, rsum = dfs(root.right)
            # 能构成二叉搜索树
            if lmax < root.val < rmin:
                self.res = max(self.res, root.val + lsum + rsum)
                return min(lmin, root.val), max(rmax, root.val), root.val + lsum + rsum
            return min_, max_, 0

        dfs(root)
        return self.res