from re import findall
from operator import truediv, mul, sub, add


def calculate(expression: str):
    if not isinstance(expression, str):
        return 'Bad object type'
    expression = expression.replace('/', '$').replace(' ', '')
    cmds = {
        '$': truediv,
        '*': mul,
        '-': sub,
        '+': add
    }

    if findall(r'[^.0123456789+\-*$]', expression):
        return 'Bad request'

    lst_line = findall(r'[0-9]+\.?[0-9]*|[\*+@$-.]', expression)
    for key in cmds.keys():
        while key in lst_line:
            i = lst_line.index(key)
            lst_line[i - 1] = cmds[key](float(lst_line.pop(i - 1)), float(lst_line.pop(i)))
    return float(*lst_line)
