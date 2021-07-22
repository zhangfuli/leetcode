class Solution:
    def __init__(self):
        self.result = []

        # print(len(graphs))

    def backtrack(self, track, graphs, dot):
        # print(track)
        if len(track) != 0 and track[-1] == len(graphs) - 1:
            # print(track)
            self.result.append(track[:])
            return None
        for i in range(0, len(graphs[dot])):
            if graphs[dot][i] != 0:
                if i not in track:
                    track.append(i)
                    self.backtrack(track, graphs, i)
                    track.pop(-1)

    def allPathsSourceTarget(self, graph):
        graphs = [[0 for j in range(len(graph))] for i in range(len(graph))]

        for index, dots in enumerate(graph):
            if len(dots) != 0:
                for dot in dots:
                    graphs[index][dot] = 1

        self.backtrack([0], graphs, 0)
        return self.result


solution = Solution()
print(solution.allPathsSourceTarget([[2], [2], [3], []]))
