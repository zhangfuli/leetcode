import bisect


class ExamRoom:

    def __init__(self, N):
        self.N = N
        self.students = []

    def seat(self):
        if not self.students:
            student = 0
        else:
            dist, student = self.students[0], 0

            for index, item in enumerate(self.students):
                if index:
                    pre = self.students[index - 1]
                    distance = (item - pre) // 2
                    if dist < distance:
                        dist = distance
                        student = pre + distance
            distance = self.N - 1 - self.students[-1]
            if distance > dist:
                student = self.N - 1
        bisect.insort(self.students, student)

        return student

    def leave(self, p):
        self.students.remove(p)
