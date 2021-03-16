import sys


def OR(x: list, y: list) -> list:
    i = 0
    j = 0
    ans = []
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            ans.append(x[i])
            i += 1
        elif x[i] > y[j]:
            ans.append(y[j])
            j += 1
        elif x[i] == y[j]:
            ans.append(x[i])
            i += 1
            j += 1
    return ans


def AND(x: list, y: list) -> list:
    i = 0
    j = 0
    ans = []
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            i += 1
        elif x[i] > y[j]:
            j += 1
        elif x[i] == y[j]:
            ans.append(x[i])
            i += 1
            j += 1
    return ans


def NOT(x: list) -> list:
    pass


OPERATORS = {
    'OR', 'NOT', 'AND'
}


def search(expr: list) -> list:
    stack = []

    for atom in expr:
        if atom not in OPERATORS:
            stack.append(atom)
        else:
            try:
                oper2 = stack.pop()
                oper1 = stack.pop()
            except IndexError:
                sys.stderr.write(u"Маловато операндов")
                sys.exit(1)

            if atom == "AND":
                oper = AND(oper1, oper2)
            elif atom == "OR":
                oper = OR(oper1, oper2)
            elif atom == "NOT":
                oper = AND(oper1, oper2)
            stack.append(oper)

    return stack
