class Solution:
    def calPoints(self, ops):
        points = []
        for i in range(0, len(ops)):
            if ops[i] == "C":
                if len(points) > 0:
                    points.pop(len(points) - 1)
            elif ops[i] == "D":
                if len(points) > 0:
                    points.append(2 * points[len(points) - 1])
            elif ops[i] == "+":
                if len(points) > 1:
                    points.append(points[len(points) - 1] + points[len(points) - 2])
            else:
                points.append(int(ops[i]))
        return sum(points)
