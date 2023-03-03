from re import findall
from operator import truediv, mul, sub, add
from sys import stdin


def calculate(expression: str):
    cmds = {'$': truediv, '*': mul, '-': sub, '+': add}

    expression = expression.replace('/', '$').replace(' ', '')
    lst_line = findall(r'[0-9]+\.?[0-9]*|[\*+@$-.]', expression)
    ()
    if findall(r'[^.0123456789+\-*$]', expression):
        return 'Bad request'
    elif not isinstance(expression, str):
        return 'Bad object type'

    for key in cmds.keys():
        while key in lst_line:
            i = lst_line.index(key)
            try:
                lst_line[i - 1] = cmds[key](float(lst_line.pop(i - 1)), float(lst_line.pop(i)))
            except ZeroDivisionError:
                return 'Zero division error'
    return float(*lst_line)


if __name__ == '__main__':
    [print(calculate(line.rstrip())) for line in stdin]