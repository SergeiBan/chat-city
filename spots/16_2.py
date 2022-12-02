# 77203831
import sys


def sol(expr, operand=None):
    values = []
    if operand:
        a, b = expr[0], expr[1]
        # Меняю операнды местами, для - и // важен порядок.
        return str(eval(b + operand + a))

    for val in expr:
        is_operand = val in ('+', '-', '*', '/')
        val = '//' if val == '/' else val
        if not is_operand:
            values.append(val)
        else:
            interim = sol((values.pop(), values.pop()), val)
            values.append(interim)
    return values[len(values) - 1]


if __name__ == '__main__':
    expression = sys.stdin.readline().rstrip().split()
    print(sol(expression))
