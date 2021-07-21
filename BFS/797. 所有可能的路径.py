class Solution:
    def dfs(self, graphs):
        result = []

        # print(len(graphs))
        def backtrack(track, graphs, dot):
            # print(track)
            if len(track) != 0 and track[-1] == len(graphs) - 1:
                # print(track)
                result.append(track[:])
                return None
            for i in range(0, len(graphs[dot])):
                if graphs[dot][i] != 0:
                    if i not in track:
                        track.append(i)
                        backtrack(track, graphs, i)
                        track.pop(-1)

        backtrack([0], graphs, 0)
        return result

    def allPathsSourceTarget(self, graph):
        graphs = [[0 for j in range(len(graph))] for i in range(len(graph))]

        for index, dots in enumerate(graph):
            if len(dots) != 0:
                for dot in dots:
                    graphs[index][dot] = 1
        return self.dfs(graphs)


solution = Solution()
print(solution.allPathsSourceTarget([[2], [2], [3], []]))
