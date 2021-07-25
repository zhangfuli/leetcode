class Solution:

    # 抽取计算评分功能，这样在回溯时可以把二维数组看作一维，更容易理解
    def calculate(self, listOne, listTwo):
        sum = 0
        for i in range(len(listOne)):
            if listOne[i] == listTwo[i]:
                sum += 1
        return sum

    # 本质是一个数组不变，另一个穷尽其所有排列，尝试所有可能
    def dfs(self, visited, index, sum):
        '''
        index即其中students的下标，变化为从0---n-1
        mentors用于回溯穷举出全排列
        '''
        if index >= self.n:
            self.max = max(self.max, sum)
        # 对mentors进行回溯尝试求其全排列
        for i in range(self.n):
            # 避开已经访问过的
            if visited[i] == 0:
                # 递归
                visited[i] = 1
                addNum = self.calculate(self.students[index], self.mentors[i])
                sum += addNum
                self.dfs(visited, index + 1, sum)
                sum -= addNum
                visited[i] = 0
                # 回溯

    def maxCompatibilitySum(self, students, mentors) -> int:
        # 置为成员变量减少参数传递
        self.students = students
        self.mentors = mentors
        self.n, self.m = len(students), len(students[0])
        self.max = 0
        # 标记是否被访问过
        visited = [0 for _ in range(self.n)]
        self.dfs(visited, 0, 0)
        return self.max
