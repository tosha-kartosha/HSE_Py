"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/max-points-on-a-line/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        x_lines = {}
        y_lines = {}

        max_dots = 1

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0]:
                    x1 = points[i][0]
                    if x_lines.get(str(x1) + "0", False) is not False:
                        if (
                            x_lines[str(x1) + "0"][0] == points[i][0]
                            and x_lines[str(x1) + "0"][1] == points[i][1]
                        ):
                            x_lines[str(x1) + "0"][2] += 1
                    else:
                        x_lines[str(x1) + "0"] = [points[i][0], points[i][1], 2]
                    max_dots = max(max_dots, x_lines[str(x1) + "0"][2])
                else:
                    x1 = points[i][0]
                    y1 = points[i][1]
                    x2 = points[j][0]
                    y2 = points[j][1]
                    k = (y2 - y1) / (x2 - x1)
                    if k == 0:
                        k = 0
                    b = y1 - k * x1
                    if y_lines.get(str(k) + str(b), False) is not False:
                        if (
                            y_lines[str(k) + str(b)][0] == x1
                            and y_lines[str(k) + str(b)][1] == y1
                        ):
                            y_lines[str(k) + str(b)][2] += 1
                    else:
                        y_lines[str(k) + str(b)] = [x1, y1, 2]
                    max_dots = max(max_dots, y_lines[str(k) + str(b)][2])
        return max_dots
