import sys
from src.DocumentClass import Document


OPERATORS = {
    'OR': Document.__or__,
    'NOT': Document.__neg__,
    'AND': Document.__and__,
}


def search(expr):
    ops = OPERATORS.keys()
    stack = []

    for atom in expr:
        if atom not in ops:
            stack.append(atom)
        else:
            try:
                oper2 = stack.pop()
                oper1 = stack.pop()
            except IndexError:
                sys.stderr.write(u"Маловато операндов")
                sys.exit(1)

            try:
                oper = OPERATORS[atom](oper1, oper2)
            except ZeroDivisionError:
                sys.stderr.write(u"Нельзя делить на 0")
                sys.exit(1)

            stack.append(oper)

    return stack.pop()
