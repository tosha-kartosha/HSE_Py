"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/basic-calculator/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        polska_zapis = []
        previous_elem = "_"
        temp_stack = []

        for elem in s:
            if elem in "0123456789":
                if previous_elem in "0123456789":
                    polska_zapis[-1] += elem
                else:
                    polska_zapis.append(elem)
            elif elem == "(":
                temp_stack.append("(")
            elif elem in "+-)":
                if len(temp_stack) != 0:
                    tek_elem = temp_stack[-1]
                    while tek_elem != "(" and len(temp_stack) != 0:
                        polska_zapis.append(tek_elem)
                        temp_stack.pop()
                        if len(temp_stack) != 0:
                            tek_elem = temp_stack[-1]
                if elem == ")":
                    temp_stack.pop()
                else:
                    temp_stack.append(elem)
            previous_elem = elem

        while len(temp_stack) != 0:
            polska_zapis += temp_stack[-1]
            temp_stack.pop()
        temp_stack.append(int(polska_zapis[0]))
        i = 1
        while i < len(polska_zapis):
            if polska_zapis[i].isdigit():
                temp_stack.append(int(polska_zapis[i]))
                i += 1
            else:
                if len(temp_stack) == 1:
                    temp_stack[0] *= -1
                    i += 1
                else:
                    if polska_zapis[i] == "+":
                        temp_stack[-2] = temp_stack[-2] + temp_stack[-1]
                        i += 1
                    else:
                        if len(temp_stack) > 2:
                            temp_stack[-2] = temp_stack[-2] - temp_stack[-1]
                            i += 1
                        elif i + 1 < len(polska_zapis) and polska_zapis[i + 1] == "-":
                            temp_stack[-2] = temp_stack[-2] + temp_stack[-1]
                            i += 2
                        else:
                            temp_stack[-2] = temp_stack[-2] - temp_stack[-1]
                            i += 1
                    temp_stack.pop()
        return temp_stack[0]
