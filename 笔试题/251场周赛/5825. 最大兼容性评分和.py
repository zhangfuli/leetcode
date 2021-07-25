class Solution:
    def maxCompatibilitySum(self, students, mentors):
        res = 0
        s = []
        for i in range(len(students)):
            if students[i] in mentors:
                res += len(students[i])
                mentors.remove(students[i])
            else:
                s.append(students[i])
        students = s

        hashmap = {}
        for i in range(len(students)):
            for j in range(len(mentors)):
                if tuple(students[i]) not in hashmap:
                    hashmap[tuple(students[i])] = []
                score = 0
                for z in range(len(students[i])):
                    if students[i][z] == mentors[j][z]:
                        score += 1
                hashmap[tuple(students[i])].append(score)
        print(hashmap)
        while hashmap:



solution = Solution()
solution.maxCompatibilitySum(
    [[0, 0, 1, 1, 1, 0, 1], [0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1], [0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1]],
    [[0, 1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 0, 0]])
