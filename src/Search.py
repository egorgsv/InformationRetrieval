import sys
from src.SPIMIClass import SPIMI


OPERATORS = {
    'OR': SPIMI.__or__,
    'NOT': SPIMI.__neg__,
    'AND': SPIMI.__and__,
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

            oper = OPERATORS[atom](oper1, oper2)
            stack.append(oper)

    print('still not available...')