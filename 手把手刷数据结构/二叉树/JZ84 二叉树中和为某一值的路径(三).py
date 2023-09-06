# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @param sum int整型 
# @return int整型
#
class Solution:
    def __init__(self):
        self.hashmap = {}
    def FindPath(self , root, sum):
        # 判断-sum是否等于0
        self.hashmap[0] = 1
        return self.dfs(root, sum, 0)
    def dfs(self, root, sum, last): # last 到上一层为止的累加和
        if root is None:
            return 0
        res = 0
        tmp = root.val + last
        if (tmp - sum) in self.hashmap: # 如果曾经出现过
            res += self.hashmap[tmp-sum]

        if tmp in self.hashmap:
            self.hashmap[tmp] += 1
        else:
            self.hashmap[tmp] = 1

        res += self.dfs(root.left, sum, tmp)
        res += self.dfs(root.right, sum, tmp)
        # 回退该路径和
        self.hashmap[tmp] -= 1
        return res


## 第二种解法
class Solution2:
    def __init__(self):
        self.res = 0
    def FindPath(self, root, sum):
        if root is None:
            return self.res

        # 查询一某节点为跟的路经数
        self.dfs(root, sum)

        # 以子节点为新根
        self.FindPath(root.left, sum)
        self.FindPath(root.right, sum)
        return self.res

    def dfs(self, root, sum):
        if root is None:
            return None

        if root.val == sum:
            self.res += 1

        self.dfs(root.left, sum - root.val)
        self.dfs(root.right, sum - root.val)



# write code here
